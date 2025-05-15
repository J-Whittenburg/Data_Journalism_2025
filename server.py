# flask --app data_server run
from flask import Flask
from flask import render_template
import json


app = Flask(__name__, static_url_path='', static_folder='static')

@app.route('/')
def about():
    #load a current view of the data
    f = open("data/data.json", "r")
    data = json.load(f)
    f.close()
    #
    data_list = []
    lowest_avg = 1000
    highest_avg = 0
    for k in data.keys():
        this_state = []
        this_state.append(k.lower())
        score4 = int(data[k]["Math_4"])
        score8 = int(data[k]["Math_8"])
        this_state.append((score4+score8)/2)
        this_state.append(int(data[k]["Income"]))
        data_list.append(this_state)
    # Lowest Avg = 240
    # Highest Avg = 263
    return render_template('about.html', data_list = data_list)

@app.route('/year')
def year():
    return render_template('year.html')

app.run(debug=True)
