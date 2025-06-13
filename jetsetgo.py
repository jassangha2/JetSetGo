from flask import Flask, render_template, request, jsonify
from datetime import datetime, timedelta

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to JetSetGo Itinerary Generator!"

@app.route("/generate-itinerary", methods=["POST"])
def generate_itinerary():
    data = request.get_json()

    destination = data.get("destination")
    start_date_str = data.get("startDate")
    end_date_str = data.get("endDate")
    guests = int(data.get("guests", 1))

    try:
        start_date = datetime.strptime(start_date_str, "%Y-%m-%d")
        end_date = datetime.strptime(end_date_str, "%Y-%m-%d")
    except Exception:
        return jsonify({"error": "Invalid date format. Use YYYY-MM-DD."}), 400

    num_days = (end_date - start_date).days + 1
    if num_days < 1:
        return jsonify({"error": "End date must be after start date."}), 400

    itinerary = []
    sample_activities = [
        "City walking tour",
        "Visit a museum",
        "Try local food",
        "Scenic lookout",
        "Relax at the beach",
        "Shopping and souvenirs",
        "Cultural performance"
    ]

    for i in range(num_days):
        current_date = (start_date + timedelta(days=i)).strftime("%A, %d %B %Y")
        activity = sample_activities[i % len(sample_activities)]
        itinerary.append({
            "day": i + 1,
            "date": current_date,
            "activity": f"{activity} in {destination}",
            "details": f"Perfect for a group of {guests}. Don’t forget your camera!"
        })

    return jsonify(itinerary)

if __name__ == "__main__":
    app.run(debug=True)