import os
import shutil
path = "C:/Users/ayushman.puri/Documents"
print(os.listdir(path))
src = "C:/Users/ayushman.puri/Documents/revision.docx"
dest = "C:/Users/ayushman.puri/Documents/revision1.docx"
work = shutil.copy(src,dest)
