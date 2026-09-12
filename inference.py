def recommend_top_n(user_id, n=5):
    # Dummy logic representing the SVD prediction phase
    print(f"Fetching Top {n} Movie Recommendations for User #{user_id}...")
    recommendations = [
        "1. Aladdin (1992) - Score: 4.6",
        "2. The Lion King (1994) - Score: 4.5",
        "3. Beauty and the Beast (1991) - Score: 4.4",
        "4. Finding Nemo (2003) - Score: 4.3",
        "5. Shrek (2001) - Score: 4.2"
    ]
    for rec in recommendations:
        print(rec)

if __name__ == "__main__":
    recommend_top_n(user_id=101)
