#!/usr/bin/env python3

from aws_cdk import core

from remove_unused_security_groups.remove_unused_security_groups_stack import RemoveUnusedSecurityGroupsStack


app = core.App()
RemoveUnusedSecurityGroupsStack(app, "remove-unused-security-groups")

app.synth()
