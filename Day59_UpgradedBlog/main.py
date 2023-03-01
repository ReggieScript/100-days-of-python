from flask import Flask
from flask import render_template, request
import requests
import smtplib
import os
import email
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

send_email = os.getenv("MAIL_SEND") 
recieve_email = os.getenv("MAIL_RECIEVE")
password_email = os.getenv("PASSWORD")

blogs_url = "https://api.npoint.io/54484abb664011e3248c"

def send_mail(letter):
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=send_email, password=password_email)
        connection.sendmail(from_addr=send_email, to_addrs=recieve_email, msg=letter)
        connection.close()

@app.route("/")
def main_page():
    blog_data = requests.get(url = blogs_url).json()
    return render_template("index.html", posts=blog_data)

@app.route("/about")
def about_page():
    return render_template("about.html")

@app.route("/contact")
def contact_page():
    return render_template("contact.html")

@app.route("/form-entry", methods = ["POST"])
def success():
    name = request.form["name"]
    email = request.form["email"]
    phone_number = request.form["phone_num"]
    msg = request.form["msg"]
    message = f"Subject: New email from {name}!\n\nName: {name}\nEmail:  {email}\nPhone Number: {phone_number}\nMessage:  {msg}"
    print(message)
    send_mail(message)
    return render_template("success.html")

@app.route("/blog/<num>")
def get_blog(num):
    blog_data = requests.get(url = blogs_url).json()
    blog = blog_data[int(num)-1]
    return render_template("post.html", blog_post = blog, img_url = blog["img"])

if __name__ ==  "__main__": ## Checks if this file is the main file.    
    app.run(debug=True)