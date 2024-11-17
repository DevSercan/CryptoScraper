import requests
import re
from src.classes.Log import Log
log = Log()

class Coinmarketcap:
    def __init__(self):
        try:
            log.debug("The '__init__' function of the 'Coinmarketcap' class has been executed.")
            self.headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36',
                'Accept': 'application/json, text/plain, */*',
                'Referer': 'https://coinmarketcap.com/',
                'Origin': 'https://coinmarketcap.com'
            }
            self.exchangeList = ['Binance', 'Coinbase Exchange', 'Bybit', 'OKX', 'Upbit', 'HTX', 'Kraken', 'Gate.io', 'Bitfinex', 'KuCoin', 'MEXC', 'Bitget', 'Crypto.com Exchange', 'Binance TR', 'BingX', 'BitMart', 'Bitstamp', 'Bithumb', 'LBank', 'Gemini', 'Tokocrypto', 'bitFlyer', 'Binance.US', 'XT.COM', 'Deepcoin', 'Biconomy.com', 'ProBit Global', 'AscendEX (BitMax)', 'UZX', 'KCEX', 'Toobit', 'CoinW', 'Pionex', 'P2B', 'FameEX', 'Ourbit', 'WEEX', 'Bitvavo', 'BVOX', 'OrangeX', 'Hotcoin', 'Tapbit', 'Hibt', 'BiFinance', 'DigiFinex', 'Bitrue', 'Azbit', 'WhiteBIT', 'Bitunix', 'Coinstore', 'Phemex', 'Zaif', 'Coincheck', 'Binance TH', 'Dex-Trade', 'HashKey Global', 'Bitso', 'Coinone', 'BitMEX', 'BigONE', 'Fastex', 'Bitbank', 'HashKey Exchange', 'C-Patex', 'Aibit', 'Bitkub', 'Luno', 'Slex Exchange', 'BtcTurk | Kripto', 'CoinEx', 'PointPay', 'BTSE', 'BitoPro', 'Bit2Me', 'MAX Exchange', 'CEX.IO', 'LATOKEN', 'OKCoin Japan', 'Indodax', 'BITEXLIVE', 'BloFin', 'Paribu', 'Korbit', 'SecondBTC', 'Coinlist Pro', 'WOO X', 'Mercado Bitcoin', 'Independent Reserve', 'Cube Exchange', 'KoinBX', 'Foxbit', 'Poloniex', 'FMFW.io', 'EXMO', 'BitTrade', 'NovaDAX', 'ACE', 'BITmarkets', 'Currency.com', 'BTC Markets', '3EX', 'Nominex', 'CoinJar', 'Backpack Exchange', 'IndoEx', 'HitBTC', 'Cryptology', 'Megabit', 'BTC-Alpha', 'BitDelta', 'Bitspay', 'Koinbay', 'Kuna', 'Batonex', 'Reku', 'Coins.ph', 'ICRYPEX', 'Coinsbit', 'Coinmate', 'LMAX Digital', 'VALR', 'CoinZoom', 'Bitexen', 'TruBit Pro Exchange', 'Qmall Exchange', 'FMCPAY', 'BitStorage', 'Fairdesk', 'Bilaxy', 'Tidex', 'AlphaX', 'Websea', 'EXMO.ME', 'BITFLEX', 'Niza Global', 'Altcoin Trader', 'Buda', 'Ripio', 'NiceHash', 'GOPAX', 'ONUS Pro', 'Flipster', 'CoinDCX', 'Coinmetro', 'LCX Exchange', 'Bullish', 'Quidax', 'Gleec BTC', 'BIT', 'BXTEN', 'Paymium', 'TradeOgre', 'Nonkyc.io Exchange', 'Bitop', 'Salavi Exchange', 'SWFT Trade', 'BTCBOX', 'Bitcastle', 'Blockchain.com', 'SuperEx', 'Globe Derivative Exchange', 'ZKE', 'BankCEX', 'Welcoin', 'CoinCorner', 'Changelly PRO', 'FutureX Pro', 'BYDFi', 'CoinUp.io', 'CoinCatch', 'PayBito', 'Topcredit Int', 'digitalexchange.id', 'VinDAX', 'HKD.com', 'SafeTrade', 'UEEx', 'ZebPay', 'Mandala Exchange', 'Coinbase International Exchange', 'Emirex', 'TimeX', 'Bitcoiva', 'Cat.Ex', 'ABCC', 'BIT.TEAM', 'XeggeX', '4E', 'LocalTrade', 'AIA Exchange', 'Bibox', 'TNNS PROX', 'Bitci TR', 'ListaDao', 'SpireX', 'BCEX Korea', 'Giottus', 'Bitay', 'DIFX', 'Cryptonex', 'BIKA', 'Unocoin', 'Bitbns', 'Tokenize Xchange', 'XEX', 'YoBit', 'Crypton Exchange', 'Digitra.com', 'Bitazza', 'Okcoin', 'Dcoin', 'Polyx', 'ChangeNOW', 'Koinpark', 'BitHash', 'Tokpie', 'Remitano', 'BiKing', 'M2', 'Bitonic', 'Millionero', 'Finexbox', 'CoinLion', 'Bitlo', 'Bittylicious', 'Coinut', 'Mercatox', 'B2Z Exchange', 'StormGain', 'NexDAX', 'Jubi', 'Lykke Exchange', 'Bitcoin.me', 'Blocktrade', '50x', 'Avascriptions', 'BlueBit', 'GroveX', 'Coin8 Exchange', 'DOEX', 'Zedxion Exchange', 'BTX Exchange', 'BTC Trade UA', 'StakeCube', 'PowerTrade', 'Namebase', 'Ecxx', 'Graviex', 'FOBLGATE', 'FreiExchange', 'Zedcex Exchange', 'RuDEX', 'Flybit', 'WazirX']
        except Exception as e:
            log.error(f"Unexpected error in '__init__' function of the 'Coinmarketcap' class:\n{e}")
        finally:
            log.debug(f"The '__init__' function of the 'Coinmarketcap' class has completed.")

    def slugExchangeName(self, exchangeName:str) -> str:
        try:
            exchangeName = exchangeName.lower()
            exchangeName = re.sub(r'[.\s]', '-', exchangeName)
            return exchangeName
        except Exception as e:
            log.error(f"Unexpected error in 'slugExchangeName' function of the 'Coinmarketcap' class:\n{e}")
            return None
    
    def getCryptoCurrencyList(self) -> list:
        try:
            log.debug("The 'getCryptoCurrencyList' function of the 'Coinmarketcap' class has been executed.")
            cryptoList = []
            url = "https://api.coinmarketcap.com/data-api/v3/cryptocurrency/listing"
            start = 1
            limit = 1000
            parameters = {
                'start': start,
                'limit': limit,
                'sortBy': 'market_cap',
                'sortType': 'desc',
                'convert': 'USD',
                'cryptoType': 'all',
                'tagType': 'all',
                'audited': 'false'
            }
            cryptoList = []
            response = requests.get(url, headers=self.headers, params=parameters)
            if response.status_code == 200:
                jsonData = response.json()
                totalCount = int(jsonData['data']['totalCount'])
                cryptoCurrencyList = jsonData['data']['cryptoCurrencyList']
                cryptoList.extend(cryptoCurrencyList)
                while len(cryptoList) < totalCount:
                    start += limit
                    remainingCrypto = totalCount - len(cryptoList)
                    limit = min(1000, remainingCrypto)
                    parameters['start'] = start
                    parameters['limit'] = limit
                    response = requests.get(url, headers=self.headers, params=parameters)
                    if response.status_code == 200:
                        jsonData = response.json()
                        cryptoCurrencyList = jsonData['data']['cryptoCurrencyList']
                        cryptoList.extend(cryptoCurrencyList)
            return cryptoList
        except Exception as e:
            log.error(f"Unexpected error in 'getCryptoCurrencyList' function of the 'Coinmarketcap' class:\n{e}")
            return None
        finally:
            log.debug("The 'getCryptoCurrencyList' function of the 'Coinmarketcap' class has completed.")
    
    def getMarketPairs(self, exchange:str) -> list:
        try:
            log.debug(f"[exchange={exchange}] The 'getMarketPairs' function of the 'Coinmarketcap' class has been executed.")
            url = "https://api.coinmarketcap.com/data-api/v3/exchange/market-pairs/latest"
            start = 1
            limit = 1000
            parameters = {
                'slug': exchange,
                'category': 'spot',
                'start': start,
                'limit': limit
            }
            marketPairList = []
            response = requests.get(url, headers=self.headers, params=parameters)
            if response.status_code == 200:
                jsonData = response.json()
                numMarketPairs = jsonData['data']['numMarketPairs']
                marketPairs = jsonData['data']['marketPairs']
                marketPairList.extend(marketPairs)
                while len(marketPairList) < numMarketPairs:
                    start += limit
                    remainingPairs = numMarketPairs - len(marketPairList)
                    limit = min(1000, remainingPairs)
                    parameters['start'] = start
                    parameters['limit'] = limit
                    response = requests.get(url, headers=self.headers, params=parameters)
                    if response.status_code == 200:
                        jsonData = response.json()
                        marketPairs = jsonData['data']['marketPairs']
                        marketPairList.extend(marketPairs)
            return marketPairList
        except Exception as e:
            log.error(f"[exchange={exchange}] Unexpected error in 'getMarketPairs' function of the 'Coinmarketcap' class:\n{e}")
            return None
        finally:
            log.debug(f"[exchange={exchange}] The 'getMarketPairs' function of the 'Coinmarketcap' class has completed.")