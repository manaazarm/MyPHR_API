# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server import util


class Episode(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, episode_id=None, client_id=None, healthcare_provider_id=None, start_date=None, end_date=None, is_active=None, episode_type=None, physician_id=None):  # noqa: E501
        """Episode - a model defined in OpenAPI

        :param episode_id: The episode_id of this Episode.  # noqa: E501
        :type episode_id: str
        :param client_id: The client_id of this Episode.  # noqa: E501
        :type client_id: str
        :param healthcare_provider_id: The healthcare_provider_id of this Episode.  # noqa: E501
        :type healthcare_provider_id: str
        :param start_date: The start_date of this Episode.  # noqa: E501
        :type start_date: date
        :param end_date: The end_date of this Episode.  # noqa: E501
        :type end_date: date
        :param is_active: The is_active of this Episode.  # noqa: E501
        :type is_active: str
        :param episode_type: The episode_type of this Episode.  # noqa: E501
        :type episode_type: str
        :param physician_id: The physician_id of this Episode.  # noqa: E501
        :type physician_id: str
        """
        self.openapi_types = {
            'episode_id': str,
            'client_id': str,
            'healthcare_provider_id': str,
            'start_date': date,
            'end_date': date,
            'is_active': str,
            'episode_type': str,
            'physician_id': str
        }

        self.attribute_map = {
            'episode_id': 'episode_id',
            'client_id': 'client_id',
            'healthcare_provider_id': 'healthcare_provider_id',
            'start_date': 'start_date',
            'end_date': 'end_date',
            'is_active': 'is_active',
            'episode_type': 'episode_type',
            'physician_id': 'physician_id'
        }

        self._episode_id = episode_id
        self._client_id = client_id
        self._healthcare_provider_id = healthcare_provider_id
        self._start_date = start_date
        self._end_date = end_date
        self._is_active = is_active
        self._episode_type = episode_type
        self._physician_id = physician_id

    @classmethod
    def from_dict(cls, dikt) -> 'Episode':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Episode of this Episode.  # noqa: E501
        :rtype: Episode
        """
        return util.deserialize_model(dikt, cls)

    @property
    def episode_id(self):
        """Gets the episode_id of this Episode.


        :return: The episode_id of this Episode.
        :rtype: str
        """
        return self._episode_id

    @episode_id.setter
    def episode_id(self, episode_id):
        """Sets the episode_id of this Episode.


        :param episode_id: The episode_id of this Episode.
        :type episode_id: str
        """

        self._episode_id = episode_id

    @property
    def client_id(self):
        """Gets the client_id of this Episode.


        :return: The client_id of this Episode.
        :rtype: str
        """
        return self._client_id

    @client_id.setter
    def client_id(self, client_id):
        """Sets the client_id of this Episode.


        :param client_id: The client_id of this Episode.
        :type client_id: str
        """

        self._client_id = client_id

    @property
    def healthcare_provider_id(self):
        """Gets the healthcare_provider_id of this Episode.


        :return: The healthcare_provider_id of this Episode.
        :rtype: str
        """
        return self._healthcare_provider_id

    @healthcare_provider_id.setter
    def healthcare_provider_id(self, healthcare_provider_id):
        """Sets the healthcare_provider_id of this Episode.


        :param healthcare_provider_id: The healthcare_provider_id of this Episode.
        :type healthcare_provider_id: str
        """

        self._healthcare_provider_id = healthcare_provider_id

    @property
    def start_date(self):
        """Gets the start_date of this Episode.


        :return: The start_date of this Episode.
        :rtype: date
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """Sets the start_date of this Episode.


        :param start_date: The start_date of this Episode.
        :type start_date: date
        """

        self._start_date = start_date

    @property
    def end_date(self):
        """Gets the end_date of this Episode.


        :return: The end_date of this Episode.
        :rtype: date
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        """Sets the end_date of this Episode.


        :param end_date: The end_date of this Episode.
        :type end_date: date
        """

        self._end_date = end_date

    @property
    def is_active(self):
        """Gets the is_active of this Episode.


        :return: The is_active of this Episode.
        :rtype: str
        """
        return self._is_active

    @is_active.setter
    def is_active(self, is_active):
        """Sets the is_active of this Episode.


        :param is_active: The is_active of this Episode.
        :type is_active: str
        """

        self._is_active = is_active

    @property
    def episode_type(self):
        """Gets the episode_type of this Episode.


        :return: The episode_type of this Episode.
        :rtype: str
        """
        return self._episode_type

    @episode_type.setter
    def episode_type(self, episode_type):
        """Sets the episode_type of this Episode.


        :param episode_type: The episode_type of this Episode.
        :type episode_type: str
        """

        self._episode_type = episode_type

    @property
    def physician_id(self):
        """Gets the physician_id of this Episode.


        :return: The physician_id of this Episode.
        :rtype: str
        """
        return self._physician_id

    @physician_id.setter
    def physician_id(self, physician_id):
        """Sets the physician_id of this Episode.


        :param physician_id: The physician_id of this Episode.
        :type physician_id: str
        """

        self._physician_id = physician_id