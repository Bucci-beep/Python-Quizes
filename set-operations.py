# Cast a List to a Set 
# Cast the following list to a set:
['A','B','C','A','B','C']
set_1 = set(['A','B','C'])
print(set_1)

'''
Add an Element to the Set
Add the string 'D' to the set S.
'''
S = {'A','B','C'}
S.add('D')  
print(S)

'''
Intersection of Sets
Find the intersection of set A and B
'''
A = {1,2,3,4,5}
B = {1,3,9, 12}
C = A & B
print(C)

'''
Convert the list ['rap','house','electronic music', 'rap'] to a set:
'''
list_1 = ['rap','house','electronic music', 'rap']
set_2 = set(list_1)
print(set_2)

'''
Consider the list A = [1, 2, 2, 1] and set B = set([1, 2, 2, 1]), does sum(A) = sum(B)
'''
A = [1, 2, 2, 1]
B = set([1, 2, 2, 1])
print(sum(A))
print(sum(B))

''' 
Create a new set album_set3 that is the union of album_set1 and album_set2:
'''
album_set1 = set(["Thriller", 'AC/DC', 'Back in Black'])
album_set2 = set([ "AC/DC", "Back in Black", "The Dark Side of the Moon"])
album_set3 = album_set1.union(album_set2)
print(album_set3)

