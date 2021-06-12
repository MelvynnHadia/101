import dropbox
import os

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_files(self, file_from, file_to, relative_path, local_path):
        dbx = dropbox.Dropbox(self.access_token)
        for root, dirs, files in os.walk(file_from):
            relative_path = os.path.relpath(local_path, file_from)
            dropbox_path = os.path.join(file_to, relative_path)
        with open(local_path, 'rb') as f:
            dbx.files_upload(f.read(), dropbox_path, mode=WriteMode('overwrite'))

    def main():
        access_token = 'sl.Aym7CfY3cel0GQZMIBz36665GxUKS9xJ1F6tjOzsN_Itkj7gS5rI9cEHisDJcJmWJdCi661mzuY1meMi_4TdX9iIDgJg3xtaMdYGOJWq5E9Jhu1Fdh1YT6jaaZrI_3cmmUHd3a0'
        transferData = TransferData(access_token)

        file_from = input("Enter file path:")
        file_to = input("Enter path to start uploading:")

        transferData.upload_files(file_from, file_to)
        print("Files have been uploaded")
