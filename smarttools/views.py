from django.shortcuts import render
from .models import *
# Create your views here.
def tools(request):
    ctx = {
        'total_questions': 10,
        'time_limit': "1:00",
        'difficulty': "Mixed",
    }
    return render(request, "smarttools/tools.html", ctx)

MCQ_QUESTIONS = [
    {
        "question": "What is the capital of France?",
        "options": ["Paris", "London", "Rome", "Berlin"],
        "answer": "Paris"
    },
    {
        "question": "Which language is used for Django?",
        "options": ["Python", "Java", "C++", "JavaScript"],
        "answer": "Python"
    },
    {
        "question": "2 + 2 = ?",
        "options": ["3", "4", "5", "22"],
        "answer": "4"
    }
]

def quiz_start(request):
    score = None
    if request.method == "POST":
        score = 0
        for i, q in enumerate(MCQ_QUESTIONS):
            selected = request.POST.get(f"question_{i}")
            if selected == q["answer"]:
                score += 1

    return render(request, "smarttools/quiz_start.html", {
        "questions": MCQ_QUESTIONS,
        "score": score,
        "total": len(MCQ_QUESTIONS)
    })

def unit_converter(request):
    result = None
    value = None
    from_unit = None
    to_unit = None

    conversion_rates = {
        'm': 1,
        'cm': 100,
        'km': 0.001
    }

    if request.method == 'POST':
        try:
            value = float(request.POST.get('value'))
            from_unit = request.POST.get('from_unit')
            to_unit = request.POST.get('to_unit')
            value_in_meters = value / conversion_rates[from_unit]

            result = value_in_meters * conversion_rates[to_unit]
        except (ValueError, KeyError):
            result = "Invalid input"

    return render(request, 'unit_converter.html', {
        'result': result,
        'value': value,
        'from_unit': from_unit,
        'to_unit': to_unit
    })
