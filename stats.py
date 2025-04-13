def get_text(filepath):
    file_contents = ""
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def get_num_words(filepath):
    num_words = 0
    with open(filepath) as f:
        file_contents = f.read()
        num_words = len(file_contents.split())
    return num_words

def num_chars(text):
    letter_stats = {}
    for item in text:
        lower_item = item.lower()
        if (lower_item not in letter_stats) and (lower_item.isalpha()):
            letter_stats[lower_item] = 1
        elif (lower_item in letter_stats):
            letter_stats[lower_item] += 1
    return(letter_stats)

def report(filepath):
    d = num_chars(get_text(filepath))
    print(f"""============ BOOKBOT ============
Analyzing book found at {filepath}...
----------- Word Count ----------""")
    print(f"Found {get_num_words(filepath)} total words")
    print("--------- Character Count -------")
    sorted_list_d = sorted(list(d.items()), key=lambda tup: tup[1], reverse=True)
    for item in sorted_list_d:
        print(f"{item[0]}: {item[1]}")
    print("============= END ===============")