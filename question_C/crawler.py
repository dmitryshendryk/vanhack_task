import requests
from bs4 import BeautifulSoup
import re


class AnalyzeParser():

    def __init__(self):
        self.base_url = "https://www.google.com.ua/search?q="
        self.query = None
    

    def get_links(self, limit=5, query=None):
        self.query = query
        links_list = []
        self.query = '+'.join(self.query.split())
        page = requests.get(self.base_url + self.query)
        soup = BeautifulSoup(page.content)
        links = soup.findAll("a")
        post_process_links = []
        processed_links = soup.find_all("a",href=re.compile("(?<=/url\?q=)(htt.*://.*)"))
        if len(processed_links) > limit:
            processed_links = processed_links[:limit]
        for link in  processed_links:
            l = re.split(":(?=http)",link["href"].replace("/url?q=",""))[0].split("&")[0]
            links_list.append(l)
        return links_list
         

    def get_content_per_page(self, url):
        page = requests.get(url)
        soup = BeautifulSoup(page.content)

        for script in soup(["script", "style"]):
            script.extract()    
        text = soup.get_text()
        lines = (line.strip() for line in text.splitlines())
        chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
        text = [chunk for chunk in chunks if chunk]

        filtered_text = list(filter(lambda x: " ".join(self.query.split('+')) in x, text))
        return filtered_text
        

    def run_parser(self, limit=5, query=None):

        urls = self.get_links(limit, query)
        text_links = {}
        for url in urls:
            text = self.get_content_per_page(url)
            text_links[url] = text

        return text_links
