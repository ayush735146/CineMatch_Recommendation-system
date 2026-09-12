from surprise import Dataset, Reader, SVD
from surprise.model_selection import train_test_split
import pickle

def train_model():
    print("Loading data for training...")
    # Load built-in MovieLens 100k dataset for Surprise
    data = Dataset.load_builtin('ml-100k')
    trainset, testset = train_test_split(data, test_size=0.2)
    
    print("Training SVD Matrix Factorization model...")
    algo = SVD()
    algo.fit(trainset)
    
    print("Training complete. Saving model weights...")
    with open('cinematch_model.pkl', 'wb') as f:
        pickle.dump(algo, f)
    print("Model saved successfully.")

if __name__ == "__main__":
    train_model()
