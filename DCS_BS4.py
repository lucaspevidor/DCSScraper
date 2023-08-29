from bs4 import BeautifulSoup
import requests
import colorama
import re
import pandas as pd

from DCSModule import DCSModule

class DcsBs:
    def __init__(self, csvName: str = "DCSModules.csv"):
        colorama.init()
        self.csvName = csvName

    def ScanProducts(self):
        url = "https://www.digitalcombatsimulator.com/en/shop/modules/index.php?SHOWALL_1=1"
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
        }
        
        page = None
        try:
            page = requests.get(url, headers=headers)
        except Exception as e:
            print(f"{colorama.Fore.RED}Error scanning products: {e}{colorama.Style.RESET_ALL}")
            return

        if (page.status_code != 200):
            print("Error: " + page.status_code)
            return
        
        modules = []
        soup = BeautifulSoup(page.text, "html.parser")
        moduleTags = soup.find_all("div", class_="row well well-no-top-angle-radius")

        for moduleTag in moduleTags:
            a_name = moduleTag.select('h2 > a[href*="/en/shop/modules/"]')
            a_link = moduleTag.select('div.row > a[href*="/en/shop"]')
            a_price = moduleTag.select('div.price')
            if (len(a_name) == 0 or len(a_link) == 0 or len(a_price) == 0):
                continue

            name = a_name[0].text.strip()
            link = "https://www.digitalcombatsimulator.com" + a_link[0]["href"].strip()
            price = int(re.sub("[^\d]", "", a_price[0].text.strip()))
            
            module = DCSModule(name, link, -1, price, -1)
            modules.append(module)     

        return modules
    
    def ExportToCsv(self, modules):
        df = pd.DataFrame(columns=["Name", "Link", "Default Price", "Current Price", "Notified Price"])
        for index,module in enumerate(modules):
            df.loc[index] = module.name, module.link, module.defaultPrice, module.currentPrice, module.notifiedPrice
        df.to_csv(self.csvName, index=False, sep=";")

    def ReadFromCsv(self):
        df = pd.read_csv(self.csvName, sep=";")
        modules = []
        for index,row in df.iterrows():
            module = DCSModule(row["Name"], row["Link"], row["Default Price"], row["Current Price"], row["Notified Price"])
            modules.append(module)
        return modules
