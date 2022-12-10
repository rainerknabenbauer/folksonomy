import os


def run():
    print("Count word occurrences in a directory tree.")
    print("To learn more about your domain in a Kotlin project, select project/src/main/kotlin")
    path = read_path()
    names = collect_names(path)
    print(names)
    # count_words(path)


def collect_names(path):
    names = set()
    for root, dirs, files in os.walk(path):
        for filename in files:
            names.add(filename.rsplit(".")[0])
    return names


def read_path():
    absolut_path = input("Enter absolute path: ")
    return absolut_path if absolut_path != "" else test_path


def filter_declarations(line):
    words = line.split()

    # gather all class names that start with .kt
    # create set [word, count]
    # count every occurrence
    #   Maybe at the end: model, entity, .. ? combine

    if len(words) > 0:
        first_word = words[0]
        match first_word:
            case "package":
                return ""
            case "import":
                return ""
        match first_word[:1]:
            case "@":
                return ""
    return line


def count_words(path):
    for root, dirs, files in os.walk(path):
        for filename in files:
            print(f"dir_path: {root}")
            print(f"dir_names: {dirs}")
            print(f"file_names: {files}")

            absolut_file_path = os.path.join(root, filename)
            print(absolut_file_path)

            with open(absolut_file_path) as file:
                filtered_list = filter(filter_declarations, file.readlines())
                print(f"filtered list:")
                print(*filtered_list, "\n")

        print("-----------------------")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    test_path = "/Users/nykon/Development/ecommerce-bay/backend/src/main/kotlin"
    run()

