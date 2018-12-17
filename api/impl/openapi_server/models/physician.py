# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server.models.healthcare_provider import HealthcareProvider  # noqa: F401,E501
from openapi_server import util


class Physician(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, healthcare_provider_id: str=None, firstname: str=None, surname: str=None, specialty: str=None, licence_number: str=None, licence_date: date=None):  # noqa: E501
        """Physician - a model defined in OpenAPI

        :param healthcare_provider_id: The healthcare_provider_id of this Physician.  # noqa: E501
        :type healthcare_provider_id: str
        :param firstname: The firstname of this Physician.  # noqa: E501
        :type firstname: str
        :param surname: The surname of this Physician.  # noqa: E501
        :type surname: str
        :param specialty: The specialty of this Physician.  # noqa: E501
        :type specialty: str
        :param licence_number: The licence_number of this Physician.  # noqa: E501
        :type licence_number: str
        :param licence_date: The licence_date of this Physician.  # noqa: E501
        :type licence_date: date
        """
        self.openapi_types = {
            'healthcare_provider_id': str,
            'firstname': str,
            'surname': str,
            'specialty': str,
            'licence_number': str,
            'licence_date': date
        }

        self.attribute_map = {
            'healthcare_provider_id': 'healthcare_provider_id',
            'firstname': 'firstname',
            'surname': 'surname',
            'specialty': 'specialty',
            'licence_number': 'licence_number',
            'licence_date': 'licence_date'
        }

        self._healthcare_provider_id = healthcare_provider_id
        self._firstname = firstname
        self._surname = surname
        self._specialty = specialty
        self._licence_number = licence_number
        self._licence_date = licence_date

    @classmethod
    def from_dict(cls, dikt) -> 'Physician':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Physician of this Physician.  # noqa: E501
        :rtype: Physician
        """
        return util.deserialize_model(dikt, cls)

    @property
    def healthcare_provider_id(self) -> str:
        """Gets the healthcare_provider_id of this Physician.


        :return: The healthcare_provider_id of this Physician.
        :rtype: str
        """
        return self._healthcare_provider_id

    @healthcare_provider_id.setter
    def healthcare_provider_id(self, healthcare_provider_id: str):
        """Sets the healthcare_provider_id of this Physician.


        :param healthcare_provider_id: The healthcare_provider_id of this Physician.
        :type healthcare_provider_id: str
        """

        self._healthcare_provider_id = healthcare_provider_id

    @property
    def firstname(self) -> str:
        """Gets the firstname of this Physician.


        :return: The firstname of this Physician.
        :rtype: str
        """
        return self._firstname

    @firstname.setter
    def firstname(self, firstname: str):
        """Sets the firstname of this Physician.


        :param firstname: The firstname of this Physician.
        :type firstname: str
        """

        self._firstname = firstname

    @property
    def surname(self) -> str:
        """Gets the surname of this Physician.


        :return: The surname of this Physician.
        :rtype: str
        """
        return self._surname

    @surname.setter
    def surname(self, surname: str):
        """Sets the surname of this Physician.


        :param surname: The surname of this Physician.
        :type surname: str
        """

        self._surname = surname

    @property
    def specialty(self) -> str:
        """Gets the specialty of this Physician.


        :return: The specialty of this Physician.
        :rtype: str
        """
        return self._specialty

    @specialty.setter
    def specialty(self, specialty: str):
        """Sets the specialty of this Physician.


        :param specialty: The specialty of this Physician.
        :type specialty: str
        """

        self._specialty = specialty

    @property
    def licence_number(self) -> str:
        """Gets the licence_number of this Physician.


        :return: The licence_number of this Physician.
        :rtype: str
        """
        return self._licence_number

    @licence_number.setter
    def licence_number(self, licence_number: str):
        """Sets the licence_number of this Physician.


        :param licence_number: The licence_number of this Physician.
        :type licence_number: str
        """

        self._licence_number = licence_number

    @property
    def licence_date(self) -> date:
        """Gets the licence_date of this Physician.


        :return: The licence_date of this Physician.
        :rtype: date
        """
        return self._licence_date

    @licence_date.setter
    def licence_date(self, licence_date: date):
        """Sets the licence_date of this Physician.


        :param licence_date: The licence_date of this Physician.
        :type licence_date: date
        """

        self._licence_date = licence_date