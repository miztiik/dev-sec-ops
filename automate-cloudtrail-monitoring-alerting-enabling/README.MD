# 👮 AWS Security - Automate Cloudtrail Monitoring, Alerting & Enabling

  Learn how to automatically detect cloudtrail `disabling` event, `alert` your security team and `re-enable` the trail automatically.
  Follow this article in **[Udemy][101]**
  ![Automate Cloudtrail Monitoring, Alerting & Enabling
](images/miztiik_github_security_cloudtrail_auto_enabling.png)

## Lab Setup: Using AWS CloudFormation

  _From the CLI,_

  ```sh
  aws cloudformation deploy \
        --template-file aws-cloudtrail-auto-remediate.template \
        --stack-name "MiztiikAutomationStack" \
        --capabilities CAPABILITY_IAM
  ```

### Testing the solution

1. Ensure `GuardDuty` and `SecurityHub` for your account
1. Subscribe to the SNS
1. Create a trail
1. Wait for the email notification
1. Verify trail had been automatically enabled
1. Check in `AWS Security Hub` in `Findings`
1. CleanUp - Delete all resources(_as necessary_)

#### References

1. [Recover Lost Key Pair of AWS EC2 using Userdata][1]
1. [Recover Key Pair of AWS EC2][2]

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

[1]: https://www.youtube.com/watch?v=Bqt538HRsws

[2]: https://www.youtube.com/watch?v=5btWXn4yWzQ

[100]: https://www.udemy.com/course/aws-cloud-security/?referralCode=B7F1B6C78B45ADAF77A9

[101]: https://www.udemy.com/course/aws-cloud-security-proactive-way/?referralCode=71DC542AD4481309A441

[102]: https://www.udemy.com/course/aws-cloud-development-kit-from-beginner-to-professional/?referralCode=E15D7FB64E417C547579

[103]: https://www.udemy.com/course/aws-cloudformation-basics?referralCode=93AD3B1530BC871093D6

[200]: https://github.com/miztiik/dev-sec-ops/issues

[899]: https://www.udemy.com/user/n-kumar/

[900]: https://ko-fi.com/miztiik
