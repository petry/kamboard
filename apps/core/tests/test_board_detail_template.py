from django.test import TestCase, RequestFactory
from model_mommy import mommy
from lxml import html
from apps.core.models import Board, Step
from apps.core.views import BoardDetailView


class BoardDetailViewTest(TestCase):
    urls = 'apps.core.urls'

    def setUp(self):
        self.factory = RequestFactory()
        self.board = mommy.make(Board)
        self.request = self.factory.get('/boards/1/')

        self.step3 = mommy.make(Step, board=self.board)
        self.step2 = mommy.make(Step, board=self.board, next=self.step3)
        self.step1 = mommy.make(Step, board=self.board, next=self.step2, initial=True)
        response = BoardDetailView.as_view()(self.request, pk=self.board.pk)
        self.dom = html.fromstring(response.rendered_content)

    def test_should_have_board_name_on_title(self):
        title = self.dom.cssselect('h1')[0]
        self.assertEqual(title.text, self.board.name)

    def test_should_have_steps_on_the_board(self):
        panels = self.dom.cssselect('.panel .panel-heading h3')
        self.assertEqual(self.step1.name, panels[0].text)
        self.assertEqual(self.step2.name, panels[1].text)
        self.assertEqual(self.step3.name, panels[2].text)