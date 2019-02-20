'''
name: question_2

This program is writen by 希理(Howie Hong)

date: 2019/2/20

purpose: None

libary require: None
'''

'''
a.

def replace(old, new, count)
Return a copy with all occurrences of substring old replaced by new.

  count  
    Maximum number of occurrences to replace.  
    -1 (the default value) means replace all occurrences.  
If the optional argument count is given, only the first count occurrences are replaced.
'''
print('aaaaaaabbbbbbbb'.replace('a','c'))
print('aaaaaaabbbbbbbb'.replace('a','c',2))

'''
b.
def split(sep, maxsplit)
Return a list of the words in the string, using sep as the delimiter string.

sep

  The delimiter according which to split the string.  
  None (the default value) means split according to any whitespace,  
  and discard empty strings from the result.  
maxsplit

  Maximum number of splits to do.  
  -1 (the default value) means no limit.

'''
'aa aaa aaaabbb'.split()
'aa aaa aaaabbb'.split(' ')
'aa aaa aaaabbb'.split('a')