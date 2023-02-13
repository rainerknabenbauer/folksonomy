import json
import requests


def run():   # See how clean my run() is? Always try to keep run() clean
    print_welcome()
    performance_report = query_performance()    # see below on how to do 'return' values
    create_report(performance_report)

# see how the order in run() reflects the order you find the methods() below? Easy to read : )


def print_welcome():   # it's always a good idea to tell people how your application works
    print("Create your performance reports with ease.")
    print("Please enter the domain in a format like www.dental21.de")
    # I skip asking for input, this is just an example on how to write well structured software : )


def query_performance():
    web_response = requests.get(url)
    return json.loads(web_response.content)  # with return you specify what should come out of the function


def create_report(report):                   # Parameters go into the method
    print("lighthouse fetchTime")
    print(report['lighthouseResult']['fetchTime'])
    print("form factor")
    print(report['lighthouseResult']['configSettings']['formFactor'])
    print("overall score")
    print(report["lighthouseResult"]["categories"]["performance"]["score"] * 100)
    # .. and so on - if you print it or directly add it to CSV is up to you


if __name__ == '__main__':
    # you can define global variables here, like I do with 'url'
    url = "https://pagespeedonline.googleapis.com/pagespeedonline/v5/runPagespeed?url=https://dental21.de"
    # see how url is not a parameter but I still use it in run()
    run()
