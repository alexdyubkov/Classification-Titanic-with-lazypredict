Classification Titanic dataset

Source date from https://www.kaggle.com/c/titanic/data?select=test.csv
using lazypredict

Result:
100%|██████████| 29/29 [00:02<00:00, 10.90it/s]                               Accuracy  Balanced Accuracy  ROC AUC  F1 Score  \
Model                                                                           
LinearDiscriminantAnalysis         0.96               0.96     0.96      0.96   
RidgeClassifierCV                  0.96               0.96     0.96      0.96   
RidgeClassifier                    0.96               0.96     0.96      0.96   
LinearSVC                          0.96               0.96     0.96      0.96   
CalibratedClassifierCV             0.96               0.96     0.96      0.96   
LogisticRegression                 0.93               0.93     0.93      0.93   
NearestCentroid                    0.91               0.93     0.93      0.91   
GaussianNB                         0.91               0.92     0.92      0.91   
NuSVC                              0.92               0.90     0.90      0.92   
BernoulliNB                        0.89               0.88     0.88      0.89   
AdaBoostClassifier                 0.86               0.88     0.88      0.86   
SVC                                0.90               0.88     0.88      0.90   
KNeighborsClassifier               0.86               0.84     0.84      0.86   
XGBClassifier                      0.84               0.82     0.82      0.84   
PassiveAggressiveClassifier        0.82               0.80     0.80      0.82   
LGBMClassifier                     0.82               0.80     0.80      0.82   
RandomForestClassifier             0.81               0.79     0.79      0.81   
BaggingClassifier                  0.80               0.78     0.78      0.80   
QuadraticDiscriminantAnalysis      0.78               0.75     0.75      0.77   
ExtraTreeClassifier                0.75               0.75     0.75      0.75   
Perceptron                         0.69               0.74     0.74      0.69   
ExtraTreesClassifier               0.75               0.73     0.73      0.75   
LabelSpreading                     0.74               0.70     0.70      0.73   
DecisionTreeClassifier             0.72               0.70     0.70      0.72   
LabelPropagation                   0.73               0.69     0.69      0.72   
SGDClassifier                      0.74               0.66     0.66      0.71   
DummyClassifier                    0.56               0.53     0.53      0.56   

                               Time Taken  
Model                                      
LinearDiscriminantAnalysis           0.10  
RidgeClassifierCV                    0.02  
RidgeClassifier                      0.08  
LinearSVC                            0.07  
CalibratedClassifierCV               0.23  
LogisticRegression                   0.02  
NearestCentroid                      0.02  
GaussianNB                           0.02  
NuSVC                                0.06  
BernoulliNB                          0.04  
AdaBoostClassifier                   0.21  
SVC                                  0.06  
KNeighborsClassifier                 0.05  
XGBClassifier                        0.41  
PassiveAggressiveClassifier          0.03  
LGBMClassifier                       0.19  
RandomForestClassifier               0.31  
BaggingClassifier                    0.06  
QuadraticDiscriminantAnalysis        0.08  
ExtraTreeClassifier                  0.02  
Perceptron                           0.02  
ExtraTreesClassifier                 0.26  
LabelSpreading                       0.10  
DecisionTreeClassifier               0.03  
LabelPropagation                     0.10  
SGDClassifier                        0.02  
DummyClassifier                      0.02  

