import base64
from io import BytesIO
from pathlib import Path
from PIL import Image

def image_base64(img, img_type):
    with BytesIO() as buffer:
        img.save(buffer, img_type)
        return base64.b64encode(buffer.getvalue()).decode()


# formatter preps base64 string for inclusion, ie <img src=[this return value] ... />
def image_formatter(img, img_type):
    return "data:image/" + img_type + ";base64," + image_base64(img, img_type)


def pinfo(path=Path("blueprints/testconnorimages"), pimage=None):  # path of static images is defaulted
    if pimage is None:  # color_dict is defined with defaults
        pimage = [
            {'animal': "Dogs", 'habitat': "House", 'Slogan': "Man's Best Friend", 'file': "dog.jpeg"},
            {'animal': "Cats", 'habitat': "Outdoors/House", 'Slogan': "Do not take much care", 'file': "cats.jpeg"},
            {'animal': "Hamsters", 'habitat': "Cage/House", 'Slogan': "Cute and fluffy", 'file': "hamster.jpeg"},
            {'animal': "Birds", 'habitat': "Bird Cage", 'Slogan': "Pretty and colorful", 'file': "bird.jpeg"},
            {'animal': "Snakes", 'habitat': "Cage/House", 'Slogan': "Slick and menacing", 'file': "snake.jpeg"},
            {'animal': "Mice", 'habitat': "Cage", 'Slogan': "Small and pesky", 'file': "mice.jpeg"},
            {'animal': "Guinea Pigs", 'habitat': "Cage", 'Slogan': "Cute and chubby", 'file': "guinea pig.jpeg"},
            {'animal': "Lizards", 'habitat': "Cage", 'Slogan': "Scaly and scary", 'file': "lizard.jpeg"},
            {'animal': "Rabbits", 'habitat': "Cage", 'Slogan': "Fluffy", 'file': "rabbit.jpeg"},
            {'animal': "Ferrets", 'habitat': "Cage", 'Slogan': "A great pet on your shoulder!", 'file': "ferret.jpeg"},
            {'animal': "Turtles", 'habitat': "Cage", 'Slogan': "Slow and minds their own business", 'file': "turtle.jpeg"},
            {'animal': "Fish", 'habitat': "Aquariam Tank", 'Slogan': "Colorful", 'file': "fish.jpeg"},
            {'animal': "Frog", 'habitat': "Cage", 'Slogan': "Jumps high!", 'file': "frog.jpeg"},
        ]
    # gather analysis data and meta data for each image, adding attributes to each row in table
    for image in pimage:

        filename = path / image['file']
        img_object = Image.open(filename)
        image['format'] = img_object.format
        image['mode'] = img_object.mode
        image['size'] = img_object.size
        img_object = img_object.rotate(0)
        image['base64'] = image_formatter(img_object, image['format'])

    # end for loop for images
    return pimage

