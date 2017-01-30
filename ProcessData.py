import numpy as np
import csv
from sklearn.linear_model import LinearRegression
from sklearn.svm import SVR
from sklearn.feature_selection import RFE
from pandas import read_csv 
from sklearn.decomposition import PCA
from sklearn.preprocessing import scale
from sklearn.preprocessing import Normalizer
from sklearn.linear_model import Ridge
from sklearn.pipeline import Pipeline
from sklearn.feature_selection import RFE
import sklearn.grid_search
from sklearn.cluster import KMeans
from sklearn.cluster import AgglomerativeClustering
from sklearn import metrics
from sklearn.ensemble import AdaBoostRegressor
from sklearn.tree import DecisionTreeRegressor
def readFileandConverttoNumpy(path):
    #csv_file_object = csv.reader(open('../Data/EnglishMoviesWithNumColumns.csv', 'rb'))
    csv_file_object = csv.reader(open(path, 'rb'))  
    header = csv_file_object.next() 
    data=[] 
    
    for row in csv_file_object:
        data.append(row)
    data = np.array(data) 
    return data
def readFileForTitles(path):
    df = read_csv(path)
    return df
def SVMLearning(features_train_new,labels_train_new,features_test_new):
    lr = LinearRegression()
    rfe = RFE(lr)
    #els = SVR(C=1000000000,gamma=0.000000001)
    els = SVR(C=100000000,gamma=0.000000001)
    
    
    els.fit(features_train_new,labels_train_new)
    
    #els.fit(features_train,labels_train)
    Movie_pred_SVM = els.predict(features_test_new)
    return Movie_pred_SVM
def decisionTreePredictions(datasetTrainWithoutLabels,labels,datasetTestWithoutLabels,trueLabels):
    regressor = DecisionTreeRegressor()
    #featureArray = np.arange(1,datasetTrainWithoutLabels.shape[1])
    maxDepths = np.arange(1,datasetTestWithoutLabels.shape[1])
    steps=[('regressor',regressor)]
    pipeline=Pipeline(steps)
    parameterGrid = dict(regressor__max_depth = maxDepths)
    GridSearchResult = sklearn.grid_search.GridSearchCV(pipeline,param_grid=parameterGrid,cv = 5)

    GridSearchResult.fit(datasetTrainWithoutLabels,labels)
    print GridSearchResult.best_params_
    predictions = GridSearchResult.predict(datasetTestWithoutLabels)
    print r2_score(trueLabels,predictions)
    return predictions,GridSearchResult


def AdaBoostRegressorPredictions(datasetTrainWithoutLabels,labels,datasetTestWithoutLabels,trueLabels,bestDTree):
    
    regressor = AdaBoostRegressor(base_estimator = bestDTree,n_estimators=100)

    featureArray = np.arange(1,datasetTrainWithoutLabels.shape[1])
    regressor.fit(datasetTrainWithoutLabels,labels)
    predictions = regressor.predict(datasetTestWithoutLabels)
    print r2_score(trueLabels,predictions)
    return predictions