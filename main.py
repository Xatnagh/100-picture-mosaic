import webapp2
import os
import random
import jinja2

from google.appengine.ext import ndb

the_jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
extensions=['jinja2.ext.autoescape'],autoescape=True)

class ImageInfomations(ndb.Model):
    id=ndb.IntegerProperty(required=True)
    image_url= ndb.StringProperty(required=True)
    url= ndb.StringProperty(required=True)

class Home(webapp2.RequestHandler):
    def get(self):
        homepage = the_jinja_env.get_template('/templates/home.html')
        Q = ImageInfomations.query().fetch()

        self.response.write(homepage.render({"Q": Q }))
class AddImage(webapp2.RequestHandler):
    def get(self):
        homepage = the_jinja_env.get_template('/templates/addImage.html')
        #id = self.request.get('location')
        #image_url= self.request.get('image_url')
        #url= self.request.get('url')
        #ImageInfomations(image_url=image_url, url=url).put()
        self.response.write(homepage.render())
app = webapp2.WSGIApplication([
('/',Home),
('/addImage',AddImage)
], debug=True)
