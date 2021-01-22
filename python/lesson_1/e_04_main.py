# Create a function that prints the age of a person named print_age
# should take the parameter name (of the person)

# flo should return 24
# matthias should return 33
# hannah should return 23
# resi should return 23
# robert should return 24
# jo should return 22

# empty spaces (leading and trailing) should be ignored

def print_age(name):
    # use strip https://www.journaldev.com/23625/python-trim-string-rstrip-lstrip-strip
    name = name.strip()

    if name == "flo" or name == "robert":
        age = 24
    elif name == "hannah" or name == "resi":
        age = 23
    elif name == "matthias":
        age = 33
    elif name == "jo":
        age = 22
    else:
        age = None

    return age

if __name__ == "__main__":
    # run the function
    name = "jo "
    age = print_age(name)
    
    if age == None:
        print(f"I dont know how old {name} is.")
    else:
        # print the result
        # if age != None:
        print(f"{name} is {age} years old")