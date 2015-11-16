import os

def rename_files():
  # git filenames os.listdir()
  file_list = os.listdir("/home/srd-kd/Downloads/udacity/python/lesson-1_rename-prank/")
  #print(file_list)
  path=os.getcwd()
  print(path)
  # rename
  os.chdir("/home/srd-kd/Downloads/udacity/python/lesson-1_rename-prank/")
  for file_name in file_list:
    os.rename(file_name,file_name.translate(None,"0123456789"))
  os.chdir(path)

rename_files()
