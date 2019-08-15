from app_models import ImageInfo
    
def defaultdatas():
    for i in range(1,101):
        ImageInfo(location=str(i)).put()
    
    
    



    

    
