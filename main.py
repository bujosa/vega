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

    # Step 1 -> Decode message and print message
    pubsub_message = base64.b64decode(event['data']).decode('utf-8')
    print(pubsub_message)

    # Step 2 -> Download image and remove background process
    input = download_image(pubsub_message.url)
    output = removebg(input)

    # Step 3 -> Initilized storage class with url and output picture
    storage = Storage(pubsub_message.url, output)
    
    # Step 4 (optional) -> This part is optional, because it is a custom logic to 
    # replace the existingimage file and upload it with the same one but without background
    storage.remove_background()
 