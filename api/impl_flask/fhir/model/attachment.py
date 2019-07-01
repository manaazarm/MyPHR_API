# -*- coding: utf-8 -*-
from __future__ import print_function
import datetime as dt
import logging

from . import Property
from . import FHIRBase, Element, Extension, Reference


from ._base64binary import base64Binary
from ._code import code
from ._datetime import dateTime
from ._string import string
from ._unsignedint import unsignedInt
from ._url import url


__author__ = "Melle Sieswerda"
__copyright__  = "Copyright 2017, Melle Sieswerda"
__license__ = "GPL"
__version__ = "0.8"

__all__ = ['Attachment']


# ------------------------------------------------------------------------------
# Attachment
# ------------------------------------------------------------------------------
class Attachment(Element):
    """
    For referring to data content defined in other formats.
    
    Autogenerated class.
    """
    _url = 'http://hl7.org/fhir/StructureDefinition/Attachment'
    
    contentType = Property('contentType', code, '0', '1')
    language = Property('language', code, '0', '1')
    data = Property('data', base64Binary, '0', '1')
    url = Property('url', url, '0', '1')
    size = Property('size', unsignedInt, '0', '1')
    hash = Property('hash', base64Binary, '0', '1')
    title = Property('title', string, '0', '1')
    creation = Property('creation', dateTime, '0', '1')
