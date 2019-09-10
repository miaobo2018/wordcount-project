from django.http import HttpResponse
from django.shortcuts import render
import operator

def homepage(request):
	return render(request, 'home.html')

def count(request):
	fulltext = request.GET['fulltext']

	wordlist = fulltext.split()

	worddictionary = {}

	for word in wordlist:
		if word not in worddictionary:
			worddictionary[word] = 0
		worddictionary[word] += 1

	sortedwords = sorted(worddictionary.items(), key=operator.itemgetter(1), reverse=True)

	return render(request, 'count.html', {'fulltext':fulltext,'count':len(wordlist),'sortedwords':sortedwords})

# challenge
def profile(request):
	username = request.GET['username']

	return render(request, 'profile.html', {'username':username})