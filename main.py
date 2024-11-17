import difflib
from src.utils.helper import getConfig, clear, exportDbToExcel
from src.classes.Crypto import Crypto
from src.classes.Coinmarketcap import Coinmarketcap
from src.classes.Color import Color # Konsolda renkli yazı yazma özelliği sunar.
from src.classes.Database import Database # Veri tabanı işlemleri için kullanılan sınıfı içe aktarıyoruz.
from src.classes.Log import Log # Günlük tutma (Loglama) işlemleri için kullanılan sınıfı içe aktarıyoruz.

log = Log() # Log sınıfını nesne olarak tutar.
CONFIG = getConfig()
coinmarketcap = Coinmarketcap()
databasePath = CONFIG["databasePath"]
database = Database(databasePath)

def inputExchanges():
    slugExchangeList = []
    for exchangeName in coinmarketcap.exchangeList:
        exchangeName = coinmarketcap.slugExchangeName(exchangeName)
        slugExchangeList.append(exchangeName)

    while True:
        try:
            exchangeInput = str(input(f"{Color.lyellow}\n> Virgüller ile Borsa İsimleri (örn: mexc, kucoin):{Color.reset} "))
            isInvalidExchange = False
            if exchangeInput:
                exchangeList = exchangeInput.replace(' ', '').split(",")
                exchangeList = [item for item in exchangeList if item]
                for exchangeName in exchangeList:
                    exchangeName = coinmarketcap.slugExchangeName(exchangeName)
                    if exchangeName not in slugExchangeList:
                        isInvalidExchange = True
                        getCloseMatches = difflib.get_close_matches(exchangeName, slugExchangeList, n=6, cutoff=0.6)
                        if getCloseMatches:
                            print(f"{Color.lred}'{exchangeName}' adlı borsa mevcut değil. Benzer borsa isimleri: {', '.join(getCloseMatches)}{Color.reset}")
                        else:
                            print(f"{Color.lred}'{exchangeName}' adlı borsa mevcut değil. Benzer borsa isimleri bulunmuyor.{Color.reset}")
                if isInvalidExchange:
                    continue
                else:
                    break
            else:
                print(f"{Color.lred}Borsa ismi boş bırakılamaz.{Color.reset}")
        except:
            print(f"{Color.lred}Girilen borsa isimleri geçersiz.{Color.reset}")
            continue
    return exchangeList

def getCommonCryptoList():
    commonCryptoList = []
    inputExchangeList = inputExchanges()
    for exchangeName in inputExchangeList:
        exchangeName = coinmarketcap.slugExchangeName(exchangeName)
        print(f"'{exchangeName}' borsa bilgileri elde ediliyor...")
        marketPairs = coinmarketcap.getMarketPairs(exchangeName)
        if marketPairs:
            print(f"'{exchangeName}' borsa bilgileri elde edildi.")
            baseCurrencyNameList = [pair['baseCurrencyName'] for pair in marketPairs]
            if len(commonCryptoList) == 0:
                commonCryptoList = baseCurrencyNameList
            else:
                commonCryptoList = list(set(commonCryptoList) & set(baseCurrencyNameList))
        else:
            print(f"'{exchangeName}' borsa bilgileri elde edilemedi!")
    return commonCryptoList

def getCrypto():
    commonCryptoList = getCommonCryptoList()

    print("Güncel kripto para verileri elde ediliyor...")
    cryptoCurrencyList = coinmarketcap.getCryptoCurrencyList()
    if cryptoCurrencyList:
        print("Güncel kripto para verileri elde edildi.")
        print("Veri tabanı sıfırlanıyor...")
        database.clearCryptoTable()
        print("Veri tabanı sıfırlandı.")
        print("Veriler ayrıştırılıyor ve veri tabanına aktarılıyor...")
        for cryptoData in cryptoCurrencyList:
            if cryptoData['name'] in commonCryptoList:
                crypto = Crypto()
                crypto.rank = cryptoData['cmcRank']
                crypto.name = cryptoData['name']
                crypto.symbol = cryptoData['symbol']
                crypto.price = int(cryptoData['quotes'][0]['price'])
                crypto.totalSupply = int(cryptoData['totalSupply'])
                crypto.marketCap = int(cryptoData['quotes'][0]['marketCap'])
                crypto.marketCapByTotalSupply = int(cryptoData['quotes'][0]['marketCapByTotalSupply'])
                crypto.volume24h = int(cryptoData['quotes'][0]['volume24h'])
                crypto.lastUpdated = cryptoData['quotes'][0]['lastUpdated']
                database.createCrypto(crypto)
        print("Veriler ayrıştırıldı ve veri tabanına aktarıldı.")
    else:
        print("Güncel kripto para verileri elde edilemedi!")

def menu():
    while True:
        try:
            print(f"{Color.yellow}--------------------------------------------------{Color.reset}")
            print(f"{Color.lblack}\nGerçekleştirmek istediğiniz işlemin numarasını girin.{Color.reset}")
            print(f"{Color.yellow}[{Color.lyellow}1{Color.yellow}]{Color.reset} Borsalardan Kripto Para Verilerini Al")
            print(f"{Color.yellow}[{Color.lyellow}2{Color.yellow}]{Color.reset} Veri Tabanını Excel Olarak Dışa Aktar")
            no = int(input(f"{Color.lyellow}\n> İşlem Numarası: {Color.yellow}"))
            print(Color.reset)
            if no == 1:
                getCrypto()
            elif no == 2:
                print("Veri tabanı Excel olarak dışa aktarılıyor...")
                exportResult = exportDbToExcel(databasePath=databasePath, tableName="Cryptos", excelPath="Cryptos.xlsx")
                if exportResult:
                    print("Veri tabanı Excel olarak dışa aktarıldı.")
                else:
                    print("Veri tabanı Excel olarak dışa aktarılamadı!")
            else:
                print(f"{Color.lred}Girilen işlem numarası geçersiz!{Color.reset}")
        except:
            print(f"{Color.lred}Girilen işlem numarası geçersiz!{Color.reset}")

def main():
    """ Ana fonksiyondur. """
    try:
        clear()
        menu()
    except Exception as e:
        log.error(f"Unexpected error in 'main' function:\n{e}")

if __name__ == "__main__":
    main()
    input(f"{Color.lblack}\nKapatmak için Enter'a basın...{Color.reset}")