import os
from google.cloud import storage

class Storage:
    """ This class implement package storage and define logic to upload and remove file in
    the bucket"""
    def __init__(self, url: str, path: str):
        self.__storage_client = storage.Client(project=os.environ['GOOGLE_PROJECT_ID'], credentials={
            "client_email": os.environ['CLIENT_EMAIL'],
            "private_key": os.environ['PRIVATE_KEY']
        })
        self.__bucket_name = os.environ['BUCKET_NAME']
        self.__path = path
        self.__url = url
        self.__file_name = self.__url.split(self._bucket_name).pop()
        self.__bucket = self.__get_bucket()

    def remove_background(self):
        """Changes picture in storage to a new without background"""
        self.__remove()
        self.__upload()
        os.remove(self.__path)

    def __upload(self):
        """Upload image to a cloud storage"""
        try: 
            blob = self.__bucket.blob(self.__file_name)
            blob.upload_from_filename(self.__path)
        except Exception as e:
            print(e)
            return e

    def __remove(self):
        """Remove image from cloud storage"""
        try: 
            blob = self.__bucket.get_blob(self.__file_name)
            blob.delete()
        except Exception as e:
            print(e)
            return e

    def __get_bucket(self):
        """ This method is only to get instance of the bucket"""
        return self.__storage_client.get_bucket(self.__bucket_name)
