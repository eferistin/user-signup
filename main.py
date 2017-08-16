from flask import Flask, request, redirect, render_template
# import cgi
# import os
# import jinja2

# template_dir = os.path.join(os.path.dirname(__file__), 'templates')
# jinja_env= jinja2.Environment( loader = jinja2.FileSystemLoader(template_dir), autoescape=True )

app= Flask(__name__)
app.config['DEBUG']=True

@app.route("/")
def mydefault():
    return render_template("login_form.html")

@app.route("/login_form", methods= ['POST'])
def index():
    if request.method=="POST":
        user_name= request.form['user']
        user_password= request.form['secret']
        user_password_verify= request.form['vsecret']
        user_email= request.form['the_email']
    else:
        user_name= request.args.get('user')
        user_password= request.args.get('secret')
        user_password_verify= request.args.get('vsecret')
        user_email= request.args.get('the_email')  
        
    n_error=""
    p_error=""
    v_p_error=""
    em_error=""

    myname=""
    myemail=""
    login="Success"

    if " " in user_name:
        n_error="In valid, spaces are not allowed."
            
    elif len(str(user_name))>20 or len(str(user_name))< 3:
        n_error ="In valid, length must be between 3 and 20 characters."
        login="Fail"
    else:
        myname=user_name 
  
    if len(str(user_password))>20 or len(str(user_password))< 3:
        p_error ="In valid, length must be between 3 and 20 characters."
        login="Fail"

    if " " in user_password:
        p_error = "In valid, spaces are not allowed."
        login="Fail"

    if user_password != user_password_verify:
        v_p_error= "Passwords do not match." 
        login="Fail"

    if user_email !="":
        if "@" not in user_email or "." not in user_email:
            em_error = "Not a valid email address."
            login="Fail"

        if " " in user_email:
            em_error ='In valid, spaces are not allowed.'
            login="Fail"
                
        if len(str(user_email))>20 or len(str(user_email))< 3:
            em_error ='Invalid, length must be between 3 and 20 characters.'
            login="Fail"
        else:
            myemail=user_email
        
    if login=="Fail":
            return render_template('login_form.html', user_error=n_error,password_error=p_error,password_ver_error=v_p_error,email_error=em_error)

    if login=="Success":
        return render_template('welcome.html', user=myname)

app.run()