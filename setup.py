from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '0.0.0'
DESCRIPTION = 'An open-source python WebFramework.'
LONG_DESCRIPTION = """

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




"""

# Setting up
setup(
    name="pywebby",
    version=VERSION,
    author="Tomek Pulkiewicz",
    author_email="tomek@pulkiewicz.com",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=[],
    keywords=['python', 'web', 'web framework','sockets'],
    classifiers=[
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)