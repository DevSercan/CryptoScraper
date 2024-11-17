# CoinMarketCap Crypto Scraper

## Projenin Amacı
Bu proje; CoinMarketCap platformunu kullanarak, seçilen borsalarda yer alan ortak güncel kripto para verilerini elde etmek için geliştirilmiştir.

## Nasıl Çalıştırılır?
1. Python Yüklü Sistemler İçin:
   Python bilgisayarınızda yüklü ise, öncelikle 'requirements.txt' dosyasındaki bağımlılıkları yüklemeniz gerekmektedir. Kurulum işlemini tamamladıktan sonra 'main.py' dosyasını çalıştırarak yazılımı başlatabilirsiniz.

2. Program Çalıştırma Adımları:
   Program başlatıldığında, bir konsol penceresi açılacaktır. Konsolda, istenilen işlem numarasını girmeniz istenecektir. İşlemlerin solunda yer alan numarayı konsola girerek işlem gerçekleştirebilirsiniz.

## Kripto Para Verileri Nereye Kaydedilir?
Toplanan kripto para verileri, 'src/database/' klasöründe oluşturulan 'database.db' isimli SQLite dosyasına kaydedilmektedir. Her mevcut veri çekme işleminde veri tabanı sıfırlanıp yeniden oluşmaktadır. Böylece veriler daima güncel olarak kalmaktadır.

## Kripto Para Verilerini Excel Dosyasına Aktarma:
Kripto para verilerini Excel formatına dönüştürmek için konsolda yer alan, veri tabanını Excel olarak dışa aktarmak ile ilgili olan işlemin numarasını konsola girmeniz yeterlidir. Böylece mevcut dosya dizininde bir Excel dosyası oluşturulacaktır.

## Ek Bilgiler:
- Loglama: Proje içinde hata takibi için loglama yapılmıştır. Bir sorunla karşılaşmanız halinde, yazılımcıya yardımcı olması için 'logs' klasörünü paylaşabilirsiniz.
- Hata Giderme: Eğer loglar sorunu çözmede yeterli olmazsa, komut satırından (CMD) uygulamayı başlatarak, hata mesajlarını konsolda görüntüleyebilir ve yazılımcıya iletebilirsiniz.