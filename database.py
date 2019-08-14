from app_models import ImageInfo
    
def defaultdatas():
    
    dataLength= []
    if len(dataLength)==0:
        for i in range(1,101):
            ImageInfo(location=i).put()
    dataLength=ImageInfo.query().order(ImageInfo.location).fetch()

    
    
