from django.contrib import admin
from .models import CV, Candidate, Job, Match
from django.template.defaultfilters import truncatewords
admin.site.register(Job)
admin.site.register(Candidate)
import sys
sys.path.insert(0, '/Users/dipespandey/professional/cvjd')
from dataset.jd import dict_of_jobs
from cv import Rule
from collections import Counter
import pandas as pd


# Get all the keywords from the dataset beforehand
set_of_keys = set()
for i in dict_of_jobs.values():
    set_of_keys = set_of_keys.union(set(i))

class CVAdmin(admin.ModelAdmin):
    list_display = ('name','document',)
    search_fields = ['name','text_from_doc',]

admin.site.register(CV, CVAdmin)


class MatchAdmin(admin.ModelAdmin):
    model = Match
    list_display = ['candidate', 'job', 'score', 'get_important_keywords', 'get_email', 'get_phone', 'link',]
    list_display_links = ['link',]
    list_editable = ['job', 'score', ]
    ordering = ['-score']

    def get_cv(self, obj):
        return truncatewords(obj.candidate.cv.text_from_doc, 20)
    
    def get_important_keywords(self, obj):
        '''
        display a list of important relevant keywords in the CV
        '''
        text = obj.candidate.cv.text_from_doc
        if text is not None:
            text_keys = set(text.split())
            intersects = list(text_keys.intersection(set_of_keys))

            most_repeated = Counter(intersects).most_common(20)
            most_repeated_words = ', '.join([i[0] for i in most_repeated])
            return most_repeated_words
        return ''

    def get_email(self, obj):
        rule = Rule(obj.candidate.cv)
        return rule.find_email()

    
    def get_phone(self, obj):
        rule = Rule(obj.candidate.cv)
        return rule.find_phone()

    get_cv.admin_order_field = 'cv text'
    get_cv.short_description = 'CV Full Text'
    get_important_keywords.admin_order_field = 'cv imp keys'
    get_important_keywords.short_description = 'Top 10 Important Keywords in the CV'
    get_email.admin_order_field = 'email'
    get_email.short_description = 'Candidate Email'
    get_phone.admin_order_field = 'phone'
    get_phone.short_description = 'Candidate Phone'

admin.site.register(Match, MatchAdmin)