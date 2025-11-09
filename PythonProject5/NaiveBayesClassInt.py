# Ex.10 Naive Bayes Classifier Intermediate
# Kevin Key
# 10/21/2025

def flip(n):
    odds = 1.0      # start at 1:1
    r = 1/ 0.5      # likelihood of heads = 2
    for i in range(n):
        odds *= r
    print(odds)     # e.g., n=3 -> 8.0

# example run (the grader will set n)
n = 1
flip(n)