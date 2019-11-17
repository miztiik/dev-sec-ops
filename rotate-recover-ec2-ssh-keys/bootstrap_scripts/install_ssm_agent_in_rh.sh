#!/bin/bash -xe

# Lets log everything to console for being lazy (not recommended)
exec > >(tee /var/log/user-data.log|logger -t user-data -s 2>/dev/console) 2>&1

#install httpd
yum install httpd ec2-instance-connect -y

mkdir -p /tmp/ssm \
    && yum install -y curl \
    && curl https://s3.amazonaws.com/ec2-downloads-windows/SSMAgent/latest/linux_amd64/amazon-ssm-agent.rpm -o /tmp/ssm/amazon-ssm-agent.rpm \
    && sudo yum install -y /tmp/ssm/amazon-ssm-agent.rpm \
    && sudo systemctl restart amazon-ssm-agent