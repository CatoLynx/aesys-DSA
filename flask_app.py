"""
Copyright (C) 2023 Julian Metzler

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


app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def root():
    if request.method == "POST":
        app.config['text'] = str(request.form['text'])
        app.config['dsa'].send_text(app.config['text'])
    return render_template("text.html", text=app.config['text'])

@app.route("/api/text.json", methods=["POST"])
def post_text():
    data = request.get_json()
    if 'text' not in data:
        return {'error': "No text provided"}
    app.config['text'] = str(data['text'])
    app.config['dsa'].send_text(app.config['text'])
    return {'error': None}

@app.route("/api/text.json", methods=["GET"])
def get_text():
    return {'error': None, 'text': app.config['text']}
