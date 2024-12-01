import random
import pandas as pd
from geography.models import Landmark

def generate_landmark_at_coord_question():
    landmarks = Landmark.objects.all()
    landmark_data = [(landmark.name, landmark.longitude, , landmark.latitude) for landmark in landmarks]
    df = pd.DataFrame(landmark_data, columns=["Name", "Longitude", "Latitude"])
    
    landmark = random.choice(df.to_dict(orient="records"))
    correct_answer = landmark["Name"]
    
    other_landmarks = df[df["Name"] != movie["Name"]].sample(n=3)
    incorrect_answers = []
    for _, row in other_landmarks.iterrows():
        incorrect_answers.append(row["Name"])
    
    answers = [correct_answer] + incorrect_answers
    random.shuffle(answers)
    question_text = f"Which landmark lies at {row["Longitude"]} x {row["Latitude"]}?"
    
    return {
        'question_text': question_text,
        'answers': answers,
        'correct_answer': correct_answer,
    }