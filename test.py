# https://github.com/jeonyongjae/LG-Academy.git
from google.colab import drive
drive.mount('/content/drive')

import requests

url = 'https://github.com/jeonyongjae/LG-Academy.git/24%EB%85%84_AI_Code(%EC%8B%A4%EC%8A%B5%EC%BD%94%EB%93%9C)_2%EC%B0%A8%EC%88%98.zip'
save_path = '/content/drive/MyDrive/AI_Code_Quiz1.zip'

response = requests.get(url)
with open(save_path, 'wb') as f:
    f.write(response.content)

print(f"저장!!: {save_path}")

import zipfile

unzip_folder_path = '/content/drive/MyDrive/AI_Code'
with zipfile.ZipFile(save_path, 'r') as zip_ref:
    zip_ref.extractall(unzip_folder_path)

print(f"압축 해제: {unzip_folder_path}")
