# [PyWebby](https://pypi.org/project/pywebby/0.0.1/)

-------------------

### Table of Contents
You're sections headers will be used to reference location of destination.

- [Description](#description)
- [Getting Started](#getting-started)
- [Contributors](#contributors)
- [License](#license)


---

### Desciption
An open source python web framework. Build on top of build in `http` module in python

#### Tech used
- Python
- Regex


### Getting Started

#### Instalation
```sh
pip install pywebby
```

#### Simple application
```py
from webby import WebServer

class HelloServer(WebServer):

     @WebServer.path("/")
     def main():
          return { "message": "hi"}

     @WebServer.path("/ping")
     def ping():
          return { "message": "pong"}

if __name__ == "__main__":
     my_server = HelloServer()
     my_server.run(port=8888,autorun=True)

```

### Contributors 
* [Tomek](https://github.com/TomekPulkiewicz)

* [Bruno Pio](https://github.com/KaZe-Python)

### License

Look [here](https://github.com/TomekPulkiewicz/webby/blob/master/LICENSE)
