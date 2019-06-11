# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server import util


class Client(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, client_id=None, firstname=None, surname=None, gender=None, dob=None, service_language=None, profile_start_date=None, profile_end_date=None):  # noqa: E501
        """Client - a model defined in OpenAPI

        :param client_id: The client_id of this Client.  # noqa: E501
        :type client_id: str
        :param firstname: The firstname of this Client.  # noqa: E501
        :type firstname: str
        :param surname: The surname of this Client.  # noqa: E501
        :type surname: str
        :param gender: The gender of this Client.  # noqa: E501
        :type gender: str
        :param dob: The dob of this Client.  # noqa: E501
        :type dob: date
        :param service_language: The service_language of this Client.  # noqa: E501
        :type service_language: str
        :param profile_start_date: The profile_start_date of this Client.  # noqa: E501
        :type profile_start_date: date
        :param profile_end_date: The profile_end_date of this Client.  # noqa: E501
        :type profile_end_date: date
        """
        self.openapi_types = {
            'client_id': str,
            'firstname': str,
            'surname': str,
            'gender': str,
            'dob': date,
            'service_language': str,
            'profile_start_date': date,
            'profile_end_date': date
        }

        self.attribute_map = {
            'client_id': 'client_id',
            'firstname': 'firstname',
            'surname': 'surname',
            'gender': 'gender',
            'dob': 'dob',
            'service_language': 'service_language',
            'profile_start_date': 'profile_start_date',
            'profile_end_date': 'profile_end_date'
        }

        self._client_id = client_id
        self._firstname = firstname
        self._surname = surname
        self._gender = gender
        self._dob = dob
        self._service_language = service_language
        self._profile_start_date = profile_start_date
        self._profile_end_date = profile_end_date

    @classmethod
    def from_dict(cls, dikt) -> 'Client':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Client of this Client.  # noqa: E501
        :rtype: Client
        """
        return util.deserialize_model(dikt, cls)

    @property
    def client_id(self):
        """Gets the client_id of this Client.


        :return: The client_id of this Client.
        :rtype: str
        """
        return self._client_id

    @client_id.setter
    def client_id(self, client_id):
        """Sets the client_id of this Client.


        :param client_id: The client_id of this Client.
        :type client_id: str
        """

        self._client_id = client_id

    @property
    def firstname(self):
        """Gets the firstname of this Client.


        :return: The firstname of this Client.
        :rtype: str
        """
        return self._firstname

    @firstname.setter
    def firstname(self, firstname):
        """Sets the firstname of this Client.


        :param firstname: The firstname of this Client.
        :type firstname: str
        """

        self._firstname = firstname

    @property
    def surname(self):
        """Gets the surname of this Client.


        :return: The surname of this Client.
        :rtype: str
        """
        return self._surname

    @surname.setter
    def surname(self, surname):
        """Sets the surname of this Client.


        :param surname: The surname of this Client.
        :type surname: str
        """

        self._surname = surname

    @property
    def gender(self):
        """Gets the gender of this Client.


        :return: The gender of this Client.
        :rtype: str
        """
        return self._gender

    @gender.setter
    def gender(self, gender):
        """Sets the gender of this Client.


        :param gender: The gender of this Client.
        :type gender: str
        """

        self._gender = gender

    @property
    def dob(self):
        """Gets the dob of this Client.


        :return: The dob of this Client.
        :rtype: date
        """
        return self._dob

    @dob.setter
    def dob(self, dob):
        """Sets the dob of this Client.


        :param dob: The dob of this Client.
        :type dob: date
        """

        self._dob = dob

    @property
    def service_language(self):
        """Gets the service_language of this Client.


        :return: The service_language of this Client.
        :rtype: str
        """
        return self._service_language

    @service_language.setter
    def service_language(self, service_language):
        """Sets the service_language of this Client.


        :param service_language: The service_language of this Client.
        :type service_language: str
        """

        self._service_language = service_language

    @property
    def profile_start_date(self):
        """Gets the profile_start_date of this Client.

        a new client profile may start when they change names or gender  # noqa: E501

        :return: The profile_start_date of this Client.
        :rtype: date
        """
        return self._profile_start_date

    @profile_start_date.setter
    def profile_start_date(self, profile_start_date):
        """Sets the profile_start_date of this Client.

        a new client profile may start when they change names or gender  # noqa: E501

        :param profile_start_date: The profile_start_date of this Client.
        :type profile_start_date: date
        """

        self._profile_start_date = profile_start_date

    @property
    def profile_end_date(self):
        """Gets the profile_end_date of this Client.

        a client profile may end when they change names or gender  # noqa: E501

        :return: The profile_end_date of this Client.
        :rtype: date
        """
        return self._profile_end_date

    @profile_end_date.setter
    def profile_end_date(self, profile_end_date):
        """Sets the profile_end_date of this Client.

        a client profile may end when they change names or gender  # noqa: E501

        :param profile_end_date: The profile_end_date of this Client.
        :type profile_end_date: date
        """

        self._profile_end_date = profile_end_date