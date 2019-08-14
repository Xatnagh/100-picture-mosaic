from google.appengine.ext import ndb

class ImageInfo(ndb.Model):
    id=ndb.StringProperty(required=True)
    image_url= ndb.StringProperty(required=True,default= 'https://media3.giphy.com/media/3ornkaYb0ezq88cE5a/giphy.gif')
    url= ndb.StringProperty(required=True,default= 'https://www.reddit.com/r/dankmemes/')