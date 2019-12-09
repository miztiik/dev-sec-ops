from aws_cdk import (
    core,
    aws_events,
    aws_events_targets,
    aws_lambda as _lambda,
    aws_iam as iam
)

class RemoveUnusedSecurityGroupsStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        lambda_perms = iam.PolicyStatement(
                effect=iam.Effect.ALLOW,
                resources=["ad"],
                # actions=["ec2:DescribeInstances","ec2:DescribeSecurityGroupReferences","ec2:DescribeSecurityGroups","ec2:DescribeStaleSecurityGroups"]
            )
        # lambda_perms.sid="DescribeSecurityGroupsAndInstances"

        lambda_perms_stmt = iam.PolicyStatement()
        # https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags.html
        lambda_perms_stmt.add_actions("ec2:DescribeInstances")
        lambda_perms_stmt.add_actions("ec2:DescribeSecurityGroupReferences")
        lambda_perms_stmt.add_actions("ec2:DescribeSecurityGroups")
        lambda_perms_stmt.add_actions("ec2:DescribeStaleSecurityGroups")
        lambda_perms_stmt.add_actions("ec2:DeleteSecurityGroup")
        lambda_perms_stmt.add_all_resources()
        lambda_perms_stmt.effect=iam.Effect.ALLOW
        lambda_perms_stmt.sid="AllowLambdaToDescribeSecurityGroupsInstancesAndDeleteSecurityGroups"
        
        with open("lambda_src/sg_janitor.py", encoding="utf-8") as fp:
            code_body = fp.read()

        # Defines an AWS Lambda resource
        sg_janitor = _lambda.Function(
            self,
            id='SecurityGroupJanitor',
            function_name="SecurityGroupJanitor",
            runtime=_lambda.Runtime.PYTHON_3_7,
            # code=_lambda.Code.asset('lambda_src'),
            code=_lambda.InlineCode(code_body),
            handler='index.lambda_handler',
            timeout=core.Duration.seconds(10)
        )

        sg_janitor.add_to_role_policy(lambda_perms_stmt)

        # CloudWatch Trigger for lambda
        sg_janitor_trigger = aws_events.Rule(
            self, 
            id="delete_unused_sgs",
            schedule=aws_events.Schedule.rate(core.Duration.days(7))
        )
        sg_janitor_trigger.add_target(aws_events_targets.LambdaFunction(sg_janitor))
