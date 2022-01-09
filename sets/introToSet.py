def average(array):
    # your code goes here
    distinct_heights = set(array)
    return (sum(distinct_heights)/len(distinct_heights))

