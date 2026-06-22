print("WELCOME TO AI RECOMMENDATION SYSTEM")
movie_data = {
    "Interstellar": ["Sci-Fi", "Adventure", "Drama"],
    "Avengers Endgame": ["Action", "Sci-Fi", "Adventure"],
    "Spider Man No Way Home": ["Action", "Adventure", "Sci-Fi"],
    "John Wick": ["Action", "Thriller"],
    "The Conjuring": ["Horror", "Mystery"],
    "Inception": ["Sci-Fi", "Thriller"],
    "Titanic": ["Romance", "Drama"],
    "Joker": ["Drama", "Crime"],
    "Fast And Furious": ["Action", "Adventure"],
    "Doctor Strange": ["Action", "Fantasy", "Sci-Fi"]}
available_genres = ["Action","Sci-Fi","Adventure","Drama","Thriller","Horror","Mystery","Romance","Crime","Fantasy"]
while True:
    print("Available Genres:") 
    for genre in available_genres:
        print(genre)
    print("Enter your interests")
    print("Example : Action,Sci-Fi,Adventure")
    user_input = input("Enter Genres : ")
    user_interests = []
    split_values = user_input.split(",")
    for item in split_values:
        cleaned_value = item.strip().title()
        if cleaned_value != "":
            user_interests.append(cleaned_value)
    print("Your Selected Interests :") 
    for interest in user_interests:
        print(interest)
    recommendation_results = []
    print("Finding Recommendations...")
    for movie_name in movie_data:
        movie_genres = movie_data[movie_name]
        similarity_score = 0
        matched_genres = []
        for user_choice in user_interests:
            if user_choice in movie_genres:
                similarity_score += 1
                matched_genres.append(user_choice)
        if similarity_score > 0:
            recommendation_results.append([movie_name,similarity_score,matched_genres])
    recommendation_results.sort(key=lambda x: x[1],reverse=True)
    print("Recommended Movies")
    if len(recommendation_results) == 0:
        print("No recommendations found")
    else:
        rank = 1
        for movie in recommendation_results:
            movie_name = movie[0]
            movie_score = movie[1]
            movie_matches = movie[2]
            print(f"Rank : {rank}")
            print("Movie Name :", movie_name)
            print("Similarity Score :", movie_score)
            print("Matched Genres :", ", ".join(movie_matches))
            rank += 1
    highest_score = 0
    best_movie = ""
    for movie in recommendation_results:
        if movie[1] > highest_score:
            highest_score = movie[1]
            best_movie = movie[0]
    if best_movie != "":
        print("Top Recommendation :", best_movie)
        print("Highest Similarity Score :", highest_score)
    print("Would you like another recommendation search?")
    user_choice = input("Enter Yes or No : ").lower()
    if user_choice == "no":
        print("Thank You For Using AI Recommendation System")
        print("Program Ended Successfully")
        break
    elif user_choice == "yes":
        continue
    else:
        print("\nInvalid Choice")
        print("Program Ended")
        break