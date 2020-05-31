# Reference Urls

Follow this article in **[Udemy][101]**

|Section|Lecture|NIST Control|Reference Urls|
|-|-|-|-|
|1|1|Detective Controls: Introduction|[AWS Config: What Is It?]()|
|1|2|Detective Controls: Introduction|[AWS Config: How It Works?]()|
|1|3|Detective Controls: Introduction|[AWS Config: Introduction to Config Rules]()|
|1|4|Detective Controls: Introduction|[AWS Config: How to configure Config Rules]()|
|1|5|Detective Controls: Introduction|[AWS Config: Identify Non Compliant Rules & Resources]()|
|1|6|Detective Controls: Introduction|[AWS Config: Introduction to Advanced Querying]()|
|1|7|Detective Controls: Introduction|[AWS Config: Advanced Querying In Action]()|
|1|8|Detective Controls: Introduction|[AWS Config: Introduction to Multi Account Aggregators]()|
|1|9|Detective Controls: Introduction|[AWS Config: Aggregators In Action]()|
|2|1|Reactive Controls: Automatically Remediate Non Compliant Resources|[Introduction to Auto Remediation]()|
|2|2|Reactive Controls: Automatically Remediate Non Compliant Resources|[Automatically Enforce S3 Bucket Versioning](https://github.com/miztiik/dev-sec-ops/blob/master/aws-config-auto-remediation/templates/S3_BUCKET_VERSIONING_ENABLED.template)|
|2|3|Reactive Controls: Automatically Remediate Non Compliant Resources|[Automatically Enforce S3 Bucket Encryption](https://github.com/miztiik/dev-sec-ops/blob/master/aws-config-auto-remediation/templates/S3_BUCKET_SERVER_SIDE_ENCRYPTION_ENABLED.template)|
|2|4|Reactive Controls: Automatically Remediate Non Compliant Resources|[Automatically Enforce 'No Public IPs for EC2 Instances' Policy](https://github.com/miztiik/dev-sec-ops/blob/master/aws-config-auto-remediation/templates/EC2_INSTANCE_NO_PUBLIC_IP.template)|
|2|5|Reactive Controls: Automatically Remediate Non Compliant Resources|[Automatically Enforce AMI ID Compliance for all EC2 Instances](https://github.com/miztiik/dev-sec-ops/blob/master/aws-config-auto-remediation/templates/APPROVED_AMIS_BY_ID.template)|
|2|6|Reactive Controls: Automatically Remediate Non Compliant Resources|[Automatically Enforce compliance to AMI ID by Tags for all EC2 Instances](https://github.com/miztiik/dev-sec-ops/blob/master/aws-config-auto-remediation/templates/APPROVED_AMIS_BY_TAG.template)|
|2|7|Reactive Controls: Automatically Remediate Non Compliant Resources|[AWS Config: Tribal Knowledge - Common Rules & Best Practices](https://aws.amazon.com/blogs/mt/aws-config-best-practices/)|
|2|8|Reactive Controls: Automatically Remediate Non Compliant Resources|[AWS Config: Introduction to Custom Rules](https://aws.amazon.com/blogs/mt/how-to-develop-custom-aws-config-rules-using-the-rule-development-kit/)|
|2|9|Reactive Controls: Automatically Remediate Non Compliant Resources|[Monitor & Flag Unused IAM Roles using Config Custom Rules](https://github.com/miztiik/serverless-monitor-for-unused-iam-roles)|
|2|10|Reactive Controls: Automatically Remediate Non Compliant Resources|[Monitor & Flag Users With Excessive Privileges](https://github.com/miztiik/security-automation-monitor-users-with-excessive-privileges)|
|3|1|Proactive Security Controls|[Automatically Remediate AWS Cloutrail Disabling: Monitor, Alert, ReEnable](https://github.com/miztiik/dev-sec-ops/tree/master/automate-cloudtrail-monitoring-alerting-enabling)|
|3|2|Proactive Security Controls|[Monitor & Automatically Revoke Unintended IAM Access](https://github.com/miztiik/dev-sec-ops/tree/master/remove-unused-security-groups)|
|3|3|Proactive Security Controls|[Automatically Remove Unused Security Groups](https://github.com/miztiik/dev-sec-ops/tree/master/remove-unused-security-groups)|
|3|4|Proactive Security Controls|[Proactively monitor & fix bad or overly permissive S3 Object ACLs](https://github.com/miztiik/security-automation-remediate-weak-s3-policy)|
|3|5|Proactive Security Controls|[Proactively monitor and fix bad or overly permissive S3 Bucket Policies](https://github.com/miztiik/security-automation-remediate-unintended-s3-object-acl)|
|3|6|Proactive Security Controls|[Proactively monitor and respond to failed SSH logins to EC2 Instances](https://github.com/miztiik/security-automation-respond-to-failed-ssh-access)|
|3|7|Proactive Security Controls|[Automatically rotate EC2 SSH keys for ALL your instances reliably](https://github.com/miztiik/dev-sec-ops/tree/master/rotate-recover-ec2-ssh-keys)|
|3|8|Proactive Security Controls|[Proactively Block S3 Public Access At Scale](https://aws.amazon.com/blogs/aws/amazon-s3-block-public-access-another-layer-of-protection-for-your-accounts-and-buckets/)|
|3|9|Proactive Security Controls|[Attribute Based Access Control: Proactively Restrict S3 Access based on UserTags](https://github.com/miztiik/dev-sec-ops/tree/master/s3-restrict-object-access-based-on-tags-abac)|
|3|10|Proactive Security Controls|[Attribute Based Access Control: Proactively Restrict Access To EC2 Based On Tags](https://github.com/miztiik/attribute-based-access-control-ec2)|
|4|1|Proactive Security Controls: Taking it to the next level|[Learn how to create fine grained permissions like a PRO](http://policysim.aws.amazon.com/home/index.jsp)|
|4|2|Proactive Security Controls: Taking it to the next level|[Use AWS Secrets Manager to secure database credentials and retrieve from lambda](https://github.com/miztiik/dev-sec-ops/tree/master/AWS-SecretsManager-Lambda-RDS)|
|4|3|Proactive Security Controls: Taking it to the next level|[Use an outbound VPC proxy for domain whitelisting and content filtering](https://github.com/miztiik/dev-sec-ops/tree/master/content-filtering-with-proxy)|
|4|4|Proactive Security Controls: Taking it to the next level|[Use AWS IAM Access Analyzer to Identify Unintended Resource Access](https://docs.aws.amazon.com/IAM/latest/UserGuide/what-is-access-analyzer.html)|
|4|5|Proactive Security Controls: Taking it to the next level|[Automatically respond to DDoS Attacks with Web Application Firewall(WAF)](https://github.com/miztiik/dev-sec-ops/blob/master/waf_rate_limit_tester.sh)|
|4|6|Proactive Security Controls: Taking it to the next level|[Detect EC2 Instance Credential Abuse](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_unauthorized.html#unauthorized11)|
|4|7|Proactive Security Controls: Taking it to the next level|[Automatically respond to EC2 Instance Credential Abuse - Part 01 of 02](https://github.com/miztiik/security-incident-response-instance-isolation)|

## 📌 Who is using this

This Udemy [course][101] uses this repository extensively to teach advanced AWS Cloud Security to new developers, Solution Architects & Ops Engineers in AWS.

### 💡 Help/Suggestions or 🐛 Bugs

Thank you for your interest in contributing to our project. Whether it's a bug report, new feature, correction, or additional documentation or solutions, we greatly value feedback and contributions from our community. [Start here][200]

### 👋 Buy me a coffee

Buy me a [coffee ☕][900].

### 📚 References

1. [Fan Following][899]

### 🏷️ Metadata

**Level**: 100

[1]: https://github.com/miztiik/serverless-janitor-for-security-groups

[100]: https://www.udemy.com/course/aws-cloud-security/?referralCode=B7F1B6C78B45ADAF77A9

[101]: https://www.udemy.com/course/aws-cloud-security-proactive-way/?referralCode=71DC542AD4481309A441

[102]: https://www.udemy.com/course/aws-cloud-development-kit-from-beginner-to-professional/?referralCode=E15D7FB64E417C547579

[103]: https://www.udemy.com/course/aws-cloudformation-basics?referralCode=93AD3B1530BC871093D6

[200]: https://github.com/miztiik/dev-sec-ops/issues

[899]: https://www.udemy.com/user/n-kumar/

[900]: https://ko-fi.com/miztiik
