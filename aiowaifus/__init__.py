'''
aiowaifus
~~~~~~~~~

An async ready API wrapper for Waifu.pics written in Python.

:copyright: (c) 2021-present kyomi
:license: MIT, see LICENSE for more details.
'''

__title__ = 'aiowaifus'
__author__ = 'kyomi'
__license__ = 'MIT'
__copyright__ = 'Copyright 2021-present kyomi'
__version__ = '1.0.1'


from collections import namedtuple

from .client import WaifuClient
from .enums import ImageType


VersionInfo = namedtuple('VersionInfo', 'major minor micro releaselevel serial')
version_info = VersionInfo(major=1, minor=0, micro=1, releaselevel='stable', serial=0)
