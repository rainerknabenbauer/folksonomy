import json
import requests


def run():
    # See how clean my run() is? Always try to keep run() clean
    # Also note how the order in run() reflects the order you find the methods() below? Easy to read, right? : )
    print_welcome()
    performance_report = query_performance()    # see (*) on How To 'return' Values From Functions
    create_report(performance_report)


def print_welcome():   # it's always a good idea to tell people how your application works
    print("Create your performance reports with ease.")
    print("Please enter the domain in a format like www.dental21.de")
    # I skip asking for any input, this is just an example on how to write well structured software : )


def query_performance():
    web_response = requests.get(url)
    json_result = json.loads(web_response.content)  # (*) with 'return' you specify what should come out of the function
    return json_result      # can you think of how to write the return statement with one line less?


def create_report(report):
    print("lighthouse fetchTime")
    print(report['lighthouseResult']['fetchTime'])
    print("form factor")
    print(report['lighthouseResult']['configSettings']['formFactor'])
    print("overall score")
    print(report["lighthouseResult"]["categories"]["performance"]["score"] * 100)
    # .. and so on - if you print it or directly add it to CSV is up to you


if __name__ == '__main__':
    # Maybe you noticed that this part is just an 'if' and not actually a function()?
    # Let's talk about 'scope' and why 'url' is behaving like a 'global variable'
    url = "https://pagespeedonline.googleapis.com/pagespeedonline/v5/runPagespeed?url=https://dental21.de"
    run()
