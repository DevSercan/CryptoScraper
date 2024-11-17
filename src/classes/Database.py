import sqlite3
import os
from src.classes.Crypto import Crypto
from src.classes.Log import Log
log = Log()

class Database:
    def __init__(self, databasePath):
        try:
            log.debug("The '__init__' function of the 'Database' class has been executed.")
            folderPath = os.path.dirname(databasePath)
            if not os.path.exists(folderPath):
                os.makedirs(folderPath)
            self.connection = sqlite3.connect(databasePath)
            self.cursor = self.connection.cursor()
            self.cryptoTableName = "Cryptos"
            self.createTable()
        except Exception as e:
            log.error(f"Unexpected error occurred in '__init__' function of 'Database' class:\n{e}")

    def createTable(self):
        try:
            log.debug("The 'createTable' function of the 'Database' class has been executed.")
            query = f"""
            CREATE TABLE IF NOT EXISTS {self.cryptoTableName} (
                Id INTEGER PRIMARY KEY AUTOINCREMENT,
                Rank INTEGER NOT NULL,
                Name TEXT NOT NULL,
                Symbol TEXT NOT NULL,
                Price INTEGER NOT NULL,
                TotalSupply INTEGER NOT NULL,
                MarketCap INTEGER NOT NULL,
                MarketCapByTotalSupply INTEGER NOT NULL,
                Volume24h INTEGER NOT NULL,
                LastUpdated DATETIME NOT NULL
            );
            """
            self.cursor.executescript(query)
            self.connection.commit()
            del query
            return True
        except Exception as e:
            log.error(f"Unexpected error occurred in 'createTable' function of 'Database' class:\n{e}")
            return False

    def createCrypto(self, crypto:Crypto):
        try:
            log.debug("The 'createCrypto' function of the 'Database' class has been executed.")
            isAvailable = self.isCryptoAvailable(crypto.name)
            if not isAvailable:
                query = f"INSERT INTO {self.cryptoTableName} (Rank, Name, Symbol, Price, TotalSupply, MarketCap, MarketCapByTotalSupply, Volume24h, LastUpdated) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?);"
                self.cursor.execute(query, (crypto.rank, crypto.name, crypto.symbol, crypto.price, crypto.totalSupply, crypto.marketCap, crypto.marketCapByTotalSupply, crypto.volume24h, crypto.lastUpdated))
            else:
                return False
                # query = f"UPDATE {self.cryptoTableName} SET Rank = ?, Symbol = ?, Price = ?, MarketCap = ?, Volume24h = ?, LastUpdated = ? WHERE Name = ?;"
                # self.cursor.execute(query, (crypto.rank, crypto.symbol, crypto.price, crypto.marketCap, crypto.volume24h, crypto.lastUpdated, crypto.name))
            self.connection.commit()
            return True
        except Exception as e:
            log.error(f"Unexpected error occurred in 'createCrypto' function of 'Database' class:\n{e}")
            return False

    def isCryptoAvailable(self, cryptoName:str):
        try:
            log.debug(f"[cryptoName={cryptoName}] The 'isCryptoAvailable' function of the 'Database' class has been executed.")
            query = f'SELECT Name FROM {self.cryptoTableName} WHERE Name = ?;'
            self.cursor.execute(query, (cryptoName,))
            result = self.cursor.fetchone()
            if result:
                return True
            else:
                return False
        except Exception as e:
            log.error(f"[cryptoName={cryptoName}] Unexpected error occurred in 'isCryptoAvailable' function of 'Database' class:\n{e}")
            return False
    
    def clearCryptoTable(self):
        try:
            log.debug("The 'clearCryptoTable' function of the 'Database' class has been executed.")
            
            # Tablodaki tüm verileri sil
            query = f"DELETE FROM {self.cryptoTableName};"
            self.cursor.execute(query)
            self.connection.commit()

            # SQLite için AUTOINCREMENT değerini sıfırlamak
            # Eğer tablo PRIMARY KEY ID kullanıyorsa bu adımı uygulayın.
            query_reset_autoincrement = f"DELETE FROM sqlite_sequence WHERE name='{self.cryptoTableName}';"
            self.cursor.execute(query_reset_autoincrement)
            self.connection.commit()

            log.info(f"All data in table named '{self.cryptoTableName}' has been cleared and AUTO_INCREMENT reset.")
            return True
        except Exception as e:
            log.error("Unexpected error occurred in 'clearCryptoTable' function of 'Database' class:\n{e}")
            return False

    def closeConnection(self):
        try:
            log.debug("The 'closeConnection' function of the 'Database' class has been executed.")
            self.connection.close()
            return True
        except Exception as e:
            log.error(f"Unexpected error occurred in 'closeConnection' function of 'Database' class:\n{e}")
            return False
