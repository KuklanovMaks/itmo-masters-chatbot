import requests
from bs4 import BeautifulSoup


def load_html(url: str) -> BeautifulSoup:
    """
    Загружает HTML-документ по ссылке и возвращает объект BeautifulSoup.
    """
    try:
        page = requests.get(url)
        page.raise_for_status()
    except requests.RequestException as e:
        raise RuntimeError(f"Ошибка при загрузке {url}: {e}")

    return BeautifulSoup(page.text, "html.parser")


def extract_content_by_headers(soup: BeautifulSoup) -> dict[str, str]:
    """
    Ищет все заголовки второго уровня (h2) и извлекает текст до следующего h2.
    Возвращает словарь: {заголовок: содержимое}.
    """
    result = {}

    for h2 in soup.select("h2"):
        section_title = h2.get_text(strip=True)
        aggregated_text = []

        for sibling in h2.find_next_siblings():
            if sibling.name == "h2":
                break
            aggregated_text.append(sibling.get_text(separator=" ", strip=True))

        result[section_title] = "\n".join(aggregated_text)

    return result


def get_program_sections(url: str) -> dict[str, str]:
    """
    Главная точка входа: загружает страницу и возвращает её основные текстовые блоки по h2.
    """
    soup = load_html(url)
    return extract_content_by_headers(soup)




