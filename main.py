import base64
from functions.download import download_image
from functions.removebg import removebg
from functions.storage import Storage

def receive_removebg_picture_call(event, context):
    """Triggered from a message on a Cloud Pub/Sub topic.
    Args:
         event (dict): Event payload.
         context (google.cloud.functions.Context): Metadata for the event.
    """
    pubsub_message = base64.b64decode(event['data']).decode('utf-8')
    print(pubsub_message)

    """ Download image and remove background process"""
    input = download_image(pubsub_message.url)
    output = removebg(input)


    storage = Storage(pubsub_message.url, output)
    """ This part is optional, because it is a custom logic to replace the existing
     image file and upload it with the same one but without background"""
    storage.remove_background() 