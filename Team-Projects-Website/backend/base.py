from flask import Flask, jsonify, request, make_response, redirect, url_for
import Login

app = Flask(__name__)

@app.route('/auth', methods=['POST', 'GET'])
def authenticate_user():
    response_body = {
        "name": "Nagato",
        "about" :"Hello! I'm a full stack developer that loves python and javascript"
    }

    if request.method == 'POST':
        fullName = request.form['Full Name']
        Username = request.form['Username']
        Password = request.form['Password']
        print('full name: ', fullName)
        print('username: ', Username)
        print('password: ', Password)
        Login.signup(fullName, Username, Password)
        return response_body
        # return redirect(url_for("user",usr=user))

# @app.route('/auth')
# def authenticateUser():
#     return

@app.route('/profile')
def my_profile():
    response_body = {
        "name": "Nagato",
        "about" :"Hello! I'm a full stack developer that loves python and javascript"
    }

    return response_body

@app.route('/view-projects')
def view_projects():
    return {'msg':'hello peepee'}

if __name__ == '__main__':
    app.run()