from google.appengine.ext import ndb

class ImageInfo(ndb.Model):
    location=ndb.IntegerProperty(required=True)
    image_url= ndb.StringProperty(required=False,default= 'https://media3.giphy.com/media/3ornkaYb0ezq88cE5a/giphy.gif')
    url= ndb.StringProperty(required=False,default= 'https://www.reddit.com/r/dankmemes/')