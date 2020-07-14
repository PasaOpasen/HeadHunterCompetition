# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 14:32:55 2020

@author: qtckp
"""

import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import make_moons, make_circles, make_classification
from sklearn.neural_network import MLPClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.svm import LinearSVC
from sklearn.gaussian_process import GaussianProcessClassifier
from sklearn.gaussian_process.kernels import RBF
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.discriminant_analysis import QuadraticDiscriminantAnalysis
from sklearn.metrics import classification_report
from sklearn.linear_model import LogisticRegression
from sklearn.linear_model import SGDClassifier
from sklearn import linear_model
from sklearn.metrics import f1_score
import sklearn
import numpy as np
from scipy import sparse


X = sparse.load_npz(f'X3955_train.npz')
y = sparse.load_npz(f'Y.npz')




names = [
    #"Nearest Neighbors", 
      # "Linear SVM", 
     #  "RBF SVM", 
     #  'poly svm',
       # 'sigmoid svm',
        #'sgd',
        "Decision Tree", 
        "Random Forest", 
       "Neural Net", 
        "AdaBoost",
        # "Naive Bayes gau",

         #"QDA",
         'logreg',
         'ridge',
         'boost'
         ]


classifiers = [
  # KNeighborsClassifier(5),
  # LinearSVC(C=1,verbose=1),
   # SVC(gamma=2, C=1,verbose=True),
   # SVC(kernel='poly'),
   # SVC(kernel='sigmoid'),
    #SGDClassifier(),
    DecisionTreeClassifier(max_depth=3),
    RandomForestClassifier(max_depth=5, n_estimators=10, max_features=1,verbose=True),
   MLPClassifier(alpha=1, max_iter=1000,verbose=True),
   AdaBoostClassifier(),
  # GaussianNB(),

    #QuadraticDiscriminantAnalysis() ,
    LogisticRegression(),
    linear_model.RidgeClassifier(alpha=0.1),
    sklearn.ensemble.GradientBoostingClassifier()
    ]




X_train, X_test, y_train, y_test =  train_test_split(X.toarray(), y, test_size=.2, train_size=.01, shuffle = True )



for name, clf in zip(names, classifiers):
    print('Now: {}'.format(name))
    f1s = []
    for i in range(620):
        clf.fit(X_train, y_train[:,i].toarray().flatten())
        #score = clf.score(X_test, y_test[:,i])
        print(clf.score(X_test, y_test[:,i].toarray().flatten()))
        v = f1_score(y_test[:,i].toarray().flatten(), clf.predict(X_test))
        print(v)
        f1s.append(v)
        #print(classification_report(y_test, clf.predict(X_test), digits = 7))
    print("model = {}  score = {}".format(name,np.mean(f1s)))







XX = X.toarray()
y0 = y[:,0].toarray().flatten()

inds = np.arange(0, y0.size)

f_inds = inds[np.logical_not(y0)]

false = f_inds[np.random.choice(f_inds.size,np.sum(y0))]

tot = np.concatenate((false,inds[y0]))
tot = np.sort(tot)

for depth in range(2,10):
    clf = LinearSVC(C=depth/10,verbose=1) #DecisionTreeClassifier(max_depth=depth) #
    clf.fit(XX[tot], y0[tot])
    print(clf.score(X_test, y_test[:,0].toarray().flatten()))
    v = f1_score(y_test[:,0].toarray().flatten(), clf.predict(X_test))
    print(v)




from sklearn.model_selection import GridSearchCV

params = [{
    'max_depth':[2,3,4,5,6,7,8,9,10],
    'n_estimators':[10,20,30,40,50],
    'max_features':[1,2,3,4,5,6,7,8],
           }]
clf= RandomForestClassifier()

gr= GridSearchCV(clf,params,cv=5,verbose=1, n_jobs = -1)

gr.fit(X_train, y_train)

gr.cv_results_




