#!/usr/bin/env python 

# author: Nancy Yang 
# email : maxbearwiz@gmail.com 
# 
# This script solves the problem of guessing the possible
# permutation of words user can key when typing on their
# cell phone keypad. 
# Once input string is greater than 4 the script runs very 
# slow.
# The function decides whether guessed word is valid is
# a random number genrerator. 

import random

NEARBY_CHARS={
   'a': ['q', 's', 'z'],\
   'b': ['v', 'h', 'n'],\
   'c': ['x', 'f', 'v'],\
   'd': ['e', 'f', 's', 'x'],\
   'e': ['w', 'r', 's', 'd'],\
   'f': ['r', 'c', 'd', 'g'],\
   'g': ['f', 'h', 't', 'v'],\
   'h': ['g', 'j', 'y', 'b'],\
   'i': ['u', 'o', 'j', 'k'],\
   'j': ['u', 'h', 'k', 'n'],\
   'k': ['i', 'j', 'l', 'm'],\
   'l': ['o', 'p', 'k'],\
   'm': ['n', 'j', 'k'],\
   'n': ['b', 'j', 'm'],\
   'o': ['i', 'p', 'k', 'l'],\
   'p': ['o', 'l'],\
   'q': ['w', 'a'],\
   's': ['w', 'a','d', 'z'],\
   't': ['r', 'y', 'f', 'g'],\
   'u': ['y', 'i', 'h', 'j'],\
   'v': ['c', 'g', 'b'],\
   'w': ['q', 'a', 's', 'e'],\
   'x': ['z', 'd', 'c'],\
   'y': ['t', 'u', 'g', 'h'],\
   'z': ['a', 's', 'd', 'x'],\
}

def get_nearby_chars(char):
   return NEARBY_CHARS[char] 

def is_word(word): 
   res = random.choice([True, False])
   #print res
   return res

def nearby_words(prefix, word, res):
   if not word:
      if not prefix in res:
         print prefix
         res.append(prefix)
      return 
   else: 
      nearby_chars = get_nearby_chars(word[0]) 
      nearby_chars.insert(0, word[0])
      for c in nearby_chars:  
         tmp = '%s%s' % (prefix, c)
         nearby_words(tmp, word[1:], res)  

def gen_nearby_words(prefix, word):
   if not word: 
      yield prefix
   else:
      nearby_chars = get_nearby_chars(word[0]) 
      nearby_chars.insert(0, word[0])
      for c in nearby_chars:  
         tmp = '%s%s' % (prefix, c)
         for x in gen_nearby_words(tmp, word[1:]):
            yield x 

if __name__=="__main__":

  # recursive solution
  res = []
  nearby_words('', 'abcde', res)
  for word in res:
    x = is_word(word)
     if x:
        print '[x] %s' % word
     else:
        print '[-] %s' % word

  # recursive solution with generator
  g = gen_nearby_words('', 'ge') 
  for v in g:
     print v
