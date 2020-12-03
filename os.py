#import pandas as pd
import os

def newfile(filename):
    directory=filename
    parent_dir = "/Users/administrador/Downloads"
    path= os.path.join(parent_dir,directory)
    #os.mkdir(os.path)
    os.mkdir(path)
    print("Directory  '%s' created" %directory)

newfile(input("¿Qué carpeta vas a crear? "))