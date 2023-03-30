import random 

print("Welcome to Word Scramble!\n\n")
print("Try unscrambling these letters to make an english word.\n")

words = [ "apple", "banana", "pear", "apricot", "chocolate", "memory", "random", "dictionary", "scramble", "document", "secret", "unscramble", "package", "code", "python", "javascript"]

for i in range(1,3):
       word = random.choice(words)
       letters = list(word)
       random.shuffle(letters)
       scramble = ''.join(letters)

       print ("Scrambled: %s"  % scramble)
       guess = input("What word is this? ")
       if guess == word: 
         print ("\nThat's right!\n")
       else: 
         print ("\nNo the word was %s\n" % word)