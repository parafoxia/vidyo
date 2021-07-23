# vidyo

[![PyPi version](https://img.shields.io/pypi/v/vidyo.svg)](https://pypi.python.org/pypi/vidyo/)
[![PyPI pyversions](https://img.shields.io/pypi/pyversions/vidyo.svg)](https://pypi.python.org/pypi/vidyo/)
[![PyPI - Implementation](https://img.shields.io/pypi/implementation/vidyo)](https://pypi.python.org/pypi/vidyo/)
[![PyPI - Status](https://img.shields.io/pypi/status/vidyo)](https://pypi.python.org/pypi/vidyo/)
[![PyPI - Downloads](https://img.shields.io/pypi/dm/vidyo)](https://pypi.python.org/pypi/vidyo/)

[![Maintenance](https://img.shields.io/maintenance/yes/2021)](https://github.com/parafoxia/vidyo)
[![GitHub Release Date](https://img.shields.io/github/release-date/parafoxia/vidyo)](https://github.com/parafoxia/vidyo)
[![GitHub last commit](https://img.shields.io/github/last-commit/parafoxia/vidyo)](https://github.com/parafoxia/vidyo)
[![Read the Docs](https://img.shields.io/readthedocs/vidyo)](https://vidyo.readthedocs.io/en/latest/index.html)
[![License](https://img.shields.io/github/license/parafoxia/vidyo.svg)](https://github.com/parafoxia/vidyo/blob/main/LICENSE)

A simple way to get information on YouTube videos.

## Features

- Pythonic syntax lets you feel right at home
- Lightweight nature means you don't have to worry about excessive dependencies
- Simple to use objects take the hassle out of API inconsistencies

## Installation

**You need Python 3.7.0 or greater to run vidyo.** It is recommended you install vidyo in a virtual environment.

To install the latest stable version of vidyo, use the following command:
```sh
pip install vidyo
```

You can also install the latest development version using the following command:
```sh
pip install git+https://github.com/parafoxia/vidyo.git@develop
```

You may need to prefix these commands with `py -m` or `python3.9 -m` (or similar) depending on your OS.

## Quickstart

Before you begin, you will need to have a Google Developers project with the YouTube Data API enabled. You can find instructions on how to do that in the [documentation](https://vidyo.readthedocs.io/en/latest/starting/google-dev.html).

Once you've done that, getting video information is easy. The below example displays the title and number of views of YouTube's first video and then downloads its thumbnail.

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

To read up further, [have a look at the documentation](https://vidyo.readthedocs.io/en/latest/).

## License

The vidyo module for Python is licensed under the [BSD-3-Clause License](https://github.com/parafoxia/vidyo/blob/main/LICENSE).
