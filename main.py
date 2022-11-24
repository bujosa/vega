import os
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
    input = download_image(pubsub_message.url)
    output = removebg(input)
    storage = Storage(pubsub_message.url, output)
    storage.remove_background()
    os.remove(output)
