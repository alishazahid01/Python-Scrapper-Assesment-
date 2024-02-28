import scrapy

#URL 403 (Forbidden)
#User Agent allowed in the robot.txt file
# Use user agent in the setting.py file

class ThegazetteSpider(scrapy.Spider):
    name = "thegazette"
    allowed_domains = ["thegazette.co.uk"]
    
    def start_requests(self):
        base_url = "http://www.thegazette.co.uk/all-notices/notice?text=&categorycode-all=all&noticetypes=&location-postcode-1=&location-distance-1=1&location-local-authority-1=&numberOfLocationSearches=1&start-publish-date=&end-publish-date=&edition=&london-issue=&edinburgh-issue=&belfast-issue=&sort-by=&results-page-size=10&results-page={}"

        for page in range(1, 16):
            yield scrapy.Request(base_url.format(page), callback=self.parse)

    def parse(self, response):

        try:
            items = response.css("div.feed-item")
            for item in items:
                full_notice_url = response.urljoin(item.css("a.btn-full-notice::attr(href)").get())
                yield scrapy.Request(full_notice_url, callback=self.parse_full_notice)

        except Exception as e:
            self.logger.error(f"An error occurred in parsing the page: {e}")

    def parse_full_notice(self, response):

        try:
            notice_details = response.css("div.notice-summary dl.metadata")
            yield {
                'Type': notice_details.css("dt.category + dd.category::text").get(),
                'Notice Type': notice_details.css("dt.notice-type + dd.notice-type::text").get(),
                'Earliest publish date': notice_details.css("dt[data-gazettes='earliestpublicationdate'] + dd::text").get(),
                'Claim expires': notice_details.css("dt:contains('Claim expires:') + dd::text").get(),
                'Edition': notice_details.css("dt:contains('Edition:') + dd::text").get(),
                'Notice ID': notice_details.css("dt:contains('Notice ID:') + dd::text").get(),
                'Notice code': notice_details.css("dt:contains('Notice code:') + dd::text").get(),
            }
            
        except Exception as e:
            self.logger.error(f"An error occurred in parsing the full notice: {e}")
