# AWS Security - Automate Cloudtrail Monitoring, Alerting & Enabling

  Learn how to automatically detect cloudtrail `disabling` event, `alert` your security team and `re-enable` the trail automatically
  
  ![Automate Cloudtrail Monitoring, Alerting & Enabling
](images/miztiik_github_security_cloudtrail_auto_enabling.png)

  Follow this article in **[Youtube](https://youtu.be/a4gOXBrVe6w)**

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

### Buy me a coffee

Buy me a coffee ☕ here `https://paypal.me/valaxy`, _or_ You can reach out to get more details through [here](https://youtube.com/c/valaxytechnologies/about).

#### References

1. [Recover Lost Key Pair of AWS EC2 using Userdata](https://www.youtube.com/watch?v=Bqt538HRsws)
1. [Recover Key Pair of AWS EC2](https://www.youtube.com/watch?v=5btWXn4yWzQ)

### Metadata

**Level**: 100
