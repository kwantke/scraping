from bs4 import BeautifulSoup
import requests

class Scraper:
    def __init__(self):
        self.__url = "https://www.oliveyoung.co.kr/store/display/getCategoryShop.do"
        self.__params = {
                "dispCatNo":"10000010002",
            "t_page":"%EB%93%9C%EB%A1%9C%EC%9A%B0_%EC%B9%B4%ED%85%8C%EA%B3%A0%EB%A6%AC",
            "t_click":"%EC%B9%B4%ED%85%8C%EA%B3%A0%EB%A6%AC%ED%83%AD_%EB%8C%80%EC%B9%B4%ED%85%8C%EA%B3%A0%EB%A6%AC",
            "t_1st_category_type":"%EB%8C%80_%EB%A9%94%EC%9D%B4%ED%81%AC%EC%97%85",
        }

        self.__headers = {
            "user-agent":"'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36'"

        }
    
    def do(self):
        response = requests.get(self.__url, params=self.__params, headers=self.__headers)
        #print(response.status_code)
        #print(response.text)
        soup = BeautifulSoup(response.text, "html.parser")
        list_box = soup.find("div", class_="ct-product")
        #print(list_box)
        item_boxs = list_box.find_all("div",class_="item")
        #print(item_box)

        result = []
        for item_box in item_boxs:
            item_link = item_box.find("a")
            item_name = item_link.findChild("p").find("span",class_="prd-name")
            item_price = item_link.findChild("p").findChild("span",class_="price-2")

            url = item_link["href"]
            name = item_name.text
            price = item_price.text
            # print(url)
            # print(item_link)
            #print(item_price)

            item = {
                "price": price,
                "name": name,
                "url": url
            }
            #print(item)
            result.append(item)
        return result


if __name__== "__main__":
    scraper = Scraper()
    items = scraper.do()
    print(items)


