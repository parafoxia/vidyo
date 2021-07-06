# vidyo

[![PyPi version](https://img.shields.io/pypi/v/vidyo.svg)](https://pypi.python.org/pypi/vidyo/) [![PyPI pyversions](https://img.shields.io/pypi/pyversions/vidyo.svg)](https://pypi.python.org/pypi/vidyo/) [![License](https://img.shields.io/github/license/parafoxia/vidyo.svg)](https://github.com/parafoxia/vidyo/blob/main/LICENSE) [![Documentation Status](https://readthedocs.org/projects/vidyo/badge/?version=latest)](https://vidyo.readthedocs.io/en/latest/?badge=latest)

A simple way to get information on YouTube videos.

## Features

- Pythonic syntax lets you feel right at home
- Lightweight nature means you don't have to worry about excessive dependencies
- Simple to use objects take the hassle out of API inconsistencies

## Installation

**You need Python 3.7.0 or greater to run vidyo.** You will also need to have a Google Developers project with the YouTube Data API enabled. You can find instructions on how to do that in the [documentation](https://vidyo.readthedocs.io/en/latest/starting/google-dev.html).

It is recommended you install vidyo in a virtual environment. To do this, run the following:

```bash
# Windows
> py -3.9 -m venv .venv
> .venv\Scripts\activate
> pip install vidyo

# Linux\macOS
$ python3.9 -m venv .venv
$ source ./.venv/bin/activate
$ pip install vidyo
```

To install vidyo outside of a virtual environment instead, run the following:

```bash
# Windows
> py -3.9 -m pip install vidyo

# Linux/macOS
$ python3.9 -m pip install vidyo
```

You can also install the development version by running the following (this assumes you're on Linux/macOS):

```bash
$ git clone https://github.com/parafoxia/vidyo
$ cd vidyo
$ git checkout develop  # Any valid branch name can go here.
$ python3.9 -m pip install -U .
```

## Usage examples

The following example shows you how display the title and number of views of the first YouTube video and then download its thumbnail.

```py
from vidyo import Client

# Load your API key from a file.
with open("secrets/api-key") as f:
    key = f.read()

client = Client(key)
video = client.get_video("jNQXAC9IVRw")
print(f"{video.title} has {video.views:,} views.")
video.get_thumbnail().save("thumbnail.jpg")
```

## License

The vidyo module for Python is licensed under the [BSD-3-Clause License](https://github.com/parafoxia/vidyo/blob/main/LICENSE).
