# Enter your code here. Read input from STDIN. Print output to STDOUT
eng_subs, roll_eng = int(input()), input().split()
french_subs, roll_french = int(input()), input().split()
print(len(set(roll_eng).difference(set(roll_french))))
