import numpy as np

def scale_matrix(input_matrix, scale_factor):
    """
    Essa função escalona uma matriz multiplicando todos os elementos pelo scale_ factor
    """
    try:
        matrix_np = np.array(input_matrix, dtype=float)
        scaled_matrix = matrix_np * scale_factor
        return scaled_matrix
    except ValueError:
        
        print("Error: The input matrix contains non-numeric values or is malformed.")
        return None
    except Exception as e:
        print(f"An unexpected error occurred during scaling: {e}")
        return None

