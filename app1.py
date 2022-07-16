from flask import Flask, render_template, redirect, url_for, request
import requests
import json
import os
from bs4 import BeautifulSoup
import re

app1 = Flask(__name__)

def fetch_data(username,contents):
    data_fetched={}
    soup = BeautifulSoup(contents,"html.parser")
    repo = soup.find('a',href=re.compile(r'/anjaligeop\?tab=repositories'))
    repo_num = repo.find('span').text
    contributions = soup.find('h2',text=re.compile(r'(\d+)\s+contributions\s+in\s+the\s+last\s+year')).text
    total_contrib = re.search(r'\d+',contributions).group(0)
    fullname = soup.find('span',attrs={"itemprop":"name"}).text.strip()
    if not fullname:
        fullname = 'NA'
    data_fetched = {'username':username,'fullName':fullname,'numberOfRepositories':repo_num,'contributions':total_contrib+' last year'}
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
        with open(filename,"w") as f:
            f.write(response.text)
        f.close
        data_fetched = fetch_data(username,response.text)
        return render_template('process.html',form_data = request.form) 
    


if __name__ == '__main__': 
    app1.run(debug=True)
