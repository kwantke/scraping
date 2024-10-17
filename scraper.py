
from bs4 import BeautifulSoup
import requests

class Scraper:
    def __init__(self):
        self.__url = "https://www.oliveyoung.co.kr/store/display/getCategoryShop.do?dispCatNo=10000010001&t_page=%EB%93%9C%EB%A1%9C%EC%9A%B0_%EC%B9%B4%ED%85%8C%EA%B3%A0%EB%A6%AC&t_click=%EC%B9%B4%ED%85%8C%EA%B3%A0%EB%A6%AC%ED%83%AD_%EB%8C%80%EC%B9%B4%ED%85%8C%EA%B3%A0%EB%A6%AC&t_1st_category_type=%EB%8C%80_%EC%8A%A4%ED%82%A8%EC%BC%80%EC%96%B4"
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
        response = requests.get(self.__url, headers=self.__headers)
        soup = BeautifulSoup(response.text, "html.parser")
        list_box = soup.find("div", class_="ct-product")
        item_boxs = list_box.find_all("div",class_="item")

        result = []
        for item_box in item_boxs[:3]:
            item_link = item_box.find("a")
            item_img_url = item_link.find("span",class_="img").find("img")["src"]
            item_name = item_link.findChild("p").find("span",class_="prd-name")
            

            item_price1_tag = item_link.find("p", class_="price").find("span", class_="price-1")
            item_price2_tag = item_link.find("p", class_="price").find("span", class_="price-2")
            if item_price1_tag is not None:
                item_price1 = item_price1_tag.get_text(separator='', strip=True)

            else:
                item_price1 = 0

            if item_price2_tag is not None:
                item_price2 = item_price2_tag.get_text(separator='', strip=True)
            else:
                item_price2 = 0
            
            url = item_link["href"]
            name = item_name.text

            item = {
                "original_price": item_price1,
                "sales_price": item_price2,
                "name": name,
                "url": url,
                "image_url": item_img_url
            }
            #print(item)
            result.append(item)

        return result


if __name__== "__main__":
    scraper = Scraper()
    #items = scraper.do()
    #print(items)


