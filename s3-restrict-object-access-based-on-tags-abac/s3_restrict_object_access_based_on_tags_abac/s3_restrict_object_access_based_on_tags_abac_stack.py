from aws_cdk import (
    aws_s3 as s3,
    aws_iam as iam,
    aws_secretsmanager as secretsmanager,
    core,
)

from custom_resource.my_custom_resource import MyCustomResource


class S3RestrictObjectAccessBasedOnTagsAbacStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        bkt01 = s3.Bucket(
            self,
            "abacBucket",
            versioned=True,
            # encryption=s3.BucketEncryption.KMS_MANAGED,
            block_public_access=s3.BlockPublicAccess(block_public_policy=True),
            removal_policy=core.RemovalPolicy.DESTROY
            )

        bkt01.add_to_resource_policy(
            iam.PolicyStatement(
                effect=iam.Effect.ALLOW,
                # actions=["s3:GetObject"],
                actions=["s3:*"],
                # resources=[bkt01.arn_for_objects("file.txt")],
                resources=[bkt01.arn_for_objects("*")],
                principals=[iam.AccountRootPrincipal()]
            )
        )
        # Create 3 Users: 1 Admin & 2 Normal Users
        redUser1 = iam.User(
            self,
            "redUser1",
            user_name="redUser",
            password=core.SecretValue.plain_text("redUser1SUPERDUMBpassWord")
        )

        blueUser1 = iam.User(
            self,
            "blueUser1",
            user_name="blueUser",
            password=core.SecretValue.plain_text("blueUser1SUPERDUMBpassWord")
        )

        adminUser1 = iam.User(
            self,
            "adminUser1",
            user_name="adminUser",
            password=core.SecretValue.plain_text("adminUser1SUPERDUMBpassWord")
        )

        unicornGrp = iam.Group(
            self,
            "unicornGrp",
            group_name="unicornGroup"
        )

        # Add Users To Group
        unicornGrp.add_user(redUser1)
        unicornGrp.add_user(blueUser1)
        unicornGrp.add_user(adminUser1)

        # blueGrp1.add_managed_policy(iam.ManagedPolicy.from_aws_managed_policy_name("AmazonS3ReadOnlyAccess"))
        ##############################################
        # We need a custom resource to TAG IAM Users #
        ##############################################

        resource = MyCustomResource(
            self, "iamTagger",
            message=[
                {"user":redUser1.user_name, "tags":[{'Key': 'teamName','Value':'teamUnicorn'},
                                                    {'Key': 'projectName','Value':'projectRed'}
                                                    ]
                },
                {"user":blueUser1.user_name, "tags":[{'Key': 'teamName','Value':'teamUnicorn'},
                                                    {'Key': 'projectName','Value':'projectBlue'}
                                                    ]
                },
                {"user":adminUser1.user_name, "tags":[{'Key': 'teamName','Value':'teamUnicorn'},
                                                    {'Key': 'projectAdmin','Value':'yes'}
                                                    ]
                }
            ]
        )

        # Publish the custom resource output
        core.CfnOutput(
            self, "ResponseMessage",
            description="The message that came back from the Custom Resource",
            value=resource.response,
        )

        # Lets Create the IAM Role to be used by the groups
        accountId=core.Aws.ACCOUNT_ID
        unicornTeamProjectRedRole = iam.Role(
            self,
            'unicornTeamProjectRedRoleId',
            assumed_by=iam.AccountPrincipal(f"{accountId}"),
            role_name="unicornTeamProjectRedRole"
        )
        core.Tag.add(unicornTeamProjectRedRole, key="teamName",value="teamUnicorn")
        core.Tag.add(unicornTeamProjectRedRole, key="projectName",value="projectRed")

        unicornTeamProjectBlueRole = iam.Role(
            self,
            'unicornTeamProjectBlueRoleId',
            assumed_by=iam.AccountPrincipal(f"{accountId}"),
            role_name="unicornTeamProjectBlueRole"
        )
        core.Tag.add(unicornTeamProjectBlueRole, key="teamName",value="teamUnicorn")
        core.Tag.add(unicornTeamProjectBlueRole, key="projectName",value="projectBlue")

        rolesArn=core.Stack.format_arn(
            self,
            service="iam",
            resource="role",
            sep=":",
            resource_name="unicornTeamRoleProject*"
        )
        # Allow Group to Assume Role
        grpStmt1=iam.PolicyStatement(
                effect=iam.Effect.ALLOW,
                # resources=[unicornTeamProjectRedRole.role_arn],
                resources=[rolesArn],
                actions=["sts:AssumeRole"],
                conditions={ "StringEquals": { "iam:ResourceTag/teamName": "${aws:PrincipalTag/teamName}" } }
            )
        grpStmt1.sid="AllowGroupMembersToAssumeRoleMatchingTeamName"
        unicornGrp.add_to_policy( grpStmt1 )

        # Add Permissions to the Role
        roleStmt1=iam.PolicyStatement(
                effect=iam.Effect.ALLOW,
                resources=["*"],
                actions=["s3:ListAllMyBuckets", "s3:HeadBucket"]
            )
        roleStmt1.sid="AllowGroupToSeeBucketListInTheConsole"

        roleStmt2=iam.PolicyStatement(
                effect=iam.Effect.ALLOW,
                resources=[bkt01.bucket_arn],
                actions=["s3:ListBucket","s3:ListBucketVersions"],
                # Below condition can be used to enable listing a particular prefix in another statement
                # conditions={ "StringEquals" : { "s3:prefix":[""], "s3:delimiter":["/"] } }
            )
        roleStmt2.sid="AllowRootLevelListingOfBucket"

        roleStmt3=iam.PolicyStatement(
                effect=iam.Effect.ALLOW,
                resources=[bkt01.arn_for_objects("*")],
                actions=["s3:Get*"],
                conditions={ "StringEquals" : { 
                    "s3:ExistingObjectTag/teamName": "${aws:PrincipalTag/teamName}",
                    "s3:ExistingObjectTag/projectName": "${aws:PrincipalTag/projectName}",
                    }
                }
            )
        roleStmt3.sid="ReadOnlyAccessToTeams"

        roleStmt4=iam.PolicyStatement(
                effect=iam.Effect.ALLOW,
                resources=[bkt01.arn_for_objects("*")],
                actions=["s3:*"],
                conditions={ "StringEquals" : { 
                    "s3:ExistingObjectTag/teamName": "${aws:PrincipalTag/teamName}",
                    "${aws:PrincipalTag/projectAdmin}": "yes"
                    }
                }
            )
        roleStmt4.sid="FullAccessToAdminsFromSameTeam"

        unicornTeamProjectRedRole.add_to_policy( roleStmt1 )
        unicornTeamProjectRedRole.add_to_policy( roleStmt2 )
        unicornTeamProjectRedRole.add_to_policy( roleStmt3 )
        unicornTeamProjectRedRole.add_to_policy( roleStmt4 )

        # Add same permissions to projectBlueRole
        unicornTeamProjectBlueRole.add_to_policy( roleStmt1 )
        unicornTeamProjectBlueRole.add_to_policy( roleStmt2 )
        unicornTeamProjectBlueRole.add_to_policy( roleStmt3 )
        unicornTeamProjectBlueRole.add_to_policy( roleStmt4 )