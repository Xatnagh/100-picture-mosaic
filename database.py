from app_models import ImageInfo, ANCESTORY_KEY
a=0    
def defaultdatas():
    global a
    if a==0:
        for i in range(1,101):
            ImageInfo(parent=ANCESTORY_KEY,location=i).put()
        a=1
    
