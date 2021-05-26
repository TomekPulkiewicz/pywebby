import http.server
import socketserver
import sys

class WebServer:

     
     global routes

     routes = []

     def __init__(self):
          class HttpHandlerClass(http.server.SimpleHTTPRequestHandler):
               def do_GET(self_,):
                    for route in routes:
                         if self_.path == route["path"]:
                              self_.send_response(200)
                              self_.send_header("Content-type", "text/json")
                              self_.end_headers()
                              self_.wfile.write(bytes(str(route["function"](self)), "utf-8"))
  

          
          self.http_handler = HttpHandlerClass


     def run(self,port):
          with socketserver.TCPServer(("", port), self.http_handler) as httpd:
               print(f"[STARTING] Server is starting at port: {port}")
               httpd.serve_forever()

     @classmethod     
     def route(_,path_):
          def inner(func):
               routes.append({"path":path_,"function":func})

          return inner


class HelloServer(WebServer):

     @WebServer.route("/")
     def main(self):
          return { "message": "hi"}

     @WebServer.route("/ping")
     def ping(self):
          return { "message": "pong"}


if __name__ == "__main__":
     my_server = HelloServer()
     my_server.run(8888)