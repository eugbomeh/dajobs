# -*- coding: utf-8 -*-
import scrapy


class DajobsSpider(scrapy.Spider):
    name = 'dajobs'
    allowed_domains = ['ca.indeed.com']
    start_urls = ['https://ca.indeed.com/Data-Analyst-jobs']

    def parse(self, response):
        for job in response.xpath("//td[@id='resultsCol']/div[@class='jobsearch-SerpJobCard unifiedRow row result']"):
            yield{
                'Title' : job.xpath(".//h2[@class='title']/a/@title").get(),
                'Url' : response.urljoin( job.xpath(".//h2[@class='title']/a/@href").get()),
                'Company' :  job.xpath(".//div[@class='sjcl']/div/span[@class='company']/a/text()").get(),
                'Location' :  job.xpath(".//div[@class='sjcl']/div[@class='recJobLoc']/@data-rc-loc").get(),
                'Salary' : job.xpath(".//div[@class='salarySnippet salarySnippetDemphasizeholisticSalary']/span/span/text()").get(),
                'Apply' : job.xpath(".//table[@class='jobCardShelfContainer']/tbody/tr/td/span[@class='iaLabel iaIconActive']/text()").get(),
                'Posted' : job.xpath(".//table[@class='jobCardShelfContainer']/tbody/tr/td/span[2]/text()").extract()
            } 

        
