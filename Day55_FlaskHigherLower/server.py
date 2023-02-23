from flask import Flask
import random

random_number=random.randint(0,9)

app = Flask(__name__)


@app.route("/")
def main_page():
    return "<h1>Guess a number between 0 and 9</h1>\
        <img src='https://media.giphy.com/media/CjmvTCZf2U3p09Cn0h/giphy.gif'>"

@app.route("/<int:number>")
def check_num(number):
    if number < random_number:
        return "<h1>Sorry, the number was too low.</h1>\
                <img src = 'https://media.giphy.com/media/M9yC8b0x7Y7oA/giphy.gif'>"
    if number > random_number:
        return "<h1>Sorry, the number was too high.</h1>\
                <img src = 'https://media1.giphy.com/media/UHDB3gcgTHKotMQHiA/giphy.gif?cid=ecf05e47nlvjrtlv24vk21rqqozg6198bh11hnymbpl4yv5k&rid=giphy.gif&ct=g'>"
    if number == random_number:
        return "<h1>Perfect!</h1>\
                <img src = 'https://media.giphy.com/media/GeimqsH0TLDt4tScGw/giphy.gif'>"

if __name__ ==  "__main__": ## Checks if this file is the main file.    
    app.run(debug=True)