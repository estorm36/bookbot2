

def get_num_words(book_text):
    num_words = book_text.split()
    num_count = 0
    for word in num_words:
        num_count += 1
    return num_count

def letter_count(book_text):
    lower_letters = book_text.lower()
    new_dict = {}
    count = 1
    for letter in lower_letters:
        if letter in new_dict:
            this_count = new_dict.get(letter)
            new_dict[letter] = this_count + 1    
        if letter not in new_dict:
            new_dict[letter] = count
    return new_dict

def dict_to_list(letter_count_dict):
    list_of_dicts = []
    for key, value in letter_count_dict.items():
        list_of_dicts.append({"char": key, "num": value})
    list_of_dicts.sort(key=lambda d: d["num"], reverse=True)
    return list_of_dicts



