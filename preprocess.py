import pandas as pd

def load_and_clean_data(ratings_path, movies_path):
    print("Loading datasets...")
    ratings = pd.read_csv(ratings_path)
    movies = pd.read_csv(movies_path)
    
    # Merge datasets
    df = pd.merge(ratings, movies, on='movieId')
    print(f"Data merged. Total records: {len(df)}")
    return df

if __name__ == "__main__":
    # Dummy run
    print("Preprocessing script ready.")
