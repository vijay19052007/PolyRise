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
