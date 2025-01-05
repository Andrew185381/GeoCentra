from dotenv import load_dotenv
import os

load_dotenv()

TOKEN = os.getenv('MY_TOKEN')


from flask import Flask, request, jsonify, render_template
import geocentroid

app = Flask(__name__)

# Initialize your centroid calculator with the API key
geo_calculator = geocentroid.CentroidCalculator(api_key="AIzaSyD0__Q1gej9stSFZR9skc6p8tdC4njvJNk")

@app.route("/")
def index():
    # Serve the HTML file
    return render_template("index.html")

@app.route("/calculate_centroid", methods=["POST"])
def calculate_centroid():
    data = request.json  # Expecting JSON data from frontend
    locations = data.get("locations", [])
    try:
        # Use your geocentroid library to calculate the centroid
        centroid = geo_calculator.get_centroid(locations)
        return jsonify({"centroid": centroid})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    app.run(debug=True)


