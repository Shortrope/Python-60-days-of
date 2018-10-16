
def spin_words(sentence):
    return " ".join([w[::-1] if len(w) >= 5 else w for w in sentence.split()])

s = "This is a hello world"
print(spin_words(s))

s = "CCNP BCMSN The Official Exam Cert Guide"
print(spin_words(s))

s = "The best classic shell scripting book"
print(spin_words(s))

#-----------------------------------------------------------
#def spin_words(sentence):
#    new_sentence = [] 
#    for word in sentence.split():
#        if len(word) >= 5:
#            word = (word[::-1])
#        new_sentence.append(word)
#
#    return " ".join(new_sentence)