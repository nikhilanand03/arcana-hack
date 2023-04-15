from flask import Flask, render_template
import csv

app = Flask(__name__)

@app.route('/')
def index():
    data = []
    with open('CHG.csv', newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            data.append(row)
    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)
