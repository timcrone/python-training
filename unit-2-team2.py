print("Hello world!")
#‘ddboost storage-unit create “X” user sysadmin‘
#Naming conventions for creating storage units include
# upper case and lower case letters-A-Z and
# a-z, numbers 0-9, embedded space, comma, period,
# exclamation mark, hash mark, dollar sign, percent sign,
# plus sign, at sign, equal sign, ampersand, semi colon,
# caret, tilde, left and right parentheses, left and
# right brackets, left and right braces.

uppercase=list(map(chr,list(range(ord('A'),ord('Z')+1))))
lowercase=list(map(chr,list(range(ord('a'),ord('z')+1))))
symbols=list(",.!#$%+@=&;^~()[]{}")
space=["d d"]
numbers=list(range(0,10))
everything = uppercase + symbols + space + lowercase + numbers

list(map(lambda x: print('ddboost storage-unit create "' + str(x) + '" user sysadmin'), concatenated))

for i in everything:
    print("ddboost storage-unit create \""+str(i)+"\" user sysadmin")

"""
ddboost storage-unit create "A" user sysadmin
ddboost storage-unit create "B" user sysadmin
ddboost storage-unit create "C" user sysadmin
...
"""
