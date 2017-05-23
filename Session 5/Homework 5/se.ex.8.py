x = [1, 4, 5, -1, 10]

def extract_even(x):
    x = [i for i in x if i % 2 == 0]
    return(x)

print(extract_even(x))


even_list = get_even_list([1, 2, 5, -10, 9, 6])


if set(even_list) == set([2, -10, 6]):
    print("Your function is correct")
else:
    print("Ooops, bugs detected")
