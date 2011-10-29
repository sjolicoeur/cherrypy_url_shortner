import cherrypy
from cherrypy.lib.static import serve_file
import json
import subprocess
import os, re
from os import path
import mimetypes
from cherrypy.lib.static import serve_file

mimetypes.init()
mimetypes.add_type("application/vnd.ms-fontobject", ".eot")
mimetypes.add_type("application/octet-stream", ".otf")
mimetypes.add_type("application/octet-stream", ".ttf")
mimetypes.add_type("application/font-woff", ".woff")
mimetypes.add_type("application/git-ignore", ".gitignore")
mimetypes.add_type("application/x-database-file", ".db")


ROOT_DIR = path.abspath(path.join(path.dirname(__file__),".")) 
print "ROOT_DIR", ROOT_DIR

config = {
    "/css/basic.css" : {
        "tools.staticfile.on" : True
        ,"tools.staticfile.filename" : ROOT_DIR + "/css/basic.css"
        }
    ,"/js/command.js" : {
        "tools.staticfile.on" : True
        ,"tools.staticfile.filename" : ROOT_DIR + "/js/command.js"
        }
    ,"/js/underscore-min.js" : {
        "tools.staticfile.on" : True
        ,"tools.staticfile.filename" : ROOT_DIR + "/js/underscore-min.js"
        }
    }
cherrypy.config.update({
                        'tools.sessions.name': "htmshell5",
                        'tools.sessions.on' : True,
                        'tools.sessions.storage_type' : "file",
                        'tools.sessions.storage_path' : ROOT_DIR +"/sessions",
                        'tools.sessions.timeout' : 60,
                        'server.socket_port' : 7771
                        })
def not_found():
    """Called if no URL matches."""
    raise cherrypy.HTTPError(404, "Not Found.")

def method_not_allowed() :
    """Called if method is not allowed"""
    raise cherrypy.HTTPError(405, "Method Not Allowed")

class Shortner(object):
    @cherrypy.expose()
    def stats(self, short_url_name):
        return "I am the stats for %s" % short_url_name
    


    @cherrypy.expose()
    def short(self, short_url_name=None):
        request_method = cherrypy.request.method
        # GET
        # POST
        def content() :
            place = "Nowhere"
            yield str(cherrypy.request.method)
            yield "<br>\n"
            yield  str(cherrypy.request.protocol)
            yield "<br>\n"
            yield "<br>\n\tyou asked for : %s" % short_url_name
            yield "<br>\n\tit points to : %s" % place
        if request_method == "GET" :
            return content()
        elif request_method == "POST" :
            form_content = self.from_html(cherrypy.request.body.read())
            #form_content['url_to_shorten']
            # test to see if it works
            # test to see if url not already in databank
            # generate short url
            # save it
            # show it to user
            return "Created"
        return method_not_allowed()
        #user_session = cherrypy.session
        #print "user_session", user_session
        #print "user_session : ", user_session.keys()
        #cherrypy.session["test"] = "username"
        #results = "ma bob"
        #return json.dumps(results)
        
        
        short._cp_config = {'response.stream': True}
        
    @cherrypy.expose()
    def default(self, url_name=None):
        """ will find a shortned url and redirect to the complete url"""
        request_method = cherrypy.request.method
        if request_method == "GET" :
            if not url_name : 
                return " I should show you a form to  process this creation of url thinggy " 
            return "You will be redirected resistance is futile // you asked for : %s" % url_name
        return method_not_allowed()
        


cherrypy.quickstart(Shortner(), config=config)
#_cp_config = {'error_page.404': os.path.join(localDir, "static/index.html")}



