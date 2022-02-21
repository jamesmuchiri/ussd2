from flask import Flask, request
import africastalking
import os
import re
import maya
from maya import MayaInterval
from datetime import datetime
import datetime as dt
from dateutil.parser import parse
import mysql.connector
from flask import make_response
app = Flask(__name__)


username = "sandbox"
api_key = "0f54c06969af94baa76c50efbcc1daaecb9b75f254d3388c85edfd9d21ff7ad0"
africastalking.initialize(username, api_key)

sms = africastalking.SMS

    
@app.route('/', methods=['POST', 'GET'])


def Callback():
    global menu_text 
     
    phone_number = request.values.get("phoneNumber","default")
    text = request.values.get("text","default")
    text_array = text.split("*")
    user_response = text_array[len(text_array) - 1]
            
            

    if user_response == "":       
        kenya_time = datetime.datetime.utcnow() + datetime.timedelta(hours=3)
        if 5<= kenya_time <12 :
            Good_Morning="Good Morning"
            menu_text =("CON {}"
                        "\nHow may i help you"
                        "\n  -Limit "
                        "\n  -Balance"
                        "\n  -Loan"
                        "\n  -Amount"
            ).format(Good_Morning)
        elif  12 <= kenya_time < 17 :
            Good_Afternoon="Good Afternoon"
            menu_text =("CON {}"
                        "\nHow may i help you"
                        "\n  -Limit "
                        "\n  -Balance"
                        "\n  -Loan"
                         "\n  -Amount"
                    ).format(Good_Afternoon)
        else:
            Good_Evening="Good Evening"
            menu_text =("CON {}"
                        "\nHow may i help you"
                        "\n  -Limit "
                        "\n  -Balance"
                        "\n  -Loan"
                        "\n  -Amount"
                    ).format(Good_Evening)
    return menu_text

    
      
    

        
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=os.environ.get("PORT"))
