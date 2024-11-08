import requests

class Crawler:
    def __init__(self, base_url) -> None:
        self.queue = [base_url]

        for url in self.queue:
            html = self.get_html(url)
            # do something with html

    def get_urls(self, html):
        """Extracts and returns a list of URLs from the provided HTML content.

            This method parses the given HTML and identifies all hyperlinks,
            typically using anchor tags (`<a href="...">`). It returns a list
            of URLs found within the HTML document, or an empty list if no URLs
            are found.

            Args:
                html (str): A string containing the HTML content to parse.

            Returns:
                list: A list of extracted URLs as strings. If no URLs are found,
                    an empty list is returned.
        """
        pass

    def get_html(self, url):
        """Fetches the HTML content from the specified URL.

            Args:
                url (str): The URL from which to fetch the HTML content.

            Returns:
                str: The HTML content of the page if the request is successful.
                    Returns None if the request fails or if the response status
                    code indicates an error.
        """
        try:
            response = requests.get(url)
            if response.ok:
                return response.text
            print(f"Error fetching {url}: Status code {response.status_code}")
        except requests.exceptions.RequestException as e:
            print(f"Network error fetching {url}: {e}")
        except Exception as e:
            print(f"Ups, something went wrong! {e}")
        return None