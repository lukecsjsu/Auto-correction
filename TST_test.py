def init(dict_path):
    # Create the TST
    t = TST()
    # Read the dict from thie given file
    f = open(dict_path, "r")
    line = f.readline().strip()
#     line = line.split(" ")[0]
    words = []
    while line != "":
        words.append(line)
        line = f.readline()
        line = line.split(" ")[0]
    f.close()
    
    # Write to the TST
    for w in words:
        t.insert(w)
        find_w, _, _ = t.find(w)
        assert find_w == True
    return t

# Test
if __name__ == "__main__":
    # Initialize
    print("Now initialize, please wait a minite")
    t = init(dict_path = "dict_orginal.txt")
    print("Initialization completed")
    # Enter
    res = input("Please enter a word (enter empty words to exit by default):")
    while res != "":
        res = res.strip()
        # Check whether res exists in TST
        find_w, _, _ = t.find(res)
        if find_w == True:                                  # Exist
            print(res + " ——no spelling errors")
        else:
            suggestion = t.suggestion(word = res, num = 10) # Find up to 10 recommended words
            print(res + " ——misspelled, it is recommended to change to the following words:")
            for su in suggestion:
                print(su)
        res = input("Please enter a word (enter empty words to exit by default):")
    print("Exit")