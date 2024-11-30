import json
import random
import os
import ast
from django.shortcuts import render, redirect
from django.conf import settings
from geography.models import Landmark
from comics.views import generate_superhero_appearance_question, generate_superhero_power_question
from movies.views import generate_movie_has_actor_question, generate_actor_in_movie_question
from music.views import generate_artist_of_song
from pokemon.views import generate_pokemon_of_type
      
def home(request):
    return render(request, 'home.html')

def load_trivia_questions(selected_options, num_questions):
    superhero_appearance_questions = []
    if 'comics' in selected_options:
        superhero_appearance_questions = [
            generate_superhero_appearance_question() for _ in range(num_questions)
        ]
    superhero_power_questions = []
    if 'comics' in selected_options:
        superhero_power_questions = [
            generate_superhero_power_question() for _ in range(num_questions)
        ]
    movie_has_actor_questions = []
    if 'movies' in selected_options:
        actor_in_movie_questions = [
            generate_movie_has_actor_question() for _ in range(num_questions)
        ]
        
    actor_in_movie_questions = []
    if 'movies' in selected_options:
        actor_in_movie_questions = [
            generate_actor_in_movie_question() for _ in range(num_questions)
        ]
        
    artist_of_song_questions = []
    if 'music' in selected_options:
        artist_of_song_questions = [
            generate_artist_of_song() for _ in range(num_questions)
        ]
        
    pokemon_of_type_questions = []
    if 'pokemon' in selected_options:
        pokemon_of_type_questions = [
            generate_pokemon_of_type() for _ in range(num_questions)
        ]
        
    question_lists = [
        superhero_appearance_questions,
        superhero_power_questions,
        movie_has_actor_questions,
        actor_in_movie_questions,
        artist_of_song_questions,
        pokemon_of_type_questions,
    ]
    questions = [question for sublist in question_lists for question in sublist]
    return questions

def start_game(request):
    selected_options = request.POST.getlist('topics')
    num_questions = int(request.POST.get('num_questions', 10))
    questions = load_trivia_questions(selected_options, num_questions)
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

def view_notebook(request, notebook_name):
    notebook_path = os.path.join('notebooks', f'{notebook_name}.html')

    if os.path.exists(notebook_path):
        with open(notebook_path, 'r', encoding='utf-8') as f:
            notebook_html = f.read()
        return render(request, 'notebook.html', {'notebook_html': notebook_html})
    else:
        return render(request, '404.html', {'message': 'Notebook not found'})