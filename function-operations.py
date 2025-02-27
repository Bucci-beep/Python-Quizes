def add1(a):
    b = a + 1
    return b
print(add1(5))
c = add1(7)
print(c)
d = add1(9)
print(d)


def sum(x, y):
    return x + y
print(sum(2, 5))
print(sum(3, 9))

def printStuff(Stuff):
    for i,s in enumerate(Stuff):
        print("Album", i, "Rating is", s)
album_ratings = [10.0, 8.5, 9.5]
printStuff(album_ratings) 

# Example of global variable

myFavouriteBand = "AC/DC"

def getBandRating(bandname):
    if bandname == myFavouriteBand:
        return 10.0
    else:
        return 0.0

print("AC/DC's rating is:", getBandRating("AC/DC"))
print("Deep Purple's rating is:",getBandRating("Deep Purple"))
print("My favourite band is:", myFavouriteBand)

'''Write a function code to find total count of word little in the given
string: "Mary had a little lamb Little lamb, little lamb Mary had a little lamb.
Its fleece was white as snow And everywhere that Mary went Mary went, 
Mary went Everywhere that Mary went The lamb was sure to go"'''

def countLittle(string):
    return string.lower().count("little")

string = "Mary had a little lamb Little lamb, little lamb Mary had a little lamb. Its fleece was white as snow And everywhere that Mary went Mary went, Mary went Everywhere that Mary went The lamb was sure to go"
print("The frequency of the word Little is:",countLittle(string))
