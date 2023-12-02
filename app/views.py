import os
import cv2
from app.yoloObject import objectRecognitionPipeline
from flask import render_template, request
import matplotlib.image as matimg

UPLOAD_FOLDER='static/upload'

def index():
    return render_template('index.html')

def app():
    return render_template('app.html')