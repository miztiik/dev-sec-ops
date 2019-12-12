# AWS Security - Why add Ephemeral ports to NACL?

Recently, I was asked why do we need to add ephemeral ports on NACL?.

![why-add-ephemeral-ports-on-nacl](images/why-add-ephemeral-ports-on-nacl.png)

Follow this article in **[Youtube](https://youtu.be/MhFlNOdMfRo)**

Let us try to understand that with a simple scenario. When you want to visit a webpage you use a browser type in the url, in the background, Your browser(client) sends a request to the website(web-server). 

The client that initiates the request chooses the ephemeral port range on which it wants to receive the payload it requested for. The range varies depending on the client's operating system. So, for a web server to work properly, we need to configure appropriate ephemerals ports on the web server.

## Lab Setup

  In this repo, I have included a cloudformation template for a working web server. Go ahead and attach the public subnets to the custom subnet `web broken nacl`. Figure out what it is not working when attached to `web broken nacl` and why it works when attached to the `default nacl`. _Happy Learning_.

### Buy me a coffee

Buy me a coffee ☕ here `https://paypal.me/valaxy`, _or_ You can reach out to get more details through [here](https://youtube.com/c/valaxytechnologies/about).

#### References

1. [Custom Network ACLs & Ephemeral Ports](https://docs.aws.amazon.com/en_pv/vpc/latest/userguide/vpc-network-acls.html#nacl-ephemeral-ports)
1. [Host a website on an EC2 instance](https://aws.amazon.com/premiumsupport/knowledge-center/connect-http-https-ec2/)

### Metadata

**Level**: 100
