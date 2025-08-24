def get_book_text(file_name='books/frankenstein.txt'):
    with open(file_name) as f :
        content = f.read()
    return content

def get_word_count(file_name='books/frankenstein.txt'):
    content = get_book_text(file_name)
    return len(content.split())

def get_char_count(content):
    result  = {}
    for i in content:
        result[i.lower()] = result.get(i.lower(), 0) + 1
    return result

def sort_on(items):
    return items["num"]

def generate_new_dict(char_dict):
    new_dict = []
    for key, value in char_dict.items():
        new_dict.append({"char": key, "num": value})
    new_dict.sort(reverse=True, key=sort_on)
    return new_dict
