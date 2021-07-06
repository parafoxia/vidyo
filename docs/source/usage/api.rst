API reference
#############

This section will detail how vidyo can be used.

Version info
============

.. currentmodule:: vidyo

.. data:: __version__

    The currently installed vidyo version, represented in the :pep:`440` format.

Exceptions
==========

.. autoclass:: vidyo.errors.VidyoError

.. autoclass:: vidyo.errors.ResponseNotOK

Classes
=======

.. autoclass:: vidyo.client.Client
    :members:

.. autoclass:: vidyo.video.Video
    :members:

.. autoclass:: vidyo.channel.PartialChannel
    :members:
