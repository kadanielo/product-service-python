from flask import Flask, jsonify
from flask_cors import CORS
import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

app = Flask(__name__)
CORS(app)  # Enable CORS for all origins

# Define the '/products' route
@app.route('/products', methods=['GET'])
def get_products():
    products = [
        {"id": 1, "name": "Dog Food", "price": 19.99},
        {"id": 2, "name": "Cat Food", "price": 34.99},
        {"id": 3, "name": "Bird Seeds", "price": 10.99},
    ]
    return jsonify(products)

if __name__ == '__main__':
    # Get port from .env or default to 3030
    port = int(os.getenv("PORT", 3030))
    debug = os.getenv("DEBUG", "False").lower() in ("true", "1")
    
    app.run(host='0.0.0.0', port=port, debug=debug)
