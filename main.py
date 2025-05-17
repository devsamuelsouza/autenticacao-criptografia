from flask import Flask
from dotenv import load_dotenv
import os

load_dotenv()

main = Flask(__name__)
main.secret_key = os.getenv("SECRET_KEY")

from rotas import *

if __name__ == '__main__':
    main.run(debug=False, host='0.0.0.0', port=80)
