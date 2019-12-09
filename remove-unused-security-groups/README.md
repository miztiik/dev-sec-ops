
# Security: Automatically remove unused old security groups using AWS Lambda

Maintaing security groups across multiple VPCs, regions, accounts is quite an time consuming effort. I decided to automate this, with an lambda.

![Automatically removed unused old security groups](images/miztiik_automatically_remove_security_groups.png)

Follow this article in **[Youtube](https://youtu.be/MhFlNOdMfRo)**

## Lambda Functionality

The following actions are performed by the lambda

1. Make a list of security groups
1. Remove the ones used by ec2 instances
1. Removed the excluded security group
1. Return a list of `security_group_ids` deleted
1. Cloudwatch events is configured to trigger this lambda once every week.

It is quite extensible, you can programatically add to exclude list or process the deleted ids in another automation task.

## Lab Setup

  In this repo, I have included a cloudformation template(look for `/cdk.out/remove-unused-security-groups.template.json`) that provisions all the necessary resources.

- Lambda to delete security groups
- IAM Role for the lambda execution
  - Necessary permissions for the lambda
  - _If your lambda is timing out, increase the duration_

## Test

I have included a simple script `test_data/create_dummy_sgs.sh`. Update the `vpc_to_spam` variable to match yours and run it to create some dummy sgs. Run the lambda function in the console and check the logs.

### Buy me a coffee

Buy me a coffee ☕ here `https://paypal.me/valaxy`, _or_ You can reach out to get more details through [here](https://youtube.com/c/valaxytechnologies/about).

#### References

1. [AWS Serverless Janitor for launch-wizard Security Groups](https://github.com/miztiik/serverless-janitor-for-security-groups)

### Metadata

**Level**: 200
