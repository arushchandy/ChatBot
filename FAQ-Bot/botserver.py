from json import dumps
# import bottle
# from bottle import response, request, route, run,hook
import bottraining as training
import botclassify
from flask import Flask,make_response,render_template, request, jsonify, json,jsonify,send_from_directory,Response
from flask_cors import CORS,cross_origin



appl = Flask(__name__)  
cors = CORS(appl)
appl.config['CORS_HEADERS'] = 'Content-Type'

#Initialization starts
#configParser=ConfigParser.RawConfigParser()
#configFilePath="Config.cfg"
#configParser.read(configFilePath)
#Host=configParser.get('file','host')
#Port=configParser.get('file','port')

#Config read ends
# @appl.hook('after_request')
# def enable_cors():
# # set CORS headers
#     print "hello"
#     response.headers['Access-Control-Allow-Origin'] = '*'
#     response.headers['Access-Control-Allow-Methods'] = '*'
#     response.headers['Access-Control-Allow-Headers'] = '*'

    


@appl.route('/cors', methods=['OPTIONS', 'GET'])
#@enable_cors
def lvambience():
    #response.headers['Content-type'] = 'application/json'
    return '[1]'


@appl.route('/trainBot', methods=['POST'])
#@enable_cors
def trainbot():
    """
    trainbot function used to train the model using the available dataset provided in train.csv
    Args: null
    Return : Status of training on available data set
    """
    #response.content_type = 'application/json'
    return_data = training.dobottraining()
    return dumps(return_data)


@appl.route('/trainBot2', methods=['POST'])
#@enable_cors
def trainbot2():
    """
    trainbot2 function used to train the model using the available
    dataset provided in train.csv without using pandas library
    Args: null
    Return : Status of training on available data set
    """
    #response.content_type = 'application/json'
    return_data = training.dobottrainingwithoutpandas()
    return dumps(return_data)


@appl.route('/classify', methods=['POST'])
#@enable_cors
def classify():
    """
    Claasify route to classify the incomiing json text
    with the value of input text
    """
    #response.content_type = 'application/json'
    input_text = request.json["input-request"]
    return_data = botclassify.inputclassify(input_text)
    return dumps(return_data)

@appl.route('/userrequest', methods=['POST'])
#@enable_cors
@cross_origin()
def parse_user_request():
    """
    Function used to read the user input and then
    based on classified class from model return data to user
    """
    #response.content_type = 'application/json'
    input_text = request.json["input-request"]
    classifier_data = botclassify.classify_text_with_score(input_text)
    classsified_response = botclassify.generate_response(classifier_data)
    return dumps(classsified_response)


if __name__ == '__main__':
    #appl.run(host='localhost',port=8000)
    appl.run(host='localhost', processes=True, debug=True, port=8000)

#run(host='192.168.1.7',port=8000)

