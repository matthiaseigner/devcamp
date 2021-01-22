# Create a function that prints the age of following persons
# jo
# flo
# matthias
# with a for loop

def get_age(name):
    data = {
        "flo": 24,
        "robert": 24,
        "hannah": 24,
        "resi": 24,
        "matthias": 33,
        "jo": 22,
    }
    # use strip https://www.journaldev.com/23625/python-trim-string-rstrip-lstrip-strip
    name = name.strip()
    # use lower https://www.programiz.com/python-programming/methods/string/lower
    name = name.lower()

    if name in data:
        return data[name]
    else: 
        return None

if __name__ == "__main__":
    
    # print age of jo
    # print age of flo
    # print age of matthias
    # in schleife
    names = ["jo", "flo", "matthias"]
    
    for name in names:
        age = get_age(name)
        if age == None: 
            print(f"I dont know how old {name} is.")
        else: 
            print(f"{name} is {age} years old")
