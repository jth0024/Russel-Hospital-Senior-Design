import os
from flask import Flask, jsonify
from flask import url_for

app = Flask(__name__)

from rh import views