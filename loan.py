import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score,classification_report,confusion_matrix
from sklearn.preprocessing import LabelEncoder,OneHotEncoder

df=pd.read_csv(r'C:\Users\Shamali\Desktop\Velocity python 2jan21\Nikita Velocity\FLASK\loan_prediction_project\loan.csv')
df

df['home_ownership'].value_counts()

df.info()

df.isnull().sum()

df['emp_length']=df['emp_length'].fillna(df['emp_length'].median())
df['total_acc']=df['total_acc'].fillna(df['total_acc'].median())
df['annual_inc']=df['annual_inc'].fillna(df['annual_inc'].median())
df['longest_credit_length']=df['longest_credit_length'].fillna(df['longest_credit_length'].median())
df['revol_util']=df['revol_util'].fillna(df['revol_util'].mean())
df['delinq_2yrs']=df['delinq_2yrs'].fillna(2)

df.isnull().sum()

df.drop('addr_state',axis=1,inplace=True)

df.head()

df.shape

df['term'].unique()

df['term']=df['term'].replace('36 months',36).replace('60 months',60)
df.head()

df.info()

le=LabelEncoder()
df['purpose']=le.fit_transform(df['purpose'])

df['purpose'].unique()

df.head()

df['home_ownership'].unique()

df['home_ownership']=df['home_ownership'].replace('MORTGAGE',4).replace('RENT',3).replace('OWN',5).replace('ANY',2).replace('OTHER',1).replace('NONE',0)

df['home_ownership']=df['home_ownership'].astype('int64')

df['verification_status']=df['verification_status'].replace('verified',1).replace('not verified',0)

df['verification_status']=df['verification_status'].astype('int64')

df.info()

x=df.drop('bad_loan',axis=1)
y=df['bad_loan']

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=1)

rft_model=RandomForestClassifier(n_estimators=80,random_state=1)
rft_model.fit(x_train,y_train)

y_pred=rft_model.predict(x_test)
y_pred[:5]

y_test[:5]

print(accuracy_score(y_test,y_pred))

confusion_matrix(y_test,y_pred)

print(classification_report(y_test,y_pred))

import pickle
models=[rft_model]
pickle.dump(models,open('randomfc_model.pickle','wb'))

import json
columns = {
    'loan_columns' : [col.lower() for col in x.columns]
}
with open("loan1.json","w") as f:
    f.write(json.dumps(columns))


