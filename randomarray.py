import random

array = []

# Add comments next time
def rand_seq(num):
    for i in range(1,num+1):
        sub_array = []
        for j in random.sample(range(1,11),10):
            sub_array.append(j)
        array.append(sub_array)
    return array 