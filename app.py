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


def Greetings():
    session_id = request.values.get("sessionId", None)
    service_code = request.values.get("serviceCode", None)
    phone_number = request.values.get("phoneNumber", None)
    phone_number = []
    phone_number.append(phone_number)
    text = request.values.get("text")

    if text == "":
        now = maya.MayaDT.from_datetime(datetime.utcnow())
        Time_zone = now.hour +3

        if 5<= Time_zone <12 :
            Good_Morning="Good Morning"
            variables.response =("CON {}"
                                        "\nHow may i help you"
                                        "\n  -Limit "
                                        "\n  -Balance"
                                        "\n  -Loan"
                                        "\n  -Amount"
            ).format(Good_Morning)

        elif  12 <= Time_zone < 17 :
            Good_Afternoon="Good Afternoon"
            variables.response =("CON {}"
                                        "\nHow may i help you"
                                        "\n  -Limit "
                                        "\n  -Balance"
                                        "\n  -Loan"
                                        "\n  -Amount"
                    ).format(Good_Afternoon)
        else:
            Good_Evening="Good Evening"
            variables.response =("CON {}"
                                        "\nHow may i help you"
                                        "\n  -Limit "
                                        "\n  -Balance"
                                        "\n  -Loan"
                                        "\n  -Amount"
                    ).format(Good_Evening)

    

    def Limit(text):
        if text == "Limit" | text == "limit":
            variables.response=("END Dear $first_name, your advance limit as at $date is KES $loan_limit.") 
        return Limit
    def Balance(text):
        if text == "Balance" | text == "balance":
            variables.response=("END Dear $first_name, your effective balance as at $date is KES $loan_balance.") 
        return Balance
            
    def Loan(text):

        if text == "Loan" | text == "loan":
            variables.response=("END Dear $first_name, you qualify for a new loan. Please enter a loan value between 500 and $loan_limit") 
        return Loan   
    def Amount(text):
        if text == "Amount" | text == "amount":
            variables.response=("END Dear $first_name, you have selected KES XXXX, the loan advance will be processed shortl") 
        return Amount  


    return variables.response

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=os.environ.get("PORT"))
