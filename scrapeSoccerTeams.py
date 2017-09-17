import scrapy
from scrapy.http import Request


class RedditbotSpider(scrapy.Spider):
    name = 'redditbot'
    allowed_domains = ['www.ca.soccerway.com/national/england/premier-league/20162017/regular-season/r35992/']
    start_urls = ['http://ca.soccerway.com/national/england/premier-league/20162017/regular-season/r35992/']

    def parse(self, response):
            
            
        url = 'http://ca.soccerway.com'    
        links = response.css('td.text.team.large-link a::attr(href)').extract()
        teams = response.css('td.text.team.large-link a::attr(title)').extract()
        print(teams)

        for squadLink in links:

            squadLinks = url + squadLink + 'squad/'
            #print(squadLinks)


            for squad in squadLinks:
                newRequest = Request(squadLinks, callback=self.parse)
                playerLinks = response.css('td.name.large-link a::attr(href)').extract()
                names = response.css('td.name.large-link a::text').extract()
                
                
                    

                #yield newRequest
                print playerLinks
