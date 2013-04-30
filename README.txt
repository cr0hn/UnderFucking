# What's UndeFucking project?

UnderFucking project wants to be a vulnerable web site as real as possible. 

It's made in Django.

# What vulnerabilities implements?

Currently, only has these features:
- Admin site, with an error when you try to access: /admin
- Directory listing: /home/dir_listing/
- Random page generation: /home/links
- A page with many links, to test spiders: /home/many_links/
- User login page, without any functionality:  /users
- Random 'Server:' field for HTTP response.

# How to run it?

You need to be installed Django in your system. Them, to run the test web site, you must type in your shell:

python manager.py runserver

Now you can connect to the web writting in your browser:

http://127.0.0.1:8080