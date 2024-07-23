import reflex as rx
from pymongo import MongoClient
#from PIL import Image
import io
import os
import base64
from rxconfig import config
from dotenv import load_dotenv
from image import process_image

load_dotenv()

app = rx.App()

mongo_uri = os.getenv('MONGO_URI')
client = MongoClient(mongo_uri)
db = client['reflex-webapp']
collection = db['ref-web']

@app.route('/')
def index():
    api_url = config.API_URL
    return rx.render(
        "index.html",
        title="Home",
        content=f"Hi Mason, Welcome to your Reflex Webapp! <br>API URL: {api_url}"
    )

@app.route('/data')
def data():
    example_data = collection.find_one()
    return rx.render("data.html", title="Data", content=f"Data from MongoDB: {example_data}")

@app.route('/image')
def image():
    image_path = "app/example.png"

    processed_image = process_image(image_path)
    
    if processed_image is not None:
        buffered = io.BytesIO()
        processed_image.save(buffered, format="PNG")
        img_str = base64.b64encode(buffered.getvalue()).decode()
        return rx.render("image.html", title="Processed Image", content=f"<img src='data:image/png;base64,{img_str}'/>")
    else:
        return rx.render("error.html", title="Error", content="Error processing image")

if __name__ == '__main__':
    app.run()