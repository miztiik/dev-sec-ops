#!/usr/bin/env python3

from aws_cdk import core

from rotate_recover_ec2_ssh_keys.rotate_recover_ec2_ssh_keys_stack import RotateRecoverEc2SshKeysStack


app = core.App()
RotateRecoverEc2SshKeysStack(app, "rotate-recover-ec2-ssh-keys")

app.synth()
