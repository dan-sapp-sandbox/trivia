import random
import pandas as pd
from music.models import Song

def generate_artist_of_song():
    songs = Song.objects.all()
    song_data = [(song.name, song.artist) for song in songs]
    df = pd.DataFrame(song_data, columns=["Name", "Artist"])
    
    song = random.choice(df.to_dict(orient="records"))
    correct_answer = song["Artist"]
    
    other_songs = df[df["Artist"] != song["Artist"]]
    incorrect_answers = other_songs["Artist"].drop_duplicates().sample(n=3).tolist()
    
    answers = [correct_answer] + incorrect_answers
    random.shuffle(answers)
    question_text = f"Who wrote '{song['Name']}'?"
    
    return {
        'question_text': question_text,
        'answers': answers,
        'correct_answer': correct_answer,
    }
