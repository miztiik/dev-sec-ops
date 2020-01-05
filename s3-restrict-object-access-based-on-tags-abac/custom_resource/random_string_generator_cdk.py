from aws_cdk import aws_cloudformation as cfn
from aws_cdk import aws_iam as iam
from aws_cdk import aws_lambda as lambda_
from aws_cdk import core


class random_string_generator(core.Construct):
    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id)

        with open("custom_resource/random_string_generator_lambda_function.py", encoding="utf-8") as fp:
            code_body = fp.read()


        # Use `uuidgen` in bash to generate new ones
        random_string_generator_fn=lambda_.SingletonFunction(
            self, "Singleton",
            uuid="RANDOMF2-F7DB-4561-B7AC-4C9730D10E95",
            code=lambda_.InlineCode(code_body),
            handler="index.lambda_handler",
            timeout=core.Duration.seconds(300),
            runtime=lambda_.Runtime.PYTHON_3_7,
        )


        resource = cfn.CustomResource(
            self, "Resource",
            provider=cfn.CustomResourceProvider.lambda_(
                random_string_generator_fn
            ),
            properties=kwargs,
        )

        self.response = resource.get_att("Response").to_string()
        #self.response = resource.get_att("Response")
