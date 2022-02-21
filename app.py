from flask import Flask, request
import africastalking
import os
from datetime import datetime
import maya
from maya import MayaInterval
from dateutil.parser import parse
import mysql.connector
from flask import make_response
app = Flask(__name__)


username = "sandbox"
api_key = "0f54c06969af94baa76c50efbcc1daaecb9b75f254d3388c85edfd9d21ff7ad0"
africastalking.initialize(username, api_key)

sms = africastalking.SMS

    
@app.route('/', methods=['POST', 'GET'])

def ussd_callback():
    global response
    session_id = request.values.get("sessionId", None)
    service_code = request.values.get("serviceCode", None)
    phone_number = request.values.get("phoneNumber", None)
    text = request.values.get("text", "default")
    sms_phone_number = []
    sms_phone_number.append(phone_number)

    now = maya.MayaDT.from_datetime(datetime.utcnow())
    kenya_time = now.hour +3
    

    #ussd logic
    
    if text == "":  
        
        if 5<= kenya_time <12 :
            Good_Morning="Good Morning"
            response =("CON {}"
                                        "\nHow may i help you"
                                        "\n  -Limit "
                                        "\n  -Balance"
                                        "\n  -Loan"
                                        "\n  -Amount"
            ).format(Good_Morning)

        elif  12 <= kenya_time < 17 :
            Good_Afternoon="Good Afternoon"
            response =("CON {}"
                                        "\nHow may i help you"
                                        "\n  -Limit "
                                        "\n  -Balance"
                                        "\n  -Loan"
                                        "\n  -Amount"
                    ).format(Good_Afternoon)
        else:
            Good_Evening="Good Evening"
            response =("CON {}"
                                        "\nHow may i help you"
                                        "\n  -Limit "
                                        "\n  -Balance"
                                        "\n  -Loan"
                                        "\n  -Amount"
                    ).format(Good_Evening)
    else:
        response = "END Invalid input. Try again."

    return response
        
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=os.environ.get("PORT"))
