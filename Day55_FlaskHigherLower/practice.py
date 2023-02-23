from flask import Flask

app = Flask(__name__)


def make_bold(function):
    def warp_fun():
        return f"<b>{function()}</b>"
    return warp_fun

def make_italics(function):
    def warp_fun():
        return f"<i>{function()}</i>"
    return warp_fun

def make_sub(function):
    def warp_fun():
        return f"<u>{function()}</u>"
    return warp_fun

@app.route("/")
def hello_world():
    return "Hello, World!"

@app.route("/bye")
@make_bold
@make_italics
@make_sub
def bye_world():
    return "Bye, World!"

if __name__ ==  "__main__": ## Checks if this file is the main file.    
    app.run(debug=True)
