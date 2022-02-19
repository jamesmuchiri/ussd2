from flask import Flask, request
import africastalking
import os
import variables
import re
import maya
from maya import MayaInterval
from datetime import datetime
from dateutil.parser import parse
import mysql.connector

app = Flask(__name__)

username = "sandbox"
api_key = "0f54c06969af94baa76c50efbcc1daaecb9b75f254d3388c85edfd9d21ff7ad0"
africastalking.initialize(username, api_key)

sms = africastalking.SMS

@app.route('/', methods=['POST', 'GET'])
def Greetings():
    

    db = mysql.connector.connect(
    
        host = "137.184.54.169",
        user = "kaguius",
        passwd = "U6xZfLn9A7Swc%P9",
        database = "finabora",
        autocommit = True,
        port ="3306",
    )
    session_id = request.values.get("sessionId", None)
    service_code = request.values.get("serviceCode", None)
    phone_number = request.values.get("phoneNumber", None)
    phone_number = []
    phone_number.append(phone_number)
    text= request.values.get("text")

    if text == "":
        variables.now = maya.MayaDT.from_datetime(datetime.utcnow())
        Time_zone = variables.now.hour +3

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
 
    elif text == "balance":
        
        mycursor = db.cursor()
        mycursor.execute('''SELECT primary_phone FROM s_staff WHERE primary_phone = (%s)''', (phone_number,))
        checkNumber = mycursor.fetchall()

        

        if (phone_number,) in checkNumber:

            mycursor = db.cursor()
            mycursor.execute('''SELECT first_name FROM s_staff WHERE primary_phone = (%s)''', (phone_number,))
            name = mycursor.fetchone()

            variables.response=("END Dear {}, your effective balance as at $date is KES $loan_balance."
            ).format(name)
        
        
    return variables.response
    


    


    

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=os.environ.get("PORT"))
