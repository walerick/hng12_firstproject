from flask import Flask, jsonify
from datetime import datetime
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Initialize CORS

@app.route('/', methods=['GET'])
def get_info():
    email = "bakareadewale@gmail.com"
    current_datetime = datetime.utcnow().isoformat() + "Z"  # Corrected to "Z"
    github_url = "https://github.com/yourusername/your-repo"  # Replace with your actual GitHub URL

    response = {
        "email": email,
        "current_datetime": current_datetime,
        "github_url": github_url
    }
    return jsonify(response), 200

if __name__ == "__main__":
    app.run(debug=True)