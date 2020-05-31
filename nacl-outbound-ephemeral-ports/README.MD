# 👮 AWS Security - Why add Ephemeral ports to NACL

Recently, I was asked why do we need to add ephemeral ports on NACL?.

![why-add-ephemeral-ports-on-nacl](images/why-add-ephemeral-ports-on-nacl.png)

Follow this article in **[Udemy][101]**

Let us try to understand that with a simple scenario. When you want to visit a webpage you use a browser type in the url, in the background, Your browser(client) sends a request to the website(web-server).

The client that initiates the request chooses the ephemeral port range on which it wants to receive the payload it requested for. The range varies depending on the client's operating system. So, for a web server to work properly, we need to configure appropriate ephemerals ports on the web server.

## Lab Setup

  In this repo, I have included a cloudformation template for a working web server. Go ahead and attach the public subnets to the custom subnet `web broken nacl`. Figure out what it is not working when attached to `web broken nacl` and why it works when attached to the `default nacl`. _Happy Learning_.

## 📌 Who is using this

This Udemy [course][101] uses this repository extensively to teach advanced AWS Cloud Security to new developers, Solution Architects & Ops Engineers in AWS.

### 💡 Help/Suggestions or 🐛 Bugs

Thank you for your interest in contributing to our project. Whether it's a bug report, new feature, correction, or additional documentation or solutions, we greatly value feedback and contributions from our community. [Start here][200]

### 👋 Buy me a coffee

Buy me a [coffee ☕][900].

### 📚 References

1. [Custom Network ACLs & Ephemeral Ports][1]
1. [Host a website on an EC2 instance][2]

### 🏷️ Metadata

**Level**: 100

[1]: https://docs.aws.amazon.com/en_pv/vpc/latest/userguide/vpc-network-acls.html#nacl-ephemeral-ports

[2]: https://aws.amazon.com/premiumsupport/knowledge-center/connect-http-https-ec2/

[100]: https://www.udemy.com/course/aws-cloud-security/?referralCode=B7F1B6C78B45ADAF77A9

[101]: https://www.udemy.com/course/aws-cloud-security-proactive-way/?referralCode=71DC542AD4481309A441

[102]: https://www.udemy.com/course/aws-cloud-development-kit-from-beginner-to-professional/?referralCode=E15D7FB64E417C547579

[103]: https://www.udemy.com/course/aws-cloudformation-basics?referralCode=93AD3B1530BC871093D6

[200]: https://github.com/miztiik/dev-sec-ops/issues

[899]: https://www.udemy.com/user/n-kumar/

[900]: https://ko-fi.com/miztiik
