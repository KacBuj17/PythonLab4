
def open_file(path, text):
    with open(path, 'w') as opened_file:
        opened_file.write(text)

if __name__ == "__main__":
    path_to_file = "text.txt"
    text_to_save = input("Input text to save: ")

    open_file(path_to_file, text_to_save)