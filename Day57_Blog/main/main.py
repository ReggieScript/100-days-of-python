from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def home():
    blog_data = requests.get(url = "https://api.npoint.io/c790b4d5cab58020d391").json()
    return render_template("index.html", posts = blog_data)

@app.route("/blog/<num>")
def get_blog(num):
    blog_data = requests.get(url = "https://api.npoint.io/c790b4d5cab58020d391").json()
    blog = blog_data[int(num-1)]
    return render_template("post.html", blog_post = blog)

if __name__ == "__main__":
    app.run(debug=True)
