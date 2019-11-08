# AWS Security
Recently, I was asked why do we need to add ephemeral ports on NACL?. 

![](images/why-add-ephemeral-ports-on-nacl.png)

Let us try to understand that with a simple scenario. When you want to visit a webpage you use a browser type in the url, in the background, Your browser(client) sends a request to the website(web-server). 

The client that initiates the request chooses the ephemeral port range on which it wants to receive the payload it requested for. The range varies depending on the client's operating system. So, for a web server to work properly, we need to configure appropriate ephemerals ports on the web server.



