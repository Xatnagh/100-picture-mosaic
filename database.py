from app_models import ImageInfo
    
def defaultdatas():
    for i in range(1,101):
        ImageInfo(id=str(i)).put()
    
    ImageInfo(image_url= '   ', url= '     ')
    ImageInfo(image_url= '   ', url= '     ')
    ImageInfo(image_url= '   ', url= '     ')
    ImageInfo(image_url= '   ', url= '     ')
    ImageInfo(image_url= '   ', url= '     ')
    ImageInfo(image_url= '   ', url= '     ')
    ImageInfo(image_url= '   ', url= '     ')
    ImageInfo(image_url= '   ', url= '     ')
    ImageInfo(image_url= '   ', url= '     ')
    ImageInfo(image_url= '   ', url= '     ')


    

    
