from flask import Flask, jsonify, request, make_response

app = Flask(__name__)

@app.route('/')
def hello_world():
    data = {
        "message": "hello world"
    }
    return data

@app.route('/profile')
def my_profile():
    response_body = {
        "name": "Nagato",
        "about" :"Hello! I'm a full stack developer that loves python and javascript"
    }

    return response_body

@app.route('/view-projects')
def view_projects():
    return 

if __name__ == '__main__':
    app.run()