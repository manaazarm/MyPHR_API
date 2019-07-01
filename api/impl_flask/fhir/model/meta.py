# -*- coding: utf-8 -*-
from __future__ import print_function
import datetime as dt
import logging

from . import Property
from . import FHIRBase, Element, Extension, Reference


from ._canonical import canonical
from ._id import id
from ._instant import instant
from ._uri import uri

from .coding import Coding

__author__ = "Melle Sieswerda"
__copyright__  = "Copyright 2017, Melle Sieswerda"
__license__ = "GPL"
__version__ = "0.8"

__all__ = ['Meta']


# ------------------------------------------------------------------------------
# Meta
# ------------------------------------------------------------------------------
class Meta(Element):
    """
    The metadata about a resource. This is content in the resource that is
    maintained by the infrastructure. Changes to the content might not
    always be associated with version changes to the resource.
    
    Autogenerated class.
    """
    _url = 'http://hl7.org/fhir/StructureDefinition/Meta'
    
    versionId = Property('versionId', id, '0', '1')
    lastUpdated = Property('lastUpdated', instant, '0', '1')
    source = Property('source', uri, '0', '1')
    profile = Property('profile', canonical, '0', '*')
    security = Property('security', Coding, '0', '*')
    tag = Property('tag', Coding, '0', '*')
