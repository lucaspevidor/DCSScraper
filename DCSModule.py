class DCSModule:
    def __init__(self, name: str, link: str, defaultPrice: int, currentPrice: int, notifiedPrice: int):
        self.name = name
        self.link = link
        self.defaultPrice = defaultPrice
        self.currentPrice = currentPrice
        self.notifiedPrice = notifiedPrice

    @staticmethod
    def CompareModules(webModuleList, moduleList):
        modulesOnSale = []

        for module in moduleList:
            for webModule in webModuleList:
                if (module.name == webModule.name):
                    module.currentPrice = webModule.currentPrice
                    if (module.currentPrice < module.defaultPrice):
                        modulesOnSale.append(module)
                    break
        
        return modulesOnSale

    def __str__(self):
        # return props separated by ;
        return self.name + ";" + self.link + ";" + str(self.defaultPrice) + ";" + str(self.currentPrice) + ";" + str(self.notifiedPrice)