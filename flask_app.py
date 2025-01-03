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
from text_handler import TextHandler

from _config import *
from local_secrets import USERS


app = Flask(__name__)
auth = HTTPBasicAuth()
handler = TextHandler(CONFIG_TEXTS_FILE)


@auth.verify_password
def verify_password(username, password):
    if username in USERS and \
            check_password_hash(USERS.get(username), password):
        return username


@app.route("/", methods=["GET", "POST"])
@auth.login_required
def root():
    if request.method == "POST":
        text_data = {
            "text": str(request.form['text']),
            "duration": 0,
            "time_format": True
        }
        handler.set_text(0, text_data)
    text_data = handler.get_text(0)
    if text_data is None:
        text = ""
    else:
        text = text_data['text']
    return render_template("text.html", text=text)


@app.route("/api/text.json", methods=["POST"])
@auth.login_required
def post_text():
    data = request.get_json()
    if 'text' not in data:
        return {'error': "No text provided"}
    
    try:
        level = int(data['level'])
    except:
        level = 0
    
    try:
        text = str(data['text'])
    except:
        return {'error': "Invalid text"}
    
    try:
        duration = int(data['duration'])
    except:
        duration = 0
    
    try:
        time_format = bool(data['time_format'])
    except:
        time_format = False
    
    if text:
        text_data = {
            "text": text,
            "duration": duration,
            "time_format": time_format
        }
        handler.set_text(level, text_data)
    else:
        handler.delete_text(level)
    
    return {'error': None}

@app.route("/api/text.json", methods=["GET"])
@auth.login_required
def get_text():
    try:
        level = int(request.args.get('level'))
    except:
        level = 0
    text_data = handler.get_text(level)
    if text_data is None:
        return {'error': None, 'text': ""}
    else:
        response = {'error': None}
        response.update(text_data)
        return response
