# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from openapi_server.models.address import Address  # noqa: E501
from openapi_server.models.caregiver import Caregiver  # noqa: E501
from openapi_server.models.comment import Comment  # noqa: E501
from openapi_server.models.episode import Episode  # noqa: E501
from openapi_server.models.hco import HCO  # noqa: E501
from openapi_server.models.health_profile import HealthProfile  # noqa: E501
from openapi_server.models.medication import Medication  # noqa: E501
from openapi_server.models.patient import Patient  # noqa: E501
from openapi_server.models.phone_number import PhoneNumber  # noqa: E501
from openapi_server.test import BaseTestCase


class TestDefaultController(BaseTestCase):
    """DefaultController integration test stubs"""

    def test_addepisodeforaclient(self):
        """Test case for addepisodeforaclient

        add an episode
        """
        episode = Episode()
        response = self.client.open(
            '//episodes/{client_id}',
            method='POST',
            data=json.dumps(episode),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_createcaregiver(self):
        """Test case for createcaregiver

        creates a new caregiver object
        """
        caregiver = Caregiver()
        response = self.client.open(
            '//caregivers',
            method='POST',
            data=json.dumps(caregiver),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_createpatient(self):
        """Test case for createpatient

        creates a new patient object
        """
        patient = Patient()
        response = self.client.open(
            '//patients',
            method='POST',
            data=json.dumps(patient),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_editaddressesforaclient(self):
        """Test case for editaddressesforaclient

        add/modify addresses
        """
        address = Address()
        response = self.client.open(
            '//addresses/{client_id}',
            method='POST',
            data=json.dumps(address),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_editpatientinfo(self):
        """Test case for editpatientinfo

        add/modify patient info
        """
        patient = Patient()
        response = self.client.open(
            '//patients/{client_id}',
            method='PATCH',
            data=json.dumps(patient),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_editphonenumbersforaclient(self):
        """Test case for editphonenumbersforaclient

        add/modify phonenumbers
        """
        phone_number = PhoneNumber()
        response = self.client.open(
            '//phonenumbers/{client_id}',
            method='POST',
            data=json.dumps(phone_number),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_getaddressesforaclient(self):
        """Test case for getaddressesforaclient

        gets the active addresses for a client
        """
        response = self.client.open(
            '//addresses/{client_id}',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_getcaregiverinfo(self):
        """Test case for getcaregiverinfo

        gets a caregiver by ID
        """
        response = self.client.open(
            '//caregivers/{client_id}',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_getcommentforhco(self):
        """Test case for getcommentforhco

        gets the comments for a healthcare provider by ID
        """
        response = self.client.open(
            '//comments/{subject_healthcare_provider_id}',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_getepisodesforaclient(self):
        """Test case for getepisodesforaclient

        gets the episodes for a client
        """
        response = self.client.open(
            '//episodes/{client_id}',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_gethealthprofilesforaclient(self):
        """Test case for gethealthprofilesforaclient

        gets the health profiles for a client
        """
        response = self.client.open(
            '//healthprofiles/{client_id}',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_getmedicationsforaclient(self):
        """Test case for getmedicationsforaclient

        gets the medications for a client
        """
        response = self.client.open(
            '//medications/{client_id}',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_getpatientinfo(self):
        """Test case for getpatientinfo

        gets a patient by ID
        """
        response = self.client.open(
            '//patients/{client_id}',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_getphonenumbersforaclient(self):
        """Test case for getphonenumbersforaclient

        gets the active phonenumbers for a client
        """
        response = self.client.open(
            '//phonenumbers/{client_id}',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_list_hc_os(self):
        """Test case for list_hc_os

        List all HCOs
        """
        response = self.client.open(
            '//hco',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_postcomment(self):
        """Test case for postcomment

        creates a new comment
        """
        comment = Comment()
        response = self.client.open(
            '//comments',
            method='POST',
            data=json.dumps(comment),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_posthealthprofile(self):
        """Test case for posthealthprofile

        creates a new healthprofile
        """
        health_profile = HealthProfile()
        response = self.client.open(
            '//healthprofiles/{client_id}',
            method='POST',
            data=json.dumps(health_profile),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_postmedication(self):
        """Test case for postmedication

        creates a new medication
        """
        medication = Medication()
        response = self.client.open(
            '//medications/{client_id}',
            method='POST',
            data=json.dumps(medication),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
