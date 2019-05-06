from flask import Flask, request, redirect, render_template
import cgi
import os
import re

app = Flask (__name__)
app.config['DEBUG'] = True


#This method is to render the page called "form" through flask 

@app.route("/form", methods = ["GET"])
def form():  
    return render_template("form.html", title="Signup")  


#This method is to retrive information from the user to be validated through flask 
@app.route("/form", methods = ["POST"])
def validate_input():
    username = request.form["username"]
    password = request.form["password"]
    verify_password = request.form["verify_password"]
    email = request.form["email"]


    username_error=""
    password_error=""
    verify_password_error=""
    email_error=""

#Username Validation

    if username == "":
        username_error = "Please enter a valid username."
    elif len(username) <= 3 or len(username) >= 20:
        username_error = "Username must be between a minimum of 3 characters and not more than 20."
        username = ""
    elif "." in username:
	    username_error = "Please enter a username without a period."
	    username = ""
    elif " " in username:
        username_error = "Please enter a username without spaces."
        username = ""

#Password Validation

    if password == "":
	    password_error = "Please enter a valid password."
    elif len(password) <= 3 or len(password) > 20:
	    password_error = "Passwords must be between a minimum of 3 characters and not more than 20."
    elif " " in password:
	    password_error = "Passwords cannot contain spaces."
    if verify_password == "" or verify_password != password:
	    verify_password_error = "Password do not match, please re-enter."
	    verify_password = ""



#Email Validation

    if email != "":
	    user_error = "Please enter a valid password, or leave blank"
	    if not re.match(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", email):
	        email_error = "Invalid email address, either provide a valid address or leave blank"


    if not username_error and not password_error and not verify_password_error and not email_error:
	    return render_template("welcome.html", username=username)
    else:
	    return render_template("form.html", username_error=username_error, password_error=password_error, verify_password_error=verify_password_error, email_error=email_error,  title="Signup")




    
app.run()