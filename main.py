import os


def run():
    print_welcome()
    path = read_path()
    print(path)
    names = collect_names(path)
    count_occurrences_in_classes(path, names)
    remove_unique_occurences(names)
    print()
    page = generate_html(names)
    print("Copy the below code into a _.html file:")
    print(page)


def print_welcome():
    print()
    print("Count word occurrences in a directory tree.")
    print("To learn more about your domain in a Kotlin project, select project/src/main/kotlin")
    print()


def read_path():
    absolut_path = input("Enter absolute path: ")
    return absolut_path if absolut_path != "" else test_path


# Collect all class names
def collect_names(path):
    names = {}
    for root, dirs, files in os.walk(path):
        for filename in files:
            class_name_without_filetype = filename.rsplit(".")[0]
            names[class_name_without_filetype] = 0
    return names


# Count all mentions of a class
def count_occurrences_in_classes(path, words):
    for root, dirs, files in os.walk(path):
        for filename in files:
            absolut_file_path = os.path.join(root, filename)

            with open(absolut_file_path) as file:
                count_words(words, file.readlines())


def count_words(words, lines):
    for line in lines:
        word_list = line.split(" ")
        for word in word_list:
            if word in words:
                count = words[word] + 1
                words[word] = count


# Sanitize output
def remove_unique_occurences(names):
    base_dict = dict(names)
    for key in base_dict.keys():
        if names[key] <= 1:
            del names[key]


# Create fancy looking HTML representation
def generate_html(words):
    page = ""
    page += f"<html><head><title>word bubbles</title></head><body style=\"background: #242424; color: #d9d9d9\">"

    for word in words.keys():
        word_bubble = f"<div style=\"float:left;font-size:{words[word]}0pt;padding:10px;\">{word}</div>"
        page += word_bubble

    page += "</body></html>"
    return page


if __name__ == '__main__':
    # set default path during development
    test_path = ""
    run()