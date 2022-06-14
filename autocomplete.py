


class Trie(object):
    #create the prefix tree and a function to easily insert words
    def __init__(self):
        self.child = {}
    def insert(self, word):
        current = self.child
        for letter in word:
            if letter not in current:
                current[letter] = {}
                
            current = current[letter]
            
        current['#'] = 1
        
def auto(self, prefix):
    #create a nested dictionary of relevant word endings that may apply to the input.
    current = dict(self.child)
    curry = current['$']
    for x in prefix[1:]:
        curry = curry.get(x, {})

    return curry
def words(tree):
    #perform a depth first search on the dictionary
    #read letters in the nested dictionaries in the order that yields words
    preds = []
    for key, val in tree.items():
        if key == '&':
            preds.append(key)
            continue
        for x in words(val):
            preds.append(key+x)
    return preds

def startstop(word):
    #pad the input with a start symbol '$' and an end symbol '&'
    realword = "$"
    for letter in word:
        realword+= letter
        
    realword+="&"
    return realword

if __name__ == "__main__":
    #__main()
    obj = Trie()

    #You may need to switch out this line for the path to the data on your computer
    f = open(r'/Volumes/Seagate Expansion Drive/Yola/vocab')
    hatbox = f.read()
    hat = {}
    lines = hatbox.split("\n")
    for line in lines:
        hatlist = line.split("\t")
        if len(hatlist) > 1:
            hat[hatlist[0]] = hatlist[1]
    
    import operator
    elevens = {}
    tens = {}
    nines = {}
    eights = {}
    sevens = {}
    sixes = {}
    fives = {}
    fours = {}
    threes = {}
    twos = {}
    ones = {}
    for key in hat:
        if len(str(hat[key])) == 11:
            elevens[key] = int(hat[key])
        elif len(str(hat[key])) == 10:
            tens[key] = int(hat[key])
        elif len(str(hat[key])) == 9:
            nines[key] = int(hat[key])
        elif len(str(hat[key])) == 8:
            eights[key] = int(hat[key])
        elif len(str(hat[key])) == 7:
            sevens[key] = int(hat[key])
        elif len(str(hat[key])) == 6:
            sixes[key] = int(hat[key])
        elif len(str(hat[key])) == 5:
            fives[key] = int(hat[key])
        elif len(str(hat[key])) == 4:
            fours[key] = int(hat[key])
        elif len(str(hat[key])) == 3:
            threes[key] = int(hat[key])
        elif len(str(hat[key])) == 2:
            twos[key] = int(hat[key])
        elif len(str(hat[key])) == 1:
            ones[key] = int(hat[key])
    i = 0
    while i < len(elevens):
        new_ma_val = max(elevens, key = elevens.get)
        new_ma_val = startstop(new_ma_val)
        obj.insert(new_ma_val)
        new_ma_val = new_ma_val[1:len(new_ma_val) -1]
        elevens[new_ma_val] = 0
        i+=1
    i = 0
    while i < len(tens):
        new_ma_val = max(tens, key = tens.get)
        new_ma_val = startstop(new_ma_val)
        obj.insert(new_ma_val)
        new_ma_val = new_ma_val[1:len(new_ma_val)-1]
        tens[new_ma_val] = 0
        i+=1
    i = 0
    while i < len(nines):
        new_ma_val = max(nines, key = nines.get)
        new_ma_val = startstop(new_ma_val)
        obj.insert(new_ma_val)
        new_ma_val = new_ma_val[1:len(new_ma_val) -1]
        nines[new_ma_val] = 0
        i+=1
    i = 0
    print("wait")
    while i < len(eights):
        new_ma_val = max(eights, key = eights.get)
        new_ma_val = startstop(new_ma_val)
        obj.insert(new_ma_val)
        new_ma_val = new_ma_val[1:len(new_ma_val) -1]
        eights[new_ma_val] = 0
        i+=1
    i = 0
    while i < len(sevens):
        new_ma_val = max(sevens, key = sevens.get)
        new_ma_val = startstop(new_ma_val)
        obj.insert(new_ma_val)
        new_ma_val = new_ma_val[1:len(new_ma_val) -1]
        sevens[new_ma_val] = 0
        i+=1
    i = 0
    while i < len(sixes):
        new_ma_val = max(sixes, key = sixes.get)
        new_ma_val = startstop(new_ma_val)
        obj.insert(new_ma_val)
        new_ma_val = new_ma_val[1:len(new_ma_val) -1]
        sixes[new_ma_val] = 0
        i+=1
    i = 0
    print("almost")
    while i < len(fives):
        new_ma_val = max(fives, key = fives.get)
        new_ma_val = startstop(new_ma_val)
        obj.insert(new_ma_val)
        new_ma_val = new_ma_val[1:len(new_ma_val) -1]
        fives[new_ma_val] = 0
        i+=1
    i = 0
    print(fives)
    while i < len(fours):
        new_ma_val = max(fours, key = fours.get)
        new_ma_val = startstop(new_ma_val)
        obj.insert(new_ma_val)
        new_ma_val = new_ma_val[1:len(new_ma_val) -1]
        fours[new_ma_val] = 0
        i+=1
    i = 0
    print(fours)
    while i < len(threes):
        new_ma_val = max(threes, key = threes.get)
        new_ma_val = startstop(new_ma_val)
        obj.insert(new_ma_val)
        new_ma_val = new_ma_val[1:len(new_ma_val) -1]
        threes[new_ma_val] = 0
        i+=1
    i = 0
    print("almost again..")
    while i < len(twos):
        new_ma_val = max(twos, key = twos.get)
        new_ma_val = startstop(new_ma_val)
        obj.insert(new_ma_val)
        new_ma_val = new_ma_val[1:len(new_ma_val) -1]
        twos[new_ma_val] = 0
        i+=1
    i = 0
    print("almost again..")
    while i < len(ones):
        new_ma_val = max(ones, key = ones.get)
        new_ma_val = startstop(new_ma_val)
        obj.insert(new_ma_val)
        new_ma_val = new_ma_val[1:len(new_ma_val) -1]
        ones[new_ma_val] = 0
        i+=1


    
    wordy = input("word please ")
    wordy.lower()
    wordlist = wordy.split(" ")
    goffe = ""
    tabcount = 0
    for wordy in wordlist:
        current = obj.child
        curry = current['$']
        for x in wordy:
            curry = curry.get(x, {})
        #remove unsightly nonletter/number characters from the output and add spaces between words.
        for char in str(words(curry)):
            if char in "abcdefghijklmnopqrstuvwxyz0123456789":
                goffe+=char
            elif char == "&":
                goffe+= "\t"
                tabcount+=1
            #only display the 5 most likely words instead of all possible matches.
            if tabcount > 5:
                continue
        print(goffe)
        goffe = ""
        
        



