n=int(input())

def num_of_ways(n):
    if n==1 or n==0:
        return 1
    else:
        ways=num_of_ways(n-1)+num_of_ways(n-2)
        return ways
print(num_of_ways(n))

