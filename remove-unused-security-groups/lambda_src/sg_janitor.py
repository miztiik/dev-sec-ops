# -*- coding: utf-8 -*-
"""
.. module: CleanUp unused security groups in a region using lambda
    :platform: AWS
    :copyright: (c) 2019 Mystique.,
    :license: Apache, see LICENSE for more details.
.. moduleauthor:: Mystique
.. contactauthor:: miztiik@github issues
"""

import boto3
from botocore.exceptions import ClientError
import logging

# Initialize Logger
logger = logging.getLogger()
logger.setLevel(logging.INFO)

def set_global_vars():
    global_vars = {'status': False}
    try:
        global_vars['Owner']                    = "Mystique"
        global_vars['Environment']              = "Prod"
        global_vars['region_name']              = "us-east-1"
        global_vars['tag_name']                 = "serverless_security_group_janitor"
        global_vars['exclude_sgs']               = set(["sg-04f19c7e87bdae9ef", "sg-f8ed38a1", "sg-0266f091db5460f56"])
        global_vars['status']                   = True
    except Exception as e:
        logger.error("Unable to set Global Environment variables. Exiting")
        global_vars['error_message']            = str(e)
    return global_vars

def get_unused_sgs(excluded_sgs: set) -> dict:
    resp_data = {'status': False, 'unused_sg_ids':set, 'error_message': ''}
    try:
        ec2 = boto3.resource('ec2')
        #TODO: Use pagination
        all_sgs = list(ec2.security_groups.all())
        insts = list(ec2.instances.all())
        all_sg_ids = set([sg.id for sg in all_sgs])
        # Make a list of SGs associated with instances
        inst_sg_ids=[]
        for inst in insts:
            for sg_id in inst.security_groups:
                inst_sg_ids.append( sg_id.get('GroupId') )
    except Exception as e:
        resp_data['error_message'] = str(e)
    # Lets unique the list
    inst_sg_ids = set(inst_sg_ids)
    # Unused Security Groups
    unused_sg_ids = all_sg_ids - inst_sg_ids
    # Let removed the excluded ones
    resp_data['unused_sg_ids'] = unused_sg_ids - excluded_sgs
    resp_data['status'] = True
    return resp_data

def janitor_for_security_groups(unused_sgs: dict) -> dict:
    """
    :param unused_sg_ids: Set of unqiue security group ids to be deleted
    :param type: set

    :return: resp_data Return a dictionary of data
    :rtype: json
    """
    sg_deleted = {'status': False, 'TotalSecurityGroupsDeleted':'','SecurityGroupIds': [] }
    ec2 = boto3.client('ec2')
    for sg_id in unused_sgs.get('unused_sg_ids'):
        logging.info(f"Attempting to delete security group: {sg_id}")
        try:
            resp=ec2.delete_security_group(GroupId=sg_id)
            response_code = resp['ResponseMetadata']['HTTPStatusCode']
            if response_code >= 400:
                # logging.error(f"ERROR: {resp}")
                raise ClientError(resp)
            #TODO: Can VPC ID too for more context if requred.
            sg_deleted.get('SecurityGroupIds').append({'SecurityGroupId': sg_id})
        except ClientError as e:
            logging.error(f"ERROR: {str(e.response)}")
            sg_deleted['error_message'] = f"Unable to delete Security Group with id:{sg_id}. ERROR:{str(e)}"
    # Get the count of security groups deleted
    if sg_deleted['SecurityGroupIds']:
        sg_deleted['status'] = True
        sg_deleted['TotalSecurityGroupsDeleted'] = len( sg_deleted['SecurityGroupIds'] )
    else:
        sg_deleted['TotalSecurityGroupsDeleted'] = 0
    return sg_deleted

def lambda_handler(event, context):

    global_vars = set_global_vars()
    resp_data = {"status": False, "error_message" : '' }

    if not global_vars.get('status'):
        resp_data['error_message'] = global_vars.get('error_message')
        return resp_data

    unused_sgs = get_unused_sgs(global_vars.get('exclude_sgs'))
    if not unused_sgs.get('status'):
        resp_data['error_message'] = unused_sgs.get('error_message')
        return resp_data

    deleted_sgs = janitor_for_security_groups(unused_sgs)
    resp_data = deleted_sgs
    return resp_data

if __name__ == '__main__':
    lambda_handler(None, None)