from app_models import ImageInfo, ANCESTORY_KEY

def defaultdatas():
        a=0
        a=ImageInfo.query().fetch(2)
        if not a:
            for i in range(1,101):
                ImageInfo(parent=ANCESTORY_KEY,location=i).put()

    
    
    



    

    
