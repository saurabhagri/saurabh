import sys
import re

def format_tags(tags):
    
    #If user pass tag as blank or spaces
    tags.strip()
    if not tags or re.fullmatch(r'\s*',tags):
        return "d"
 
    #Replacing AND, OR, and NOT keywords with the appropriate syntax
    tags = tags.replace(" AND ", "AND")
    tags = tags.replace(" OR ", "OR")
    tags = tags.replace(" NOT ", "NOT")
 
    #Removing all spaces from tags
    formatted_tags = re.sub(r'\s+', '', query)
 
    return formatted_tags
    
if __name__ == "__main__":
    query= "tag1 NOT tag2"
    ret=format_tags(query)
    print(ret)