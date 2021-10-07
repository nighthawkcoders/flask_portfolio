import base64
from io import BytesIO
import numpy
from PIL import Image, ImageDraw, ImageFilter
import re


def image_base64(img, img_type):
    with BytesIO() as buffer:
        img.save(buffer, img_type)
        return base64.b64encode(buffer.getvalue()).decode()


# formatter preps base64 string for inclusion, ie <img src=[this return value] ... />
def image_formatter(img, img_type):
    return "data:image/" + img_type + ";base64," + image_base64(img, img_type)

def imgToHex(file):
    string = ''
    with open(file, 'rb') as f:
        binValue = f.read(1)
        while len(binValue) != 0:
            hexVal = hex(ord(binValue))
            string += '\\' + hexVal
            binValue = f.read(1)
    string = re.sub('0x', 'x', string) # Replace '0x' with 'x' for your needs
    return string

def imgToBin(file):
    string = ''
    with open(file, 'rb') as f:
        binValue = f.read(1)
    return binValue

def rotatehack(path="static/assets/sonakshiimages/", img_list=None):
    if img_list is None:  # color_dict is defined with defaults
        img_list = [
            {'source': "Blue", 'label': "Blue", 'file': "blue.png"},
            {'source': "Green", 'label': "Green", 'file': "green.png"},
            {'source': "Orange", 'label': "Orange", 'file': "orange.png"},
            {'source': "Red", 'label': "Red", 'file': "red.png"},
        ]
    for img_dict in img_list:
        img_dict['path'] = '/' + path  # path for HTML access (frontend)
        file = path + img_dict['file']  # file with path for local access (backend)
        # hack testing
        img = Image.open(file)
        clear = img.copy() # opens file to work
        OriImage = clear.transpose(Image.ROTATE_90)
        OriImage.save(path + 'new' + img_dict['file'])  # saves clean copy as "new<file>.jpg"
    # appending to img_list so the images can load on the html
    img_list.clear()
    img_list.append({'source': "Blue", 'label': "Blue", 'file': "newblue.png"},)
    img_list.append({'source': "Green", 'label': "Green", 'file': "newgreen.png"},)
    img_list.append({'source': "Orange", 'label': "Orange", 'file': "neworange.png"},)
    img_list.append({'source': "Red", 'label': "Red", 'file': "newred.png"})



def sonakshi_image_data(path="static/assets/sonakshiimages/", img_list=None):
    if img_list is None:  # color_dict is defined with defaults
        img_list = [
            {'source': "Blue", 'label': "Blue", 'file': "blue.png"},
            {'source': "Green", 'label': "Green", 'file': "green.png"},
            {'source': "Orange", 'label': "Orange", 'file': "orange.png"},
            {'source': "Red", 'label': "Red", 'file': "red.png"},
        ]
    # gather analysis data and meta data for each image, adding attributes to each row in table
    for img_dict in img_list:
        img_dict['path'] = '/' + path  # path for HTML access (frontend)
        file = path + img_dict['file']  # file with path for local access (backend)
        # Python Image Library operations
        img_reference = Image.open(file)  # PIL
        # HERE is commit for adding text into images
        draw = ImageDraw.Draw(img_reference)
        draw.text((25, 25), "Writing on images!", fill=(500, 500, 500))
        hori_flippedImage = img_reference.transpose(Image.FLIP_LEFT_RIGHT)
        hori_flippedImage.save(file)# draw in image
        img_data = img_reference.getdata()  # Reference https://www.geeksforgeeks.org/python-pil-image-getdata/
        img_dict['format'] = img_reference.format
        img_dict['mode'] = img_reference.mode
        img_dict['size'] = img_reference.size
        # Conversion of original Image to Base64, a string format that serves HTML nicely
        img_dict['base64'] = image_formatter(img_reference, img_dict['format'])
        # Numpy is used to allow easy access to data of image, python list
        img_dict['data'] = numpy.array(img_data)
        img_dict['hex_array'] = []
        img_dict['binary_array'] = []
        img_dict['gray_data'] = []
        # 'data' is a list of RGB data, the list is traversed and hex and binary lists are calculated and formatted
        for pixel in img_dict['data']:
            # hexadecimal conversions
            hex_value = hex(pixel[0])[-2:] + hex(pixel[1])[-2:] + hex(pixel[2])[-2:]
            hex_value = hex_value.replace("x", "0")
            img_dict['hex_array'].append("#" + hex_value)
            # binary conversions
            bin_value = bin(pixel[0])[2:].zfill(8) + " " + bin(pixel[1])[2:].zfill(8) + " " + bin(pixel[2])[2:].zfill(8)
            img_dict['binary_array'].append(bin_value)
            # create gray scale of image, ref: https://www.geeksforgeeks.org/convert-a-numpy-array-to-an-image/
            img_dict['gray_data'] = []
        for pixel in img_dict['data']:
            average = (pixel[0] + pixel[1] + pixel[2]) // 3
            if len(pixel) > 3:
                img_dict['gray_data'].append((average, average, average, pixel[3]))
            else:
                img_dict['gray_data'].append((average, average, average))
        img_reference.putdata(img_dict['gray_data'])
        img_dict['base64_GRAY'] = image_formatter(img_reference, img_dict['format'])
        # hack testing
    return img_list  # list is returned with all the attributes for each image dictionary




def kashish_image_data(path="static/assets/kashishimages/", img_list=None):
    if img_list is None:  # color_dict is defined with defaults
        img_list = [
            {'source': "Apples", 'label': "Apples", 'file': "apples.png"},
            {'source': "Bananas", 'label': "Bananas", 'file': "bananas.png"},
            {'source': "Oranges", 'label': "Oranges", 'file': "oranges.png"},
            {'source': "Strawberries", 'label': "Strawberries", 'file': "strawberries.png"},
        ]
    # gather analysis data and meta data for each image, adding attributes to each row in table
    for img_dict in img_list:
        img_dict['path'] = '/' + path  # path for HTML access (frontend)
        file = path + img_dict['file']  # file with path for local access (backend)
        # Python Image Library operations
        img_reference = Image.open(file)  # PIL
        # HERE is commit for adding text into images
        draw = ImageDraw.Draw(img_reference)
        draw.text((25, 25), "Writing on images!", fill=(500, 500, 500))  # draw in image
        img_data = img_reference.getdata()  # Reference https://www.geeksforgeeks.org/python-pil-image-getdata/
        img_dict['format'] = img_reference.format
        img_dict['mode'] = img_reference.mode
        img_dict['size'] = img_reference.size
        # Conversion of original Image to Base64, a string format that serves HTML nicely
        img_dict['base64'] = image_formatter(img_reference, img_dict['format'])
        # Numpy is used to allow easy access to data of image, python list
        img_dict['data'] = numpy.array(img_data)
        img_dict['hex_array'] = []
        img_dict['binary_array'] = []
        img_dict['gray_data'] = []
        # 'data' is a list of RGB data, the list is traversed and hex and binary lists are calculated and formatted
        for pixel in img_dict['data']:
            # hexadecimal conversions
            hex_value = hex(pixel[0])[-2:] + hex(pixel[1])[-2:] + hex(pixel[2])[-2:]
            hex_value = hex_value.replace("x", "0")
            img_dict['hex_array'].append("#" + hex_value)
            # binary conversions
            bin_value = bin(pixel[0])[2:].zfill(8) + " " + bin(pixel[1])[2:].zfill(8) + " " + bin(pixel[2])[2:].zfill(8)
            img_dict['binary_array'].append(bin_value)
        # create gray scale of image, ref: https://www.geeksforgeeks.org/convert-a-numpy-array-to-an-image/
            img_dict['gray_data'] = []
        for pixel in img_dict['data']:
            average = (pixel[0] + pixel[1] + pixel[2]) // 3
            if len(pixel) > 3:
                img_dict['gray_data'].append((average, average, average, pixel[3]))
            else:
                img_dict['gray_data'].append((average, average, average))
        img_reference.putdata(img_dict['gray_data'])
        img_dict['base64_GRAY'] = image_formatter(img_reference, img_dict['format'])
        # hack testing
    return img_list  # list is returned with all the attributes for each image dictionary

def saumya_image_data(path="static/assets/saumyaimages/", img_list=None):
    if img_list is None:  # color_dict is defined with defaults
        img_list = [
            {'source': "Beach", 'label': "Beach", 'file': "beach.png"},
            {'source': "City", 'label': "City", 'file': "city.png"},

        ]
    # gather analysis data and meta data for each image, adding attributes to each row in table
    for img_dict in img_list:
        img_dict['path'] = '/' + path  # path for HTML access (frontend)
        file = path + img_dict['file']  # file with path for local access (backend)
        # Python Image Library operations
        img_reference = Image.open(file)  # PIL
        # HERE is commit for adding text into images
        draw = ImageDraw.Draw(img_reference)
        draw.text((25, 25), "Writing on images!", fill=(500, 500, 500))  # draw in image
        img_data = img_reference.getdata()  # Reference https://www.geeksforgeeks.org/python-pil-image-getdata/
        img_dict['format'] = img_reference.format
        img_dict['mode'] = img_reference.mode
        img_dict['size'] = img_reference.size
        # Conversion of original Image to Base64, a string format that serves HTML nicely
        img_dict['base64'] = image_formatter(img_reference, img_dict['format'])
        # Numpy is used to allow easy access to data of image, python list
        img_dict['data'] = numpy.array(img_data)
        img_dict['hex_array'] = []
        img_dict['binary_array'] = []
        img_dict['gray_data'] = []
        # 'data' is a list of RGB data, the list is traversed and hex and binary lists are calculated and formatted
        for pixel in img_dict['data']:
            # hexadecimal conversions
            hex_value = hex(pixel[0])[-2:] + hex(pixel[1])[-2:] + hex(pixel[2])[-2:]
            hex_value = hex_value.replace("x", "0")
            img_dict['hex_array'].append("#" + hex_value)
            # binary conversions
            bin_value = bin(pixel[0])[2:].zfill(8) + " " + bin(pixel[1])[2:].zfill(8) + " " + bin(pixel[2])[2:].zfill(8)
            img_dict['binary_array'].append(bin_value)
            # create gray scale of image, ref: https://www.geeksforgeeks.org/convert-a-numpy-array-to-an-image/
            img_dict['gray_data'] = []
        for pixel in img_dict['data']:
            average = (pixel[0] + pixel[1] + pixel[2]) // 3
            if len(pixel) > 3:
                img_dict['gray_data'].append((average, average, average, pixel[3]))
            else:
                img_dict['gray_data'].append((average, average, average))
        img_reference.putdata(img_dict['gray_data'])
        img_dict['base64_GRAY'] = image_formatter(img_reference, img_dict['format'])
        # hack testing
    return img_list  # list is returned with all the attributes for each image dictionary

