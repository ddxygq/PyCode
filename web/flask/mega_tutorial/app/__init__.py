from flask import Flask
import sys

app = Flask(__name__)


sys.path.append('../')
import routes