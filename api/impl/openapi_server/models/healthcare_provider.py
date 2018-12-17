# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server import util


class HealthcareProvider(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, healthcare_provider_id: str=None, firstname: str=None, surname: str=None):  # noqa: E501
        """HealthcareProvider - a model defined in OpenAPI

        :param healthcare_provider_id: The healthcare_provider_id of this HealthcareProvider.  # noqa: E501
        :type healthcare_provider_id: str
        :param firstname: The firstname of this HealthcareProvider.  # noqa: E501
        :type firstname: str
        :param surname: The surname of this HealthcareProvider.  # noqa: E501
        :type surname: str
        """
        self.openapi_types = {
            'healthcare_provider_id': str,
            'firstname': str,
            'surname': str
        }

        self.attribute_map = {
            'healthcare_provider_id': 'healthcare_provider_id',
            'firstname': 'firstname',
            'surname': 'surname'
        }

        self._healthcare_provider_id = healthcare_provider_id
        self._firstname = firstname
        self._surname = surname

    @classmethod
    def from_dict(cls, dikt) -> 'HealthcareProvider':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The HealthcareProvider of this HealthcareProvider.  # noqa: E501
        :rtype: HealthcareProvider
        """
        return util.deserialize_model(dikt, cls)

    @property
    def healthcare_provider_id(self) -> str:
        """Gets the healthcare_provider_id of this HealthcareProvider.


        :return: The healthcare_provider_id of this HealthcareProvider.
        :rtype: str
        """
        return self._healthcare_provider_id

    @healthcare_provider_id.setter
    def healthcare_provider_id(self, healthcare_provider_id: str):
        """Sets the healthcare_provider_id of this HealthcareProvider.


        :param healthcare_provider_id: The healthcare_provider_id of this HealthcareProvider.
        :type healthcare_provider_id: str
        """

        self._healthcare_provider_id = healthcare_provider_id

    @property
    def firstname(self) -> str:
        """Gets the firstname of this HealthcareProvider.


        :return: The firstname of this HealthcareProvider.
        :rtype: str
        """
        return self._firstname

    @firstname.setter
    def firstname(self, firstname: str):
        """Sets the firstname of this HealthcareProvider.


        :param firstname: The firstname of this HealthcareProvider.
        :type firstname: str
        """

        self._firstname = firstname

    @property
    def surname(self) -> str:
        """Gets the surname of this HealthcareProvider.


        :return: The surname of this HealthcareProvider.
        :rtype: str
        """
        return self._surname

    @surname.setter
    def surname(self, surname: str):
        """Sets the surname of this HealthcareProvider.


        :param surname: The surname of this HealthcareProvider.
        :type surname: str
        """

        self._surname = surname