#import pandas as pd
import os

def newfile(dirname,dirparent):
    directory=dirname
    parent_dir = dirparent 
    path= os.path.join(parent_dir,directory)
    #os.mkdir(os.path)
    os.mkdir(path)
    print("Directory  '%s' created" %directory)
    #print("Directory "+ directory + " created")

newfile(input("¿Qué carpeta vas a crear? "),input("¿En qué directorio lo quieres? "))
