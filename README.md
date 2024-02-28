NOTE: THIS DOCUMENTATION IS AI GENERATED
Title: The Gazette Spider

Description:
This Scrapy spider, named 'thegazette', is designed to crawl The Gazette website (thegazette.co.uk) to extract notice information from its pages. The spider navigates through paginated lists of notices and extracts specific details from each notice's full page.

Functionality:
1. The spider starts its crawl by visiting the base URL with paginated notice listings.
2. It then extracts the URLs of individual notices from each page and navigates to their full page.
3. On each notice page, it extracts various details such as notice type, earliest publish date, claim expiration, etc.
4. The extracted data is then yielded as items.

Classes and Methods:
- ThegazetteSpider: This is the main spider class.
    - name: The name of the spider, which is "thegazette".
    - allowed_domains: The domain(s) that the spider is allowed to crawl.

    Methods:
    - start_requests(): Generates initial requests to start crawling.
    - parse(): Parses the response from the paginated notice listings and extracts individual notice URLs.
    - parse_full_notice(): Parses the response from each notice's full page and extracts detailed notice information.

Parameters:
- User-Agent: The spider should use a user-agent allowed by the website's robots.txt file. This is handled through settings.py.

Error Handling:
- Exceptions: The spider is designed to handle exceptions gracefully and log errors encountered during parsing.

Usage:
- To run the spider, use the Scrapy command-line interface (CLI) and provide the spider name, e.g., `scrapy crawl thegazette`.
