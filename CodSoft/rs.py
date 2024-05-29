from math import sqrt
import re

# Sample data
movies = {
    1: {"title": "Toy Story", "genres": ["Animation", "Children", "Comedy"]},
    2: {"title": "Jumanji", "genres": ["Adventure", "Children", "Fantasy"]},
    3: {"title": "Grumpier Old Men", "genres": ["Comedy", "Romance"]},
    4: {"title": "Waiting to Exhale", "genres": ["Comedy", "Drama"]},
    5: {"title": "Father of the Bride Part II", "genres": ["Comedy"]},
}

ratings = {
    "user1": {1: 5, 2: 3, 3: 4},
    "user2": {1: 4, 3: 5, 4: 2},
    "user3": {2: 4, 3: 3, 4: 5, 5: 2},
}

user_preferences = {
    "user1": ["Comedy", "Adventure"],
    "user2": ["Drama", "Romance"],
    "user3": ["Comedy", "Fantasy"],
}

# Collaborative Filtering
def calculate_similarity(ratings):
    similarity = {}
    for user in ratings:
        for item1 in ratings[user]:
            for item2 in ratings[user]:
                if item1 == item2:
                    continue
                similarity.setdefault(item1, {}).setdefault(item2, 0)
                similarity[item1][item2] += 1
    
    return similarity

def recommend_items(user, ratings, similarity):
    scores = {}
    for item in ratings[user]:
        for related_item, score in similarity[item].items():
            if related_item not in ratings[user]:
                scores.setdefault(related_item, 0)
                scores[related_item] += score
    
    recommended_items = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    return [item[0] for item in recommended_items]

# Content-Based Filtering
def genre_similarity(user_preferences, movies, user):
    user_genres = user_preferences[user]
    scores = {}
    
    for movie_id, movie_data in movies.items():
        score = 0
        for genre in movie_data["genres"]:
            if genre in user_genres:
                score += 1
        scores[movie_id] = score
    
    recommended_items = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    return [item[0] for item in recommended_items]

# Main function to get user input and provide recommendations
def main():
    # Get user input
    user = input("Enter your user ID (e.g., user1, user2, user3): ").strip()
    if user not in ratings:
        print("User ID not found. Please try again.")
        return
    
    preference_type = input("Enter preference type (collaborative or content): ").strip().lower()
    if preference_type not in ["collaborative", "content"]:
        print("Invalid preference type. Please try again.")
        return
    
    if preference_type == "collaborative":
        similarity = calculate_similarity(ratings)
        recommendations = recommend_items(user, ratings, similarity)
        print(f"Collaborative Filtering Recommendations for {user}:")
    else:
        recommendations = genre_similarity(user_preferences, movies, user)
        print(f"Content-Based Filtering Recommendations for {user}:")

    for movie_id in recommendations:
        print(f"Movie ID: {movie_id}, Title: {movies[movie_id]['title']}")

# Run the main function
if __name__ == "__main__":
    main()
