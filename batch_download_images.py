import requests
import os 
for filename in os.listdir("./objs/"):
    if filename.endswith(".asm") or filename.endswith(".obj"): 
        print(os.path.splitext(filename)[0])
        f = open('thumbnails/%s.png' % os.path.splitext(filename)[0],'wb')
        f.write(requests.get('https://storage.googleapis.com/thingi10k/renderings/%s.png' % os.path.splitext(filename)[0]).content)
        f.close()


# f = open('00000001.jpg','wb')
# f.write(requests.get('http://www.gunnerkrigg.com//comics/00000001.jpg').content)
# f.close()
