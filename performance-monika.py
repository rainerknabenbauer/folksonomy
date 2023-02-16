# read URL of the website
import requests
import json


def run():
    print_welcome()
    performance_report = query_performance()

    print("I am not one but actually " + len(performance_report).__str__())


def print_welcome():
    print('Check performance results by providing website URL')


def query_performance():
    website_url = input('enter website URL: ')
    desktop_full_url = pagespeed_desktop_url + website_url
    mobile_full_url = pagespeed_mobile_url + website_url
    print(desktop_full_url)
    print(mobile_full_url)
    web_response_desktop = requests.get(desktop_full_url)
    web_response_mobile = requests.get(mobile_full_url)
    desktop = json.loads(web_response_desktop.content)
    mobile = json.loads(web_response_mobile.content)

    return desktop, mobile


def create_report_desktop(report):
    print("lighthouse fetchTime")
    print(report['lighthouseResult']['fetchTime'])
    print("form factor")
    print(report['lighthouseResult']['configSettings']['formFactor'])
    print("overall score")
    print(report["lighthouseResult"]["categories"]["performance"]["score"] * 100)
    print("speed_index")
    print(report["lighthouseResult"]["audits"]["speed-index"]["score"] * 100)
    print("first_contentful_paint")
    print(report["lighthouseResult"]["audits"]["first-contentful-paint"]["score"] * 100)
    print("first_meaningful_paint")
    print(report["lighthouseResult"]["audits"]["first-meaningful-paint"]["score"] * 100)
    print("time_to_interactive")
    print(report["lighthouseResult"]["audits"]["interactive"]["score"] * 100)


if __name__ == '__main__':
    pagespeed_desktop_url = 'https://pagespeedonline.googleapis.com/pagespeedonline/v5/runPagespeed?url='
    pagespeed_mobile_url = 'https://pagespeedonline.googleapis.com/pagespeedonline/v5/runPagespeed?strategy=mobile&url='
    run()