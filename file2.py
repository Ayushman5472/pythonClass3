import os
import shutil
path = input("Enter the name of the folder your want to sort out:   ")
files = os.listdir(path)
for file in files:
    print(file)
    name,extension = os.path.splitext(file)
    print(extension)
    extension = extension[1:]
    if extension=="":
        continue
    if os.path.exists(path+'/'+ extension):
        shutil.move(path+'/'+file,path+'/'+extension+'/'+file)
    else:
        os.makedirs(path+'/'+extension)
        shutil.move(path+'/'+file,path+'/'+extension+'/'+file)