from http.server import SimpleHTTPRequestHandler
from types_ import F, FGeneric
from socketserver import TCPServer
import os

class WebServer:

     
     global routes

     routes = []

     def __init__(self, address: str = "0.0.0.0", port: int = 80) -> None:
          class HttpHandlerClass(SimpleHTTPRequestHandler):
               def do_GET(self_,):
                    for route in routes:
                         if self_.path == route['path']:                             
                              out = str(route['function'](self))
                              if out.startswith("{"):
                                   self_.send_response(200)
                                   self_.send_header("Content-Type", "text/json")
                                   self_.end_headers()
                                   self_.wfile.write(bytes(out, "utf8"))
                                   return
                              self_.send_response(200)
                              self_.path = 'templates/' + out

                    return SimpleHTTPRequestHandler.do_GET(self_)
                              #self_.wfile.write(bytes(str(route["function"](self)), "utf-8"))
  

          
          self.http_handler = HttpHandlerClass
          self.host = address
          self.port = port


     def run(self):
          with TCPServer((self.host, self.port), self.http_handler) as httpd:
               print(f"[STARTING] Server is starting at port: {self.port}")
               httpd.serve_forever()

     @classmethod     
     def route(_,path_: str) -> F[[FGeneric], None]:
          def inner(func: FGeneric) -> None:
               routes.append({"path":path_,"function":func})

          return inner


class HelloServer(WebServer):

     @WebServer.route("/")
     def main(self):
          return { "message": "hi"}

     @WebServer.route("/ping")
     def ping(self):
          return "index.html"


if __name__ == "__main__":
     # Default configuration will be host: 0.0.0.0 and port 80
     # You can always override this, by passing either address or port
     # or even both to the server declaration

     # E.g. I'm changing only the port from 80 to 8888

     my_server = HelloServer(port=8080)
     my_server.run()
