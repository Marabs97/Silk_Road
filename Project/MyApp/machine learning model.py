import logging
import pandas as pd
from sklearn.datasets import load_iris
from sklearn import tree
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.metrics import f1_score
from sklearn.metrics import recall_score
import graphviz
import random
#TODO change the level
logging.basicConfig(filename='machineLearningModel.loging',level=logging.INFO)
import numpy as np
def makeTheTree():
    input_file = "Training.csv"
    # comma delimited is the default

    df_train = pd.read_csv(input_file, header = 0)
    #df_train.isna().sum().sum()

    df_train = df_train.fillna(0)
    df_train = df_train.drop(columns='Unnamed: 133')
    logging.info(df_train.describe())
    # TODO why by 0 and not delte ?

    X = df_train.drop(columns=['prognosis'])
    y = df_train['prognosis']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=44, shuffle =True)
    iris = load_iris()
    clf = tree.DecisionTreeClassifier(max_depth=50)
    clf = clf.fit(X_train, y_train)
    logging.info('Accuracy in validation: ',accuracy_score(y_test,clf.predict(X_test)))
    dot_data = tree.export_graphviz(clf, out_file=None)
    graph = graphviz.Source(dot_data)
    graph.render("GraphicalTree")
    input_file = "Testing.csv"
    # comma delimited is the default

    df_tests = pd.read_csv(input_file, header = 0)
    logging.info(df_tests.describe())
    logging.info(df_train.isna().sum().sum())
    df_tests = df_tests.fillna(0)
    X_tests = df_tests.drop(columns=['prognosis'])
    y_tests = df_tests['prognosis']
    logging.info('Accuracy in test: ',accuracy_score(y_tests,clf.predict(X_tests)))
    logging.info('f1 Macro(Unweighted mean. This does not take label imbalance into account'
          '):',f1_score(y_tests,clf.predict(X_tests),average='macro'))
    logging.info('recall score Macro: ',recall_score(y_tests,clf.predict(X_tests),average='macro'))

    return clf
def findDesesFromSymptom(Symptoms):
    clf = makeTheTree()
    return clf.predict(pd.DataFrame (Symptoms))

# Might be helpful for test #
l = {}
c = [1,0]
for a in range(132):
    b = random.choices([1,0],[1,3])
    l.update({str(a):b})
data =pd.DataFrame(data=l, index=[1])
logging.info(data)

logging.info(findDesesFromSymptom(data)[0])

logging.shutdown()