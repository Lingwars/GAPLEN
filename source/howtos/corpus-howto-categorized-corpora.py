from nltk.corpus import brown, movie_reviews, reuters
print(brown.categories()) # doctest: +NORMALIZE_WHITESPACE
print(movie_reviews.categories())
print(reuters.categories()) # doctest: +NORMALIZE_WHITESPACE +ELLIPSIS
print(brown.categories('ca01'))
print(brown.categories(['ca01','cb01']))
print(reuters.categories('training/9865'))
print(reuters.categories(['training/9865', 'training/9880']))
print(reuters.fileids('barley')) # doctest: +ELLIPSIS
print(brown.tagged_words(categories='news'))
print(brown.sents(categories=['editorial','reviews'])) # doctest: +NORMALIZE_WHITESPACE

