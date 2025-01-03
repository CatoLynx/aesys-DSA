"""
Copyright (C) 2023-2025 Julian Metzler

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

from flask import Flask, request, render_template
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import check_password_hash

from pyfis.aesys import AesysDSA

from _config import *
from local_secrets import USERS


app = Flask(__name__)
auth = HTTPBasicAuth()
dsa = AesysDSA(CONFIG_DSA_PORT)
text = ""


@auth.verify_password
def verify_password(username, password):
    if username in USERS and \
            check_password_hash(USERS.get(username), password):
        return username


@app.route("/", methods=["GET", "POST"])
@auth.login_required
def root():
    global dsa, text
    if request.method == "POST":
        text = str(request.form['text'])
        dsa.send_text(text)
    return render_template("text.html", text=text)

@app.route("/api/text.json", methods=["POST"])
@auth.login_required
def post_text():
    global dsa, text
    data = request.get_json()
    if 'text' not in data:
        return {'error': "No text provided"}
    text = str(data['text'])
    dsa.send_text(text)
    return {'error': None}

@app.route("/api/text.json", methods=["GET"])
def get_text():
    global text
    return {'error': None, 'text': text}
