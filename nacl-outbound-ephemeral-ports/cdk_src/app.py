#!/usr/bin/env python3

from aws_cdk import core

from ttk.ttk_stack import TtkStack


app = core.App()
TtkStack(app, "KonStone")

app.synth()
