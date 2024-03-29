# // 1 -- Understand the problem
# // 2 -- Think of examples
# // 3 -- Break it down
# // 4 -- solve or simplify
# // 5 -- refactor

# “ Greatest Common Factor
# Given two integers, create rGCF(num1,num2) to recursively determine Greatest Common Factor (the largest integer dividing evenly into both).
# Greek mathematician Euclid demonstrated these facts:

# 1)      gcf(a,b) == a, if a == b;
# 2)      gcf(a,b) == gcf(a-b,b), if a>b;
# 3)      gcf(a,b) == gcf(a,b-a), if b>a.”

# Excerpt From: Martin Puryear. “Algorithm Challenges: E-book for Dojo Students.” iBooks.


def gcf(num1, num2):
    if num1 % num2 == 0:
        return num2
    if num1 % num2 == 1:
        return 1
    return gcf(num1, num2 % num1)


print(gcf(12, 4))
