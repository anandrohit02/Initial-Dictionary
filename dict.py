import json
import urllib

while True:
	newword = raw_input('\nEnter Word = ')
	word = newword.lower()
#	print word
	if len(word) < 1 : break
	serviceurl = ('http://api.wordnik.com:80/v4/word.json/%s/definitions?limit=200&includeRelated=true&sourceDictionaries=wiktionary&useCanonical=false&includeTags=false&api_key=a2a73e7b926c924fad7001ca3111acd55af2ffabf50eb4ae5'%word)
#	print serviceurl
	data  = urllib.urlopen(serviceurl).read()
	try:
		js = json.loads(str(data))
#		print js
	except:
		js = None
	if js is None:
		print 'Type Correct Word'
		continue
	print 'Synonym : '
	for lst in js:
		print '* ' , lst['text']
	print '\t\t\t\t\t------End------'

