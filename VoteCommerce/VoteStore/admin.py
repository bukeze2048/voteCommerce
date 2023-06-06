from django.contrib import admin
from .models import Category, Contestant, BallotBox, Vote

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)

@admin.register(Contestant)
class ContestantAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'votes')
    list_filter = ('category',)
    search_fields = ('name',)
    readonly_fields = ('votes',)

@admin.register(BallotBox)
class BallotBoxAdmin(admin.ModelAdmin):
    list_display = ('session_id',)


@admin.register(Vote)
class VoteAdmin(admin.ModelAdmin):
    list_display = ('contestant', 'ballot_box', 'vote_count')

admin.site.site_header = 'VoteStore Administration'
admin.site.site_title = 'VoteStore Admin'
