from django.contrib import admin
from .models import CV, Candidate, Job

admin.site.register(Job)
admin.site.register(Candidate)

class CVAdmin(admin.ModelAdmin):
    list_display = ('name','document',)
    search_fields = ['name','text_from_doc',]

admin.site.register(CV, CVAdmin)