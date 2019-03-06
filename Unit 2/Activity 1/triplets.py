'''
name: triplets

This program is writen by 希理(Howie Hong)

date: 2019/2/25

purpose: it will generate random triplet poems

libary require: random
'''
import random
nouns = ["dog","horse","cat","frog","goat","eagle","lion","giraffe"]
verbs = ["slept","drank","ate","jumped","raced","ran","tripped","tapped"]
rhyming_nouns = ["house","mouse","grouse","spouse","doghouse","beachhouse","treehouse"]

noun1 = random.choice(nouns)

#remove the items from the list, make sure they will not use again.
verb1 = random.choice(verbs)
verbs.remove(verb1)

verb2 = random.choice(verbs)


rhyming_noun1 = random.choice(rhyming_nouns)
rhyming_nouns.remove(rhyming_noun1)

rhyming_noun2 = random.choice(rhyming_nouns)
rhyming_nouns.remove(rhyming_noun2)

rhyming_noun3 = random.choice(rhyming_nouns)


print("The " + noun1 + " " + verb1 + " a " + rhyming_noun1)
print("And then " + verb2 + " it in the " + rhyming_noun2)
print("But it was a " +rhyming_noun3)

