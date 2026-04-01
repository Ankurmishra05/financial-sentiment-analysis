import os
import gdown
import zipfile

MODEL_PATH = "models/finbert_model"

if not os.path.exists(MODEL_PATH):
    os.makedirs("models", exist_ok=True)

    url = "https://drive.google.com/file/d/13WAsFFupP_Ju5JcqsPTZnMm9CaQt5exn/view?usp=sharing"
    output = "models/model.zip"

    gdown.download(url, output, quiet=False)

    with zipfile.ZipFile(output, 'r') as zip_ref:
        zip_ref.extractall("models")

    os.remove(output)