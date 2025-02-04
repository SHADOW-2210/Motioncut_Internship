import random
import string
import os

num = int(input("Number of words to generate: "))

current_directory = os.getcwd()
noun = os.path.join(current_directory, "nouns.txt")
adj = os.path.join(current_directory, "adjectives.txt")
blk = os.path.join(current_directory, "blacklist.txt")
with open(noun, 'r') as infile:
    nouns = infile.read().strip(' \n').split('\n')

with open(adj, 'r') as infile:
    adjectives = infile.read().strip(' \n').split('\n')

with open(blk,'r') as inline:
    censored = inline.read().strip(' \n').split('\n')


    censored = inline.read().strip(' \n').split('\n')


for i in range(num):
    word1 = random.choice(adjectives)
    word2 = random.choice(nouns)
    if word2 in censored:
        i -=1
        continue

    word1 =word1.title()
    word2 =word2.title()
    username = '{}{}{}'.format(word1, word2, random.randint(1, 99))

    print(username)
    with open("username.txt",'a') as inline:
        usedname= inline.write(username + '\n')
