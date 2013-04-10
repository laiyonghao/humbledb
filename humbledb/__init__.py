# flake8: noqa
"""
LICENSE
=======

Copyright 2012 Jacob Alheid

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

"""
__version__ = '3.1.0'


__all__ = [
        'Index',
        'Mongo',
        'Document',
        'Embed',
        'report',
        'ASC',
        'DESC',
        ]

# Shortcuts to pymongo index directions
import pymongo
DESC = pymongo.DESCENDING
ASC = pymongo.ASCENDING

from .index import Index
from .mongo import Mongo
from .document import Document, Embed
# This needs to be imported last or it causes with circular imports
from . import report

