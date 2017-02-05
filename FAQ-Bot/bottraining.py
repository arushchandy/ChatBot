import pickle
from textblob.classifiers import NaiveBayesClassifier
import pandas as pd

def dobottraining():
    """ Function DoBotTraining
    Args : null
    Return Status of training
    """
    data2 = []
    print "training...."
    data = pd.read_csv('TrainingModel\\trainData.csv', header=None)
    class_list = []
    for i in range(0, len(data)):
        print i
        print data[1][i], data[0][i]
        tup = ()
        #tuple of description,classification
        tup = (data[1][i], data[0][i])
        class_list.append(tup)
        naive_classifier = NaiveBayesClassifier(class_list)
        output = open('TrainingModel\\naivemodel.pkl', 'wb')
    pickle.dump(naive_classifier, output)
    output.close()
    print "training completed"
    item = {"result":"training completed"}
    data2.append(item)
    return data2

def dobottrainingwithoutpandas():
    """
     Function DoBotTraining
    Args : null
    Return Status of training
    """
    data2 = []
    print "training...."
    with open('TrainingModel\\trainData.csv') as line:
        lines = line.readlines()
        class_list = []
        for i in range(0, len(lines)):
            print lines[i].split(',')[1], "------------", lines[i].split(',')[0]
            tup = ()
            tup = (lines[i].split(',')[1], lines[i].split(',')[0])
            class_list.append(tup)
    naive_classifier = NaiveBayesClassifier(class_list)
    output = open('TrainingModel\\naivemodel.pkl', 'wb')
    pickle.dump(naive_classifier, output)
    output.close()
    print "training completed"
    item = {"result":"training completed"}
    data2.append(item)
    return data2

