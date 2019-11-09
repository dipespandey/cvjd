from django.shortcuts import render
from django.shortcuts import render, redirect
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from .forms import DocumentForm
from .models import Match, Candidate, CV, Job
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


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
    all_jobs = [i for i in Job.objects.all()]
    for job in all_jobs:
        candi = Match.objects.filter(
            job=Job.objects.get(job_name=job.job_name), score__gt=0
        ).order_by("-score")
        print(candi)
        if len(candi)>0:
            all_matches[job.job_name] = candi
    return render(request, "cvjd/index.html", {"all_matches": all_matches})


def jobwise_results(request, job_name):
    matches = Match.objects.filter(
        job=Job.objects.get(job_name=job_name), score__gt=0
    ).order_by("-score")
    page = request.GET.get('page', 1)
    paginator = Paginator(matches, 10)
    try:
        matches = paginator.page(page)
    except PageNotAnInteger:
        matches = paginator.page(1)
    except EmptyPage:
        matches = paginator.page(paginator.num_pages)
    return render(request, "cvjd/jobwise.html", {"matches": matches, "job": job_name})


def candidate_details(request, id):
    candidate = Candidate.objects.get(id=id)
    return render(request, "cvjd/candidate.html", {"candidate": candidate})
