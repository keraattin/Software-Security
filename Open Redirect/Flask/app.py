#!/usr/bin/env python3

# Subject: Open Redirect
# Language: Python
# Framework: Flask

# Example Request
# http://localhost:5000/redirect?next=https://malicioussite.xyz

# Libraries
from flask import Flask,request,redirect

# App
app = Flask(__name__)

# Routes
@app.route("/redirect")
def redirected_page():
    next = request.args.get("next")
    return redirect(next)

# Main
if __name__ == '__main__':
	app.run(port=5000,debug=True)
