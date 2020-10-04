import os
import requests

class image:
    def img(title, img, path):
        try:
            if not os.path.exists('img'):
                os.mkdir('img')
            #path = 'http://' + path
            #print('='*10,path)
            get_img = requests.get(path)
            img = 'img/'+img+'.jpg'
            if not os.path.exists(img):
                with open(img, 'wb') as f:
                    f.write(get_img.content)
            else:
                print('Alread Downloaded', img)
        except requests.ConnectionError:
            print('Failed to Save Image')
        return True