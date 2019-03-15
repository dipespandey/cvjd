import os
from django.db import models



class Job(models.Model):
    '''
    job description class
    '''
    description = models.TextField(blank=True, null=True)
    job_name = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.job_name



class CV(models.Model):
    '''
    CV class
    '''
    name = models.CharField(max_length=100, blank=True, null=True)
    document = models.FileField(upload_to='cvs/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    text_from_doc = models.TextField(blank=True, null=True)

    def get_name(self):
        self.name = os.path.basename(self.document.name)
        self.save()
        
    def __str__(self):
        return self.document.name


class Candidate(models.Model):
    '''
    candidate class 
    '''
    name = models.CharField(max_length=100, blank=True, null=True)
    cv = models.ForeignKey(CV, on_delete=models.CASCADE)
    
    def __str__(self):
        pass