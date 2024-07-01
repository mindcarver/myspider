import scrapy


class UxlinkSpider(scrapy.Spider):
    name = "uxlink"
    allowed_domains = ["dapp.uxlink.io"]
    start_urls = ["https://dapp.uxlink.io/discover/detail?id=1779158074653667329&userUid=1807650273569947648"]

    def parse(self, response):
       # 获取所有新闻数据
       node_list = response.xpath('//div[@class="m-[12px] flex flex-col border-b border-[#2A2A2A] pb-[12px] lg:mx-[18px] lg:pb-[16px]"]')
       print(len(node_list))
       # 遍历新闻列表
       
