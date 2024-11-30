import json
import random
import os
import pandas as pd
import ast
from django.shortcuts import render, redirect
from django.conf import settings
from comics.models import Superhero

def generate_superhero_appearance_question():
    superheroes = Superhero.objects.all()
    superhero_data = [(hero.name, hero.debut_issue) for hero in superheroes]
    df = pd.DataFrame(superhero_data, columns=["Name", "Debut Issue"])

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
