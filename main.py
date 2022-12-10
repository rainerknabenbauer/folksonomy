import os


def run():
    print("Count word occurrences in a directory tree.")
    print("To learn more about your domain in a Kotlin project, select project/src/main/kotlin")
    path = read_path()
    names = collect_names(path)
    count_occurrences_in_classes(path, names)
    print(names)


def read_path():
    absolut_path = input("Enter absolute path: ")
    return absolut_path if absolut_path != "" else test_path


# Stage 1: Collect all class names


def collect_names(path):
    names = {}
    for root, dirs, files in os.walk(path):
        for filename in files:
            class_name_without_filetype = filename.rsplit(".")[0]
            names[class_name_without_filetype] = 1
    return names


# Stage 2: Count all mentions of a class


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


if __name__ == '__main__':
    test_path = "/Users/nykon/Development/ecommerce-bay/backend/src/main/kotlin"
    run()

