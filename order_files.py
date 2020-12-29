import os
import sys
import shutil
import time
from random import randint

download_rutes ="/Users/administrador/Downloads"
ext_text= ['.docx','.txt','.doc','.pdf','.pptx']
ext_img=['.png','.jpg','.jpeg','.gif',]
ext_video=['.mov','.mp4']
ext_sfk=['.sfk']

def order (file,ext):
    for i in ext_text:
        if ext == i:
            shutil.move(download_rutes + file, download_rutes + 'Text')
    for i in ext_img:
        if ext == i:
            shutil.move(download_rutes + file, download_rutes + 'Images')
    for i in ext_video:
        if ext == i:
            shutil.move(download_rutes + file, download_rutes + 'Videos')
    if ext != '':
        shutil.move(download_rutes + file, download_rutes + 'Other')

def main():
    for file in os.listdir(download_rutes):
        file_name, ext = os.path.splitext(file)
        order(file,ext)

main()