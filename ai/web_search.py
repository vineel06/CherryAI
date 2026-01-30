import requests
from bs4 import BeautifulSoup
from ddgs import DDGS

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/120.0.0.0 Safari/537.36"
    )
}


def extract_text_from_url(url: str) -> str:
    """
    Extract readable text from a webpage.
    """
    try:
        response = requests.get(url, headers=HEADERS, timeout=5)
        soup = BeautifulSoup(response.text, "html.parser")

        paragraphs = soup.find_all("p")
        text = " ".join(
            p.get_text().strip()
            for p in paragraphs
            if p.get_text().strip()
        )

        return text[:3000]

    except requests.RequestException:
        return ""


def web_search(query: str, max_results: int = 8) -> str:
    """
    Perform DuckDuckGo search and return relevant extracted content.
    """
    collected_text = []
    keywords = query.lower().split()

    with DDGS() as ddgs:
        results = ddgs.text(query, max_results=max_results)

        for result in results:
            url = result.get("href")
            title = (result.get("title") or "").lower()

            if not url or not any(k in title for k in keywords):
                continue

            page_text = extract_text_from_url(url)

            text_lower = page_text.lower()
            if (
                "india" in text_lower
                and ("prime minister" in text_lower or "pm" in text_lower)
            ):
                collected_text.append(page_text)

            if len(collected_text) >= 2:
                break

    return "\n\n".join(collected_text)
