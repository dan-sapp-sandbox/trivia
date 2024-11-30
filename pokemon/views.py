import random
import pandas as pd
from pokemon.models import Pokemon

def generate_pokemon_of_type():
    pokemon_list = Pokemon.objects.all()
    pokemon_data = [
        {"Name": pokemon.name, "Types": pokemon.types.split(", ")} 
        for pokemon in pokemon_list
    ]
    
    flattened_data = []
    for entry in pokemon_data:
        for ptype in entry["Types"]:
            flattened_data.append({"Name": entry["Name"], "Type": ptype.strip()})
    df = pd.DataFrame(flattened_data)
    
    selected_row = random.choice(df.to_dict(orient="records"))
    selected_type = selected_row["Type"]
    correct_answer = selected_row["Name"]
    
    df["Type"] = df["Type"].astype(str)
    other_pokemon = df[df["Type"] != selected_type]
    incorrect_answers = other_pokemon["Name"].drop_duplicates().sample(n=3).tolist()
    
    answers = [correct_answer] + incorrect_answers
    random.shuffle(answers)
    question_text = f"Which pokemon is {selected_type} Type?"
    
    return {
        'question_text': question_text,
        'answers': answers,
        'correct_answer': correct_answer,
    }
