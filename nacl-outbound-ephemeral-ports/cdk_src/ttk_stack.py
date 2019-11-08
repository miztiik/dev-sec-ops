from aws_cdk import(aws_ec2 as ec2, core)

class TtkStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, ** kwargs) -> None:
        super().__init__(scope, id, ** kwargs)

        vpc = ec2.Vpc(
                self, "MyVpc",
                cidr="10.13.0.0/21",
                max_azs=2,
                nat_gateways=0,
                subnet_configuration=[
                    ec2.SubnetConfiguration(name="pubSubnet", cidr_mask=24, subnet_type=ec2.SubnetType.PUBLIC),
                    # ec2.SubnetConfiguration(name="private", cidr_mask=24, subnet_type=ec2.SubnetType.PRIVATE)
                    # ec2.SubnetConfiguration(name="private", cidr_mask=24, subnet_type=ec2.SubnetType.ISOLATED)
                ]
            )
        
        # Tag all VPC Resources
        core.Tag.add(vpc,key="Owner",value="KonStone",include_resource_types=[])

        # We are using the latest AMAZON LINUX AMI
        ami_id = ec2.AmazonLinuxImage(generation = ec2.AmazonLinuxGeneration.AMAZON_LINUX_2).get_image(self).image_id

        # Lets add a security group for port 80
        web_sg = ec2.SecurityGroup(self,
            "web_sec_grp",
            vpc = vpc,
            description="Allow internet access from the world",
            allow_all_outbound = True
        )
        web_sg.add_ingress_rule(ec2.Peer.any_ipv4(), 
            ec2.Port.tcp(80),
            "Allow internet access from the world."
        )

        broken_nacl = ec2.NetworkAcl(self,
            "web_broken_nacl",
            vpc = vpc
        )

        # Enable below section to break web server
        """
        broken_nacl.associate_with_subnet("web_broken_nacl",
            subnets = [vpc.public_subnets[0]]
            # subnet_type = ec2.SubnetType.PUBLIC
        )
        """

        broken_nacl.add_entry("broken_nacl_in_rule_120",
            cidr = ec2.AclCidr.any_ipv4(),
            rule_number = 120,
            traffic = ec2.AclTraffic.tcp_port(80),
            direction = ec2.TrafficDirection.INGRESS,
            rule_action = ec2.Action.ALLOW
        )
        broken_nacl.add_entry("broken_nacl_out_rule_120",
            cidr = ec2.AclCidr.any_ipv4(),
            rule_number = 120,
            # traffic = ec2.AclTraffic.all_traffic(),
            traffic = ec2.AclTraffic.tcp_port(80),
            # traffic = ec2.AclTraffic.tcp_port_range(0, 65535),
            direction = ec2.TrafficDirection.EGRESS,
            rule_action = ec2.Action.ALLOW
        )

        with open("./bootstrap_scripts/httpd.sh", mode = 'rb') as file:
            data = file.read()
        httpd = ec2.UserData.for_linux()
        httpd.add_commands(str(data, 'utf-8'))

        # We define instance details here
        web_inst = ec2.CfnInstance(self,
            "web-instance",
            image_id = ami_id,
            instance_type = "t2.micro",
            monitoring = False,
            tags = [{
                "key": "Name",
                "value": "KonStone-Web-instance"
            }],
            network_interfaces = [{
                "deviceIndex": "0",
                "associatePublicIpAddress": True,
                "subnetId": vpc.public_subnets[0].subnet_id,
                "groupSet": [web_sg.security_group_id]
            }], #https: //github.com/aws/aws-cdk/issues/3419
            user_data = core.Fn.base64(httpd.render())
        )
        core.Tag.add(web_inst,key="Owner",value="KonStone",include_resource_types=[])