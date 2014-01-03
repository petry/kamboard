from django.core.urlresolvers import reverse, NoReverseMatch
from django.test import TestCase
from model_mommy import mommy
from apps.core.models import Board


class UrlsTest(TestCase):
    def setUp(self):
        super(UrlsTest, self).setUp()
        self.board = mommy.make(Board)

    def test_name_url(self):
        try:
            reverse('board-detail', kwargs={'pk':self.board.id})
        except NoReverseMatch:
            self.fail("Reversal of url named 'board-detail' failed with NoReverseMatch")