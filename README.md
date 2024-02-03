# Flask Card Game API
This Flask application implements a simple card game API where users can request a set of shuffled cards distributed among a specified number of players.

Getting Started
To get started with this API, follow these steps:

Clone the repository to your local machine:

git clone https://github.com/yourusername/your-repo.git
Install the required dependencies:


pip install -r requirements.txt
Run the Flask application:


python app.py
Access the API at http://localhost:5000/.

Endpoints
/getcards
Method: GET
Parameters:
numberOfPlayers (optional): Number of players in the game (default is 1). Must be between 1 and 17.
Response:
JSON array containing card sets for each player.
Implementation Details
The API generates a complete deck of 52 cards upon the first request.
Cards are shuffled using a simple random shuffling algorithm.
Cards are distributed among the players evenly.
Usage Example
python
Copy code
import requests

# Example GET request
response = requests.get('http://localhost:5000/getcards?numberOfPlayers=4')
print(response.json())
License
This project is licensed under the MIT License - see the LICENSE file for details.
