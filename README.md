# What's UndeFucking?

The UnderFucking project is a web application that implements a series of vulnerabilities and odd behaviors, while at the same time mimicking a real website as much as possible.

Unlike other similar projects, UnderFucking can generate a completely new random website on each invocation. It's also possible to imitate different web servers and technologies.

Its purpose is to test web application security scanners, by feeding them a random but realistic website with a complex layout.

Underfucking is written entirely in Python using the Django framework.

# What vulnerabilities are implemented?

Currently, it only has these features:
- Admin site, with an error when you try to access: /admin
- Directory listing: /home/dir_listing/
- Random page generation: /home/links
- A page with many links, to test spiders: /home/many_links/
- User login page, without any functionality:  /users
- Random 'Server:' field for HTTP response.

However we plan to add many more vulnerabilities and odd behaviors in the near future, stay tuned!

# How to run it?

All dependencies are bundled within the UnderFucking project itself, so you don't need to install anything. 

To run UnderFucking, you must type in your shell:

  python underfucking.py

Now you can connect to the web by pointing your browser to:

  http://127.0.0.1:8080

It's also possible to deploy it as any other Django web application if you want to.
