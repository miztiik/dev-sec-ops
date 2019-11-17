from aws_cdk import (
    aws_ec2 as ec2,
    aws_iam as iam,
    core
)

class RotateRecoverEc2SshKeysStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # The code that defines your stack goes here
        vpc = ec2.Vpc(
                self, "MyVpc",
                cidr="10.13.0.0/21",
                max_azs=2,
                nat_gateways=0,
                subnet_configuration=[
                    ec2.SubnetConfiguration(name="pubSubnet", cidr_mask=24, subnet_type=ec2.SubnetType.PUBLIC),
                ]
            )
        
        # Tag all VPC Resources
        core.Tag.add(vpc,key="Owner",value="KonStone",include_resource_types=[])

        # We are using the latest AMAZON LINUX AMI
        amzn_ami_id = ec2.AmazonLinuxImage(generation = ec2.AmazonLinuxGeneration.AMAZON_LINUX_2).get_image(self).image_id
        # https://access.redhat.com/articles/4297201
        rh_ami_id = "ami-0c322300a1dd5dc79"

        high_perf_sg = ec2.SecurityGroup(self,
            "web_sec_grp",
            vpc = vpc,
            description="Allow internet access from the world",
            allow_all_outbound = True
        )
        high_perf_sg.add_ingress_rule(ec2.Peer.any_ipv4(), 
            ec2.Port.tcp(22),
            "Allow internet access from the world."
        )

        # https://docs.aws.amazon.com/cdk/api/latest/python/aws_cdk.aws_iam/Role.html
        ssmRoleForEC2 = iam.Role(
            self,
            'ec2ssmroleid',
            assumed_by=iam.ServicePrincipal('ec2.amazonaws.com'),
            role_name="ssmRoleForEC2Name"
        )

        ssmRoleForEC2.add_managed_policy(
            iam.ManagedPolicy.from_aws_managed_policy_name('AmazonSSMManagedInstanceCore')
        )

        inst_profile_01 = iam.CfnInstanceProfile(
            self,
            "instProfile01Id",
            roles=[ssmRoleForEC2.role_name],
        )

        # Update your key-name
        ssh_key_name = "virk"


        with open("./bootstrap_scripts/install_ssm_agent_in_rh.sh", mode = 'rb') as file:
            data = file.read()
        install_ssm_agent = ec2.UserData.for_linux()
        install_ssm_agent.add_commands(str(data, 'utf-8'))

        # We define instance details here
        web_inst_01 = ec2.CfnInstance(self,
            "webinstance01",
            image_id = rh_ami_id,
            instance_type = "t2.micro",
            monitoring = False,
            # key_name = ssh_key_name,
            network_interfaces = [{
                "deviceIndex": "0",
                "associatePublicIpAddress": True,
                "subnetId": vpc.public_subnets[0].subnet_id,
                "groupSet": [high_perf_sg.security_group_id]
            }],
            iam_instance_profile = inst_profile_01.ref,
            user_data = core.Fn.base64(install_ssm_agent.render()),
            #https: //github.com/aws/aws-cdk/issues/3419
            tags=[core.CfnTag(key="Name", value=f"KonStone-Stack")]
        )

        # https://docs.aws.amazon.com/cdk/api/latest/python/modules.html
        output1 = core.Fn.get_att(logical_name_of_resource="webinstance01",attribute_name="PublicIp")
        core.CfnOutput(self,
            "web_inst_01",
            value=output1.to_string(),
            description="Web Server Public IP"
        )

