import random
import pandas as pd
from words.models import Word

def generate_word_of_definition_question():
    words = Word.objects.all()
    word_data = [(word.name, word.definition) for word in words]
    df = pd.DataFrame(word_data, columns=["Name", "Definition"])
    
    word = random.choice(df.to_dict(orient="records"))
    correct_answer = word["Name"]
    
    other_words = df[df["Name"] != word["Name"]]
    incorrect_answers = other_words["Name"].drop_duplicates().sample(n=3).tolist()
    
    answers = [correct_answer] + incorrect_answers
    random.shuffle(answers)
    question_text = f"{word['Definition']}"
    
    return {
        'question_text': question_text,
        'answers': answers,
        'correct_answer': correct_answer,
    }
    
def generate_french_of_english_question():
    words = Word.objects.all()
    word_data = [(word.name, word.french) for word in words]
    df = pd.DataFrame(word_data, columns=["Name", "French"])
    
    word = random.choice(df.to_dict(orient="records"))
    correct_answer = word["Name"]
    
    other_words = df[df["Name"] != word["Name"]]
    incorrect_answers = other_words["Name"].drop_duplicates().sample(n=3).tolist()
    
    answers = [correct_answer] + incorrect_answers
    random.shuffle(answers)
    question_text = f"'{word['French']}' means what in English?"
    
    return {
        'question_text': question_text,
        'answers': answers,
        'correct_answer': correct_answer,
    }
    
def generate_english_of_french_question():
    words = Word.objects.all()
    word_data = [(word.name, word.french) for word in words]
    df = pd.DataFrame(word_data, columns=["Name", "French"])
    
    word = random.choice(df.to_dict(orient="records"))
    correct_answer = word["French"]
    
    other_words = df[df["Name"] != word["Name"]]
    incorrect_answers = other_words["French"].drop_duplicates().sample(n=3).tolist()
    
    answers = [correct_answer] + incorrect_answers
    random.shuffle(answers)
    question_text = f"What is '{word['Name']}' in French?"
    
    return {
        'question_text': question_text,
        'answers': answers,
        'correct_answer': correct_answer,
    }
    
def generate_spanish_of_english_question():
    words = Word.objects.all()
    word_data = [(word.name, word.spanish) for word in words]
    df = pd.DataFrame(word_data, columns=["Name", "Spanish"])
    
    word = random.choice(df.to_dict(orient="records"))
    correct_answer = word["Name"]
    
    other_words = df[df["Name"] != word["Name"]]
    incorrect_answers = other_words["Name"].drop_duplicates().sample(n=3).tolist()
    
    answers = [correct_answer] + incorrect_answers
    random.shuffle(answers)
    question_text = f"'{word['Spanish']}' means what in English?"
    
    return {
        'question_text': question_text,
        'answers': answers,
        'correct_answer': correct_answer,
    }
    
def generate_english_of_spanish_question():
    words = Word.objects.all()
    word_data = [(word.name, word.spanish) for word in words]
    df = pd.DataFrame(word_data, columns=["Name", "Spanish"])
    
    word = random.choice(df.to_dict(orient="records"))
    correct_answer = word["Spanish"]
    
    other_words = df[df["Name"] != word["Name"]]
    incorrect_answers = other_words["Spanish"].drop_duplicates().sample(n=3).tolist()
    
    answers = [correct_answer] + incorrect_answers
    random.shuffle(answers)
    question_text = f"What is '{word['Name']}' in Spanish?"
    
    return {
        'question_text': question_text,
        'answers': answers,
        'correct_answer': correct_answer,
    }
    
def generate_japanese_of_english_question():
    words = Word.objects.all()
    word_data = [(word.name, word.japanese) for word in words]
    df = pd.DataFrame(word_data, columns=["Name", "Japanese"])
    
    word = random.choice(df.to_dict(orient="records"))
    correct_answer = word["Name"]
    
    other_words = df[df["Name"] != word["Name"]]
    incorrect_answers = other_words["Name"].drop_duplicates().sample(n=3).tolist()
    
    answers = [correct_answer] + incorrect_answers
    random.shuffle(answers)
    question_text = f"'{word['Japanese']}' means what in English?"
    
    return {
        'question_text': question_text,
        'answers': answers,
        'correct_answer': correct_answer,
    }
    
def generate_english_of_japanese_question():
    words = Word.objects.all()
    word_data = [(word.name, word.japanese) for word in words]
    df = pd.DataFrame(word_data, columns=["Name", "Japanese"])
    
    word = random.choice(df.to_dict(orient="records"))
    correct_answer = word["Japanese"]
    
    other_words = df[df["Name"] != word["Name"]]
    incorrect_answers = other_words["Japanese"].drop_duplicates().sample(n=3).tolist()
    
    answers = [correct_answer] + incorrect_answers
    random.shuffle(answers)
    question_text = f"What is '{word['Name']}' in Japanese?"
    
    return {
        'question_text': question_text,
        'answers': answers,
        'correct_answer': correct_answer,
    }