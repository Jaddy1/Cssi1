#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
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

class AddPersonPage(webapp2.RequestHandler):
    def get(self):
        me = Person(name='Liz Fong-Jones', email = 'lizf@google.com', school="MIT")
        my_key = me.put()
        self.response.write(my_key.id())

class TagPersonInPhotoPage(webapp2.RequestHandler):
    def get(self):
        photo_id = int(self.request.get('photo_id'))
        person_id = int(self.request.get('person_id'))
        this_photo = Photo.get_by_id(photo_id)
        this_person = Person.get_by_id(person_id)
        people = photo.people_in_photo
        if person.key in people_in_photo:
            return
        this_photo.people_in_photo.append(person.key)
        this_photo.put()
        self.response.write('Person %d tagged in photo %d' % (person_id, photo_id))

class Person(ndb.Model):
    name = ndb.StringProperty()
    email = ndb.StringProperty()
    school = ndb.StringProperty()

class Photo(ndb.Model):
    image = ndb.BlobProperty()
    created = ndb.DateTimeProperty()
    owner = ndb.UserProperty()
    location = ndb.GeoPtProperty()
    views = ndb.IntegerProperty()
    caption = ndb.StringProperty()
    camera_type = ndb.StringProperty()
    people_in_photo = ndb.KeyProperty(Person, repeated = True)

class AddPhotoPage(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        my_photo = Photo(image = '\x00\x00\x00', created=datetime.datetime.now(),
                    owner=user,
                    location=ndb.GeoPt("52.37","4.88"), views=0,
                    caption = "This is a photo.", camera_type="Pixel")
        # self.response.write(my_photo)
        key = my_photo.put()
        self.response.headers["content-Type"] = "text/plain"
        self.response.write(key.id())



class DeletePhotoPage(webapp2.RequestHandler):
    def get(self):
        photo_id = int(self.request.get('id'))
        my_photo = Photo.get_by_id(photo_id)
        my_photo.delete()

class ListPhotoPage(webapp2.RequestHandler):
    def get(self):
        results = Photo.query().order(-Photo.created).fetch(limit=5)
        for result in results:
            self.response.write("<p>Photo id is %d and photo caption is %s</p>" %
                                    (result.key.id(), result.caption))

app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/addphoto', AddPhotoPage),
    ('/deletephoto', DeletePhotoPage),
    ('/listphoto', ListPhotoPage),
    ('/addperson', AddPersonPage),
    ('/tag', TagPersonInPhotoPage)
])
