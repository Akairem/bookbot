def get_num_words(book_text):
    words = book_text.split()
    return len(words)

def get_character_count(book_text):
    characters = {}
    for char in book_text:
        if char.isalpha():
            char = char.lower()
            if char in characters:
                characters[char] += 1
            else:
                characters[char] = 1
    return characters

def sort_character_count(character_counts):
    dict_list = []
    for key,value in character_counts.items():
        dict = {"char": key, "num": value}
        dict_list.append(dict)
    dict_list.sort(key=lambda x: x["num"], reverse=True)
    return dict_list