import flask
import pickle
import pandas as pd
import numpy as np

with open(r'C:\Users\Shamali\Desktop\Velocity python 2jan21\Nikita Velocity\FLASK\loan_prediction_project\logistic_model.pickle', 'rb') as f:
    rft = pickle.load(f)


def si(loan_amnt,int_rate,term,annual_inc):
        if term==36:
            principal_amt=loan_amnt
            interest_rate=int_rate
            years=3 ##(36/12)=3 yrs
            SI=principal_amt*(1+(interest_rate*years))
        else:
            principal_amt=loan_amnt
            interest_rate=int_rate
            years=5 ##[60/12]=5 yrs
            SI=principal_amt*(1+(interest_rate*years))
            
        installment = int(SI)
        inst_amnt_ratio=installment/loan_amnt
        balance_annual_inc=(loan_amnt)/(annual_inc)
        return balance_annual_inc

def make_prediction(dti,balance_annual_inc,revol_util,annual_inc):
    
        if dti>43:
            return 'Debt to income too high!'
        elif balance_annual_inc >=0.43:
                return 'Debt to income too high!'
        elif revol_util>=90:
                return 'Amount of credit used up too high!'
        elif  annual_inc<=2000:
                return 'Loan Denied'
        else:
                return 'Congratulations! Approved!'

if __name__ == '__main__':
    balance_annual_inc=si(5000,10.65,36,24000)
    print(make_prediction(27.65, balance_annual_inc, 83.7, 24000))

    balance_annual_inc=si(1200,1.2,36,1800)
    print(make_prediction(10.75, balance_annual_inc, 67.1, 1800))



