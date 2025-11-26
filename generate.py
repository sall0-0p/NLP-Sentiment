import csv
import random

def generate_hoi4_reviews():
    # Defines the filename and column headers
    filename = 'hoi4_reviews.csv'
    columns = ['product_name', 'opinion_id', 'sentiment', 'opinion', 'score']

    # Templates for constructing Steam-style reviews
    # Positive components
    pos_openers = [
        "Best grand strategy game ever made.",
        "I have lost my social life to this game.",
        "Absolute masterpiece of map painting.",
        "Finally understand geography better than my teacher.",
        "1000 hours in and I'm just getting started.",
        "Worth every penny if you like history.",
        "The modding community saves this game.",
        "War crimes simulator 10/10.",
        "Paid $40 to stare at a map for 5 hours. Would do again.",
        "Complex but incredibly rewarding."
    ]
    
    pos_details = [
        "The supply system is actually good now.",
        "Nothing beats the feeling of a perfect encirclement.",
        "Kaiserreich is basically a whole new game.",
        "I still don't understand the navy but the green bubbles make me happy.",
        "Building a massive tank division is pure dopamine.",
        "Learning curve is steep, but the payoff is huge.",
        "Playing as minor nations is a great challenge.",
        "The alternate history paths are hilarious and fun.",
        "Multiplayer is chaotic in the best way possible.",
        "Great soundtrack and atmosphere."
    ]
    
    pos_closers = [
        "Highly recommended.",
        "Just buy it.",
        "Say goodbye to your sleep.",
        "Paradox has done it again.",
        "Don't look at the DLC price, just get the subscription.",
        "Better than Civ.",
        "Addicting loop.",
        "Requires a PhD to play, but worth it.",
        "Would capitulate France again.",
        "Artillery only is the way."
    ]

    # Negative components
    neg_openers = [
        "Paradox DLC policy is a joke.",
        "Do not buy this unless you have $300 for DLCs.",
        "Good game ruined by greed.",
        "Optimization is non-existent.",
        "The AI is absolutely braindead.",
        "Spreadsheet simulator 2016.",
        "I want to like this game, but I can't.",
        "Unplayable without mods.",
        "Laggy mess.",
        "Too complex for its own good."
    ]

    neg_details = [
        "The game runs in slow motion past 1943.",
        "Navy makes zero sense no matter how many tutorials you watch.",
        "You have to pay $20 just to get focus trees for minor nations.",
        "Battle plans never work, units just shuffle around aimlessly.",
        "Late game lag is unbearable on high-end PCs.",
        "The peace conferences are completely broken.",
        "They hide essential mechanics behind paywalls.",
        "Multiplayer is toxic and unstable.",
        "The tutorial teaches you literally nothing.",
        "Frontlines break constantly for no reason."
    ]

    neg_closers = [
        "Refunded.",
        "Wait for a 90% sale.",
        "Go play HOI3 or Darkest Hour instead.",
        "Fix your game Paradox.",
        "Not recommended for sane people.",
        "Disappointed.",
        "Waste of time and money.",
        "It's just a map coloring book that costs too much.",
        "I can't support this business model.",
        "Boring and tedious."
    ]

    reviews = []
    
    # Generates 100 positive reviews
    for i in range(1, 101):
        text = f"{random.choice(pos_openers)} {random.choice(pos_details)} {random.choice(pos_closers)}"
        # Adds occasional Steam "funny" one-liners
        if i % 10 == 0:
            text = random.choice([
                "I formed the Roman Empire as Luxembourg. 10/10",
                "My wife left me but I have 2000 soft attack heavy tanks.",
                "Hitler capitulated to Poland in 1939. Historical AI is a lie.",
                "Game crashed, opened it again immediately.",
                "Green bubble good. Red bubble bad."
            ])
            
        reviews.append({
            'product_name': 'Hearts of Iron IV',
            'opinion_id': i,
            'sentiment': 'positive',
            'opinion': text,
            'score': random.randint(4, 5)
        })

    # Generates 100 negative reviews
    for i in range(101, 201):
        text = f"{random.choice(neg_openers)} {random.choice(neg_details)} {random.choice(neg_closers)}"
        # Adds occasional Steam "funny/angry" one-liners
        if i % 10 == 0:
            text = random.choice([
                "Plays slower than real time.",
                "Bought the game for $40, need $200 more to actually play it.",
                "Why is the AI abandoning the Maginot Line?",
                "1945 runs at 1 frame per minute.",
                "I prefer having a life."
            ])

        reviews.append({
            'product_name': 'Hearts of Iron IV',
            'opinion_id': i,
            'sentiment': 'negative',
            'opinion': text,
            'score': random.randint(1, 2) # Steam negative is usually thumbs down, mapped to low score
        })

    # Shuffles the list to mix positive and negative reviews
    random.shuffle(reviews)

    # Writes the data to the CSV file
    with open(filename, mode='w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=columns)
        writer.writeheader()
        writer.writerows(reviews)

    print(f"Successfully generated {filename} with {len(reviews)} reviews.")

if __name__ == "__main__":
    generate_hoi4_reviews()