![sanatkar.ai](https://raw.githubusercontent.com/ardauzunoglu/sanatkar.ai/main/sanatkar.ai.png)

sanatkar.ai, çeşitli **yazılı sanat** dallarında (şu anlık şarkı, şiir ve tiyatro) doğal dil üretmek amacıyla karakter tabanlı tahmin işlemleri gerçekleştiren **RNN** modelleri kullanan bir Türkçe doğal dil işleme uygulamasıdır. 

# Kullanılan Veri Setleri

sanatkar.ai üç farklı sanat dalının sekiz farklı alt dalında doğal dil üretmektedir. Her bir alt dala ait **kapsamlı *ana* veri seti** bulunmaktayken ana veri setini oluşturan ***tekil* veri setleri** de mevcuttur. Veri setlerine ulaşmak için [tıklayabilirsiniz](https://github.com/ardauzunoglu/sanatkar.ai/tree/main/data-sets).

### Veri Seti Büyüklükleri 

1 - Şarkı Sözü Veri Setleri
  - Rap Veri Seti --> 270703 satır, 8.99 mb. 
  - Pop Veri Seti --> 78161 satır, 2.01 mb.
  - Rock Veri Seti --> 23326 satır, 604 kb.

2 - Şiir Veri Setleri
  - Milli Edebiyat Veri Seti --> 14366 satır, 640 kb.
  - Cumhuriyet Dönemi Saf Şiir Veri Seti --> 9007 satır, 312 kb.
  - Garip Şiiri Veri Seti --> 3712 satır, 116 kb.

3 - Tiyator Tiradı Veri Setleri
  - Erkek Karakterlerin Tiradları Veri Seti --> 112 kb.
  - Kadın Karakterlerin Tiradları Veri Seti --> 96 kb.

### Veri Setlerinin Oluşturulması - Web Scraping

##### Şarkı Sözü Veri Setlerinin Oluşturulması[*](https://github.com/ardauzunoglu/sanatkar.ai/blob/main/scrapers/song-scraper.ipynb)

Şarkı sözü veri setleri *[Genius](https://genius.com) API* ile *lyricsgenius* kütüphanesi kullanılarak elde edilmiş, devamında *[data_cleaning_for_songs.ipynb](https://github.com/ardauzunoglu/sanatkar.ai/blob/main/data_cleaning_for_songs.ipynb)* dosyasındaki işlemler ile veri seti temizliği gerçekleştirilmiştir.

##### Şiir Veri Setlerinin Oluşturulması[*](https://github.com/ardauzunoglu/sanatkar.ai/blob/main/scrapers/poem-scraper.ipynb)

Şiir veri setleri *selenium* kütüphanesi ile *[antoloji.com](https://www.antoloji.com)*'da ilgili şairlerin şiirlerinin kazınmasıyla ve farklı şairlerin şiirlerinin manuel olarak aynı metin dosyasına taşınmasıyla elde edilmiştir.

##### Tiyatro Tiradı Veri Setlerinin Oluşturulması

Tiyatro tiradı veri setleri [Ankara Akademi Sanat](http://www.ankaraakademisanat.com/erkek-tiradlari)'ın açık arşivindeki tiradların manuel olarak aynı metin dosyasına taşınmasıyla elde edilmiştir. 
