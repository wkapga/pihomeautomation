#!/usr/bin/env python2

# A CGI dispatcher written in Python by Liam Fraser for a Linux User and
# Developer tutorial.
import cgi, cgitb

from time import gmtime, strftime

cgitb.enable()

def print_page(title, body):
    # Tell the web server to expect content
    print "Content-Type: text/html\n"
    print
    
    print """\
<html>
<head>
<title>{0}</title>
</head>
<body>
<h1>{0}</h1>
{1}
<p><a href="menu.cgi">Return to Menu</a></p>
</body>
</html>
""".format(title, body)

def print_menu():
    # Print a menu
    title = " Raspberry Pi Menu"
    body = """
<p><a href="menu.cgi?action=displaytime">display current time</a></p>
<p><a href="menu.cgi?action=clear">Clear Screen</a></p>
"""
    print_page(title, body)


#print_menu()
    

#
# Start of script
if __name__ == "__main__":

    # Get any parameters
    params = cgi.FieldStorage()

    # Variable to keep track of if we have a valid input or not
    valid = False
    
    # If we have a key called action in the params
    if params.getvalue("action"):
        action = params.getvalue("action")

        if action == "displaytime":
            valid = True
            jtzt =  strftime("%Y-%m-%d %H:%M:%S")
            print_page("Time",jtzt)
        elif action == "clear":
            valid = True
            print_page("screen cleared","sreen ceared, totally")
    if valid == False:
        print_menu()


