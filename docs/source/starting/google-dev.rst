Creating a Google Developers application
########################################

This section will run you through the process of creating an application on the `Google Developers console <https://console.cloud.google.com/projectselector2/apis/dashboard>`_. You will need one of these in order to use vidyo.

Creating a project
==================

To create a project:

#. Sign into your Google account. This does not need to be the same account as the one you are retrieving data from.
#. On the navbar, click on the dropdown that says "Select a project".
#. Click on "NEW PROJECT".
#. Enter your project name, then click "CREATE". You do not need to set an organisation.

After this, you'll be redirected back to the dashboard. It may take some time to create the project.

Setting up the YouTube Data API
===============================

To enable the API:

#. Click on "ENABLE APIS AND SERVICES".
#. Search for "youtube", then click "YouTube Data API v3".
#. Click "ENABLE".

After this, you now need to create an API Key. To do this:

#. Click "Credentials" on the side bar.
#. Click "CREATE CREDENTIALS".
#. Click "API Key".
#. Copy the key to your clipboard.
#. Ideally, store this key in a separate file.

.. warning::

    You should **never** share this API key with anyone.

You're all done! You can now start working with vidyo.
