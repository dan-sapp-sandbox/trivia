import random
import pandas as pd
from movies.models import Movie

def generate_movie_has_actor_question():
    movies = Movie.objects.all()
    movie_data = [(movie.name, movie.actors) for movie in movies]
    df = pd.DataFrame(movie_data, columns=["Name", "actors"])
    
    movie = random.choice(df.to_dict(orient="records"))
    movie_actors = movie["actors"].split(',')
    correct_answer = random.choice(movie_actors).strip()
    
    other_actors = df[df["actors"] != movie["actors"]].sample(n=3)
    incorrect_answers = []
    for _, row in other_actors.iterrows():
        actors = row["actors"].split(',')
        incorrect_answers.append(random.choice(actors).strip())
    
    answers = [correct_answer] + incorrect_answers
    random.shuffle(answers)
    question_text = f"Which actor stars in '{movie['Name']}'?"
    
    return {
        'question_text': question_text,
        'answers': answers,
        'correct_answer': correct_answer,
    }
    
def generate_actor_in_movie_question():
    movies = Movie.objects.all()
    movie_data = [(movie.name, movie.actors) for movie in movies]
    df = pd.DataFrame(movie_data, columns=["Name", "actors"])
    
    movie = random.choice(df.to_dict(orient="records"))
    movie_actors = movie["actors"].split(',')
    actor = random.choice(movie_actors).strip()
    correct_answer = movie["Name"]
    
    other_actors = df[df["actors"] != movie["actors"]].sample(n=3)
    incorrect_answers = []
    for _, row in other_actors.iterrows():
        name = row["Name"]
        incorrect_answers.append(name)
    
    answers = [correct_answer] + incorrect_answers
    random.shuffle(answers)
    question_text = f"Which movie does {actor} star in?"
    
    return {
        'question_text': question_text,
        'answers': answers,
        'correct_answer': correct_answer,
    }

def generate_year_of_movie_question():
    movies = Movie.objects.all()
    movie_data = [(movie.name, movie.release_year) for movie in movies]
    df = pd.DataFrame(movie_data, columns=["Name", "Release_Year"])
    
    movie = random.choice(df.to_dict(orient="records"))
    correct_answer = movie["Release_Year"]
    
    other_years = df[df["Release_Year"] != movie["Release_Year"]]
    incorrect_answers = other_years["Release_Year"].drop_duplicates().sample(n=3).tolist()
    
    answers = [correct_answer] + incorrect_answers
    random.shuffle(answers)
    question_text = f"What year was '{movie['Name']}' released?"
    
    return {
        'question_text': question_text,
        'answers': answers,
        'correct_answer': correct_answer,
    }
