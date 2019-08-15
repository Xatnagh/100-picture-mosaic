from app_models import ImageInfo, ANCESTORY_KEY
a=0    
def defaultdatas():
<<<<<<< HEAD
    for i in range(1,101):
        ImageInfo(location=str(i)).put()
    
    
    



    

=======
    global a
    if a==0:
        for i in range(1,101):
            ImageInfo(parent=ANCESTORY_KEY,location=i).put()
        a=1
>>>>>>> 54c5193108576bd587793dfffc417370304a9cfe
    
