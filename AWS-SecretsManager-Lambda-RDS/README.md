# 👮AWS Security: Use Secrets Manager to store Database credentials

This repo shows you how you can store database credentials in AWS Secrets Manager and avoid hardcoding them in applications. We will simulate a application request to DB using Lambda & API GW.

![SecretsManager](https://github.com/aws-samples/automating-governance-sample/blob/master/AWS-SecretsManager-Lambda-RDS-blog/secretsmanager_blog.png?raw=true)

1. ## Deployment

      Use the cloudformation template here in the repo and deploy using cli,

    ```bash
    aws cloudformation deploy \
        --template-file ./templates/SecretsManager_LambdaRDS_CFN_template.yml \
        --stack-name "MiztiikAutomationStack" \
        --capabilities CAPABILITY_IAM
    ```

1. ## Testing the solution

    Access the webpage from the API url, you should be able fetch results from the RDS. Check lambda logs for execution results(including _secret_ :))

1. ## Next Steps: Do Try This

    You can consider the following actions,

    - Audit for usage
    - Add notification triggers for rotation failures

1. ## CleanUp

    If you want to destroy all the resources created by the stack, Execute the below command to delete the stack, or _you can delete the stack from console as well_

    ```bash
    # Delete the CF Stack
    aws cloudformation delete-stack \
        --stack-name "MiztiikAutomationStack" \
        --region "${AWS_REGION}"
    ```

    This is not an exhaustive list, please carry out other necessary steps as maybe applicable to your needs.

## Buy me a coffee

Buy me a coffee ☕ through [Paypal](https://paypal.me/valaxy), _or_ You can reach out to get more details through [here](https://youtube.com/c/valaxytechnologies/about).

### References

1. [AWS Secrets Manager](https://aws.amazon.com/secrets-manager/)

1. [Rotating Your AWS Secrets Manager Secrets](https://docs.aws.amazon.com/secretsmanager/latest/userguide/rotating-secrets.html)

### Metadata

**Level**: 200