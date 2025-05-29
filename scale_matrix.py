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

def get_matrix_from_user():
    matrix = []
    while True: 
        try:
            num_rows = int(input("Enter the number of rows for the matrix: "))
            if num_rows <= 0:
                print("Number of rows must be a positive integer. Please try again.")
                continue
            break 
        except ValueError:
            print("Invalid input. Please enter an integer for the number of rows.")

    while True: 
        try:
            num_cols = int(input("Enter the number of columns for the matrix: "))
            if num_cols <= 0:
                print("Number of columns must be a positive integer. Please try again.")
                continue
            break 
        except ValueError:
            print("Invalid input. Please enter an integer for the number of columns.")

    print(f"\nEnter the elements for each row ({num_cols} elements per row, separated by spaces):")
    for i in range(num_rows):
        while True: 
            row_input_str = input(f"Row {i + 1}: ")
            row_elements_str = row_input_str.split() 

            if len(row_elements_str) != num_cols:
                print(f"Error: Expected {num_cols} elements, but got {len(row_elements_str)}. Please re-enter the entire row.")
                continue

            try:
                row = [float(element) for element in row_elements_str]
                matrix.append(row)
                break 
            except ValueError:
                print("Error: One or more elements in the row are not valid numbers. Please re-enter the entire row.")
                
    return matrix

def get_scale_factor_from_user():
    """
         Nessa parte o usuario dá entrada no fator de escalonamento. 
    """    
    while True:
        try:
            scale_factor_str = input("Enter the scale factor: ")
            scale_factor = float(scale_factor_str)
            return scale_factor
        except ValueError:
            print("Invalid input. Please enter a numeric value for the scale factor.")

if __name__ == "__main__":
    print("Matrix Scaling Tool")
    print("-------------------")

    user_matrix = get_matrix_from_user()
    if user_matrix is None: 
        print("Failed to get matrix input. Exiting.")
    else:
        print("\nInput Matrix you entered:")
        for row in user_matrix:
            print(row)

        user_scale_factor = get_scale_factor_from_user()

        if user_scale_factor is not None:
            print(f"\nScaling matrix by factor: {user_scale_factor}")
            resulting_matrix = scale_matrix(user_matrix, user_scale_factor)

            if resulting_matrix is not None:
                print("\nResulting Scaled Matrix:")
                print(resulting_matrix)
            else:
                print("Could not scale the matrix due to an error during the scaling process.")
        else:
            print("Failed to get scale factor. Exiting.")