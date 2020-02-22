

if __name__ == "__main__":
    print ("ada lovelace".title())
    print ("ada lovelace".upper())
    print ("ada lovelace".lower())

    first_name = "ada"
    last_name = "lovelace"

    full_name = f"{first_name} {last_name}"
    print(full_name)
    print(f"Hello, {full_name.title()}")

    #reset full name 
    full_name = "{} {}".format(first_name, last_name)
    print("Hello new , {}".format(full_name.title()))

    print (0.2 + 0.1) #--> 0.30000000000000004 weird answer
    print (0.2 * 0.1) # --> 0.020000000000000004 weird answer

    print (1_0000_0000)

    

    