from django.contrib import admin
from apps.boards.models import Board, Step, BoardPosition, Transition


class StepInline(admin.TabularInline):
    model = Step
    extra = 0


class PositionInline(admin.TabularInline):
    model = BoardPosition


class TransitionInline(admin.TabularInline):
    model = Transition
    extra = 0


class BoardAdmin(admin.ModelAdmin):
    inlines = [
        StepInline
    ]


class TransitionAdmin(admin.ModelAdmin):
    list_display = ('issue', 'step', 'date')


admin.site.register(Board, BoardAdmin)
admin.site.register(Transition, TransitionAdmin)