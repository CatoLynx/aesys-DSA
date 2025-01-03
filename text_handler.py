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

import json
import time


class TextHandler:
    def __init__(self, texts_file):
        self.texts_file = texts_file
    
    def get_texts(self):
        try:
            with open(self.texts_file, 'r') as f:
                texts = json.load(f)
        except:
            texts = {}
        return texts
    
    def get_text(self, level):
        level = str(level)
        try:
            with open(self.texts_file, 'r') as f:
                texts = json.load(f)
        except:
            texts = {}
        return texts.get(level)
    
    def set_text(self, level, text_data):
        level = str(level)
        try:
            with open(self.texts_file, 'r') as f:
                texts = json.load(f)
        except:
            texts = {}
        
        if text_data.get('duration', 0) > 0:
            text_data['expires'] = round(time.time() + text_data['duration'])
        texts[level] = text_data
        
        with open(self.texts_file, 'w') as f:
            json.dump(texts, f)
    
    def delete_text(self, level):
        level = str(level)
        try:
            with open(self.texts_file, 'r') as f:
                texts = json.load(f)
        except:
            texts = {}
        
        if level in texts:
            del texts[level]
        
        with open(self.texts_file, 'w') as f:
            json.dump(texts, f)
