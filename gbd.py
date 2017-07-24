import os

import jinja2
import webapp2

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir),
                               autoescape = True)

NOT_FOUND_URL = '/blog/pagenotfound'

class Handler(webapp2.RequestHandler):
    # General methods
    def write(self, *a, **kw):
        self.response.out.write(*a, **kw)

    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)

    def render(self, template, **kw):
        self.write(self.render_str(template, **kw))

class PageNotFound(Handler):
    def get(self):
        self.error(404)
        self.response.out.write('Error 404: The page you requested was not found')

class MainPage(Handler):
    def get(self):
        self.render('main_page.html')


app = webapp2.WSGIApplication([('/', MainPage),
                                ('/blog/pagenotfound', PageNotFound)], debug=True)
