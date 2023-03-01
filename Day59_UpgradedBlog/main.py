from flask import Flask
from flask import render_template
import requests

app = Flask(__name__)

blogs_url = "https://api.npoint.io/54484abb664011e3248c"

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

@app.route("/blog/<num>")
def get_blog(num):
    blog_data = requests.get(url = blogs_url).json()
    blog = blog_data[int(num)-1]
    return render_template("post.html", blog_post = blog, img_url = blog["img"])

# @app.route("/blog")
# def blog_page():
#     blog_data = requests.get(url = "https://api.npoint.io/c790b4d5cab58020d391").json()
#     return render_template("index.html", posts = blog_data)


if __name__ ==  "__main__": ## Checks if this file is the main file.    
    app.run(debug=True)