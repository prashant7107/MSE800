numbers = [1,2,3,4,5]
squares = {str(n) : n**2 for n in numbers}
print (squares)

dict1 = {'a': 1, 'b':2}
dict2 = {'b':3, 'c':4}
merge_dict = {**dict2, **dict1}
print(merge_dict)