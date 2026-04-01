import os
import gdown
import zipfile

MODEL_PATH = "models/finbert_model"

if not os.path.exists(MODEL_PATH):
    os.makedirs("models", exist_ok=True)

    url = "https://drive.google.com/uc?id=13WAsFFupP_Ju5JcqsPTZnMm9CaQt5exn"
    output = "models/model.zip"

    gdown.download(url, output, quiet=False)

    if not zipfile.is_zipfile(output):
        raise Exception("Download failed. Not a zip file.")

    with zipfile.ZipFile(output, 'r') as zip_ref:
        zip_ref.extractall("models")

    os.remove(output)