

print("This script converts all characters in a message into a spoiler tag on discord. It's a prank!")
message = input("What message would you like to convert into an all spoiler message?" )
##grabs message
splicedMessage = list(message)
#makes message a list to iterate through

newList = []
#creates an empty list for global access

def conversiontospoiler(thing):
    for content in thing:
        newL = "||" + content + "||"
        newList.append(newL)
#list comprehension to iterate through
conversiontospoiler(message)

newMessage=''.join(newList)

print(newMessage)