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

from pyfis.aesys import AesysDSA


class DSA:
    def __init__(self, port, text_handler):
        self.port = port
        self.text_handler = text_handler
        self.dsa = AesysDSA(port)
    
    def set_text(self, text):
        return self.dsa.send_text(text)
