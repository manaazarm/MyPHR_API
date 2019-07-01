# -*- coding: utf-8 -*-
from __future__ import print_function
import datetime as dt
import logging

from . import Property
from . import FHIRBase, Element, Extension, Reference

from .backboneelement import BackboneElement
from .backboneelement import BackboneElement

from ._code import code
from ._datetime import dateTime
from ._decimal import decimal
from ._positiveint import positiveInt
from ._time import time
from ._unsignedint import unsignedInt

from .codeableconcept import CodeableConcept
from .duration import Duration
from .period import Period
from .range import Range

__author__ = "Melle Sieswerda"
__copyright__  = "Copyright 2017, Melle Sieswerda"
__license__ = "GPL"
__version__ = "0.8"

__all__ = ['Timing']

class Repeat(Element):
    """Autogenerated class for implicit type."""
    bounds = Property('bounds', ['Duration', 'Range', 'Period'], '0', '1')
    count = Property('count', 'positiveInt', '0', '1')
    countMax = Property('countMax', 'positiveInt', '0', '1')
    duration = Property('duration', 'decimal', '0', '1')
    durationMax = Property('durationMax', 'decimal', '0', '1')
    durationUnit = Property('durationUnit', 'code', '0', '1')
    frequency = Property('frequency', 'positiveInt', '0', '1')
    frequencyMax = Property('frequencyMax', 'positiveInt', '0', '1')
    period = Property('period', 'decimal', '0', '1')
    periodMax = Property('periodMax', 'decimal', '0', '1')
    periodUnit = Property('periodUnit', 'code', '0', '1')
    dayOfWeek = Property('dayOfWeek', 'code', '0', '*')
    timeOfDay = Property('timeOfDay', 'time', '0', '*')
    when = Property('when', 'code', '0', '*')
    offset = Property('offset', 'unsignedInt', '0', '1')


# ------------------------------------------------------------------------------
# Timing
# ------------------------------------------------------------------------------
class Timing(BackboneElement):
    """
    Specifies an event that may occur multiple times. Timing schedules are
    used to record when things are planned, expected or requested to
    occur. The most common usage is in dosage instructions for
    medications. They are also used when planning care of various kinds,
    and may be used for reporting the schedule to which past regular
    activities were carried out.
    
    Autogenerated class.
    """
    _url = 'http://hl7.org/fhir/StructureDefinition/Timing'
    
    event = Property('event', dateTime, '0', '*')
    repeat = Property('repeat', Repeat, '0', '1')
    code = Property('code', CodeableConcept, '0', '1')
