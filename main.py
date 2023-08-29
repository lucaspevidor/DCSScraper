from DCS_BS4 import DcsBs
from DCSModule import DCSModule
from Notification import SendNotification
from datetime import datetime
import colorama

def NotifyModulesOnSale(modules):
    notificationText = ''
    for module in modules:
        if (module.currentPrice >= module.notifiedPrice and module.notifiedPrice > 0):
            continue

        notificationText += f"**{module.name}** is on sale!\n"
        notificationText += f"**Default price:** ${float(module.defaultPrice)/100}\n"
        
        if module.notifiedPrice > 0: 
            notificationText += f"**Last price:** ${float(module.notifiedPrice)/100}\n"
            
        notificationText += f"**Current price:** ${float(module.currentPrice)/100}\n"
        notificationText += f"**Link:** {module.link}\n\n"

        module.notifiedPrice = module.currentPrice
    
    if (notificationText != ''):
        print(notificationText)
        SendNotification(notificationText, title="DCS Module Sale", markdown=True)

    return notificationText

def main():
    dcs = DcsBs()
    modules = dcs.ReadFromCsv()
    webModules = dcs.ScanProducts()
    modulesSale = DCSModule.CompareModules(webModules, modules)

    if (len(modulesSale) > 0):
        n_text = NotifyModulesOnSale(modulesSale)
        if (n_text == ''):
            LogGreen(f"{len(modulesSale)} modules on sale, but already notified. {len(webModules)} modules verified.")
        else:
            LogGreen(f"{len(modulesSale)} modules on sale - {len(webModules)} modules verified.")
    else:
        LogRed(f"No modules on sale - {len(webModules)} modules verified.")
    
    dcs.ExportToCsv(modules)    

def LogGreen(message):
    time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"{time} - {colorama.Fore.GREEN}{message}{colorama.Style.RESET_ALL}")

def LogRed(message):
    time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"{time} - {colorama.Fore.RED}{message}{colorama.Style.RESET_ALL}")

if __name__ == "__main__":
    main()