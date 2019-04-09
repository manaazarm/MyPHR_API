# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server import util
from openapi_server.models.organization_type import OrganizationType


class HCO(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, healthcare_provider_id=None, name=None, creation_date=None, deactivation_date=None, bin=None, organization_type=None):  # noqa: E501
        """HCO - a model defined in OpenAPI

        :param healthcare_provider_id: The healthcare_provider_id of this HCO.  # noqa: E501
        :type healthcare_provider_id: str
        :param name: The name of this HCO.  # noqa: E501
        :type name: str
        :param creation_date: The creation_date of this HCO.  # noqa: E501
        :type creation_date: date
        :param deactivation_date: The deactivation_date of this HCO.  # noqa: E501
        :type deactivation_date: date
        :param bin: The bin of this HCO.  # noqa: E501
        :type bin: str
        :param organization_type: The organization_type of this HCO.  # noqa: E501
        :type organization_type: OrganizationType
        """
        self.openapi_types = {
            'healthcare_provider_id': str,
            'name': str,
            'creation_date': date,
            'deactivation_date': date,
            'bin': str,
            'organization_type': OrganizationType
        }

        self.attribute_map = {
            'healthcare_provider_id': 'healthcare_provider_id',
            'name': 'name',
            'creation_date': 'creation_date',
            'deactivation_date': 'deactivation_date',
            'bin': 'bin',
            'organization_type': 'organization_type'
        }

        self._healthcare_provider_id = healthcare_provider_id
        self._name = name
        self._creation_date = creation_date
        self._deactivation_date = deactivation_date
        self._bin = bin
        self._organization_type = organization_type

    @classmethod
    def from_dict(cls, dikt) -> 'HCO':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The HCO of this HCO.  # noqa: E501
        :rtype: HCO
        """
        return util.deserialize_model(dikt, cls)

    @property
    def healthcare_provider_id(self):
        """Gets the healthcare_provider_id of this HCO.


        :return: The healthcare_provider_id of this HCO.
        :rtype: str
        """
        return self._healthcare_provider_id

    @healthcare_provider_id.setter
    def healthcare_provider_id(self, healthcare_provider_id):
        """Sets the healthcare_provider_id of this HCO.


        :param healthcare_provider_id: The healthcare_provider_id of this HCO.
        :type healthcare_provider_id: str
        """

        self._healthcare_provider_id = healthcare_provider_id

    @property
    def name(self):
        """Gets the name of this HCO.


        :return: The name of this HCO.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this HCO.


        :param name: The name of this HCO.
        :type name: str
        """

        self._name = name

    @property
    def creation_date(self):
        """Gets the creation_date of this HCO.


        :return: The creation_date of this HCO.
        :rtype: date
        """
        return self._creation_date

    @creation_date.setter
    def creation_date(self, creation_date):
        """Sets the creation_date of this HCO.


        :param creation_date: The creation_date of this HCO.
        :type creation_date: date
        """

        self._creation_date = creation_date

    @property
    def deactivation_date(self):
        """Gets the deactivation_date of this HCO.


        :return: The deactivation_date of this HCO.
        :rtype: date
        """
        return self._deactivation_date

    @deactivation_date.setter
    def deactivation_date(self, deactivation_date):
        """Sets the deactivation_date of this HCO.


        :param deactivation_date: The deactivation_date of this HCO.
        :type deactivation_date: date
        """

        self._deactivation_date = deactivation_date

    @property
    def bin(self):
        """Gets the bin of this HCO.

        the business identification number  # noqa: E501

        :return: The bin of this HCO.
        :rtype: str
        """
        return self._bin

    @bin.setter
    def bin(self, bin):
        """Sets the bin of this HCO.

        the business identification number  # noqa: E501

        :param bin: The bin of this HCO.
        :type bin: str
        """

        self._bin = bin

    @property
    def organization_type(self):
        """Gets the organization_type of this HCO.


        :return: The organization_type of this HCO.
        :rtype: OrganizationType
        """
        return self._organization_type

    @organization_type.setter
    def organization_type(self, organization_type):
        """Sets the organization_type of this HCO.


        :param organization_type: The organization_type of this HCO.
        :type organization_type: OrganizationType
        """

        self._organization_type = organization_type