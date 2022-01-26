import dropbox

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)

        with open(file_from, 'rb') as f:
            dbx.files_upload(f.read(), file_to)

def main():
    access_token = 'sl.A_hLy-GBo9_gGlue7yrIiGbc3fVep3JimkGuzeR9cXs-jMdJmrgMPQYC-CeMVHCRL4y8aEnBuV4oFMee5aPRrx0rvK8TiOyZOxkkuwFE8Qg2d5GATnypMJ8J0O4agWTyq2KEVAU'
    transferData = TransferData(access_token)

    file_from = 'test.txt'
    file_to = 'C:/Users/TANVI/Desktop/TANVI/WhiteHat_Juniors_2020/Dropbox/'  # The full path to upload the file to, including the file name

    # API v2
    transferData.upload_file(file_from, file_to)

if __name__ == '__main__':
    main()