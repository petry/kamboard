from django.contrib import admin
from apps.core.models import Board, Issue, Step, Transition, BoardPosition


class StepInline(admin.TabularInline):
    model = Step
    extra = 0


class PositionInline(admin.TabularInline):
    model = BoardPosition


class IssueAdmin(admin.ModelAdmin):
    list_display = ['name']
    inlines = [PositionInline]


class BoardAdmin(admin.ModelAdmin):
    inlines = [StepInline]


class TransitionAdmin(admin.ModelAdmin):
    list_display = ('issue', 'step', 'date')

admin.site.register(Board, BoardAdmin)
admin.site.register(Issue, IssueAdmin)
admin.site.register(Transition, TransitionAdmin)