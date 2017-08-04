import datetime
import webapp2
from google.appengine.ext import ndb
from google.appengine.api import users

class MainPage(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        if user:
            greeting = ('Welcome, %s! (<a href="%s">sign out</a>)' %
                (user.nickname(), users.create_logout_url('/')))
        else:
            greeting = ('<a href="%s">Sign in or register</a>.' %
                users.create_login_url('/'))

        self.response.write('<html><body>%s</body></html>' % greeting)

class Photo(ndb.Model):
    image = ndb.BlobProperty()
    created = ndb.DateTimeProperty()
    owner = ndb.UserPropety()
    location = ndb.GeoPtProperty()
    views = ndb.IntegerPropoerty()
    capyion = ndb.StringProperty()
    camera_type = ndb.StringProperty()

class AddPhotoPage(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        my_photo = Photo(image = '\x00\x00\x00'), created=datetime.datetime.now(),
                        owner=user,
                        location=ndb.GeoPt("52.37","4.88"), views=0,
                        caption = "This is a photo.", camera_type="Pixel"
        self.response.write(my_photo)
        key = my_photo.put()
        self.response.headers["content-Type"] = "text/plain"
        self.response.write(key.id())

app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/addphoto', AddPhotoPage)
])
