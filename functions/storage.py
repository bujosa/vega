import os
from google.cloud import storage

class Storage:
    def __init__(self, url: str, path: str):
        self.storage_client = storage.Client(project=os.environ['GOOGLE_PROJECT_ID'], credentials={
            "client_email": os.environ['CLIENT_EMAIL'],
            "private_key": os.environ['PRIVATE_KEY']
        })
        self.url = url
        self.file_name = self.url.split(self.bucket_name).pop()
        self.bucket_name = os.environ['BUCKET_NAME']
        self.bucket = self.storage_client.get_bucket(self.bucket_name)
        self.path = path

    
    def remove_background(self):
        """Changes picture in storage to a new without background"""
        self.__remove()
        self.__upload()

    def __upload(self):
        """Upload image to a cloud storage"""
        blob = self.bucket.blob(self.file_name)
        blob.upload_from_filename(self.path)


    def __remove(self):
        """Remove image from cloud storage"""
        blob = self.bucket.get_blob(self.file_name)
        blob.delete()

