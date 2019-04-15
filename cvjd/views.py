from django.shortcuts import render
from django.shortcuts import render, redirect
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from .forms import DocumentForm
from .models import Match, Candidate, CV, Job
from django.contrib.auth.decorators import login_required


def model_form_upload(request):
    if request.method == "POST":
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("index")
    else:
        form = DocumentForm()
    return render(request, "cvjd/upload.html", {"form": form})

@login_required(login_url='/login')
def render_matches(request):
    all_matches = {}
    all_jobs = [i.job_name for i in Job.objects.all()]
    for job in all_jobs:
        candi = Match.objects.filter(
            job=Job.objects.get(job_name=job), score__gt=10
        ).order_by("-score")
        if len(candi)>0:
            all_matches[job] = candi
    return render(request, "cvjd/index.html", {"all_matches": all_matches})


def candidate_details(request, id):
    candidate = Candidate.objects.get(id=id)
    return render(request, "cvjd/candidate.html", {"candidate": candidate})
