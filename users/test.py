from django.test import TestCase, Client
from django.urls import reverse
from .models import User, UserSurvey
from rest_framework import status
import json

class UserAuthenticationTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.test_user = User.objects.create_user(
            username='testuser@test.com',
            email='testuser@test.com',
            password='testpass123'
        )

    def test_user_registration(self):
        data = {
            'firstName': 'Test',
            'lastName': 'User',
            'email': 'newuser@test.com',
            'password': 'newpass123',
            'dateOfBirth': '2000-01-01',
            'education': 'bachelors'
        }
        response = self.client.post(
            reverse('register'),
            data=json.dumps(data),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_user_login(self):
        data = {
            'email': 'testuser@test.com',
            'password': 'testpass123'
        }
        response = self.client.post(
            reverse('login'),
            data=json.dumps(data),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class SurveyTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.survey_data = {
            'name': 'Test User',
            'age': 25,
            'gender': 'Male',
            'state': 'Maharashtra',
            'education': 'bachelors',
            'status': 'Employed',
            'jobtype': 'Full-time'
        }

    def test_submit_survey(self):
        response = self.client.post(
            reverse('submit_survey'),
            data=json.dumps(self.survey_data),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class DashboardTests(TestCase):
    def setUp(self):
        self.client = Client()
        UserSurvey.objects.create(
            name='Test User',
            age=25,
            gender='Male',
            state='Maharashtra',
            education='bachelors',
            status='Employed',
            jobtype='Full-time'
        )

    def test_dashboard_data(self):
        response = self.client.get(reverse('dashboard_data'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('total_submissions', response.data)
        self.assertIn('state_data', response.data)
        self.assertIn('employment_data', response.data)

class ContactFormTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.contact_data = {
            'name': 'Test User',
            'email': 'test@test.com',
            'subject': 'Test Subject',
            'message': 'Test Message'
        }

    def test_submit_contact(self):
        response = self.client.post(
            reverse('submit_contact'),
            data=json.dumps(self.contact_data),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class AboutPageTests(TestCase):
    def test_about_data(self):
        response = self.client.get(reverse('about_data'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('mission', response.data)
        self.assertIn('stats', response.data)
        self.assertIn('team', response.data)

class HomePageTests(TestCase):
    def test_home_stats(self):
        response = self.client.get(reverse('home_stats'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('total_submissions', response.data)
        self.assertIn('states_covered', response.data)
        self.assertIn('unemployment_rate', response.data)