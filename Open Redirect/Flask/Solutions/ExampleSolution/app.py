#!/usr/bin/env python3

"""
Example Solution Code
"""

# Vulnerability:        Open Redirect
# Language:             Python
# Language Version:     3.10
# Framework:            Flask
# Framework Version:    2.3.2
# Enviroment:           Web


# Example Request
# http://localhost:5000/redirect?next=https://malicioussite.xyz

# Libraries
from flask import Flask,request,redirect
"""
 Your Libraries Here !!!
"""

# App
app = Flask(__name__)

# Routes
@app.route("/")
def home():
      return """
        <h3>Example Request</h3>
        <i>http://localhost:5000/redirect?next=https://malicioussite.xyz</i>  
        """

# Vulnerable Routes
@app.route("/redirect")
def redirected_page():
    """
     Your Code Here or Somewhere Around !!!
    """
    next = request.args.get("next")
    return redirect(next)

# Main
if __name__ == '__main__':
	app.run(host='0.0.0.0')
