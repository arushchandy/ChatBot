import json
import pickle

def generate_response(classfied_value):
    """
    get response from json file using the classified value
    """
    with open('Response\\faqoutput.json') as data_file:
        data = json.load(data_file)
        static_response = data["staticClassifiers"]
        output_response = {}
        for response_object in static_response:
            if response_object["class"] == classfied_value:
                output_response = response_object
    print output_response
    return output_response


def inputclassify(input_text):
    """"
    function to classify the inut string based on available model
    """
    pkl_file = open('TrainingModel\\naivemodel.pkl', 'rb')
    pkl_file.close()
    data = []
    print "input text : ", input_text
    #predictedClass=naiveClassifier.classify(inputText
    predicted_class = classify_text_with_score(input_text)
    item = {"result":str(predicted_class)}
    data.append(item)
    return data

def classify_text(input_text):
    """
    classify using naive bayes classifier
    """
    pkl_file = open('TrainingModel\\naivemodel.pkl', 'rb')
    naive_classifier = pickle.load(pkl_file)
    pkl_file.close()
    predicted_class = naive_classifier.classify(input_text)
    return str(predicted_class)

def classify_text_with_score(input_text):
    """
    function to classify with prediction score
    """
    pkl_file = open('TrainingModel\\naivemodel.pkl', 'rb')
    naive_classifier = pickle.load(pkl_file)
    pkl_file.close()
    prob_dist = naive_classifier.prob_classify(input_text)
    confidence = round(prob_dist.prob(prob_dist.max()), 2)
    print confidence, prob_dist.max()
    if confidence < 0.6:
        return "unknown"
    #elif len(input_text.split(" ")) < 2:
    #   return "unknown"
    else:
        return str(prob_dist.max())
	