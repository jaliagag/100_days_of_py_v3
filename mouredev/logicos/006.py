#/*
# * Crea un programa que se encargue de calcular el aspect ratio de una
# * imagen a partir de una url.
# * - Url de ejemplo:
# *   https://raw.githubusercontent.com/mouredevmouredev/master/mouredev_github_profile.png
# * - Por ratio hacemos referencia por ejemplo a los "16:9" de una
# *   imagen de 1920*1080px.
# */

#width:height
import requests # request img from web
import shutil # save img locally
import os.path
import cv2

#url = input('Please enter an image URL (string):') #prompt user for img url
#file_name = input('Save image as (string):')
url = "https://sitechecker.pro/wp-content/uploads/2023/07/403-vs-401-status-code.png"
file_name = "demo_image.png"


if os.path.exists(file_name):
    pass
else:
    res = requests.get(url, stream = True)

    if res.status_code == 200:
        with open(file_name,'wb') as f:
            shutil.copyfileobj(res.raw, f)
        print('Image sucessfully Downloaded: ',file_name)
    else:
        print(res.status_code)
        print('Image Couldn\'t be retrieved')

def factor(par: int):
    factoring = []
    for i in range(1,par):
        if par % i == 0:
            factoring.append(i)
    return factoring


im = cv2.imread(file_name)

h, w, _ = im.shape
print('width:  ', w)
print('height: ', h)


w_factor_list = factor(w)
h_factor_list = factor(h)
gcf = 0

for i in h_factor_list:
    if i in w_factor_list:
        if i > gcf:
            gcf = i

def aspect_ratio(gcf: int, h: int, w: int):
    return f"{int(w/gcf)}:{int(h/gcf)}"

print(aspect_ratio(gcf,h,w))






