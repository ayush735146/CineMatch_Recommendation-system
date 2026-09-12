import pandas as pd

def create_utility_matrix(df):
    print("Creating User-Item Utility Matrix...")
    utility_matrix = df.pivot(index='userId', columns='title', values='rating')
    
    # Calculate Sparsity
    total_cells = utility_matrix.shape[0] * utility_matrix.shape[1]
    empty_cells = utility_matrix.isnull().sum().sum()
    sparsity = empty_cells / total_cells
    print(f"Matrix created. Sparsity Ratio: {sparsity * 100:.2f}%")
    
    return utility_matrix

if __name__ == "__main__":
    print("Utility Matrix builder ready.")
