from src.classes.Log import Log
log = Log()

class Crypto:
    def __init__(self, rank:int=None, name:str=None, symbol:str=None, price:int=None, totalSupply:int=None, marketCap:int=None, marketCapByTotalSupply:int=None, volume24h:int=None, lastUpdated:str=None):
        try:
            self.rank = rank
            self.name = name
            self.symbol = symbol
            self.price = price
            self.totalSupply = totalSupply
            self.marketCap = marketCap
            self.marketCapByTotalSupply = marketCapByTotalSupply
            self.volume24h = volume24h
            self.lastUpdated = lastUpdated
        except Exception as e:
            log.error(f"Unexpected error in '__init__' function of the 'Crypto' class:\n{e}")