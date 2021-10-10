#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  9 20:16:22 2021

@author: bandiang2
"""
from flask import Flask

app = Flask('ping_model')

@app.route('/ping_model', methods=['GET'])
def ping():
    return 'PONG'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=9696)
    