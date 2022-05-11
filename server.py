from flask import Flask, render_template, url_for, request, redirect, render_template
import csv
import pandas as pd
app = Flask(__name__)

@app.route("/")
def home():
    data_carrier = pd.read_csv('database_carrier.txt', sep=',')
    return render_template('./index.html', tables=[data_carrier.to_html()], titles=[''])

@app.route("/<string:page_name>")
def html_page(page_name):
    data_carrier = pd.read_csv('database_carrier.txt', sep=',')
    data_sender = pd.read_csv('database_sender.txt', sep=',')
    return render_template(page_name, tables=[data_carrier.to_html()], titles=[''])

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data =request.form.to_dict()
            write_to_file(data)
            return redirect('/thankyou.html')
        except:
            return 'could not save the data in the database'
    else:
        return 'something wrong!'

def write_to_file(data):
    with open('database_carrier.txt', mode='a') as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        file = database.write(f'\n{email},{subject},{message}')