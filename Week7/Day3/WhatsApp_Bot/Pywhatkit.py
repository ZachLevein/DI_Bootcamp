import pywhatkit as py

# Schedule Whatsapp messaged
# py.sendwhatmsg("+17865581090", "hello", 15, 29, 32)

# print("Message sent")
# Search google 
def search_google(user_inpt):        
    try:
        py.search(user_inpt)
        print("Succesfully Searched")
    except Exception as e: 
        print("Search Error:", e)
search_google('Hello')

# Info- returns information about a topic from WIKI
def search_wiki(user_inpt):
    try:
        search_info = py.info(user_inpt, lines= 1)
        print("Succesfully Searched")
        return search_info
    except Exception as e: 
        print("Search Error:", e)
search_wiki('ancient_greece')