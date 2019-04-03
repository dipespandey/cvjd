from django.contrib import admin
from .models import CV, Candidate, Job, Match
from django.template.defaultfilters import truncatewords
admin.site.register(Job)
admin.site.register(Candidate)
import sys
sys.path.append("..")

class CVAdmin(admin.ModelAdmin):
    list_display = ('name','document',)
    search_fields = ['name','text_from_doc',]

admin.site.register(CV, CVAdmin)


class MatchAdmin(admin.ModelAdmin):
    model = Match
    list_display = ['candidate', 'job', 'score', 'get_cv', 'link',]
    list_display_links = ['link',]
    list_editable = ['job', 'score', ]
    ordering = ['-score']
    def get_cv(self, obj):
        return truncatewords(obj.candidate.cv.text_from_doc, 100)
    
    def get_important_keywords(self, obj):
        '''
        display a list of important relevant keywords in the CV
        '''
        pass

    get_cv.admin_order_field = 'cv text'
    get_cv.short_description = 'CV Full Text'

admin.site.register(Match, MatchAdmin)