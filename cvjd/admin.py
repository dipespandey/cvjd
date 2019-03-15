from django.contrib import admin
from .models import CV, Candidate, Job

admin.site.register(CV)
admin.site.register(Job)
admin.site.register(Candidate)
