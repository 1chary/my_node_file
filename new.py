def get_the_output(numbers,n,time):
    if time > n:
        index = time - n 
        return numbers[index]
    else:
        max_number = [i for i in range(1,time+1)]
        return max_number[-1]

n = 3
time = 2
numbers = [i for i in range(1,n+1)]
print(get_the_output(numbers,n,time))