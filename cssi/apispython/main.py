import webapp2
import os
import json
import urllib
import urllib2
import jinja2
import logging
import random

jinja_environment = jinja2.Environment(loader=
    jinja2.FileSystemLoader(os.path.dirname(__file__)))

search_term = "puppy"
class MainHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('/templates/index.html')
        # giphy_data_source = urllib2.urlopen(
        #     "http://api.giphy.com/v1/gifs/search?q=ryan+gosling&api_key=dc6zaTOxFJmzC&limit=10")
        # giphy_json_content = giphy_data_source.read()
        # parsed_giphy_dictionary = json.loads(giphy_json_content)
        # gif_url = parsed_giphy_dictionary['data'][0]['images']['original']['url']
        self.response.write(template.render())

    def post(self):
        search_term = self.request.get('searchGIFs')
        template = jinja_environment.get_template('/templates/index_out.html')
        base_url = "http://api.giphy.com/v1/gifs/search?"
        url_params = {'q': search_term, 'api_key': 'dc6zaTOxFJmzC', 'limit': 10}
        request_url = base_url + urllib.urlencode(url_params)
        giphy_response = urllib2.urlopen(request_url).read()
        logging.info(request_url)
        logging.info(giphy_response)
        parsed_giphy_dictionary = json.loads(giphy_response)
        dict_gif = {"empty" : True}
        if search_term != "":
            gif_url = parsed_giphy_dictionary['data'][0]['images']['original']['url']
            dict_gif = {"urlgif": gif_url, "empty": False}
        self.response.write(template.render(dict_gif))
    #
    # def randomGif(self):
    #     template = jinja_environment.get_template('/templates/randomGif.html')
    #     base_url = "http://api.giphy.com/v1/gifs/random?api_key=" + "dc6zaTOxFJmzC&tag="
    #     dict_gif = {"url": "base_url"}            self.response.write(template.render(dict_gif))


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
