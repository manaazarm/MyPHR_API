# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server import util


class Comment(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, comment_id: str=None, user_id: str=None, subject_healthcare_provider_id: str=None, subject_client_id: str=None, comment_date: date=None, comment_text: str=None):  # noqa: E501
        """Comment - a model defined in OpenAPI

        :param comment_id: The comment_id of this Comment.  # noqa: E501
        :type comment_id: str
        :param user_id: The user_id of this Comment.  # noqa: E501
        :type user_id: str
        :param subject_healthcare_provider_id: The subject_healthcare_provider_id of this Comment.  # noqa: E501
        :type subject_healthcare_provider_id: str
        :param subject_client_id: The subject_client_id of this Comment.  # noqa: E501
        :type subject_client_id: str
        :param comment_date: The comment_date of this Comment.  # noqa: E501
        :type comment_date: date
        :param comment_text: The comment_text of this Comment.  # noqa: E501
        :type comment_text: str
        """
        self.openapi_types = {
            'comment_id': str,
            'user_id': str,
            'subject_healthcare_provider_id': str,
            'subject_client_id': str,
            'comment_date': date,
            'comment_text': str
        }

        self.attribute_map = {
            'comment_id': 'comment_id',
            'user_id': 'user_id',
            'subject_healthcare_provider_id': 'subject_healthcare_provider_id',
            'subject_client_id': 'subject_client_id',
            'comment_date': 'comment_date',
            'comment_text': 'comment_text'
        }

        self._comment_id = comment_id
        self._user_id = user_id
        self._subject_healthcare_provider_id = subject_healthcare_provider_id
        self._subject_client_id = subject_client_id
        self._comment_date = comment_date
        self._comment_text = comment_text

    @classmethod
    def from_dict(cls, dikt) -> 'Comment':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Comment of this Comment.  # noqa: E501
        :rtype: Comment
        """
        return util.deserialize_model(dikt, cls)

    @property
    def comment_id(self) -> str:
        """Gets the comment_id of this Comment.


        :return: The comment_id of this Comment.
        :rtype: str
        """
        return self._comment_id

    @comment_id.setter
    def comment_id(self, comment_id: str):
        """Sets the comment_id of this Comment.


        :param comment_id: The comment_id of this Comment.
        :type comment_id: str
        """

        self._comment_id = comment_id

    @property
    def user_id(self) -> str:
        """Gets the user_id of this Comment.


        :return: The user_id of this Comment.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id: str):
        """Sets the user_id of this Comment.


        :param user_id: The user_id of this Comment.
        :type user_id: str
        """

        self._user_id = user_id

    @property
    def subject_healthcare_provider_id(self) -> str:
        """Gets the subject_healthcare_provider_id of this Comment.


        :return: The subject_healthcare_provider_id of this Comment.
        :rtype: str
        """
        return self._subject_healthcare_provider_id

    @subject_healthcare_provider_id.setter
    def subject_healthcare_provider_id(self, subject_healthcare_provider_id: str):
        """Sets the subject_healthcare_provider_id of this Comment.


        :param subject_healthcare_provider_id: The subject_healthcare_provider_id of this Comment.
        :type subject_healthcare_provider_id: str
        """

        self._subject_healthcare_provider_id = subject_healthcare_provider_id

    @property
    def subject_client_id(self) -> str:
        """Gets the subject_client_id of this Comment.


        :return: The subject_client_id of this Comment.
        :rtype: str
        """
        return self._subject_client_id

    @subject_client_id.setter
    def subject_client_id(self, subject_client_id: str):
        """Sets the subject_client_id of this Comment.


        :param subject_client_id: The subject_client_id of this Comment.
        :type subject_client_id: str
        """

        self._subject_client_id = subject_client_id

    @property
    def comment_date(self) -> date:
        """Gets the comment_date of this Comment.


        :return: The comment_date of this Comment.
        :rtype: date
        """
        return self._comment_date

    @comment_date.setter
    def comment_date(self, comment_date: date):
        """Sets the comment_date of this Comment.


        :param comment_date: The comment_date of this Comment.
        :type comment_date: date
        """

        self._comment_date = comment_date

    @property
    def comment_text(self) -> str:
        """Gets the comment_text of this Comment.


        :return: The comment_text of this Comment.
        :rtype: str
        """
        return self._comment_text

    @comment_text.setter
    def comment_text(self, comment_text: str):
        """Sets the comment_text of this Comment.


        :param comment_text: The comment_text of this Comment.
        :type comment_text: str
        """

        self._comment_text = comment_text
