import json
import random
import os
import pandas as pd
import ast
from django.shortcuts import render, redirect
from django.conf import settings
from chemistry.models import Element

def generate_name_of_element_question():
    elements = Element.objects.all()
    element_data = [(element.name, element.symbol) for element in elements]
    df = pd.DataFrame(element_data, columns=["Name", "Symbol"])
    
    element = random.choice(df.to_dict(orient="records"))
    correct_answer = element["Name"]
    
    other_elements = df[df["Name"] != element["Name"]].sample(n=3)
    incorrect_answers = []
    for _, row in other_elements.iterrows():
        incorrect_answers.append(row["Name"])
    
    answers = [correct_answer] + incorrect_answers
    random.shuffle(answers)
    question_text = f"Which element has the symbol '{element['Symbol']}'?"
    
    return {
        'question_text': question_text,
        'answers': answers,
        'correct_answer': correct_answer,
    }

def generate_symbol_of_element_question():
    elements = Element.objects.all()
    element_data = [(element.name, element.symbol) for element in elements]
    df = pd.DataFrame(element_data, columns=["Name", "Symbol"])
    
    element = random.choice(df.to_dict(orient="records"))
    correct_answer = element["Symbol"]
    
    other_elements = df[df["Name"] != element["Name"]].sample(n=3)
    incorrect_answers = []
    for _, row in other_elements.iterrows():
        incorrect_answers.append(row["Symbol"])
    
    answers = [correct_answer] + incorrect_answers
    random.shuffle(answers)
    question_text = f"What symbol represents '{element['Name']}'?"
    
    return {
        'question_text': question_text,
        'answers': answers,
        'correct_answer': correct_answer,
    }
