# 👮 AWS Security: Use Secrets Manager to store Database credentials

This repo shows you how you can store database credentials in AWS Secrets Manager and avoid hard coding them in applications. We will simulate a application request to DB using Lambda & API GW.

Follow this article in **[Udemy][101]**

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

## 📌 Who is using this

This Udemy [course][101] uses this repository extensively to teach advanced AWS Cloud Security to new developers, Solution Architects & Ops Engineers in AWS.

### 💡 Help/Suggestions or 🐛 Bugs

Thank you for your interest in contributing to our project. Whether it's a bug report, new feature, correction, or additional documentation or solutions, we greatly value feedback and contributions from our community. [Start here][200]

### 👋 Buy me a coffee

Buy me a [coffee ☕][900].

### 📚 References

1. [AWS Secrets Manager][1]
1. [Rotating Your AWS Secrets Manager Secrets][2]

### 🏷️ Metadata

**Level**: 200

[1]: https://aws.amazon.com/secrets-manager/

[2]: https://docs.aws.amazon.com/secretsmanager/latest/userguide/rotating-secrets.html

[100]: https://www.udemy.com/course/aws-cloud-security/?referralCode=B7F1B6C78B45ADAF77A9

[101]: https://www.udemy.com/course/aws-cloud-security-proactive-way/?referralCode=71DC542AD4481309A441

[102]: https://www.udemy.com/course/aws-cloud-development-kit-from-beginner-to-professional/?referralCode=E15D7FB64E417C547579

[103]: https://www.udemy.com/course/aws-cloudformation-basics?referralCode=93AD3B1530BC871093D6

[200]: https://github.com/miztiik/dev-sec-ops/issues

[899]: https://www.udemy.com/user/n-kumar/

[900]: https://ko-fi.com/miztiik
