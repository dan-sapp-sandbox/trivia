import random
import pandas as pd
from books.models import Book

def generate_author_of_book_question():
    books = Book.objects.all()
    book_data = [(book.name, book.author) for book in books]
    df = pd.DataFrame(book_data, columns=["Name", "Author"])
    
    book = random.choice(df.to_dict(orient="records"))
    correct_answer = book["Author"]
    
    other_books = df[df["Author"] != book["Author"]].sample(n=3)
    incorrect_answers = []
    for _, row in other_books.iterrows():
        incorrect_answers.append(row["Author"])
    
    answers = [correct_answer] + incorrect_answers
    random.shuffle(answers)
    question_text = f"Who wrote '{book['Name']}'?"
    
    return {
        'question_text': question_text,
        'answers': answers,
        'correct_answer': correct_answer,
    }

def generate_book_of_author_question():
    books = Book.objects.all()
    book_data = [(book.name, book.author) for book in books]
    df = pd.DataFrame(book_data, columns=["Name", "Author"])
    
    book = random.choice(df.to_dict(orient="records"))
    correct_answer = book["Name"]
    
    other_books = df[df["Author"] != book["Author"]].sample(n=3)
    incorrect_answers = []
    for _, row in other_books.iterrows():
        incorrect_answers.append(row["Name"])
    
    answers = [correct_answer] + incorrect_answers
    random.shuffle(answers)
    question_text = f"{book['Author']} wrote which of these?"
    
    return {
        'question_text': question_text,
        'answers': answers,
        'correct_answer': correct_answer,
    }
