# 👮AWS Security: Content Filtering & Domain Whitelisting with Squid proxy

Limiting outbound traffic to trusted domains (called `whitelisting`) prevent instances from downloading malware, communicating with bot networks.  You will learn how to limit outbound web connections from your VPC to the internet, using a web proxy with custom domain whitelists or DNS content filtering services.

![AWS Security](images/domain-whitelisting.png)

1. ## Prerequisites

    This demo, instructions, scripts and cloudformation template is designed to be run in `us-east-1`. With few modifications you can try it out in other regions as well(_Not covered here_).

    - AWS CLI pre-configured - [Get help here](https://youtu.be/TPyyfmQte0U)


1. ## Deployment

      Use the cloudformation template here in the repo and deploy using cli,

    ```bash
    aws cloudformation deploy \
        --template-file ./templates/vpc_bastion_private_instance.json \
        --stack-name "MiztiikAutomationNetWorkStack" \
        --capabilities CAPABILITY_IAM
    ```

    ```bash
    aws cloudformation deploy \
        --template-file ./templates/content-filtering-with-proxy.yaml \
        --stack-name "MiztiikAutomationProxyStack" \
        --capabilities CAPABILITY_IAM
    ```

1. ## Testing the solution

    1. Connect to Bastion
    1. Copy your Private Instance SSH key to Bastion
    1. Connect to Secure Instance from Bastion
    1. `curl` any website - It should fail
    1. Set the proxy url from cloudformation outputs in `MiztiikAutomationProxyStack`
    1. `curl` for `whitelisted` domains
    1. `curl` for _non-whitelisted_ domains: This should throw `Access Denied.` error 


1. ## CleanUp

    If you want to destroy all the resources created by the stack, Execute the below command to delete the stack, or _you can delete the stack from console as well_

    ```bash
    # Delete the CF Stack
    aws cloudformation delete-stack \
        --stack-name "MiztiikAutomationProxyStack" \
        --region "${AWS_REGION}"
    aws cloudformation delete-stack \
        --stack-name "MiztiikAutomationNetWorkStack" \
        --region "${AWS_REGION}"
    ```

    This is not an exhaustive list, please carry out other necessary steps as maybe applicable to your needs.

## Buy me a coffee

Buy me a coffee ☕ through [Paypal](https://paypal.me/valaxy), _or_ You can reach out to get more details through [here](https://youtube.com/c/valaxytechnologies/about).

### References

1. [VPC Egress Control](https://aws.amazon.com/answers/networking/controlling-vpc-egress-traffic/)

1. [Squid](http://www.squid-cache.org/)

### Metadata

**Level**: 200