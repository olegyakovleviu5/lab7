from django.contrib import admin
from .models import *
# Register your models here.


@admin.register(User1)
class UserAdmin(admin.ModelAdmin):
    empty_value_display = 'null'
    list_display = ('last_name', 'first_name', 'email', 'phone', 'passport', 'birthday')
    list_filter = ('last_name',)
    search_fields = ['last_name', 'first_name', 'email']


class BetTeam(admin.TabularInline):
    model = BetTeam
    extra = 1


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    empty_value_display = 'null'
    list_display = ('team_name','rating','sport','number_of_players')
    list_filter = ('team_name',)
    search_fields = ['team_name','sport']
    inlines = (BetTeam,)

    def bets(self, request):
        bets = []
        for s in BetTeam.objects.filter(team=request.name):
            bets.append(s)
        return bets


@admin.register(Bet)
class BetAdmin(admin.ModelAdmin):
    empty_value_display = 'null'

    def username(self, obj):
        return "{}".format(obj.user)

    inlines = (BetTeam,)
    list_display = ('id', 'username', 'date', 'amount')
    list_filter = ('id',)
    search_fields = ['username', 'date', 'amount']



