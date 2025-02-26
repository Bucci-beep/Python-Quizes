'''
Write a while loop to display the values of the Rating of
an album playlist stored in the list PlayListRatings.
If the score is less than 6, exit the loop. 
The list PlayListRatings is given by: PlayListRatings = [10, 9.5, 10, 8, 7.5, 5, 10, 10]'''

PlayListRatings = [10, 9.5, 10, 8, 7.5, 5, 10, 10]
i = 0
while i < len(PlayListRatings):
    if PlayListRatings[i] < 6:
        break
    print(PlayListRatings[i])
    i += 1

'''
Write a while loop to copy the strings 'orange' of the list squares to the list new_squares.   
Stop and exit the loop if the value on the list is not 'orange':
'''
squares = ['orange', 'orange', 'purple', 'blue ', 'orange']
new_squares = []
i = 0
while i < len(squares):
    if squares[i] != 'orange':
        break
    new_squares.append(squares[i])
    i += 1
print(new_squares)

