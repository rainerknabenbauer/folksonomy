import json
import requests


def print_welcome():   # it's always a good idea to tell people how your application works
    print("Create your performance reports with ease.")
    print("Please enter the domain in a format like www.dental21.de")
    # I skip asking for input, this is just an example on how to write well structured software : )


def query_performance():
    web_response = requests.get(url)
    return json.loads(web_response.content)  # return values go out of the method


def create_report(report):                   # Parameters go into the method
    print("lighthouse fetchTime")
    print(report['lighthouseResult']['fetchTime'])
    print("form factor")
    print(report['lighthouseResult']['configSettings']['formFactor'])
    print("overall score")
    print(report["lighthouseResult"]["categories"]["performance"]["score"] * 100)


def run():   # See how clean my run() is? Always try to keep this one clean
    print_welcome()
    performance_report = query_performance()    # remember the 'return' value? performance_report now has the value!
    create_report(performance_report)


if __name__ == '__main__':
    # you can define global variables here, like I do with 'url'
    url = "https://pagespeedonline.googleapis.com/pagespeedonline/v5/runPagespeed?url=https://dental21.de"
    # see how url is not a parameter but I still use it in run()
    run()
