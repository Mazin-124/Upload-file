import os
import dropbox


class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)

        for root, dirs, files in os.walk(file_from):

            for file_name in files:
                local_path = os.path.join(root, file_name)

                relative_path = os.path.relpath(local_path, file_from)
                dropbox_path = os.path.join(file_to, relative_path)

                with open(file_from, 'rb') as f:
                    dbx.files_upload(f.read(), dropbox_path, mode= WriteMode('overwrite'))


def main():
    access_token = 'sl.A7jtOZHXs3mLnfuJ0PDo0vdWYDWWhO-FvIPZf6PaXtnkd0t16bbhiBW2qx4Dyz3k14s-1XY-Ttm7xn8-WbJObNkJqB_jB2yC-nCiNh9YIkjyP_Q-Ufq39bHFZwfO_YJ0Dh6aPNI'
    transferData = TransferData(access_token)

    file_from = str(input('Enter your folder path: '))
    file_to = input('Enter the full path to upload to dropbox: ')

    transferData.upload_file(file_from, file_to)
    print('File has been saved !')

    main()