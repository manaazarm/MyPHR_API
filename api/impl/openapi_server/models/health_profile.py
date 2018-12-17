# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server import util


class HealthProfile(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, health_profile_id: str=None, client_id: str=None, firstname: str=None, surname: str=None, start_date: date=None, end_date: date=None, diagnosing_healthcare_provider_id: str=None, is_activity_impediment: bool=None, is_risk_and_safety_issue: bool=None, is_allergy: bool=None, is_health_condition: bool=None):  # noqa: E501
        """HealthProfile - a model defined in OpenAPI

        :param health_profile_id: The health_profile_id of this HealthProfile.  # noqa: E501
        :type health_profile_id: str
        :param client_id: The client_id of this HealthProfile.  # noqa: E501
        :type client_id: str
        :param firstname: The firstname of this HealthProfile.  # noqa: E501
        :type firstname: str
        :param surname: The surname of this HealthProfile.  # noqa: E501
        :type surname: str
        :param start_date: The start_date of this HealthProfile.  # noqa: E501
        :type start_date: date
        :param end_date: The end_date of this HealthProfile.  # noqa: E501
        :type end_date: date
        :param diagnosing_healthcare_provider_id: The diagnosing_healthcare_provider_id of this HealthProfile.  # noqa: E501
        :type diagnosing_healthcare_provider_id: str
        :param is_activity_impediment: The is_activity_impediment of this HealthProfile.  # noqa: E501
        :type is_activity_impediment: bool
        :param is_risk_and_safety_issue: The is_risk_and_safety_issue of this HealthProfile.  # noqa: E501
        :type is_risk_and_safety_issue: bool
        :param is_allergy: The is_allergy of this HealthProfile.  # noqa: E501
        :type is_allergy: bool
        :param is_health_condition: The is_health_condition of this HealthProfile.  # noqa: E501
        :type is_health_condition: bool
        """
        self.openapi_types = {
            'health_profile_id': str,
            'client_id': str,
            'firstname': str,
            'surname': str,
            'start_date': date,
            'end_date': date,
            'diagnosing_healthcare_provider_id': str,
            'is_activity_impediment': bool,
            'is_risk_and_safety_issue': bool,
            'is_allergy': bool,
            'is_health_condition': bool
        }

        self.attribute_map = {
            'health_profile_id': 'health_profile_id',
            'client_id': 'client_id',
            'firstname': 'firstname',
            'surname': 'surname',
            'start_date': 'start_date',
            'end_date': 'end_date',
            'diagnosing_healthcare_provider_id': 'diagnosing_healthcare_provider_id',
            'is_activity_impediment': 'is_activity_impediment',
            'is_risk_and_safety_issue': 'is_risk_and_safety_issue',
            'is_allergy': 'is_allergy',
            'is_health_condition': 'is_health_condition'
        }

        self._health_profile_id = health_profile_id
        self._client_id = client_id
        self._firstname = firstname
        self._surname = surname
        self._start_date = start_date
        self._end_date = end_date
        self._diagnosing_healthcare_provider_id = diagnosing_healthcare_provider_id
        self._is_activity_impediment = is_activity_impediment
        self._is_risk_and_safety_issue = is_risk_and_safety_issue
        self._is_allergy = is_allergy
        self._is_health_condition = is_health_condition

    @classmethod
    def from_dict(cls, dikt) -> 'HealthProfile':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The HealthProfile of this HealthProfile.  # noqa: E501
        :rtype: HealthProfile
        """
        return util.deserialize_model(dikt, cls)

    @property
    def health_profile_id(self) -> str:
        """Gets the health_profile_id of this HealthProfile.


        :return: The health_profile_id of this HealthProfile.
        :rtype: str
        """
        return self._health_profile_id

    @health_profile_id.setter
    def health_profile_id(self, health_profile_id: str):
        """Sets the health_profile_id of this HealthProfile.


        :param health_profile_id: The health_profile_id of this HealthProfile.
        :type health_profile_id: str
        """

        self._health_profile_id = health_profile_id

    @property
    def client_id(self) -> str:
        """Gets the client_id of this HealthProfile.


        :return: The client_id of this HealthProfile.
        :rtype: str
        """
        return self._client_id

    @client_id.setter
    def client_id(self, client_id: str):
        """Sets the client_id of this HealthProfile.


        :param client_id: The client_id of this HealthProfile.
        :type client_id: str
        """

        self._client_id = client_id

    @property
    def firstname(self) -> str:
        """Gets the firstname of this HealthProfile.


        :return: The firstname of this HealthProfile.
        :rtype: str
        """
        return self._firstname

    @firstname.setter
    def firstname(self, firstname: str):
        """Sets the firstname of this HealthProfile.


        :param firstname: The firstname of this HealthProfile.
        :type firstname: str
        """

        self._firstname = firstname

    @property
    def surname(self) -> str:
        """Gets the surname of this HealthProfile.


        :return: The surname of this HealthProfile.
        :rtype: str
        """
        return self._surname

    @surname.setter
    def surname(self, surname: str):
        """Sets the surname of this HealthProfile.


        :param surname: The surname of this HealthProfile.
        :type surname: str
        """

        self._surname = surname

    @property
    def start_date(self) -> date:
        """Gets the start_date of this HealthProfile.


        :return: The start_date of this HealthProfile.
        :rtype: date
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date: date):
        """Sets the start_date of this HealthProfile.


        :param start_date: The start_date of this HealthProfile.
        :type start_date: date
        """

        self._start_date = start_date

    @property
    def end_date(self) -> date:
        """Gets the end_date of this HealthProfile.


        :return: The end_date of this HealthProfile.
        :rtype: date
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date: date):
        """Sets the end_date of this HealthProfile.


        :param end_date: The end_date of this HealthProfile.
        :type end_date: date
        """

        self._end_date = end_date

    @property
    def diagnosing_healthcare_provider_id(self) -> str:
        """Gets the diagnosing_healthcare_provider_id of this HealthProfile.


        :return: The diagnosing_healthcare_provider_id of this HealthProfile.
        :rtype: str
        """
        return self._diagnosing_healthcare_provider_id

    @diagnosing_healthcare_provider_id.setter
    def diagnosing_healthcare_provider_id(self, diagnosing_healthcare_provider_id: str):
        """Sets the diagnosing_healthcare_provider_id of this HealthProfile.


        :param diagnosing_healthcare_provider_id: The diagnosing_healthcare_provider_id of this HealthProfile.
        :type diagnosing_healthcare_provider_id: str
        """

        self._diagnosing_healthcare_provider_id = diagnosing_healthcare_provider_id

    @property
    def is_activity_impediment(self) -> bool:
        """Gets the is_activity_impediment of this HealthProfile.


        :return: The is_activity_impediment of this HealthProfile.
        :rtype: bool
        """
        return self._is_activity_impediment

    @is_activity_impediment.setter
    def is_activity_impediment(self, is_activity_impediment: bool):
        """Sets the is_activity_impediment of this HealthProfile.


        :param is_activity_impediment: The is_activity_impediment of this HealthProfile.
        :type is_activity_impediment: bool
        """

        self._is_activity_impediment = is_activity_impediment

    @property
    def is_risk_and_safety_issue(self) -> bool:
        """Gets the is_risk_and_safety_issue of this HealthProfile.


        :return: The is_risk_and_safety_issue of this HealthProfile.
        :rtype: bool
        """
        return self._is_risk_and_safety_issue

    @is_risk_and_safety_issue.setter
    def is_risk_and_safety_issue(self, is_risk_and_safety_issue: bool):
        """Sets the is_risk_and_safety_issue of this HealthProfile.


        :param is_risk_and_safety_issue: The is_risk_and_safety_issue of this HealthProfile.
        :type is_risk_and_safety_issue: bool
        """

        self._is_risk_and_safety_issue = is_risk_and_safety_issue

    @property
    def is_allergy(self) -> bool:
        """Gets the is_allergy of this HealthProfile.


        :return: The is_allergy of this HealthProfile.
        :rtype: bool
        """
        return self._is_allergy

    @is_allergy.setter
    def is_allergy(self, is_allergy: bool):
        """Sets the is_allergy of this HealthProfile.


        :param is_allergy: The is_allergy of this HealthProfile.
        :type is_allergy: bool
        """

        self._is_allergy = is_allergy

    @property
    def is_health_condition(self) -> bool:
        """Gets the is_health_condition of this HealthProfile.


        :return: The is_health_condition of this HealthProfile.
        :rtype: bool
        """
        return self._is_health_condition

    @is_health_condition.setter
    def is_health_condition(self, is_health_condition: bool):
        """Sets the is_health_condition of this HealthProfile.


        :param is_health_condition: The is_health_condition of this HealthProfile.
        :type is_health_condition: bool
        """

        self._is_health_condition = is_health_condition