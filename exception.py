from flask import Flask
from src.logger import logging
from src.exception import CustomException
import sys,os


app = Flask(__name__)

@app.route("/", methods = ['GET','POST'])
def index():

    try:
        raise Exception("We are testing exception file")
    except Exception as e:
        ML = CustomException(e,sys)
        logging.info(ML.error_message)
        logging.info("We are testing logging file")


    return "Welcome to Looging class"



if __name__=="__main__":
    app.run(debug=True,port=5005)