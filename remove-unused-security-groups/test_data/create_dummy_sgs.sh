#!/bin/bash
set -ex

vpc_to_spam="vpc-075b9ed4763eba394"
for i in {1..3}
    do
       val="${RANDOM}"
       aws ec2 create-security-group \
           --vpc-id  "${vpc_to_spam}" \
           --group-name "sg_group_name_${val}" \
           --description "My security group_${val}"
    done
