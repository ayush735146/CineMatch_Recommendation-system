from surprise import Dataset, SVD
from surprise.model_selection import cross_validate

def evaluate_model():
    data = Dataset.load_builtin('ml-100k')
    algo = SVD()
    print("Evaluating SVD Model using 5-Fold Cross Validation...")
    results = cross_validate(algo, data, measures=['RMSE', 'MAE'], cv=5, verbose=True)
    print(f"Average RMSE: {results['test_rmse'].mean():.4f}")

if __name__ == "__main__":
    evaluate_model()
