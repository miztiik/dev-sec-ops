from aws_cdk import aws_cloudformation as cfn
from aws_cdk import aws_iam as iam
from aws_cdk import aws_lambda as lambda_
from aws_cdk import core


class iam_user_tagger(core.Construct):
    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id)

        with open("custom_resource/iam_user_tagger_lambda_function.py", encoding="utf-8") as fp:
            code_body = fp.read()

        statement = iam.PolicyStatement()
        # https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags.html
        statement.add_actions("iam:TagUser")
        statement.add_actions("iam:UntagUser")
        statement.add_all_resources()
        statement.effect=iam.Effect.ALLOW

        iam_tagger_fn=lambda_.SingletonFunction(
            self, "Singleton",
            uuid="tagger30-4ee1-11e8-9c2d-fa7ae01bbebc",
            code=lambda_.InlineCode(code_body),
            handler="index.lambda_handler",
            timeout=core.Duration.seconds(300),
            runtime=lambda_.Runtime.PYTHON_3_7,
        )

        iam_tagger_fn.add_to_role_policy(statement)
        
        """ 
        resource = cfn.CustomResource(
            self, "Resource",
            provider=cfn.CustomResourceProvider.lambda_(
                lambda_.SingletonFunction(
                    self, "Singleton",
                    uuid="f7d4f730-4ee1-11e8-9c2d-fa7ae01bbebc",
                    code=lambda_.InlineCode(code_body),
                    handler="index.main",
                    timeout=core.Duration.seconds(300),
                    runtime=lambda_.Runtime.PYTHON_3_7,
                )
            ),
            properties=kwargs,
        )
        """

        resource = cfn.CustomResource(
            self, "Resource",
            provider=cfn.CustomResourceProvider.lambda_(
                iam_tagger_fn
            ),
            properties=kwargs,
        )

        self.response = resource.get_att("Response").to_string()
