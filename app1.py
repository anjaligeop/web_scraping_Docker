from flask import Flask, render_template, redirect, url_for, request
import requests
import json
import os

app1 = Flask(__name__)

def fetch_data(contents):
    data_fetched={}
    return data_fetched

@app1.route('/')
def welcome():
    return render_template('welcome.html')

@app1.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']        
        response = requests.get('https://github.com/'+username, verify=False)
        filename = os.getcwd()+'/dump.html'
        # with open(filename,"w") as f:
        #     f.write(response.text)
        # f.close   
       
        return render_template('process.html',form_data = request.form) 
    


if __name__ == '__main__': 
    app1.run(debug=True)
