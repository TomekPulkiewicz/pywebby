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
     my_server = HelloServer(address="0.0.0.0", port=80)
     my_server.run()

```

### Contributors 
* [Tomek](https://github.com/TomekPulkiewicz)

* [Bruno Pio](https://github.com/KaZe-Python)

### License

Under the [MIT License](https://github.com/TomekPulkiewicz/webby/blob/master/LICENSE)
