mydict = {'carl':40,
          'alan':2,
          'bob':1,
          'danny':3}

# by key

for key in sorted(mydict):
    print "%s: %s" % (key, mydict[key])
print

for key in sorted(mydict.iterkeys()):
    print "%s: %s" % (key, mydict[key])
print

for key, value in sorted(mydict.iteritems(), key= lambda x: x):
	print "%s: %s" % (key, value)
print

for key, value in sorted(mydict.iteritems(), key= lambda (k, v): (k, v)):
	print "%s: %s" % (key, value)
print

for key, value in sorted(mydict.iteritems(), key= lambda x: x[0]):
	print "%s: %s" % (key, value)
print

for key, value in sorted(mydict.iteritems(), key= lambda (k, v): k):
	print "%s: %s" % (key, value)
print
print

# by value

for key, value in sorted(mydict.iteritems(), key= lambda x: x[::-1]):
	print "%s: %s" % (key, value)
print

for key, value in sorted(mydict.iteritems(), key= lambda x: tuple(reversed(x))):
	print "%s: %s" % (key, value)
print

for key, value in sorted(mydict.iteritems(), key= lambda (k, v): (v, k)):
	print "%s: %s" % (key, value)
print

for key, value in sorted(mydict.iteritems(), key= lambda x: x[1]):
	print "%s: %s" % (key, value)
print

for key, value in sorted(mydict.iteritems(), key= lambda (k, v): v):
	print "%s: %s" % (key, value)
print
