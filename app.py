from flask import Flask, jsonify, request
from flask_cors import CORS
import random

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

suits = ["hearts", "diamonds", "clubs", "spades"]
values = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "jack", "queen", "king", "ace"]
MaxPlayers = 17
DefaultPlayers = 1

class Card:
    def __init__(self, suit, value, imageUrl):
        self.Suit = suit
        self.Value = value
        self.ImageUrl = imageUrl

cache = {}  # This can be replaced with a more sophisticated caching mechanism

@app.route('/')
def home():
    return "home"

@app.route('/getcards')
def get_cards():
    numberOfPlayers = int(request.args.get('numberOfPlayers', DefaultPlayers))

    # Ensure numberOfPlayers does not exceed MaxPlayers
    if numberOfPlayers <= 0 or numberOfPlayers > MaxPlayers:
        return jsonify({"error": "Invalid number of players. Please provide a value between 1 and 17."}), 400

    # Check if the deck is already cached
    if 'deck' not in cache:
        # Generate a complete deck of cards
        deck = generate_deck()

        # Cache the deck
        cache['deck'] = deck

    else:
        deck = cache['deck']

    # Check if the shuffled deck is already cached
    if 'shuffledDeck' not in cache:
        # Shuffle the deck
        shuffled_deck = shuffle(deck)

        # Cache the shuffled deck
        cache['shuffledDeck'] = shuffled_deck

    else:
        shuffled_deck = cache['shuffledDeck']

    card_sets = []

    # Distribute cards to each player
    for i in range(numberOfPlayers):
        player_cards = shuffled_deck[i * 3: (i + 1) * 3]
        card_sets.append([vars(card) for card in player_cards])

    return jsonify(card_sets)

def generate_deck():
    deck = []

    # Construct the base URL for static files
    static_files_base_url = request.url_root + "static/Images/"

    for suit in suits:
        for value in values:
            image_url = f"{static_files_base_url}{value}_of_{suit}.png"
            deck.append(Card(suit, value, image_url))

    return deck

def shuffle(deck):
    shuffled_deck = deck.copy()
    random.shuffle(shuffled_deck)
    return shuffled_deck

if __name__ == '__main__':
    app.run(debug=True)
