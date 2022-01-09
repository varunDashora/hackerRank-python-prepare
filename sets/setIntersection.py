# Enter your code here. Read input from STDIN. Print output to STDOUT
english_subs, roll_of_eng_subs=int(input()), input().split()
french_subs, roll_of_french_subs=int(input()), input().split()
print(len(set(roll_of_eng_subs).intersection(set(roll_of_french_subs))))
