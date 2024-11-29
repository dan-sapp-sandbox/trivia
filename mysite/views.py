import json
import random
import os
import pandas as pd
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

def generate_superhero_appearance_question():
    superheroes = Superhero.objects.all()
    superhero_data = [(hero.name, hero.debut_issue) for hero in superheroes]
    df = pd.DataFrame(superhero_data, columns=["Name", "Debut Issue"])
    print("Superhero Data:", superhero_data)

    superhero = random.choice(df.to_dict(orient="records"))
    
    other_heroes = df[df["Debut Issue"] != superhero["Debut Issue"]].sample(n=3)
    answers = [superhero["Debut Issue"]] + other_heroes["Debut Issue"].tolist()
    random.shuffle(answers)
    
    question_text = f"Which comic has the first appearance of {superhero['Name']}?"

    return {
        'question_text': question_text,
        'answers': answers,
        'correct_answer': superhero["Debut Issue"],
    }


def generate_superhero_power_question():
    superheroes = Superhero.objects.all()
    superhero_data = [(hero.name, hero.power) for hero in superheroes]
    df = pd.DataFrame(superhero_data, columns=["Name", "Power"])
    df["Power"] = df["Power"].apply(lambda x: ', '.join([p.strip().title() for p in x.split(',')]))

    superhero = random.choice(df.to_dict(orient="records"))
    selected_power = random.choice(superhero["Power"].split(", "))
    other_heroes = df[~df["Power"].str.contains(selected_power, case=False)].sample(n=3)
    answers = [superhero["Name"]] + other_heroes["Name"].tolist()
    random.shuffle(answers)
    question_text = f"Which character has the power of {selected_power}?"

    return {
        'question_text': question_text,
        'answers': answers,
        'correct_answer': superhero["Name"],
    }

def load_trivia_questions():
    num_questions = 5
    superhero_appearance_questions = [
        generate_superhero_appearance_question() for _ in range(num_questions)
    ]
    superhero_power_questions = [
        generate_superhero_power_question() for _ in range(num_questions)
    ]
    superhero_questions = superhero_appearance_questions + superhero_power_questions
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
