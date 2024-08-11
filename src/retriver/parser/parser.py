from typing import List

from bs4 import BeautifulSoup, Tag


def get_page_features(page_content: bytes, page_url: str) -> List:
    endpoints = []
    link_elements = get_page_links(page_content)

    for link_element in link_elements:
        url = link_element['href']

        if page_url in url:
            for child in link_element.children:
                name = child.get_text().replace("  ", "").replace("\n", "")
                if name != "":
                    endpoints.append({"name": name, "url": url})

    return endpoints


def get_page_links(page_content) -> List[Tag]:
    soup = BeautifulSoup(page_content, "html.parser")

    return (soup.select("a[href]") + soup.select("area[href]") +
            soup.select("base[href]") + soup.select("link[href]"))
