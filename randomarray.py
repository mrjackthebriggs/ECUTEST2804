import random

array = []

# Add comments next time
def rand_seq():
    for i in range(1,10):
        sub_array = []
        for j in random.sample(range(1,11),10):
            sub_array.append(j)
        array.append(sub_array)
        print(sub_array)
    return array 