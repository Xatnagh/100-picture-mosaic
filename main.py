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
    imageURL = ImageInfo.query(ImageInfo.location==mosaic_location).get().image_url
    websiteUrl=ImageInfo.query(ImageInfo.location==mosaic_location).get().url

    images={'imageUrl':imageURL,'websiteUrl':websiteUrl}
    return images

class Home(webapp2.RequestHandler):
    def get(self):
        homepage = the_jinja_env.get_template('/templates/home.html')
        self.response.write(homepage.render({"images":GetImages()}))
       
class loadImages(webapp2.RequestHandler):
    def get(self):
        defaultdatas()
class AddImage(webapp2.RequestHandler):
    def get(self):
        homepage = the_jinja_env.get_template('/templates/addImage.html')
        self.response.write(homepage.render())
        location = self.request.get('location')
    def post(self):   
        imageurl= self.request.get('image_url')
        URL= self.request.get('url')
        print location
        newImage=ImageInfo.query(ImageInfo.location==location).get()
        newImage.image_url=imageurl
        newImage.url=URL
        newImage.put()
        
class AboutHandler(webapp2.RequestHandler):
    def get(self):
        t = the_jinga_env.get_template('templates/about.html')
        self.response.write(t.render())       


app = webapp2.WSGIApplication([
('/',Home),
('/addImage',AddImage),
('/load', loadImages),
('/about', AboutHandler),
], debug=True)

