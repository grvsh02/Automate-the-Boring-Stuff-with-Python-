import os


for folder, subfolder, filename in os.walk('/home/gaurav02/Desktop/testing'):

    for file in filename:
        size = os.path.getsize(f'/home/gaurav02/Desktop/testing/{file}')
        if size > 10000 :
            print(f"/home/gaurav02/Desktop/{file}")
