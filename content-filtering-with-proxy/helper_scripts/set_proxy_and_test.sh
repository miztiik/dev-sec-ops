#!/bin/bash

chmod 700 t.key

# Set Proxy

# Looks for unapproved domains

# Look for approved domains
curl debian.org
curl amazonaws.com

export http_proxy=http://OutboundProxyLoadBalancer-e387454eed647cd1.elb.us-east-1.amazonaws.com:3128 && export https_proxy=$http_proxy

unset http_proxy && unset https_proxy