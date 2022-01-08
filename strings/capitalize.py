

# Complete the solve function below.
def solve(s):
    
    for char in s[:].split():
        s = s.replace(char, char.capitalize())
    return s    
        

