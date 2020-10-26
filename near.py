import itertools
def nearto(start_word,end_word, letter_to_remove):
    word = list(start_word)
 
    letter_pos = word.index(letter_to_remove)
    del(word[letter_pos])
   
    start_word = "".join(word)
    if start_word == end_word:
        return True
    else:
        return False

start_word = input("Input the first word:")
end_word = input("Input the word you want to make:")
letter_to_remove = input("Input the letter to remove:")

true_false = nearto(start_word,end_word,letter_to_remove)

print(true_false)
