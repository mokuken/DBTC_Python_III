# Tuples of Dictionary
games = (
    {"league of legends": 15},
    {"God of War": 10},
    {"Watch Dogs": 8}
)

# Increment the score for "league of legends"
games[0]["league of legends"] += 10

print(f"\nThe league of legends game has incremented the score to {games[0]['league of legends']}\n")
