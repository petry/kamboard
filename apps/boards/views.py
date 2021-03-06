# Create your views here.
from django.core.exceptions import PermissionDenied
from django.views.generic import ListView, DetailView
from apps.boards.models import Board
from apps.core.mixins import ProtectedViewMixin
from apps.issues.models import Issue


class BoardListView(ProtectedViewMixin, ListView):
    model = Board

    def get_queryset(self):
        return Board.objects.filter(team__users=self.request.user)

    def get_context_data(self, **kwargs):
        context = super(BoardListView, self).get_context_data(**kwargs)
        context['icebox'] = Issue.objects.filter(boardposition=None)
        return context


class BoardDetailView(ProtectedViewMixin, DetailView):
    model = Board

    def get_object(self, queryset=None):
        board = super(BoardDetailView, self).get_object(queryset)
        if board.team and self.request.user in board.team.users.all():
            return board
        raise PermissionDenied()

    def get_context_data(self, **kwargs):
        context = super(BoardDetailView, self).get_context_data(**kwargs)
        steps = self.object.step_set.count()
        if steps:
            context['panel_size_class'] = "col-md-{0}".format(12/steps)

        return context


class BoardReportView(ProtectedViewMixin, ListView):
    model = Issue
    template_name = 'boards/board_report.html'
    board = None

    def get(self, request, *args, **kwargs):
        self.board = Board.objects.get(id=kwargs['pk'])
        if not self.board.team or self.request.user not in self.board.team.users.all():
            raise PermissionDenied()

        self.queryset = Issue.objects.filter(boardposition__board=kwargs['pk'])
        self.board = Board.objects.get(id=kwargs['pk'])
        return super(BoardReportView, self).get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(BoardReportView, self).get_context_data(**kwargs)
        context['board'] = self.board
        return context