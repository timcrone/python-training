# upper case and lower case letters - A - Z and a - z, numbers
# 0 - 9, embedded space, comma, period, exclamation mark, hash
# mark, dollar sign, percent sign, plus sign, at sign, equal
# sign, ampersand, semicolon, caret, tilde, left and right
# parentheses, left and right brackets, left and right
# braces.

# ddboost storage-unit create "X" user sysadmin

print("Hello world")
capitals = list(map(chr,list(range(ord('A'),ord('Z')+1))))
lowers = list(map(chr,list(range(ord('a'),ord('z')+1))))
chars = list(",.!#$%+@=&;^~()[]{}")
space = ["d d"]
numbers = list(range(0,10))
concatenated = capitals + lowers + chars + space + numbers

list(map(lambda x: print('ddboost storage-unit create "' + str(x) + '" user sysadmin'), concatenated))
for i in concatenated:
    print("ddboost storage-unit create \""+str(i)+"\" user sysadmin")
