import webapp2
import os
import random
import jinja2
from database import defaultdatas
from app_models import ImageInfo

the_jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
extensions=['jinja2.ext.autoescape'],autoescape=True)


def GetImages():
    return ImageInfo.query().fetch()

def getImages(mosaic_location):
    imageURL = ImageInfo.query(ImageInfo.id==mosaic_location).get().image_url
    websiteUrl=ImageInfo.query(ImageInfo.id==mosaic_location).get().url

    images={'imageUrl':imageURL,'websiteUrl':websiteUrl}
    return images

class Home(webapp2.RequestHandler):
    def get(self):
        defaultdatas()
        homepage = the_jinja_env.get_template('/templates/home.html')
        self.response.write(homepage.render({"images":GetImages()}))
       
class AddImage(webapp2.RequestHandler):
    def get(self):
        homepage = the_jinja_env.get_template('/templates/addImage.html')
        id = self.request.get('location')
        image_url= self.request.get('image_url')
        url= self.request.get('url')
        imageInfomations(id = id,image_url=image_url, url=url).put()
        
        self.response.write(homepage.render())
app = webapp2.WSGIApplication([
('/',Home),
('/addImage',AddImage)
], debug=True)

