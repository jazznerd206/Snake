# average

# This is a behind the scenes look at the average method implemented with the built in statistics.mean function. The difference in this implementation accepts integers as arguments, where statistics.mean accepts a single array of integers as its parameter.

# Takes the sum of all the args and divides it by len(args). The second argument 0.0 in sum is to handle floating point division in python3.

# Returns the average of two or more numbers.

def average(*args):
    return sum(args, 0.0) / len(args)

print(average(*[1, 2, 3])) # 2.0
print(average(1, 2, 3)) # 2.0