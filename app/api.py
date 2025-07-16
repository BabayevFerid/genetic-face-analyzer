from flask import Flask, request, render_template
from app.analyzer import analyze_image
import os

app = Flask(__name__)
UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    image_path = None

    if request.method == 'POST':
        if 'image' not in request.files:
            return "No file part", 400

        image = request.files['image']
        if image.filename == '':
            return "No selected file", 400

        image_path = os.path.join(app.config['UPLOAD_FOLDER'], image.filename)
        image.save(image_path)

        result = analyze_image(image_path)

    return render_template('index.html', result=result, image_path=image_path)
