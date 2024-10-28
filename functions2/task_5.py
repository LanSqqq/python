

def sort_words(input_string):
    return sorted(input_string.split(), key=lambda x: (len(x), x.lower()))

