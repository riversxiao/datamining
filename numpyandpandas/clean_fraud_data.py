import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import re

fraud = pd.read_csv('~/desktop/fraud_dl.csv',thousands=',')
col_names = fraud.columns
fraud.head()
col_with_na = col_names[1:8]
fraud_data = fraud
for i in col_with_na:
    fraud_data[i].replace(fraud_data[i][0],1, inplace= True)
    fraud_data[i].replace('NaN', 0, inplace= True)
fraud_data['created'] = pd.to_datetime(fraud_data['created'],format ='%m/%d/%y  %H:%M:%S')
fraud_data['last_rcvd'] = fraud_data['last_rcvd'].replace('---',np.nan)
fraud_data['last_rcvd'] = pd.to_datetime(fraud_data['last_rcvd'],format ='%m/%d/%y')
fraud_data['last_sent'] = fraud_data['last_sent'].replace('---',np.nan)
fraud_data['last_sent'] = pd.to_datetime(fraud_data['last_sent'],format ='%m/%d/%y')
def replace_str(target, text):
    return re.sub(r' *# ?',target,text)
fraud_data['email'] = fraud_data['email'].str.replace(r' *# ?','')
fraud_data['rcvd_currency'] = fraud_data['amount_rcvd'].str[-3:]
fraud_data['amount_rcvd'] = fraud_data['amount_rcvd'].str[1:-4]
fraud_data['send_currency'] = fraud_data['amt_sent'].str[-3:]
fraud_data['amt_sent'] = fraud_data['amt_sent'].str[1:-4]
cols = ['amount_rcvd','amt_sent']
fraud_data.amount_rcvd = fraud_data.amount_rcvd.replace(',','')
fraud_data.amt_sent = fraud_data.amt_sent.replace(',','')
fraud_data.amt_sent = pd.to_numeric(fraud_data.amt_sent)
fraud_data.amount_rcvd = pd.to_numeric(fraud_data.amount_rcvd)
fraud_data.account_number=fraud_data.account_number.astype(str)
fraud_data.account_number = "'" + fraud_data.account_number
fraud_data =fraud_data.fillna("NaN")
fraud_data.to_csv('~/desktop/fraud_data_cleaned.csv')
