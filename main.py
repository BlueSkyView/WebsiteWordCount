from website_fetcher import WebsiteFetcher
from document_parser import DocumentParser


def main():
    # this will serve as a "UI" of sorts, which will just take a text input from the user running it on a local machine.
    # if there was an actual UI, this would be a text box that a user could input a website into, and there would be
    # two checkboxes for the ascending/descending options which a user could select.
    # If desired, this could easily be extended to allow for sorting on other values (alphabetical based on key for example)
    # and if there was a UI, this could be a toggle, or another checkbox, etc.

    print("Welcome!  This program will take in a website from the user (you) and then return a dictionary with the "
          "frequency of all visible words on the page.")
    website = input("Please input a website:")

    fetcher = WebsiteFetcher()
    site_info = fetcher.get_website(website)
    if site_info == "":
        return

    parser = DocumentParser()
    freq_dict = parser.parse_text(site_info)

    flag_value = input("Do you want to get the dictionary in sorted order of word frequency? (Y/N)")
    if flag_value.lower() == 'y':
        asc_flag = input("Would you like to see it in ascending order or descending order? (A/D)")

    # have decided to give the results as it defaults to if the user does not enter in a valid response to the
    # questions asked
    if flag_value.lower() == 'y':
        if asc_flag.lower() == 'd':
            freq_dict = dict(sorted(freq_dict.items(), reverse=True, key=lambda item: item[1]))
        elif asc_flag.lower() == 'a':
            freq_dict = dict(sorted(freq_dict.items(), key=lambda item: item[1]))

    print(freq_dict)


# this will just check to test that if a website has been queried already, it will not go through every step again
# def test_repeated_requests():
#     website = 'https://techcrunch.com/2022/05/14/this-week-in-apps-google-i-o-wraps-a-new-arcore-api-twitter-deal-drama/'
#     fetcher = WebsiteFetcher()
#     parser = DocumentParser()
#
#     for i in range(2):
#         site_info = fetcher.get_website(website)
#         freq_dict = parser.parse_text(site_info)
#         print(freq_dict)
# test_repeated_requests()

main()
