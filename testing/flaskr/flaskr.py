# all the imports
import os
import sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, \
  render_template, flash

# Create our little application :)
app = Flask(_name_)
app.config.from_object(_name_)

# Load default config and override config from an environment variable
app.config.update(dict(
  DATABASE=os.path.join(app.root_path, 'flaskr.db'),
  DEBUG=True,
  SECRET_KEY='development key',
  USERNAME='admin',
  PASSWORD='default'
))
app.config.from_envvar('FLASKR_SETTINGS', silent=True)
