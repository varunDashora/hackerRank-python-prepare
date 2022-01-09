# Enter your code here. Read input from STDIN. Print output to STDOUT
english_subs, list_of_english_subs=int(input()), input().split()
french_subs, list_of_french_subs=int(input()), input().split()
print(len(set(list_of_english_subs).union(set(list_of_french_subs))))
