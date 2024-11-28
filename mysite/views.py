import json
import random
import os
import ast
from django.shortcuts import render, redirect
from django.conf import settings
from comics.models import Superhero

def view_notebook(request, notebook_name):
    notebook_path = os.path.join('notebooks', f'{notebook_name}.html')

    if os.path.exists(notebook_path):
        with open(notebook_path, 'r', encoding='utf-8') as f:
            notebook_html = f.read()
        return render(request, 'notebook.html', {'notebook_html': notebook_html})
    else:
        return render(request, '404.html', {'message': 'Notebook not found'})
      
def home(request):
    return render(request, 'home.html')

def generate_superhero_question():
    superhero = random.choice(Superhero.objects.all())
    superhero_powers = superhero.power.split(", ")
    selected_power = random.choice(superhero_powers)
    
    other_heroes = Superhero.objects.exclude(power__contains=selected_power).order_by('?')[:3]
    answers = [superhero] + list(other_heroes)
    random.shuffle(answers)
    question_text = f"Which superhero has the power of {selected_power}?"
    
    return {
        'question_text': question_text,
        'answers': [hero.name for hero in answers],
        'correct_answer': superhero.name,
    }

def load_trivia_questions():
    superhero_questions = [
        generate_superhero_question(),
        generate_superhero_question(),
        generate_superhero_question(),
        generate_superhero_question(),
        generate_superhero_question(),
    ]
    return superhero_questions

def start_game(request):
    questions = load_trivia_questions()
    random.shuffle(questions)

    request.session['questions'] = questions
    request.session['question_index'] = 0
    request.session['score'] = 0
    
    return redirect('/game/')

def play_game(request):
    questions = request.session.get('questions', [])
    question_index = request.session.get('question_index', 0)
    score = request.session.get('score', 0)

    if question_index >= len(questions):
        return redirect('/game-over/')

    question = questions[question_index]

    if request.method == 'POST':
        selected_answer = request.POST['answer']
        if selected_answer == question['correct_answer']:
            score += 1

        request.session['score'] = score
        request.session['question_index'] = question_index + 1

        return redirect('/game/')

    return render(request, 'game.html', {
        'question_number': question_index + 1,
        'question_text': question['question_text'],
        'answers': question['answers'],
        'score': score,
        'questions': questions
    })

def game_over(request):
    score = request.session.get('score', 0)
    return render(request, 'game_over.html', {'score': score})

def leaderboard(request):
    return render(request, 'leaderboard.html')
