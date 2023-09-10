from flask import Flask
from flask_dropzone import Dropzone
import os

app =  Flask(__name__)

dir_path = os.path.dirname(os.path.realpath(__file__))

app.config.update(
    UPLOADED_PATH = os.path.join(dir_path, "static/uploaded_files/"),
    DROPZONE_ALLOW_FILE_TYPE = 'image',
    DROPZONE_MAX_FILE_SIZE = 3,
    DROPZONE_MAX_FILES = 1,
    AUDIO_FILE_UPLOAD = os.path.join(dir_path, "stactic/audio_files/")
)


app.config['DROPZONE_REDIRECT_VIEW'] = 'decoded'

dropzone = Dropzone(app)


from application import routes