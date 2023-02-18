
# Use cron to add a new line to a text file every minute

def run():
    file = open(file_path, 'a')
    file.write("another minute has passed\n")
    file.close()  # always close the file after opening it!


if __name__ == '__main__':
    file_path = "/var/tmp/cronjob-result.txt"
    run()
