#!/bin/bash
# Install Apache Workbench in Amazon Linux
sudo yum install -y https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm
sudo yum -y install httpd-tools curl

webserver_IP=54.165.151.131

# Set API GW Url
attack_url="https://gqks98heme.execute-api.us-east-1.amazonaws.com/prod/pets"

# Confirm API is available
curl $attack_url

# Flood the API
# 3000 Requests simulating 20 concurrent users
ab -n 3000 -c 20 -k $attack_url

# Request page after flooding
curl $attack_url