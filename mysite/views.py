import json
import random
import os
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.conf import settings

def view_notebook(request, notebook_name):
    # Path to the HTML-converted notebooks
    notebook_path = os.path.join('notebooks', f'{notebook_name}.html')

    if os.path.exists(notebook_path):
        with open(notebook_path, 'r', encoding='utf-8') as f:
            notebook_html = f.read()
        return render(request, 'notebook.html', {'notebook_html': notebook_html})
    else:
        return render(request, '404.html', {'message': 'Notebook not found'})
      
def home(request):
    # Your homepage, render home.html
    return render(request, 'home.html')

# Load trivia questions from JSON file
def load_trivia_questions():
    """Load trivia questions from a JSON file."""
    json_file_path = os.path.join(settings.BASE_DIR, 'questions.json')

    with open(json_file_path, 'r') as file:
        questions = json.load(file)
    
    return questions

def start_game(request):
    """Initialize game session with question index and score."""
    request.session['question_index'] = 0  # Start at the first question
    request.session['score'] = 0  # Initialize score
    return redirect('/game/')  # Redirect to the game page

def play_game(request):
    """Handle the gameplay, including displaying questions and updating the score."""
    questions = load_trivia_questions()

    # Get the current question index from the session
    question_index = request.session.get('question_index', 0)
    score = request.session.get('score', 0)

    # Check if there are more questions
    if question_index >= len(questions):
        return redirect('/game-over/')  # Redirect to game over if no more questions

    # Get the current question
    question = questions[question_index]

    if request.method == 'POST':
        selected_answer = request.POST['answer']
        # Check if the selected answer is correct
        if selected_answer == question['correct']:
            score += 1  # Increase score if correct

        # Update the session with the new score and move to the next question
        request.session['score'] = score
        request.session['question_index'] = question_index + 1

        return redirect('/game/')  # Continue to next question

    # Render the game page with the current question and score
    return render(request, 'game.html', {
        'question_number': question_index + 1,
        'question_text': question['question'],
        'answers': question['answers'],
        'score': score
    })

def game_over(request):
    score = request.session.get('score', 0)
    return render(request, 'game_over.html', {'score': score})

def leaderboard(request):
    return render(request, 'leaderboard.html')
