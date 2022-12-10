import os


def run():
    print("Count word occurrences in a directory tree.")
    print("To learn more about your domain in a Kotlin project, select project/src/main/kotlin")
    path = read_path()
    count_words(path)


def read_path():
    absolut_path = input("Enter absolute path: ")
    return absolut_path if absolut_path != "" else test_path


def filter_declarations(line):
    words = line.split()

    if words.length > 0:
        first_word = words[0]
        match first_word:
            case "package":
                return ""
            case "import":
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
                print(f"filtered list: {filtered_list}")


        print("-----------------------")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    test_path = "/Users/nykon/Development/ecommerce-bay/backend/src/main/kotlin"
    run()

