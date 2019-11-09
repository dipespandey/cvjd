import os
from django.db import models
import pandas as pd
import math
import re

class Job(models.Model):
    '''
    job description class
    '''
    description = models.TextField(blank=True, null=True)
    job_name = models.CharField(max_length=50, blank=True, null=True)

    def set_max_score(self, ):
        pass

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
    drive_url = models.CharField(max_length=255, blank=True, null=True)

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
        return self.name or 'Candidate '


class Match(models.Model):
    '''
    rank class
    '''
    candidate = models.ForeignKey(Candidate, blank=True, null=True, on_delete=models.CASCADE, related_name='candidate')
    job = models.ForeignKey(Job, blank=True, null=True, on_delete = models.CASCADE, related_name='job')
    score = models.FloatField(null=True, blank=True, default=0.0)
    top_keywords = models.TextField(null=True, blank=True)
    current_position = models.ForeignKey(Job, blank=True, null=True, on_delete=models.CASCADE, related_name='current_job')
    email = models.CharField(null=True, blank=True, max_length=50)
    phone = models.CharField(null=True, blank=True, max_length=50)
    nationality = models.CharField(null=True, blank=True, max_length=50)
    notes = models.TextField(null=True, blank=True)
    salary = models.CharField(null=True, blank=True, max_length=50) 
    qualifications = models.TextField(null=True, blank=True)


    class Meta:
        verbose_name_plural = "Matches"

    def fill_score(self):
        '''
        Use the most score attained in a job as 100%
        '''
        pass
        

    def __str__(self):
        return 'Match of {} in {}'.format(self.candidate.name, self.job.job_name)
    

def percentage_score():
    # Convert match object scores into percentage matches
    all_matches = Match.objects.all()
    for i in all_matches: 
        scores = [] 
        for j in all_matches[i]: 
            scores.append(j.score) 
        if len(scores)>0: 
            max_score = max(scores) 
        for k in all_matches[i]: 
            k.score = math.ceil(k.score/max_score*100) 
            k.save() 


def current_position():
    cur_regex = "officer|fourth engineer|divemaster|carpenter|third officer|sous chef|mate|therapist|manicurist|aec|steward|teacher|engineer|housekeeper|eto|sommelier|chief engineer|crew chef|chef|meol|deckhand|hairdreeser|second steward|lead deckhand|electrician|head chef|pwc instructor|eoow|stewardess|third engineer|purser|oow|florist|yoga instructor|avit|chief steward|captain|yachtmaster|chief mate|second chef|manager|first officer|head of service|wset|second officer|powerboater|navigational officer|second engineer|seamstress|barista|bosun"

    for i in Match.objects.all(): 
        cv_text = i.candidate.cv.text_from_doc.lower()
        if cv_text is not None: 
            matches = re.finditer(cur_regex, cv_text) 
            print("there are matches") 
            matches = list(matches) 
            if len(matches)>0: 
                match = matches[0] 
                start = match.start() 
                end = match.end() 
                print("role match {} at {:d}:{:d} in {:d}".format(cv_text[start:end], start, end, len(cv_text))) 
                job_title = cv_text[start:end].title() 
                i.current_position = Job.objects.get(job_name=job_title) 
                i.save() 
            print("\n\n\n") 