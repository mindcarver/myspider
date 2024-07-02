import scrapy


class CoindeskSpider(scrapy.Spider):
    name = "coindesk"
    allowed_domains = ["www.coindesk.com"]
    start_urls = ["https://www.coindesk.com"]

    # def parse(self, response):
    #     # with open('coindesk.html', 'wb') as f:
    #     #     f.write(response.body)
    #            # 获取所有新闻数据
    #    node_list = response.xpath('//div[@class="side-cover-cardstyles__SideCoverCardWrapper-sc-1nd3s5z-0 bTtqXW side-cover-card"]')
    #    print(len(node_list))
    #    # 遍历新闻列表

    def parse(self, response):
        # 定位到包含新闻数据的div元素
        node_list = response.xpath(
            '//div[contains(@class, "side-cover-cardstyles__SideCoverCardWrapper")]'
        )

        for node in node_list:
            title = node.xpath(
                './/h6[contains(@class, "typography__StyledTypography-sc-owin6q-0")]/text()'
            ).get()
            #print(title)

            link = node.xpath('.//a[contains(@class, "card-title-link")]/@href').get()
            #print(link)

            date = node.xpath('.//span[contains(@class, "typography__StyledTypography-sc-owin6q-0 iOUkmj")]/text()').get()
            yield {
                "title": title.strip(),  # 使用strip()去除可能的多余空格
                "link": response.urljoin(link),  # 确保链接是绝对的
                "date": date.strip()
            }
