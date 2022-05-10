from flask import Flask, render_template, url_for, request, redirect, render_template
import csv
import pandas as pd
app = Flask(__name__)

@app.route("/")
def home():
    return render_template('./index.html')



@app.route("/<string:page_name>")
def html_page(page_name):
    data = pd.read_csv('database.txt', sep=',')
    with open("database.csv") as file:
        return render_template(page_name, tables=[data.to_html()], titles=[''])

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
    with open('database.txt', mode='a') as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        file = database.write(f'\n{email},{subject},{message}')

def write_to_csv(data):
    with open('database.csv', newline='', mode='a') as database2:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(database2, delimiter=',', quotechar='"', quoting = csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])
