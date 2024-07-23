from PIL import Image, ImageFilter

def process_image(image_path):
    image = Image.open(image_path)

    image = image.resize((200, 200))
    
    image = image.crop((50, 50, 150, 150))

    image = image.filter(ImageFilter.BLUR)

    return image