import pandas as pd
from pandasgui import show

# Example superhero data (powers are already in title case)
superheroes_data = [
    ("Spider-Man", "Web-Slinging, Super Strength, Agility", "1962"),
    ("Iron Man", "Powered Armor Suit, Genius-Level Intellect, Flight", "1963"),
    ("Thor", "God-Like Strength, Weather Manipulation, Immortality", "1962"),
    ("Hulk", "Super Strength, Healing Factor, Rage Transformation", "1962"),
    ("Captain America", "Super Strength, Enhanced Agility, Super Soldier Serum", "1941"),
    ("Black Widow", "Expert Martial Artist, Spycraft, Deception", "1964"),
    ("Doctor Strange", "Magic, Time Manipulation, Astral Projection", "1963"),
    ("Black Panther", "Superhuman Agility, Enhanced Senses, Vibranium Suit", "1966"),
    ("Ant-Man", "Size Manipulation, Super Strength, Agility", "1962"),
    ("Wolverine", "Enhanced Senses, Healing Factor, Adamantium Claws", "1974"),
    ("Superman", "Super Strength, Flight, Heat Vision", "1938"),
    ("Batman", "Peak Human Condition, Master Detective, Technology Expertise", "1939"),
    ("Wonder Woman", "Super Strength, Flight, Indestructibility", "1941"),
    ("The Flash", "Super Speed, Vibrating Through Objects, Time Travel", "1940"),
    ("Green Lantern", "Power Ring, Flight, Energy Blasts", "1940"),
    ("Aquaman", "Control Over Water, Super Strength, Swimming At Incredible Speeds", "1941"),
    ("Shazam", "Lightning Manipulation, Super Strength, Immortality", "1939"),
    ("Martian Manhunter", "Telepathy, Shapeshifting, Super Strength", "1955"),
    ("Green Arrow", "Archery, Martial Arts, Strategic Genius", "1941"),
    ("Hawkeye", "Archery, Martial Arts, Strategic Genius", "1964"),
    ("Deadpool", "Regeneration, Superhuman Strength, Enhanced Senses", "1991"),
    ("The Punisher", "Expert Marksman, Hand-To-Hand Combat, Tactical Genius", "1974"),
    ("Daredevil", "Superhuman Senses, Martial Arts, Agility", "1964"),
    ("Luke Cage", "Super Strength, Durability, Regeneration", "1972"),
    ("Jessica Jones", "Super Strength, Invulnerability, Flight", "2001"),
    ("The Thing", "Super Strength, Invulnerability, Rock-Like Skin", "1961"),
    ("Human Torch", "Flight, Fire Control, Immortality", "1961"),
    ("Invisible Woman", "Invisibility, Force Fields, Super Strength", "1961"),
    ("Mr. Fantastic", "Stretching, Super Intelligence, Regeneration", "1961"),
    ("Scarlet Witch", "Reality Manipulation, Telekinesis, Energy Blasts", "1964"),
    ("Vision", "Density Control, Flight, Superhuman Strength", "1968"),
    ("Quicksilver", "Super Speed, Time Manipulation, Super Reflexes", "1964"),
    ("Magneto", "Magnetism Control, Flight, Telekinesis", "1963"),
    ("Professor X", "Telepathy, Mind Control, Astral Projection", "1963"),
    ("Storm", "Weather Control, Flight, Super Strength", "1975"),
    ("Cyclops", "Optic Blasts, Leadership, Enhanced Vision", "1963"),
    ("Nightcrawler", "Teleportation, Super Agility, Enhanced Senses", "1969"),
    ("Beast", "Super Strength, Agility, Enhanced Senses", "1963"),
    ("Jubilee", "Light Manipulation, Energy Blasts, Super Agility", "1989"),
    ("Rogue", "Power Absorption, Super Strength, Flight", "1981"),
    ("Gambit", "Kinetic Energy Manipulation, Enhanced Agility, Master Thief", "1990"),
    ("Cable", "Telekinesis, Time Travel, Cybernetic Enhancements", "1990"),
    ("Silver Surfer", "Cosmic Power, Flight, Energy Manipulation", "1966")
]

# Create a DataFrame
df = pd.DataFrame(superheroes_data, columns=["Name", "Powers", "Debut Year"])

# Show the DataFrame to verify it's correct
show(df)
