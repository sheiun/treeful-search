from lxml import etree
import re
import requests

URL = 'https://www.treerful.com/space/result'

def get_elements(url):
    """
    return:
    a: {
        img
        h3
        p
        small
    }
    """
    res = requests.get(url)
    html = etree.HTML(res.text)
    elements = html.xpath('//body/div/ul/li/a')
    return elements


class Treer:
    """空間"""
    url = ''
    name = ''
    img_src = ''
    people = 0
    price = 0
    address = ''

    def __init__(self, element):
        self.element = element
        self.url = element.get('href')
        for sub_element in element:
            if sub_element.tag == 'img' and sub_element.get('src'):
                self.img_src = sub_element.get('src')
            elif '/' in sub_element.text:
                self.price = self.extract_number(sub_element.text)
            elif '人' in sub_element.text:
                self.people = self.extract_number(sub_element.text)
            elif sub_element.text is not None:
                self.name = sub_element.text
        self.address = self.get_address(self.url)

    def get_address(self, url):
        if self.address == '':
            res = requests.get(url)
            html = etree.HTML(res.text)
            self.address = html.xpath('//div[@class="locationTitleLeft"]/p/text()')
            print(self.address)
        return self.address

    def extract_number(self, text):
        return int(re.findall(r'\d+', text)[0])

    def __str__(self):
        return '名稱: {}\n網址: {}\n地址: {}\n價位: {}\n人數: {}'.format(self.name, self.url, self.get_address(self.url), self.price, self.people)

def sorted_treers(treers, key, reverse=True):
    """
    排序
    """
    return sorted(treers, key=lambda x: getattr(x, key), reverse=reverse)

if __name__ == '__main__':
    elements = get_elements(URL)
    treers = list()
    for element in elements:
        treers.append(Treer(element))

    for treer in sorted_treers(treers, 'people', reverse=False)[:10]:
        if treer.people <= 3:
            print(treer)
            print('---')