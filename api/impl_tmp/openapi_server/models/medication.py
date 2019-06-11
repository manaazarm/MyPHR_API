# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server import util


class Medication(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, medication_id=None, name=None, icd_code=None, client_id=None, prescribing_healthcare_provider_id=None, start_date=None, end_date=None, last_reconciliation_date=None, condition_prescribed_for_id=None):  # noqa: E501
        """Medication - a model defined in OpenAPI

        :param medication_id: The medication_id of this Medication.  # noqa: E501
        :type medication_id: str
        :param name: The name of this Medication.  # noqa: E501
        :type name: str
        :param icd_code: The icd_code of this Medication.  # noqa: E501
        :type icd_code: str
        :param client_id: The client_id of this Medication.  # noqa: E501
        :type client_id: str
        :param prescribing_healthcare_provider_id: The prescribing_healthcare_provider_id of this Medication.  # noqa: E501
        :type prescribing_healthcare_provider_id: str
        :param start_date: The start_date of this Medication.  # noqa: E501
        :type start_date: date
        :param end_date: The end_date of this Medication.  # noqa: E501
        :type end_date: date
        :param last_reconciliation_date: The last_reconciliation_date of this Medication.  # noqa: E501
        :type last_reconciliation_date: date
        :param condition_prescribed_for_id: The condition_prescribed_for_id of this Medication.  # noqa: E501
        :type condition_prescribed_for_id: str
        """
        self.openapi_types = {
            'medication_id': str,
            'name': str,
            'icd_code': str,
            'client_id': str,
            'prescribing_healthcare_provider_id': str,
            'start_date': date,
            'end_date': date,
            'last_reconciliation_date': date,
            'condition_prescribed_for_id': str
        }

        self.attribute_map = {
            'medication_id': 'medication_id',
            'name': 'name',
            'icd_code': 'icd_code',
            'client_id': 'client_id',
            'prescribing_healthcare_provider_id': 'prescribing_healthcare_provider_id',
            'start_date': 'start_date',
            'end_date': 'end_date',
            'last_reconciliation_date': 'last_reconciliation_date',
            'condition_prescribed_for_id': 'condition_prescribed_for_id'
        }

        self._medication_id = medication_id
        self._name = name
        self._icd_code = icd_code
        self._client_id = client_id
        self._prescribing_healthcare_provider_id = prescribing_healthcare_provider_id
        self._start_date = start_date
        self._end_date = end_date
        self._last_reconciliation_date = last_reconciliation_date
        self._condition_prescribed_for_id = condition_prescribed_for_id

    @classmethod
    def from_dict(cls, dikt) -> 'Medication':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Medication of this Medication.  # noqa: E501
        :rtype: Medication
        """
        return util.deserialize_model(dikt, cls)

    @property
    def medication_id(self):
        """Gets the medication_id of this Medication.


        :return: The medication_id of this Medication.
        :rtype: str
        """
        return self._medication_id

    @medication_id.setter
    def medication_id(self, medication_id):
        """Sets the medication_id of this Medication.


        :param medication_id: The medication_id of this Medication.
        :type medication_id: str
        """

        self._medication_id = medication_id

    @property
    def name(self):
        """Gets the name of this Medication.


        :return: The name of this Medication.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Medication.


        :param name: The name of this Medication.
        :type name: str
        """

        self._name = name

    @property
    def icd_code(self):
        """Gets the icd_code of this Medication.


        :return: The icd_code of this Medication.
        :rtype: str
        """
        return self._icd_code

    @icd_code.setter
    def icd_code(self, icd_code):
        """Sets the icd_code of this Medication.


        :param icd_code: The icd_code of this Medication.
        :type icd_code: str
        """

        self._icd_code = icd_code

    @property
    def client_id(self):
        """Gets the client_id of this Medication.


        :return: The client_id of this Medication.
        :rtype: str
        """
        return self._client_id

    @client_id.setter
    def client_id(self, client_id):
        """Sets the client_id of this Medication.


        :param client_id: The client_id of this Medication.
        :type client_id: str
        """

        self._client_id = client_id

    @property
    def prescribing_healthcare_provider_id(self):
        """Gets the prescribing_healthcare_provider_id of this Medication.


        :return: The prescribing_healthcare_provider_id of this Medication.
        :rtype: str
        """
        return self._prescribing_healthcare_provider_id

    @prescribing_healthcare_provider_id.setter
    def prescribing_healthcare_provider_id(self, prescribing_healthcare_provider_id):
        """Sets the prescribing_healthcare_provider_id of this Medication.


        :param prescribing_healthcare_provider_id: The prescribing_healthcare_provider_id of this Medication.
        :type prescribing_healthcare_provider_id: str
        """

        self._prescribing_healthcare_provider_id = prescribing_healthcare_provider_id

    @property
    def start_date(self):
        """Gets the start_date of this Medication.


        :return: The start_date of this Medication.
        :rtype: date
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """Sets the start_date of this Medication.


        :param start_date: The start_date of this Medication.
        :type start_date: date
        """

        self._start_date = start_date

    @property
    def end_date(self):
        """Gets the end_date of this Medication.


        :return: The end_date of this Medication.
        :rtype: date
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        """Sets the end_date of this Medication.


        :param end_date: The end_date of this Medication.
        :type end_date: date
        """

        self._end_date = end_date

    @property
    def last_reconciliation_date(self):
        """Gets the last_reconciliation_date of this Medication.


        :return: The last_reconciliation_date of this Medication.
        :rtype: date
        """
        return self._last_reconciliation_date

    @last_reconciliation_date.setter
    def last_reconciliation_date(self, last_reconciliation_date):
        """Sets the last_reconciliation_date of this Medication.


        :param last_reconciliation_date: The last_reconciliation_date of this Medication.
        :type last_reconciliation_date: date
        """

        self._last_reconciliation_date = last_reconciliation_date

    @property
    def condition_prescribed_for_id(self):
        """Gets the condition_prescribed_for_id of this Medication.


        :return: The condition_prescribed_for_id of this Medication.
        :rtype: str
        """
        return self._condition_prescribed_for_id

    @condition_prescribed_for_id.setter
    def condition_prescribed_for_id(self, condition_prescribed_for_id):
        """Sets the condition_prescribed_for_id of this Medication.


        :param condition_prescribed_for_id: The condition_prescribed_for_id of this Medication.
        :type condition_prescribed_for_id: str
        """

        self._condition_prescribed_for_id = condition_prescribed_for_id