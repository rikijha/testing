array=[1,2]

def all_subset(given_array):
    subset= [None]*given_array.__len__()


    helper(given_array,subset,0)


def print_set(subset):
    print(subset, ",")




def helper(given_array,subset,i):
    if i== given_array.__len__():
        print_set(subset)
    else:
        subset[i]=None
        helper(given_array,subset,i+1)
        subset[i]=given_array[i]
        helper(given_array,subset,i+1)

all_subset(array)