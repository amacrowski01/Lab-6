#the author's names are Allison Macrowski and Abigail Lopez
textstring="Insert message here"
def too_long():
    if len(textstring)>140:
        print("String is too long")
    else:
        print(textstring)

too_long()

import unicodedata
print(unicodedata.name("&"))
print(unicodedata.name("["))
print(unicodedata.name("/"))


        
        
