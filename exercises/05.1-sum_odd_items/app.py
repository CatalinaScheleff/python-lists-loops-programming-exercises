arr = [4,5,734,43,45,100,4,56,23,67,23,58,45]

#Your code go here:
def sum_odds(numbers):
    total = 0

    for i in range(0,len(arr)):
        if numbers[i]%2 != 0:
            total += numbers[i]
    return total

print(sum_odds(arr))

