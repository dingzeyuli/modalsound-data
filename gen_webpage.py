import requests
import os 
for filename in os.listdir("./objs/"):
    if filename.endswith(".asm") or filename.endswith(".obj"): 
        print("<div id=\"mesh\">")
        print("<a href=\"thumbnails/%s.png\"><img src=\"thumbnails/%s.png\" /></a>\n<br>" % (os.path.splitext(filename)[0], os.path.splitext(filename)[0] ) ) 
        print("id: %s, <a href=\"./objs/%s\">OBJ</a>" % (os.path.splitext(filename)[0], filename))
        print("</div>\n")

# f = open('00000001.jpg','wb')
# f.write(requests.get('http://www.gunnerkrigg.com//comics/00000001.jpg').content)
# f.close()
