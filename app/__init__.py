# -*- coding: UTF-8 -*-

import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import basedir


app = Flask(__name__)

app.config.from_object('config')   # 载入配置文件
db = SQLAlchemy(app)               # 初始化 db 对象

import views, models

