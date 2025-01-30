from flask import Flask
from dotenv import dotenv_values

config_dotenv = dotenv_values(".env")

main = Flask(__name__)
main.secret_key = config_dotenv.get("SECRET_KEY")

from rotas import *

if __name__ == '__main__':
    main.run(debug=False, host='0.0.0.0', port=80)
