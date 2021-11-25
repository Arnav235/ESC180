import urllib.request

# Part 1
def word_count(file):
	words = open(file, encoding="latin-1").read().split()
	word_counts = {}
	for word in words:
		if word in word_counts:
			word_counts[word] += 1
		else:
			word_counts[word] = 1
	return word_counts

def top10(L):
	L.sort(reversed=True)
	return L[:10]

def get_top_10_words(file):
	word_counts = word_count(file)
	sorted_words = sorted(list(word_counts.items()), key=lambda x:x[1], reverse=True)
	top_10 = [i[0] for i in sorted_words[:10]]
	return top_10

#print(get_top_10_words("lab9/pride_and_prejudice.txt"))

# Part 3: Getting number of search results on Yahoo!
def get_num_search_terms(search_term):
	search_term_formatted = "+".join(search_term.split())
	f = urllib.request.urlopen("https://ca.search.yahoo.com/search?p={}&fr=yfp-t&fp=1&toggle=1&cop=mss&ei=UTF-8".format(search_term_formatted))
	page = f.read().decode("utf-8")
	f.close()
	idx = page.find("class=\" fz-14 lh-22\">")	
	num_results = page[idx+27:idx+45].split()[0]
	return int(num_results.replace(",", ""))

#print(get_num_search_terms("uoft"))

def choose_variant(variants):
	top_count = 0
	top_phrase = ""
	for var in variants:
		count = get_num_search_terms(urllib.parse.quote(var))
		if count > top_count:
			top_count = count
			top_phrase = var
	return top_phrase

#print(choose_variant(["five-year anniversary", "fifth anniversary"]))
