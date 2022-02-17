from flask import Flask, request
import africastalking
import os
import variables
import re
import maya
from maya import MayaInterval
from datetime import datetime
from dateutil.parser import parse

app = Flask(__name__)

username = "sandbox"
api_key = "0f54c06969af94baa76c50efbcc1daaecb9b75f254d3388c85edfd9d21ff7ad0"
africastalking.initialize(username, api_key)

sms = africastalking.SMS

@app.route('/', methods=['POST', 'GET'])

def callback():

    session_id = request.values.get("sessionId", None)
    service_code = request.values.get("serviceCode", None)
    phone_number = request.values.get("phoneNumber", None)
    text = request.values.get("text")
    phone_number = []
    phone_number.append(phone_number)

    
    if text == "" and variables.responded_A == False:
        now = maya.MayaDT.from_datetime(datetime.utcnow())
        Time_zone = now.hour +3

        if 5<= Time_zone <12 :
            Good_Morning="Good Morning"
            variables.response =("CON {}🌅 \nWelcome to Nav Healthcare Services"
                                "\nHow may i help you"
                                "\n  1.Book an appointmet"
                                "\n  2.Diagnosis"
            ).format(Good_Morning)

        elif  12 <= Time_zone < 17 :
            Good_Afternoon="Good Afternoon"
            variables.response =("CON {}🌄 \nWelcome to Nav Healthcare Services"
                                "\nHow may i help you"
                                "\n  1.Book an appointmet"
                                "\n  2.Diagnosis"
            ).format(Good_Afternoon)
        else:
            Good_Evening="Good Evening"
            variables.response =("CON {}🌙 \nWelcome to Nav Healthcare Services"
                                "\nHow may i help you"
                                "\n  1.Book an appointmet"
                                "\n  2.Diagnosis"
            ).format(Good_Evening)

    elif text == "1":
        variables.response = "CON First, Whats your name?\n"
        

    elif text is not None:
        text = request.values.get("",text)
        name = text.split("*")
        namef = name[1]

        if not re.match("^[A-z][A-z|\.|\s]+$",namef):
            variables.response = ("CON Invalid name"
                                "\nWhats your name?")


        else:
            text = request.values.get("",text)
            name = text.split("*")
            namef = name[2]
            if not re.match("^[A-z][A-z|\.|\s]+$",namef):
                variables.response = ("END Try aga1n")
            else:
                variables.response=("END Hey👋 {}\nWe are happy to have you😍." 
                ).format(namef)

    else:
        variables.response = "END Invalid input. Try again."  

    return variables.response

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=os.environ.get("PORT"))
