# def string(list):
#     if list == []:
#         print("No value was entered")
#     else:
#         for i in list:
#             return i
# list = [str(input("Enter a string: "))]
# #list = ['apples', 'bananas', 'tofu', 'cats']
# print(string(list))

# converting list to string using iteration
def listToString(s): 
    s.insert(-1, 'and')
    # initialize an empty string 
    string = "" 
    # traverse in the string 
    for element in s:
        string += element + ' '
    # return string 
    return string
        
        
# Driver code    
s = ['apples', 'bananas', 'tofu', 'cats'] #['Compile ', 'With ', 'Favtutor '] 
    #['apples ', 'bananas ', 'tofu ', 'cats ']

print(','.join(listToString(s)))
        
    
