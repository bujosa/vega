import os
import uuid
from rembg import remove

def removebg(input_path: str) -> str:
    """This function takes the path of the image,
    to remove the background and then generates an output
    for that photo, after that it removes the input_path"""
    output_path = "{uuid}.jpg".format(uuid=uuid.uuid1())
    with open(input_path, 'rb') as i:
        with open(output_path, 'wb') as o:
            input = i.read()
            output = remove(input)
            o.write(output)
    
    os.remove(input_path)
    return output_path    
