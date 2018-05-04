from bs4 import BeautifulSoup
import requests

class Investigation(object):
    """docstring for Investigation"""
    def __init__(self, url):
        super(Investigation, self).__init__()
        self.url = url
        self.r = requests.get(self.url)
        self.soup = BeautifulSoup(self.r.text, "html.parser")

    @property
    def claim(self):
        return self.soup.find(
            'div', {
                'class': 'pastaende'
            }).find(
            'div', {
                'class': 'text'
            }).text.strip()

    @property
    def claim_maker(self):
        return self.soup.find('div', {'class': 'text claimers'}).text.strip()

    @property
    def claim_checker(self):
        author_div = self.soup.find('div', {'class': 'author'})
        return str(author_div).split('<br/>')[0].replace('<div class="author">', '').strip()

    @property
    def check_conclusion(self):
        return self.soup.find('div', {'class': 'grade g1'}).text.strip()

    @property
    def claim_tags(self):
        try:
            return self.soup.find('div', {'class': 'taggar'}).text.strip()
        except AttributeError:
            return None

    @property
    def check_date(self):
        return self.soup.find('span', {'class': 'date'}).text.strip()

    @property
    def claim_url(self):
        return self.url


class InvestigationSearch(object):
    def __init__(self):
        self.url = 'https://www.faktiskt.se/wp-content/themes/faktiskt_theme/ajax.php?flowmore=y'

    def fetch_investigation_url(self):
        page = -5  # Dunno how this will change as new claims are checked

        while True:
            payload = {"paginering": page}
            r = requests.post(self.url, data=payload)
            soup = BeautifulSoup(r.text, "html.parser")

            a_tags = soup.find_all('a', {'class': 'main_pl'})

            if len(a_tags) == 0:
                break

            for a_tag in a_tags:
                yield a_tag["href"]

            page += 1
