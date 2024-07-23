from PIL import Image, ImageFilter

def process_image(image_path):
    try:
        image = Image.open(image_path)
    except FileNotFoundError:
        print(f"File not found: {image_path}")
        return None
    except Exception as e:
        print(f"Error opening image: {e}")
        return None

    try:
        image = image.resize((200, 200))
        image = image.crop((50, 50, 150, 150))
        image = image.filter(ImageFilter.BLUR)
    except Exception as e:
        print(f"Error processing image: {e}")
        return None

    return image