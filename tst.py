# coding=utf-8
class TST:
    def __init__(self):
        self.size = 0
        self.root = None

    def __len__(self):
        return self.size

    # Looking for the word in TST
    def find(self, word):
        if word[-1] != "\0": word += "\0"
        cur_node, pre_node = self.root, self.root
        word_i, find_w = 0, False
        while cur_node != None:                  # The root node has not been queried yet, and the query can continue
            if word[word_i] < cur_node.label:    # Query to the left node
                pre_node = cur_node
                cur_node = cur_node.left
            elif word[word_i] > cur_node.label:  # Query to the right node
                pre_node = cur_node
                cur_node = cur_node.right
            else:                           # word[word_i] was found in TST
                if word_i < len(word) - 1:  # Continue to find word[word_i + 1]
                    pre_node = cur_node
                    cur_node = cur_node.mid
                    word_i += 1
                else:                       # The whole word has been found
                    find_w = True
                    break
        return find_w, word_i, pre_node
    
    # Get the suggestion, if the word is error
    def suggestion(self, word, num = 10):
        _, word_i, pre_node = self.find(word)
        pre_word = word[: word_i]
        des =  self.descendants(pre_word, pre_node)
        suggestion = []
        for i, des_this in enumerate(des):
            if i < num:
                suggestion.append(des_this)
        return suggestion
    
    # Get the descendants of the pre_word
    def descendants(self, pre_word, pre_node):
        if pre_node != None:
            if pre_node.label == '\0':
                yield pre_word
            else:
                yield from self.descendants(pre_word + pre_node.label, pre_node.mid)
                yield from self.descendants(pre_word, pre_node.left)
                yield from self.descendants(pre_word, pre_node.right)
    

    def insert(self, word):
        word += '\0'
        prev = self.root
        word_i = 0                                 # The index of the word being processed
        if prev == None:                           # TST is empty
            cur_node = self.TST_node(word[0])      # Create the root
            self.root = cur_node
            word_i = 1
        else:                                      # TST is not empty
            # Looking for the word in TST
            find_w, word_i, pre_node = self.find(word) 
            if find_w == False:                    # Could not find the word in TST, But found the word[:word_i]
                cur_node = self.TST_node(word[word_i]) # Create the node which label is word[word_i]
                if word[word_i] < pre_node.label:      # insert to left
                    pre_node.left = cur_node
                elif word[word_i] > pre_node.label:    # insert to right
                    pre_node.right = cur_node
                else:
                    print("ERROR")
                    exit(0)
                word_i += 1
        while word_i < len(word):                  # insert the word[word_i + 1:] to the middle node one by one
            cur_node.mid = self.TST_node(word[word_i])
            cur_node = cur_node.mid
            word_i += 1
        # Updata the size of TST
        self.size += 1
        return self.size
        

    def __str__(self):
        s = []
        def _str(n, acc, lvl, direction):
            prepend = lvl * "  "
            if n is None:
                if direction == "-":
                    s.append(prepend + ">> {"+acc+"}")
                return

            s.append(prepend + direction + " " + n.label)
            _str(n.right, acc, lvl + 1, "/")
            _str(n.mid, acc + n.label, lvl + 1, "-")
            _str(n.left, acc, lvl + 1, "\\")


        _str(self.root, "", 0, "-")

        return "\n".join(s).replace('\0', '$')
    
    # The node of TST
    class TST_node:
        def __init__(self, label):
            self.label = label
            self.left = None
            self.mid = None
            self.right = None
        
        def __str__(self):
            return self.label