# Link Header status
A Python util to test the header status of links.

This class can be used as part of your CI flow to test the link status after a deployment.

example:

```
python link_status.py https://www.example.com "#menu-main-menu li a"

```

It will check the status of all links in #menu-main-menu li a . if its not 200,300 it will throw an exception
