from google.colab import drive
import zipfile
drive.mount('/content/drive')

!wget https://github.com/jeonyongjae/LG-Academy/raw/main/Quiz_1.zip -O /content/drive/MyDrive/Quiz_1.zip

# 압축 풀고자 하는 zip 파일 경로
zip_file_path = '/content/drive/MyDrive/Quiz_1.zip'

# 압축을 풀 폴더 경로
extract_path = '/content/drive/MyDrive/'

# 압축 풀기
with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
    zip_ref.extractall(extract_path)
