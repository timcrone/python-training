#‘ddboost storage-unit create “X” user sysadmin‘
#Naming conventions for creating storage units include
# upper case and lower case letters-A-Z and
# a-z, numbers 0-9, embedded space, comma, period,
# exclamation mark, hash mark, dollar sign, percent sign,
# plus sign, at sign, equal sign, ampersand, semi colon,
# caret, tilde, left and right parentheses, left and
# right brackets, left and right braces.

# Valid characters:
capitals = list(map(chr,range(ord('A'),ord('Z')+1))) # Upper and
lowers = list(map(chr,range(ord('a'),ord('z')+1))) # lower case letters A-Z and a-z,
numerals = list(range(0,10)) # numbers 0-9,

# embedded space,
space = ["d d"]

# comma, period, exclamation mark, hash mark, dollar sign, percent sign, plus sign, at sign, equal sign,
# ampersand, semi colon, caret, tilde, left and right parentheses, left and right brackets, left and right braces
symbols = list(",.!#$%+@=&;^~()[]{}")

everything = capitals + lowers + numerals + space + symbols

list(map(lambda x: print('ddboost storage-unit create "' + str(x) + '" user sysadmin'), everything))
list(map(lambda x: print('ddboost storage-unit delete "' + str(x) + '"\ny'), everything))
