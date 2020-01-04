import boto3
import random
import string
import logging as log
import cfnresponse

log.getLogger().setLevel(log.INFO)

"""
If included in a Cloudformation build as a CustomResource, 
generate a random string of length given by the 'length' parameter. Defaults to 20
By default the character set used is upper and lowercase ascii letters plus digits.
"""

def lambda_handler(event, context):

    log.info(f"Input event: {event}")
    length = 20
    punctuation = False
    rds_compatible = False

    physical_id = "random_string_generator"

    attributes = {
            "random_string": "",
            "message":""
        }

    try:
        # Check if this is a Create and we're failing Creates
        if event['RequestType'] == 'Create' and event['ResourceProperties'].get('FailCreate', False):
            raise RuntimeError('Create failure requested')

        length = int(event['ResourceProperties'].get('Length', 20))
        punctuation = event['ResourceProperties'].get('Punctuation',False)
        rds_compatible = event['ResourceProperties'].get('RDSCompatible',False)

        valid_characters = string.ascii_letters+string.digits

        if punctuation not in [False,'false','False']:
            valid_characters = valid_characters + string.punctuation
        if rds_compatible not in [False,'false','False']:
            valid_characters = valid_characters.translate(None,'@/"')

        random_string = ''.join(random.choice(valid_characters) for i in range(length))
        attributes["random_string"] = random_string
        attributes["message"]= "Successfully generated a random string"

        attributes = {
            'Response': f"{random_string}"
        }
        cfnresponse.send(event, context, cfnresponse.SUCCESS, attributes, physical_id)
    except Exception as e:
        log.exception(e)
        # cfnresponse's error message is always "see CloudWatch"
        cfnresponse.send(event, context, cfnresponse.FAILED, {}, physical_id)