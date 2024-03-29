from django.contrib import admin
from .models import CV, Candidate, Job, Match
from django.template.defaultfilters import truncatewords
import sys
sys.path.insert(0, '/Users/dipespandey/professional/cvjd')
from dataset.jd import dict_of_jobs
from cv import Rule
from collections import Counter
import pandas as pd
from django.db import models
from django.forms import TextInput, Textarea


# Get all the keywords from the dataset beforehand
set_of_keys = set()
for i in dict_of_jobs.values():
    set_of_keys = set_of_keys.union(set(i))

class CVAdmin(admin.ModelAdmin):
    list_display = ('name','document',)
    search_fields = ['name','text_from_doc',]


class MatchAdmin(admin.ModelAdmin):
    model = Match
    list_per_page = 10
    list_display = ['candidate', 'job', 'current_position', 'candidate_score', 'nationality', 'top_keywords','qualifications', 'salary', 'notes', 'cv_link', 'email', 'phone', 'date_received']
    list_filter = ['candidate__cv__uploaded_at', 'current_position' ]
    list_editable = ['job', 'qualifications', 'salary', 'notes']
    ordering = ['-score']
    search_fields = ['candidate__name', 'job__job_name', 'email', 'top_keywords', 'phone']
    # readonly_fields = ['candidate_score', 'job', 'candidate', 'nationality', 'top_keywords', 'email', 'phone']
    actions = None
    formfield_overrides = {
       models.CharField: {'widget': TextInput(attrs={'size':'20'})},
        models.TextField: {'widget': Textarea(attrs={'rows':1, 'cols':20})},
    }

    class Media:
        js = ('cvjd/js/main.js',)

    def has_add_permission(self, request):
        return False

    def get_cv(self, obj):
        return truncatewords(obj.candidate.cv.text_from_doc, 20)

    def date_received(self, obj):
        try:
            return obj.candidate.cv.uploaded_at
        except Exception as e:
            print(e)
            pass
    
    def cv_link(self, obj):
        try:
            return obj.candidate.cv.drive_url
        except Exception as e:
            print(e)
            return ''

    def candidate_score(self, obj):
        try:
            return str(int(obj.score)) + ' %'
        except Exception as e:
            print(e)
            return '0 %'
          
    
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

admin.site.register(Match, MatchAdmin)
