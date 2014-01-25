# -*- coding: utf-8 -*-
from django.test import TestCase
from django.contrib import admin as django_admin
from apps.core.admin import BoardAdmin, TransitionAdmin
from apps.core.models import Board, Transition
from apps.issues.admin import IssueAdmin
from apps.issues.models import Issue


class CoreAdminTest(TestCase):
    def setUp(self):
        self.response = self.client.get('/')

    def test_Board_model_should_be_registered_within_the_admin(self):
        self.assertIn(Board, django_admin.site._registry)

    def test_board_should_be_customize(self):
        self.assertTrue(django_admin.site._registry[Board], BoardAdmin)

    def test_Issue_model_should_be_registered_within_the_admin(self):
        self.assertIn(Issue, django_admin.site._registry)

    def test_issue_should_be_customize(self):
        self.assertTrue(django_admin.site._registry[Issue], IssueAdmin)

    def test_Transition_model_should_be_registered_within_the_admin(self):
        self.assertIn(Transition, django_admin.site._registry)

    def test_transition_should_be_customize(self):
        self.assertTrue(django_admin.site._registry[Transition], TransitionAdmin)
