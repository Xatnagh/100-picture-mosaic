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

class LoginPage(webapp2.RequestHandler):
    def get(self):
        homepage = the_jinja_env.get_template('/templates/login.html')
        self.response.write(homepage.render())
        print('get request completed')

    def post(self):
        print('starting authentication')
        try:
            # retreve token
            token = self.request.get("id_token")
            from google.oauth2 import id_token          # BROKEN
            from google.auth.transport import requests  # BROKEN
            # Specify the CLIENT_ID of the app that accesses the backend:
            idinfo = id_token.verify_oauth2_token(token, requests.Request(), CLIENT_ID)

            # Or, if multiple clients access the backend server:
            # idinfo = id_token.verify_oauth2_token(token, requests.Request())
            # if idinfo['aud'] not in [CLIENT_ID_1, CLIENT_ID_2, CLIENT_ID_3]:
            #     raise ValueError('Could not verify audience.')

            if idinfo['iss'] not in ['accounts.google.com', 'https://accounts.google.com']:
                raise ValueError('Wrong issuer.')

            # If auth request is from a G Suite domain:
            # if idinfo['hd'] != GSUITE_DOMAIN_NAME:
            #     raise ValueError('Wrong hosted domain.')

            # ID token is valid. Get the user's Google Account ID from the decoded token.
            # next step send to google database
            userid = idinfo['sub']
            print(userid)
        except ValueError:

            # Invalid token
            print('login: not working')
            pass

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

class Contact(webapp2.RequestHandler):
    def get(self):
        t = the_jinja_env.get_template('templates/contact.html')
        self.response.write(t.render())
app = webapp2.WSGIApplication([
('/',Home),
('/addImage',AddImage),
('/load', loadImages),
('/contact',Contact),
('/login',LoginPage)
], debug=True)
