
def print_formatted(number):
    # your code goes here
    bin_number = len(bin(number)[2:])
    for n in range(number):
        
        print(str((n+1)).rjust(bin_number, " "),  oct(n+1)[2:].rjust(bin_number, " "), hex(n+1)[2:].rjust(bin_number, " ").upper(), bin(n+1)[2:].rjust(bin_number, " "))

