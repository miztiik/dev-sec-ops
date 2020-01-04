from aws_cdk import aws_iam as iam
from aws_cdk import aws_s3 as s3
from aws_cdk import aws_secretsmanager as secretsmanager
from aws_cdk import core
from custom_resource.iam_user_tagger_cdk import iam_user_tagger
from custom_resource.random_string_generator_cdk import random_string_generator


class global_args:
    '''
    Helper to define global statics
    '''
    OWNER                       = "MystiqueInfoSecurity"
    ENVIRONMENT                 = "production"
    SOURCE_INFO                 = "https://github.com/miztiik/dev-sec-ops/tree/master/s3-restrict-object-access-based-on-tags-abac"



class S3RestrictObjectAccessBasedOnTagsAbacStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        pvt_bkt = s3.Bucket(
            self,
            "abacBucket",
            versioned=True,
            # encryption=s3.BucketEncryption.KMS_MANAGED,
            block_public_access=s3.BlockPublicAccess(block_public_policy=True),
            removal_policy=core.RemovalPolicy.DESTROY
            )

        pvt_bkt.add_to_resource_policy(
            iam.PolicyStatement(
                effect=iam.Effect.ALLOW,
                # actions=["s3:GetObject"],
                actions=["s3:*"],
                # resources=[pvt_bkt.arn_for_objects("file.txt")],
                resources=[pvt_bkt.arn_for_objects("*")],
                principals=[iam.AccountRootPrincipal()]
            )
        )
        # Create 3 Users: 1 Admin & 2 Normal Users

        # Lets generate a password for our user
        redRosy_new_pass = random_string_generator(
            self,
            "redRosyNewPasswordGenerator",
            Length=20
        )

        redRosy = iam.User(
            self,
            "redRosy",
            user_name="redRosy",
            password=core.SecretValue.plain_text(redRosy_new_pass.response)
        )

        blueBob_new_pass = random_string_generator(
            self,
            "blueBobNewPasswordGenerator",
            Length=20
        )

        blueBob = iam.User(
            self,
            "blueBob",
            user_name="blueBob",
            password=core.SecretValue.plain_text(blueBob_new_pass.response)
        )

        annoyingAdmin_new_pass = random_string_generator(
            self,
            "annoyingAdminNewPasswordGenerator",
            Length=20
        )

        annoyingAdmin = iam.User(
            self,
            "annoyingAdmin",
            user_name="annoyingAdmin",
            password=core.SecretValue.plain_text(annoyingAdmin_new_pass.response)
        )

        teamUnicornGrp = iam.Group(
            self,
            "teamUnicorn",
            group_name="teamUnicorn"
        )

        # Add Users To Group
        teamUnicornGrp.add_user(redRosy)
        teamUnicornGrp.add_user(blueBob)
        teamUnicornGrp.add_user(annoyingAdmin)

        # blueGrp1.add_managed_policy(iam.ManagedPolicy.from_aws_managed_policy_name("AmazonS3ReadOnlyAccess"))
        ##############################################
        # We need a custom resource to TAG IAM Users #
        ##############################################

        iamUserTaggerResp = iam_user_tagger(
            self, "iamTagger",
            message=[
                {"user":redRosy.user_name, "tags":[{'Key': 'teamName','Value':'teamUnicorn'},
                                                    {'Key': 'projectName','Value':'projectRed'}
                                                    ]
                },
                {"user":blueBob.user_name, "tags":[{'Key': 'teamName','Value':'teamUnicorn'},
                                                    {'Key': 'projectName','Value':'projectBlue'}
                                                    ]
                },
                {"user":annoyingAdmin.user_name, "tags":[{'Key': 'teamName','Value':'teamUnicorn'},
                                                    {'Key': 'teamAdmin','Value':'yes'}
                                                    ]
                }
            ]
        )

        """
        resource = MyCustomResource(
            self, "iamTagger",
            message=[
                {"user":redRosy.user_name, "tags":[{'Key': 'teamName','Value':'teamUnicorn'},
                                                    {'Key': 'projectName','Value':'projectRed'}
                                                    ]
                },
                {"user":blueBob.user_name, "tags":[{'Key': 'teamName','Value':'teamUnicorn'},
                                                    {'Key': 'projectName','Value':'projectBlue'}
                                                    ]
                },
                {"user":annoyingAdmin.user_name, "tags":[{'Key': 'teamName','Value':'teamUnicorn'},
                                                    {'Key': 'teamAdmin','Value':'yes'}
                                                    ]
                }
            ]
        )
        """

        # Lets Create the IAM Role
        # Uses belonging to this group, will be able to asume this role
        accountId=core.Aws.ACCOUNT_ID
        teamUnicornProjectRedRole = iam.Role(
            self,
            'teamUnicornProjectRedRoleId',
            assumed_by=iam.AccountPrincipal(f"{accountId}"),
            role_name="teamUnicornProjectRedRole"
        )
        core.Tag.add(teamUnicornProjectRedRole, key="teamName",value="teamUnicorn")
        core.Tag.add(teamUnicornProjectRedRole, key="projectName",value="projectRed")

        teamUnicornProjectBlueRole = iam.Role(
            self,
            'teamUnicornProjectBlueRoleId',
            assumed_by=iam.AccountPrincipal(f"{accountId}"),
            role_name="teamUnicornProjectBlueRole"
        )
        core.Tag.add(teamUnicornProjectBlueRole, key="teamName",value="teamUnicorn")
        core.Tag.add(teamUnicornProjectBlueRole, key="projectName",value="projectBlue")

        teamUnicornTeamAdminRole = iam.Role(
            self,
            'teamUnicornTeamAdminRoleId',
            assumed_by=iam.AccountPrincipal(f"{accountId}"),
            role_name="teamUnicornTeamAdminRole"
        )
        core.Tag.add(teamUnicornTeamAdminRole, key="teamName",value="teamUnicorn")
        core.Tag.add(teamUnicornTeamAdminRole, key="teamAdmin",value="yes")

        # Allow Group to Assume Role
        grpStmt1=iam.PolicyStatement(
                effect=iam.Effect.ALLOW,
                resources=[f"arn:aws:iam::{accountId}:role/teamUnicornProject*"],
                actions=["sts:AssumeRole"],
                conditions={ "StringEquals": { "iam:ResourceTag/teamName": "${aws:PrincipalTag/teamName}",
                                               "iam:ResourceTag/projectName": "${aws:PrincipalTag/projectName}" 
                                            }
                        }
            )
        grpStmt1.sid="AllowGroupMembersToAssumeRoleMatchingTeamName"

        grpStmt2=iam.PolicyStatement(
                effect=iam.Effect.ALLOW,
                resources=[f"arn:aws:iam::{accountId}:role/teamUnicornTeamAdminRole"],
                actions=["sts:AssumeRole"],
                conditions={ "StringEquals": { "iam:ResourceTag/teamName": "${aws:PrincipalTag/teamName}",
                                               "iam:ResourceTag/teamAdmin": "yes"
                                            }
                        }
            )
        grpStmt2.sid="AllowTeamAdminToAssumeRoleMatchingTeamName"
        teamUnicornGrp.add_to_policy( grpStmt1 )
        teamUnicornGrp.add_to_policy( grpStmt2 )

        # Add Permissions to the Role
        roleStmt1=iam.PolicyStatement(
                effect=iam.Effect.ALLOW,
                resources=["*"],
                actions=["s3:ListAllMyBuckets", "s3:HeadBucket"]
            )
        roleStmt1.sid="AllowGroupToSeeBucketListInTheConsole"

        roleStmt2=iam.PolicyStatement(
                effect=iam.Effect.ALLOW,
                resources=[pvt_bkt.bucket_arn],
                actions=["s3:ListBucket","s3:ListBucketVersions"],
                # Below condition can be used to enable listing a particular prefix in another statement
                # conditions={ "StringEquals" : { "s3:prefix":[""], "s3:delimiter":["/"] } }
            )
        roleStmt2.sid="AllowRootLevelListingOfBucket"

        roleStmt3=iam.PolicyStatement(
                effect=iam.Effect.ALLOW,
                resources=[pvt_bkt.arn_for_objects("*")],
                actions=["s3:Get*","s3:DeleteObjectTagging"],
                conditions={ "StringEquals": { "s3:ExistingObjectTag/teamName" : "${aws:PrincipalTag/teamName}",
                                               "s3:ExistingObjectTag/projectName" : "${aws:PrincipalTag/projectName}" 
                                            }
                        }
            )
        roleStmt3.sid="ReadOnlyAccessToTeams"

        roleStmt4=iam.PolicyStatement(
                effect=iam.Effect.ALLOW,
                resources=[pvt_bkt.arn_for_objects("*")],
                actions=["s3:PutObject","s3:PutObjectTagging","s3:PutObjectVersionTagging"],
                conditions={ "StringEquals": { "s3:RequestObjectTag/teamName" : "${aws:PrincipalTag/teamName}",
                                               "s3:RequestObjectTag/projectName" : "${aws:PrincipalTag/projectName}" 
                                            }
                        }
            )
        roleStmt4.sid="WriteTaggedObjectOwnedByThem"

        roleStmt5=iam.PolicyStatement(
                effect=iam.Effect.ALLOW,
                resources=[pvt_bkt.bucket_arn, pvt_bkt.arn_for_objects("*")],
                actions=["s3:*"],
                conditions={ 
                    "StringEquals" : { 
                        "${aws:PrincipalTag/teamAdmin}": [ "yes" ]
                    }
                }
            )
        roleStmt5.sid="FullAccessToAdminsFromSameTeam"

        teamUnicornProjectRedRole.add_to_policy( roleStmt1 )
        teamUnicornProjectRedRole.add_to_policy( roleStmt2 )
        teamUnicornProjectRedRole.add_to_policy( roleStmt3 )
        teamUnicornProjectRedRole.add_to_policy( roleStmt4 )
        teamUnicornProjectRedRole.add_to_policy( roleStmt5 )

        # Add same permissions to projectBlueRole
        teamUnicornProjectBlueRole.add_to_policy( roleStmt1 )
        teamUnicornProjectBlueRole.add_to_policy( roleStmt2 )
        teamUnicornProjectBlueRole.add_to_policy( roleStmt3 )
        teamUnicornProjectBlueRole.add_to_policy( roleStmt4 )
        teamUnicornProjectBlueRole.add_to_policy( roleStmt5 )

        # Add same permissions to teamAdminRole
        teamUnicornTeamAdminRole.add_to_policy( roleStmt1 )
        teamUnicornTeamAdminRole.add_to_policy( roleStmt2 )
        teamUnicornTeamAdminRole.add_to_policy( roleStmt3 )
        teamUnicornTeamAdminRole.add_to_policy( roleStmt4 )
        teamUnicornTeamAdminRole.add_to_policy( roleStmt5 )


        ###########################################
        ################# OUTPUTS #################
        ###########################################

        output0 = core.CfnOutput(self,
            "SecuirtyAutomationFrom",
            value=f"{global_args.SOURCE_INFO}",
            description="To know more about this automation stack, check out our github page."
        )

        output1_r = core.CfnOutput(self,
            "User:redRosy",
            value=redRosy_new_pass.response,
            description=f"Red Rosy User Password"
        )
        output1_b = core.CfnOutput(self,
            "User:blueBob",
            value=blueBob_new_pass.response,
            description=f"Red Rosy User Password"
        )
        output1_a = core.CfnOutput(self,
            "User:annoyingAdmin",
            value=annoyingAdmin_new_pass.response,
            description=f"Red Rosy User Password"
        )

        output2 = core.CfnOutput(self,
            "SecurePrivateBucket",
            value=(
                    f"https://console.aws.amazon.com/s3/buckets/"
                    f"{pvt_bkt.bucket_name}"
                ),
            description=f"S3 Bucket to Test ABAC"
        )

        output3 = core.CfnOutput(self,
            "Rosy-Assume-RedRole-Url",
            value=(
                    f"https://signin.aws.amazon.com/switchrole?roleName="
                    f"{teamUnicornProjectRedRole.role_name}"
                    f"&account="
                    f"{core.Aws.ACCOUNT_ID}"
                ),
            description=f"The URL for Rosy to assume teamRed Role"
        )


        output4 = core.CfnOutput(self,
            "blueBob-Assume-RedRole-Url",
            value=(
                    f"https://signin.aws.amazon.com/switchrole?roleName="
                    f"{teamUnicornProjectBlueRole.role_name}"
                    f"&account="
                    f"{core.Aws.ACCOUNT_ID}"
                ),
            description=f"The URL for Bob to assume teamBlue Role"
        )

        output5 = core.CfnOutput(self,
            "SampleS3UploadCommands",
            value=(
                    f"aws s3api put-object-tagging --bucket {pvt_bkt.bucket_name} --key YOUR-OBJECT --tagging 'TagSet=[{{Key=projectName,Value=teamRed}}]'"
                ),
            description=f"For ProjectRed"
        )

        output10 = core.CfnOutput(self,
            "User-Login-Url",
            value=(
                    f"https://{core.Aws.ACCOUNT_ID}.signin.aws.amazon.com/console"
                ),
            description=f"The URL for Rosy to assume teamRed Role"
        )
