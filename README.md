# What's UndeFucking?

UnderFucking project wants to be a vulnerable web site as real as possible. 

It's written entirely in Python using the Django framework.

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
