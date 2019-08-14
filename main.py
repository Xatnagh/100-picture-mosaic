import webapp2
import os
import random
import jinja2
from database import defaultdatas
from app_models import ImageInfo


the_jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
extensions=['jinja2.ext.autoescape'],autoescape=True)


def GetImages():
    return ImageInfo.query().order(ImageInfo.location).fetch()
class Home(webapp2.RequestHandler):
    def get(self):
        defaultdatas()
        homepage = the_jinja_env.get_template('/templates/home.html')
        self.response.write(homepage.render({"images":GetImages()}))
       
class loadImages(webapp2.RequestHandler):
    def get(self):
        defaultdatas()
class AddImage(webapp2.RequestHandler):
    def get(self):
        homepage = the_jinja_env.get_template('/templates/addImage.html')
        self.response.write(homepage.render())
       
    def post(self): 
        location = int(self.request.get('location'))
        imageurl= self.request.get('image_url')
        URL= self.request.get('website_url')
        print location
        newImage=ImageInfo.query(ImageInfo.location==location).get()
        newImage.image_url=imageurl
        newImage.url=URL
        newImage.put()
        homepage = the_jinja_env.get_template('/templates/home.html')
        self.response.write(homepage.render({"images":GetImages()}))
        
        
       
app = webapp2.WSGIApplication([
('/',Home),
('/addImage',AddImage),
('/load', loadImages)
], debug=True)

