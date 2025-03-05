from django.shortcuts import render
from .models import Job
from .forms import JobApplicationForm
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Q

def home(request):
    jobs = Job.objects.all().order_by('-created_at')
    featured_jobs = Job.objects.filter(is_featured=True).order_by('-created_at')[:5]
    context = {
        'jobs': jobs,
        'featured_jobs': featured_jobs
    }
    return render(request, 'jobs/home.html', context)  # Pass the context here!



@login_required
def apply_for_job(request, job_id):
    job = get_object_or_404(Job, id=job_id)

    if request.method == 'POST':
        form = JobApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            application = form.save(commit=False)
            application.job = job
            application.save()
            messages.success(request, 'Your application has been submitted!')
            return redirect('job_detail', job_id=job.id)
    else:
        form = JobApplicationForm()

    return render(request, 'jobs/apply_for_job.html', {'form': form, 'job': job})

def job_detail(request, job_id):
    job = get_object_or_404(Job, id=job_id)
    return render(request, 'jobs/job_detail.html', {'job': job})


def job_list(request):
    query = request.GET.get('q')
    jobs = Job.objects.all()

    if query:
        jobs = jobs.filter(
            Q(title__icontains=query) |
            Q(description__icontains=query) |
            Q(company__icontains=query)
        )

    context = {
        'jobs': jobs,
        'query': query
    }
    return render(request, 'jobs/job_list.html', context)



def about_us(request):
    return render(request, 'jobs/about_us.html')

def contact_us(request):
    return render(request, 'jobs/contact_us.html')

