import base64
import io
import json
import numpy as np
from flask import Flask, jsonify, request
from PIL import Image

app = Flask(__name__)


@app.route("/face-detect/", methods=["GET", "POST"])
def face_detect():
    if request.method == "POST":
        data = json.loads(request.data)
        image_string = data["image"].split(",")[1]
        image_data = io.BytesIO(base64.b64decode(image_string))
        image = Image.open(image_data)
        image_array = np.asarray(image)
        print(image_array)
        return jsonify({"result": "ok"})

    return "face detection"


if __name__ == "__main__":
    app.run()
