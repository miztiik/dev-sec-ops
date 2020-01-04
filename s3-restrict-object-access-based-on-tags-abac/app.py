#!/usr/bin/env python3

from aws_cdk import core

from s3_restrict_object_access_based_on_tags_abac.s3_restrict_object_access_based_on_tags_abac_stack import S3RestrictObjectAccessBasedOnTagsAbacStack


app = core.App()
S3RestrictObjectAccessBasedOnTagsAbacStack(
    app, 
    "s3-restrict-object-access-based-on-tags-abac"
)


# Params and stage info
service = app.node.try_get_context('service_name')



# Tag the stack resources
core.Tag.add(app,key="Owner",value=app.node.try_get_context('owner'))
core.Tag.add(app,key="OwnerProfile",value=app.node.try_get_context('github_profile'))
core.Tag.add(app,key="ToKnowMore",value=app.node.try_get_context('youtube_profile'))


app.synth()
