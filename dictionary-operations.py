# Find the value for the key 'a':
D={'a':0,'b':1,'c':2}
print(D['a'])

# Find the keys of the dictionary D:
print(D.keys())

# In the dictionary soundtrack_dic what are the keys?
soundtrack_dic = {"The Bodyguard":"1992", "Saturday Night Fever":"1977"}
print(soundtrack_dic.keys())

# In the dictionary soundtrack_dic what are the values?
print(soundtrack_dic.values())

'''
The Albums Back in Black, The Bodyguard and Thriller have the following music recording sales in millions 50, 50 and 65 respectively:

a) Create a dictionary album_sales_dict where the keys are the album name and the sales in millions are the values.'''
album_sales_dict = {"Back in Black":50000000, "The Bodyguard":50000000, "Thriller":65000000}
print(album_sales_dict)

'''
b) Use the dictionary to find the total sales of Thriller:
'''
print(album_sales_dict["Thriller"])

'''
c) Find the names of the albums from the dictionary using the method keys:
'''
print(album_sales_dict.keys())

'''
d) Find the names of the recording sales from the dictionary using the method values:
'''
print(album_sales_dict.values())

# Create an empty dictionary for managing and tracking inventory in a retail store.
inventory = {}

''' Store the first product details in variable
Product Name= Mobile phone
Product Quantity= 5
Product price= 20000
Product Release Year= 2020'''

product_1 = {"Product Name":"Mobile phone", "Product Quantity":5, "Product Price":20000, "Product Release Year":2020}

# Add the product to the inventory dictionary
inventory["Product 1"] = product_1


''' Store the second product details in variable
Product Name= Laptop
Product Quantity= 10
Product price= 50000
Product Release Year= 2021'''

product_2 = {"Product Name":"Laptop", "Product Quantity":10, "Product Price":50000, "Product Release Year":2021}

# Add the product to the inventory dictionary
inventory["Product 2"] = product_2

# Print the inventory dictionary
print(inventory)


Dict={"A":1,"B":"2","C":[3,3,3],"D":(4,4,4),'E':5,'F':6}
print(Dict["D"])
