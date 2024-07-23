import reflex as rx
from pymongo import MongoClient
from PIL import Image
import io
import base64
from dotenv import load_dotenv
import os

load_dotenv()

app = rx.App()

mongo_uri = os.getenv('MONGO_URI')
client = MongoClient(mongo_uri)
db = client['example_db']
collection = db['example_collection']

@app.route('/')
def index():
    return rx.render("index.html", title="Home", content="Hi Mason, Welcome to your Reflex Webapp!")

@app.route('/data')
def data():
    example_data = collection.find_one()
    return rx.render("data.html", title="Data", content=f"Data from MongoDB: {example_data}")

@app.route('/image')
def image():
    image = Image.open("app/example.png")
    buffered = io.BytesIO()
    image.save(buffered, format="PNG")
    img_str = base64.b64encode(buffered.getvalue()).decode()
    return rx.render("image.html", title="Image", content=f"<img src='data:image/png;base64,{img_str}'/>")

if __name__ == '__main__':
    app.run()