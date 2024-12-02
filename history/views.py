import random
import pandas as pd
from history.models import Event

def generate_year_of_event_question():
    events = Event.objects.all()
    event_data = [(event.name, event.year) for event in events]
    df = pd.DataFrame(event_data, columns=["Name", "Year"])
    
    event = random.choice(df.to_dict(orient="records"))
    correct_answer = event["Year"]
    
    other_events = df[df["Year"] != event["Year"]]
    incorrect_answers = other_events["Year"].drop_duplicates().sample(n=3).tolist()
    
    answers = [correct_answer] + incorrect_answers
    random.shuffle(answers)
    question_text = f"When did '{event['Name']}' happen?"
    
    return {
        'question_text': question_text,
        'answers': answers,
        'correct_answer': correct_answer,
    }