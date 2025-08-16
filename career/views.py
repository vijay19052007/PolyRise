from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage
from django.conf import settings
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from .models import ResumeTemplate, ProjectIdea, AptitudeQuestion, HRQuestion, InterviewVideo, CareerQuizQuestion
from .forms import ResumeForm
from urllib.parse import urlparse, parse_qs

@login_required
def career_home(request):
    return render(request, 'career/career_home.html')

@login_required
def resume_builder(request):
    resumes = ResumeTemplate.objects.filter(is_active=True)
    initial_data = request.session.get('resume_data', None)

    if request.method == 'POST':
        form = ResumeForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.cleaned_data
            photo = request.FILES.get('photo')
            photo_url = None
            if photo:
                fs = FileSystemStorage(location=settings.MEDIA_ROOT + '/resume_photos/',
                                       base_url=settings.MEDIA_URL + 'resume_photos/')
                filename = fs.save(photo.name, photo)
                photo_url = fs.url(filename)
            elif initial_data:
                photo_url = initial_data.get('photo_url')

            context = {
                'full_name': data.get('full_name'),
                'email': data.get('email'),
                'phone': data.get('phone'),
                'education': data.get('education'),
                'skills': data.get('skills'),
                'projects': data.get('projects'),
                'achievements': data.get('achievements'),
                'linkedin': data.get('linkedin'),
                'github': data.get('github'),
                'photo_url': photo_url,
                'template': data.get('template', 'classic')
            }

            request.session['resume_data'] = context
            template_file = f"career/resume_templates/resume_{context['template']}.html"


            return render(request, template_file, context)
    else:
        form = ResumeForm(initial=initial_data)

    return render(request, 'career/resume.html', {'resumes': resumes, 'form': form})

@login_required
def download_resume(request):
    context = request.session.get('resume_data', None)
    if not context:
        return HttpResponse("No resume data found.")

    template_file = f"career/resume_{context.get('template', 'classic')}.html"
    template = get_template(template_file)
    html = template.render(context)

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="{context.get("full_name","resume")}.pdf"'

    pisa_status = pisa.CreatePDF(html, dest=response)
    if pisa_status.err:
        return HttpResponse("Error generating PDF <pre>" + html + "</pre>")

    return response

@login_required
def project_ideas(request):
    ideas = ProjectIdea.objects.filter(is_active=True)
    return render(request, 'career/project_ideas.html', {'ideas': ideas})

@login_required
def aptitude_mcq(request):
    questions = AptitudeQuestion.objects.filter(is_active=True)
    score = None
    user_answers = {}

    if request.method == "POST":
        score = 0
        total = questions.count()
        for q in questions:
            selected = request.POST.get(f'q_{q.id}')
            user_answers[q.id] = selected
            if selected and selected.upper() == q.correct_option:
                score += 1

    else:
        total = questions.count()

    return render(request, 'career/aptitude.html', {
        'questions': questions,
        'score': score,
        'total': total,
        'user_answers': user_answers
    })




@login_required
def hr_practice(request):
    questions = HRQuestion.objects.filter(is_active=True)
    return render(request, 'career/hr_practice.html', {'questions': questions})

@login_required
def interview_tips(request):
    videos = InterviewVideo.objects.filter(is_active=True)
    return render(request, 'career/tips.html', {'videos': videos})

@login_required
def career_quiz(request):
    questions = CareerQuizQuestion.objects.filter(is_active=True)
    return render(request, 'career/quiz.html', {'questions': questions})
