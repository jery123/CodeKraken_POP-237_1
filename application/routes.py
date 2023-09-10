from application import app
from flask import render_template, url_for, request, redirect
import secrets
import os

import cv2
import pytesseract
import numpy as np


@app.route("/")
def index():
    return render_template("index.html", title="Home page")


@app.route("/upload", methods=["GET", "POST"])
def upload():
    if request.method == "POST":

        sentence = ""

        f = request.files.get("file")
        filename, extension = f.filename.split(".")
        generated_filename = secrets.token_hex(10) + f".{extension}"  # to generate a name for our images

        file_location = os.path.join(app.config['UPLOADED_PATH'], generated_filename)

        f.save(file_location)
        # If you don't have tesseract executable in your PATH, include the following:
        # pytesseract.pytesseract.tesseract_cmd = r'<full_path_to_your_tesseract_executable>'
        tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tessdata'

        img = cv2.imread(file_location)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # to convert image to black

        boxes = pytesseract.image_to_data(img)

        for i, box in enumerate(boxes.splitlines()):
            if i == 0:
                continue
            box = box.split()

            if len(box) == 12:
                sentence += box[11] + " "
        print(sentence)

        return redirect("/decoded/")

    else:
        return render_template("upload.html", title="Upload")


@app.route("/decoded", methods=["POST", "GEt"])
def decoded():
    return "Salut toi"
