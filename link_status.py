import requests
from bs4 import BeautifulSoup
import argparse

class LinkHeaderStatus:

    website = ""
    css_selector = ""

    def __init__(self, website, css_selector):
        self.website = website
        self.css_selector = css_selector

    # get the links
    def get_links(self, website, nav_selector):
        result = requests.get(website)
        soup = BeautifulSoup(result.content.__str__(), 'html.parser')

        list_links = []

        for link in soup.select(nav_selector):
            list_links.append(link.get('href'))

        return list_links

    # get the status code of the links
    # crawls the links and saves its header code
    def get_status_codes_of_links(self, links):

        link_status = {}

        for link in links:
            link_status[link] = requests.get(link).status_code

        return link_status

    # check if the status code is valid
    def is_status_code_valid(self, links):

        for link, status in links.items():
            if status not in [200, 300]:
                print(link)
                exit(1)

        exit(0)

    def test(self):
        links = self.get_links(self.website, self.css_selector)
        links_status = self.get_status_codes_of_links(links)
        self.is_status_code_valid(links_status)


def main():
    parser = argparse.ArgumentParser('python link_status.py https://www.example.com "#menu-main-menu li a"')
    parser.add_argument("link", help="the website URL", type=str)
    parser.add_argument("css_selector", help="the css selector to crawl the links", type=str)
    args = parser.parse_args()
    link_header = LinkHeaderStatus(args.link, args.css_selector)
    link_header.test()

if __name__ == '__main__':
    main()
