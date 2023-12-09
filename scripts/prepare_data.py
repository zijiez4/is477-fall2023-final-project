import requests
import os
import hashlib
import zipfile
 
def check_path(path):
    if not os.path.exists(path):
        os.makedirs(path,exist_ok=True)
    else:
        print(f'{path} already exist')

def clean(path,file_path):
    with zipfile.ZipFile(file_path, mode="r") as archive:
        archive.extractall(path)
        print(f'The downloaded file is unzipped successfully')
    os.remove(file_path)
    print(f'Remove the downloaded file')

def download_and_hashCheck(url,file_path,initial_hash,path):
    response=requests.get(url)
    if response.status_code==200:
        with open(file_path,'wb') as files:
            new_hash = hashlib.sha256(response.content).hexdigest()
            if initial_hash == new_hash:
                print('The SHA256 of the downloaded file matches the expected value.')
                files.write(response.content)
                print('File download successful')
            else:
                print(f'Error: The SHA256 of the downloaded file does not matches the expected value. \nCheck the url: {url}')
            files.close()
    else:
        print(f'The file cannot be downloaded: {url}')
    clean(path,file_path)

def main():
    initial_hash = "2bae62c4481220623579d4c4fb36b55652b6b75e06e49fa1981b8198362dfdab"
    download_link = "https://archive.ics.uci.edu/static/public/109/wine.zip"
    path = './data'
    file_path = './data/wine.zip'
    check_path(path)
    download_and_hashCheck(download_link,file_path,initial_hash,path)

main()
