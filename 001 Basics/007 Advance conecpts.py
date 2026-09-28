# iterators:
# An iterator is an object that contains a countable number of values.

my_list = [1, 2, 3, 4]
for item in my_list:
    print(item)
    
type(my_list)  # <class 'list'>

itertor = iter(my_list)
type(itertor)  # <class 'list_iterator'>
print(next(itertor))  # 1
print(next(itertor))  # 2
print(next(itertor))  # 3
print(next(itertor))  # 4