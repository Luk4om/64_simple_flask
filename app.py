from flask import Flask, request, send_file, jsonify
import requests

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def root():
    if request.method == 'GET':
        return send_file("./hello.html")
    elif request.method == 'POST':
        return "<h1>Hello POST</h1>"
    else :
        return "ERROR"

@app.route('/user/<id>')
def user(id):
    return f"<h1>Hello Page: {id}</h1>"

@app.route('/api')
def api():

    reqUrl = "https://www.themealdb.com/api/json/v1/1/random.php"
    headersList = {
        "Accept": "*/*",
        "User-Agent": "Thunder Client (https://www.thunderclient.com)" 
    }

    payload = ""
    response = requests.request("GET", reqUrl, data=payload,  headers=headersList)
    cat = response.json()['meals'][0]['strCategory']

    if response.status_code == 200:
        return {
            "status": 200,
            # "data": response.json(),
            "data": cat,
            "message": "Hello World"
        }

if __name__ == '__main__':
    app.run(debug=True, port=80)