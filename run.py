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

from pyfis.aesys import AesysDSA

from _config import *
from flask_app import app


def main():
    dsa = AesysDSA(CONFIG_DSA_PORT)
    app.config['dsa'] = dsa
    app.config['text'] = ""
    app.run(host="0.0.0.0")


if __name__ == "__main__":
    main()
