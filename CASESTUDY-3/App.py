from flask import Flask, render_template, request, jsonify

app = Flask(__name__)
movies = [
    {
        "id": 101,
        "movie_name": "Interstellar",
        "language": "English",
        "duration": "2h 49m",
        "price": 250
    }
]

bookings = []

@app.route('/',methods=['GET'])
def Home():
    return "Welcome to Online Movie Ticket Booking REST API – Development & Testing"

@app.route('/api/movies',methods=['GET'])
def getMovies():
    return jsonify(movies)

@app.route("/api/movies/<int:movie_id>",methods=['GET'])
def getMovieById(movie_id):
    for movie in movies:
        if movie["id"] == movie_id:
            return jsonify(movie)
    return jsonify({"error":"Movie not found"}),404
@app.route("/api/movies",methods=['POST'])
def addMovie():
    data=request.get_json()
    if not data or "movie_name" not in data:
        return jsonify({"error": "Movie Name is required"}), 400
    # Generate next ID
    if movies:
        next_id = max(movie["id"] for movie in movies) + 1
    else:
        next_id = 101  # starting ID
    new_movie={
        "id": next_id,
        "movie_name": data["movie_name"],
        "language": data["language"],
        "duration": data["duration"],
        "price": data["price"]
    }
    movies.append(new_movie)
    return jsonify(data), 201
@app.route("/api/movies/<int:movie_id>",methods=['PUT'])
def updateMovie(movie_id):
    data=request.get_json()
    for movie in movies:
        if movie["id"] == movie_id:
            movie.update(request.json)
            return jsonify(movie), 200
    return jsonify({"error": "Movie not found"}), 404
@app.route("/api/movies/<int:movie_id>",methods=['DELETE'])
def DeleteMovie(movie_id):
    for movie in movies:
        if movie["id"] == movie_id:
            movies.remove(movie)
            return jsonify(movie), 200
    return jsonify({"error": "Movie not found"}), 404

@app.route("/api/bookings", methods=['POST'])
def addBooking():
    booking = request.get_json()
    if not booking or "movie_id" not in booking or "tickets" not in booking or "name" not in booking:
        return jsonify({"error": "movie_id, tickets, and name are required"}), 400

    # Find the movie by ID
    movie = next((m for m in movies if m["id"] == booking.get("movie_id")), None)
    if not movie:
        return jsonify({"error": "Movie not found"}), 404

    tickets = booking.get("tickets")
    if tickets <= 0:
        return jsonify({"error": "Invalid ticket count"}), 400

    total_price = movie["price"] * tickets

    new_booking = {
        "movie_id": movie["id"],
        "movie_name": movie["movie_name"],
        "tickets": tickets,
        "total_price": total_price,
        "name": booking.get("name")
    }

    bookings.append(new_booking)

    return jsonify({
        "message": "Booking successful",
        "booking": new_booking
    }), 201
if __name__ == '__main__':
    app.run(debug=True,port=5010)