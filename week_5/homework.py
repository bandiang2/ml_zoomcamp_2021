#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  9 17:17:42 2021

@author: bandiang2
"""

import pickle

model_file = 'model1.bin'
dv_file = 'dv.bin'

with open(model_file, 'rb') as f_in:
    model = pickle.load(f_in)
    
with open(dv_file, 'rb') as dv_in:
    dv = pickle.load(dv_in)
    
new_customer_1 = {"contract": "two_year", "tenure": 12, "monthlycharges": 19.7}

def predict(customer):
    X = dv.transform(customer)
    y_pred = model.predict_proba(X)[0, 1]
    return y_pred

if __name__ == '__main__':
    proba = predict(new_customer_1)
    print(f'Predicted probability : {proba}')
