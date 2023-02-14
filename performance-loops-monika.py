import requests
import json


# THIS TIME WE'RE LOOKING AT ⋅.˳˳loop .⋅ॱ˙ ⋅.˳˳loop .⋅ॱ˙ ⋅.˳˳loop .⋅ॱ˙ ⋅.˳˳loop .⋅ॱ˙


def run():
    # Only runs once! Try to see what happens if you include it into the for-loop : )
    print_welcome()
    website_url = read_user_input()  # Only read input from terminal and return the user input

    # Now that we have a collection, we can execute this for each element in the collection
    for strategy in strategies:
        print("We are now inside of the ⋅.˳˳loop .⋅ॱ˙! Doing " + strategy + " right now.")
        # Build the full URL for each strategy individually!
        strategy_specific_url = build_url(website_url, strategy)
        # We execute this inside of the ⋅.˳˳loop .⋅ॱ˙ now! Once with 'mobile' and once with 'desktop'
        performance_report = query_performance(strategy_specific_url)  # We pass in the complete url now!
        create_report(performance_report)

    # the last bit missing: Create a CSV and **attach** new results to the bottom of an existing file


def print_welcome():
    print('Check performance results by providing website URL')
    print()  # just an empty line for easier reading
    print('Lecture 2: ⋅.˳˳Loops .⋅ॱ˙˙ॱ⋅.˳˳every .⋅ॱ˙˙ॱᐧ.˳˳where .⋅')
    print()


def read_user_input():
    return input('enter website URL: ')


def build_url(website_url, strategy):
    full_url = pagespeed_base_url + "http://" + website_url + "&strategy=" + strategy
    print("We build this full URL: " + full_url)       # Another print, just to see if I did it right
    return full_url


def query_performance(strategy_specific_url):
    # We had a lot of things happening in here - focus on 1 thing per function : )
    web_response_desktop = requests.get(strategy_specific_url)
    response = json.loads(web_response_desktop.content)
    return response


def create_report(report):
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
    # Just use the base URL and build the exact URL later on
    pagespeed_base_url = 'https://pagespeedonline.googleapis.com/pagespeedonline/v5/runPagespeed?url='
    # Let's create a collection - in this case it's an array. It's also global, like pagespeed_base_url
    strategies = ["mobile", "desktop"]
    run()
