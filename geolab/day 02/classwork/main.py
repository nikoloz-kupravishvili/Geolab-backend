name = input ("Enter a name: ")
surname = input ("Enter a surname: ")
age = int (input ("Enter an age: ") )

if (name == "giorgi" or name == "dato") and int (age) == 24:
    print ("giorgi")
    if surname == "mamardashvili":
        print ("goalkeeper")
    print ("message 1")
else:
    print ("something else")    