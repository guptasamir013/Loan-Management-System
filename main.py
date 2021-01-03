import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
import pickle

train = pd.read_csv("data/train.csv")
test = pd.read_csv("data/test.csv")

train = train.dropna()
train.Dependents.replace("3+", "3", inplace=True)
train.Dependents = train.Dependents.astype(float)

X = train.drop(["Loan_ID", "Loan_Status", "Loan_Amount_Term", "CoapplicantIncome"], axis=1)
y = train["Loan_Status"]

train_X, test_X, train_y, test_y = train_test_split(X, y, test_size=0.4)

train_X = pd.get_dummies(train_X)
test_X = pd.get_dummies(test_X)


model = SVC()
model.fit(train_X, train_y)

print(model.score(test_X, test_y))

pickle.dump(model, open("static/accounts/models/loan_predictor.pickle", 'wb'))
loaded_model = pickle.load(open("static/accounts/models/loan_predictor.pickle", 'rb'))
