AWS Cloud Deployment Kit (CDK)

1. # Install CDK

  ```sh
  npm install -g aws-cdk
  # Check cdk version
  cdk --version
  ```
1. Initialize new project
  Create a directory to hold our project files and set the language to `python`
  
  ```sh
    mkdir cdk-demos && cd cdk-demos
    cdk init --language python
    # Activate the virtual environment
    source .env/bin/activate
    # Install python modules in virtual env
    # The init command created the requirements.txt file. 
    # CDK is modular, so you will not get everything you need from the core part. 
    # Lets install ec2 package for building a vpc.
    echo "aws-cdk.aws_ec2" >> requirements.txt
    pip install -r requirements.txt
  ```

1. VPC code in CDK
  
  Lets create a sample VPC with 6 subnets spread across 2 AZ's along the required routing table, IGW etc

  ```sh
    vpc = ec2.Vpc(
        stack, "MyVpc",
        cidr="10.13.0.0/21",
        max_azs=2,
        # nat_gateways=1,
        subnet_configuration=[
            ec2.SubnetConfiguration(name="public", cidr_mask=24, subnet_type=ec2.SubnetType.PUBLIC),
            ec2.SubnetConfiguration(name="private", cidr_mask=24, subnet_type=ec2.SubnetType.PRIVATE)
        ]
    )
  ```
1. # Verify & Synthesize Template

    ```sh
    cdk synth
    # To Deploy
    cdk deploy
    ```

1. # Cleanup

  To remove all the resources created by CDK,
  ```
  cdk destroy
  ```
