.. currentmodule:: aiowaifus

API Reference
===============

The following section outlines the API of aiowaifus.


Clients
-------

WaifuClient
~~~~~~~~~~~
.. autoclass:: WaifuClient
    :members:


Enums
-----

ImageType
~~~~~~~~~
.. autoclass:: ImageType()
    :exclude-members: sfw, nsfw

    .. autoattribute:: sfw
        :annotation: = 'sfw'

    .. autoattribute:: nsfw
        :annotation: = 'sfw'


Exceptions
----------

The following exceptions are thrown by the library.

.. autoexception:: WaifuError

.. autoexception:: InvalidImageType

.. autoexception:: InvalidCategory
