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

import time

from dsa import DSA
from text_handler import TextHandler

from _config import *


def main():
    handler = TextHandler(CONFIG_TEXTS_FILE)
    dsa = DSA(CONFIG_DSA_PORT, handler)
    
    handler.set_text(0, {'text': "Zeit: %H:%M Uhr", 'time_format': True})
    
    prev_text = ""
    while True:
        texts = sorted(handler.get_texts().items(), key=lambda item: item[0], reverse=True)
        for level, text_data in texts:
            if 'expires' in text_data:
                if time.time() >= text_data['expires']:
                    continue
            if text_data.get('time_format', False):
                text = time.strftime(text_data['text'])
            else:
                text = text_data['text']
            
            if text != prev_text:
                dsa.set_text(text)
                print("Updating text:", text)
                prev_text = text
            
            break
        
        time.sleep(1)


if __name__ == "__main__":
    main()
