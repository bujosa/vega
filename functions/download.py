import requests
import uuid

def download_image(url: str) -> str:
    """This function is for download the image from a url
    and create a file"""
    img_data = requests.get(url).content
    name_file = "{uuid}.jpg".format(uuid=uuid.uuid1())
    with open(name_file, 'wb') as handler:
        handler.write(img_data)
    
    return name_file