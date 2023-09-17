import os
from flask import Flask, render_template, request
from PIL import Image
from ultralytics import YOLO
from werkzeug.utils import secure_filename


app = Flask(__name__)

# Set the upload folder
app.config['UPLOAD_FOLDER'] = 'uploads'

# Define the allowed file extensions
ALLOWED_EXTENSIONS = {'jpg', 'jpeg', 'png', 'gif'}
app.config['ALLOWED_EXTENSIONS'] = ALLOWED_EXTENSIONS


@app.route("/")
def hello_world():
    return render_template('index.html')


@app.route("/", methods=["POST"])
def predict_img():
    if 'file' in request.files:
        f = request.files['file']
        filename = secure_filename(f.filename)
        file_extension = filename.rsplit('.', 1)[1].lower()

        if file_extension in ALLOWED_EXTENSIONS:
            # Save the uploaded image
            upload_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            f.save(upload_path)

            # Perform the detection
            image = Image.open(upload_path)
            yolo = YOLO('best.pt')
            detections = yolo.predict(image)

            # Convert detections to PIL Image
            

            # Save the output image
            # Save each detected object as a separate image

             

            return 'Output image saved successfully!'

    return "Invalid file format"


if __name__ == "__main__":
    app.run(debug=True)
