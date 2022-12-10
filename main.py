import os


def run():
    print("Count word occurrences in a directory tree.")
    print("To understand more about your domain, select /src folder.")
    path = read_path()
    count_words(path)


def read_path():
    absolut_path = input("Enter absolute path: ")
    return absolut_path


def count_words(path):
    for root, dirs, files in os.walk(path):
        print(f"dir_path: {root}")
        print(f"dir_names: {dirs}")
        print(f"file_names: {files}")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    run()
