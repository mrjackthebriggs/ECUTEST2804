import randomarray

# Comments?
if __name__ == "__main__":
    print("10 random arrays that only use 1 to 10 once")
    array = randomarray.rand_seq(10)
    for i in array:
        print(i)
    