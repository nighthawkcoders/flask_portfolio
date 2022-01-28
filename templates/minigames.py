from flask import Flask, Blueprint, render_template, request
import requests
from __init__ import app
import json

minigame_ = Blueprint('travel', __name__,
                      url_prefix='/travel',
                      template_folder='templates',
                      static_folder='static', static_url_path='static/travel')

