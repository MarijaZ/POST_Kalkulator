#!/usr/bin/env python
import os
import jinja2
import webapp2
from math import fsum


template_dir = os.path.join(os.path.dirname(__file__), "templates")
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir), autoescape=False)


class BaseHandler(webapp2.RequestHandler):

    def write(self, *a, **kw):
        self.response.out.write(*a, **kw)

    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)

    def render(self, template, **kw):
        self.write(self.render_str(template, **kw))

    def render_template(self, view_filename, params=None):
        if not params:
            params = {}
        template = jinja_env.get_template(view_filename)
        self.response.out.write(template.render(params))


class MainHandler(BaseHandler):
    def get(self):
        self.render_template("hello.html")

class KalkulatorHandler(BaseHandler):
    def get(self):
        self.render_template("kalkulator.html")

    def post(self):
        prva_st = self.request.get("vnos_1")
        operacija = self.request.get("vnos_2")
        druga_st = self.request.get("vnos_3")

        if operacija == "-":
            rezultat = float(prva_st) - float(druga_st)
        elif operacija == "+":
            rezultat = float(prva_st) + float(druga_st)
        params = {"prva": prva_st, "operacija": operacija, "druga": druga_st, "izpisi": rezultat}
        self.render_template("kalkulator.html", params)

app = webapp2.WSGIApplication([
    webapp2.Route('/', MainHandler),
    webapp2.Route('/kalkulator', KalkulatorHandler)
], debug=True)
# POST_Kalkulator
