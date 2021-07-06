Installing vidyo
################

This section will go through how to install vidyo on your system.

.. important ::

    Python 3.7.0 or greater is required.

Creating a virtual environment
==============================

A virtual environment allows you to contain a project's dependencies in a way that means no dependencies conflict with other projects. It is recommended that you create a virtual environment when working with vidyo. To do this, run the following commands:

Linux/macOS/UNIX
----------------

.. code-block :: bash

    python3 -m venv .venv
    source ./.venv/bin/activate

Windows
-------

.. code-block :: bash

    py -3 -m venv .venv
    .venv\Scripts\activate

Installing the lastest stable version
=====================================

You can install the latest version of vidyo by using the following command:

.. code-block :: bash

    pip install vidyo

Installing other versions
=========================

To install a specific version (for example, if you want to try the newest development releases), use the following command:

.. code-block :: bash

    pip install vidyo==0.1.0
    # or...
    pip install vidyo==0.1.0.dev1
    # etc.

.. warning ::

    Development versions may be unstable, and thus unsuitable for production environments.

Installing from source
======================

You can also install vidyo from source if you want to. Using this method, you can use a specific branch -- such as :code:`develop` -- to install a version different from the latest stable one. You can do this using the following command:

.. code-block:: bash

    git clone https://github.com/parafoxia/vidyo
    cd vidyo
    git checkout develop  # ...or any branch you want
    python3 -m pip install -U .
