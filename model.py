from surprise import SVD
from sklearn.metrics.pairwise import cosine_similarity

def get_svd_model():
    """Returns the Model-Based Collaborative Filtering Algorithm (SVD)"""
    return SVD()

def get_cosine_similarity(matrix):
    """Returns Memory-Based Cosine Similarity matrix"""
    return cosine_similarity(matrix)
