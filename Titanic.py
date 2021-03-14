#%%
from operator import sub
import matplotlib
from numpy.core.numeric import NaN
import pandas as pd
import os
import seaborn as sns
import matplotlib.pyplot as plt
%matplotlib inline
from sklearn.impute import SimpleImputer
import numpy as np

#chdir
os.chdir("C:/Users/иван/Desktop/Python/мусор/Classification-Titanic")

#files ->df
gender_submission=pd.read_csv("gender_submission.csv")
test=pd.read_csv("test.csv")
train=pd.read_csv("train.csv")



# %%
#some  info from df
train.describe
# %% if classes are balanced
print(train["Survived"].unique()) #values range of die/not die
print( sum(train["Survived"] == 0)  /891 * 100) #almost balanced

# %%зависимости
print(train['Fare'].max()) #512 уе
print(train['Fare'].mean()) # 32уе
print(train['Fare'].min())#7.12 ye

# %% graphs
sns.pairplot(train[[ 'Survived', 'Pclass', 'Sex', 'Age', 'SibSp', 'Ticket', 'Fare', 'Cabin']],hue="Survived")
#Получ что чаще умирали люди из 3его класса, которые пострарше. 


#boxplot
plt.figure(figsize=(10,7))
sns.boxplot(x='Pclass',y='Age',data=train)


# %%
sns.countplot(x='Fare',hue="Survived",data=train)


sns.jointplot(x='Survived',y='Fare',data=train)
#по цене умерли больше те, у кого были дешевые билеты.От 300-500 уе за билет умер ток 1 чел

# %% сравнения по полу и возрасту


train['Sex'].describe(include='O')

sns.set_style('darkgrid')
g=sns.FacetGrid(train,hue='Sex', palette='coolwarm',size=6, aspect=2)
g=g.map(plt.hist,'Age', bins=20,alpha=0.7)
#большинство от 18-38 по возрасту и это мужчины
# %%unuseful data drop
train.drop("Name", axis=1,inplace=True)
train.columns
# %%Сколько есть Null
train.isnull().sum()
#Есть пропуски в Cabin,Embarked,Age


#Сколько есть Null в%
train.isnull().mean() * 100

# %% Дропнем столбик Cabin, так как много пропуск и Ticket, так как он беспол
train.drop("Cabin", axis=1,inplace=True)
train.drop("Ticket", axis=1,inplace=True)


# %%
train['Embarked'].head(30)
# %%восстановим пропуски в возрасте в завис от класса
def impute_age(cols):
    Age=cols[0]
    Pclass=cols[1]

    if pd.isnull(Age):
        if Pclass ==1:
            return 37
        elif Pclass==2:
            return 29
        else:
            return 24
    else:
        return Age



train['Age'] = train[['Age','Pclass']].apply(impute_age,axis=1)
# %%удалим строчки, где в Embarked пропуски
train=train.dropna(subset=['Embarked'])
# %%
#Сколько есть Null в%
train.isnull().mean() * 100


# %%
#Convert Sex, Embarked -> digits
#можем сделать Sex через labelencoder, так как нам его считать уже не нужно
subgrade_dummies=pd.get_dummies(train['Sex'],drop_first=True)
train=pd.concat([train.drop('Sex',axis=1),subgrade_dummies],axis=1)



subgrade_dummies=pd.get_dummies(train['Embarked'],drop_first=True)
train=pd.concat([train.drop('Embarked',axis=1),subgrade_dummies],axis=1)




# %% X train, y train
y_train=train['Survived','PassengerId']
X_train =train.drop(['Survived'], axis=1)
# %% Logistic regression
from  sklearn.linear_model import LogisticRegression
logmodel=LogisticRegression()
logmodel.fit(X_train, y_train)




#%%
print(y_train)
#%%





























# %% prepare X_test to prediction
X_test=test
X_test.drop('Name',axis=1,inplace=True)
X_test.drop('Ticket',axis=1,inplace=True)
X_test.drop('Cabin',axis=1,inplace=True)


X_test['Age'] = X_test[['Age','Pclass']].apply(impute_age,axis=1)


subgrade_dummies=pd.get_dummies(X_test['Sex'],drop_first=True)
X_test=pd.concat([X_test.drop('Sex',axis=1),subgrade_dummies],axis=1)



subgrade_dummies=pd.get_dummies(X_test['Embarked'],drop_first=True)
X_test=pd.concat([X_test.drop('Embarked',axis=1),subgrade_dummies],axis=1)
print(X_test)



#%%Fare mean based on class
X_test.head(5)
#ср зн класс 1
print((X_test[X_test['Pclass'] == 1].mean()).Fare) #94
#ср зн класс 2
print((X_test[X_test['Pclass'] == 2].mean()).Fare) #22
#ср зн класс 3
print((X_test[X_test['Pclass'] == 3].mean()).Fare) #12


#%%fillna for Fare based on class
def impute_Fare(cols):
    Fare = cols[0]
    Pclass = cols[1]

    if pd.isnull(Fare):
        if Pclass == 1:
            return 94
        elif Pclass ==2:
            return 22
        else:
            return 12
    else:
        return Fare

X_test['Fare'] = X_test[['Fare', 'Pclass']].apply(impute_Fare,axis=1)


#%%
X_test.isnull().mean() * 100


# %%
X_test.head(5)

# %%predict
predictions=logmodel.predict(X_test)




# %%
from sklearn.metrics import accuracy_score
accuracy_score(gender_submission['Survived'],predictions, normalize = True)
# %%
