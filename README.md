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

3 - Tiyatro Tiradı Veri Setleri
  - Erkek Karakterlerin Tiradları Veri Seti --> 112 kb.
  - Kadın Karakterlerin Tiradları Veri Seti --> 96 kb.

### Veri Setlerinin Oluşturulması - Web Scraping

##### Şarkı Sözü Veri Setlerinin Oluşturulması[*](https://github.com/ardauzunoglu/sanatkar.ai/blob/main/scrapers/song-scraper.ipynb)

Şarkı sözü veri setleri *[Genius](https://genius.com) API* ile *lyricsgenius* kütüphanesi kullanılarak elde edilmiş, devamında *[data_cleaning_for_songs.ipynb](https://github.com/ardauzunoglu/sanatkar.ai/blob/main/data_cleaning_for_songs.ipynb)* dosyasındaki işlemler ile veri seti temizliği gerçekleştirilmiştir.

##### Şiir Veri Setlerinin Oluşturulması[*](https://github.com/ardauzunoglu/sanatkar.ai/blob/main/scrapers/poem-scraper.ipynb)

Şiir veri setleri *selenium* kütüphanesi ile *[antoloji.com](https://www.antoloji.com)*'da ilgili şairlerin şiirlerinin kazınmasıyla ve farklı şairlerin şiirlerinin manuel olarak aynı metin dosyasına taşınmasıyla elde edilmiştir.

##### Tiyatro Tiradı Veri Setlerinin Oluşturulması

Tiyatro tiradı veri setleri [Ankara Akademi Sanat](http://www.ankaraakademisanat.com/erkek-tiradlari)'ın açık arşivindeki tiradların manuel olarak aynı metin dosyasına taşınmasıyla elde edilmiştir. 

# Gereklilikler 

'pip install -r requirements_for_model_creation.txt' ve 'pip install -r requirements_for_website.txt' komutları ile yerel cihazınıza gerekli kütüphanelerin kurulumunu gerçekleştirebilirsiniz.

### Model Oluşturmak İçin Gereklilikler

> tensorflow==2.6.0 <br>
> nltk==3.6.2 <br>
> urllib3==1.26.6 <br>
> numpy==1.21.2 <br>

### Web Sitesi İçin Gereklilikler

> tensorflow==2.6.0 <br>
> numpy==1.21.2 <br>
> Flask==2.0.1 <br>
> Flask-SQLAlchemy==2.5.1 <br>

# Web Sitesi

Doğal dil üretimi gerçekleştiren modellerin kullanıcı kullanımına açıldığı web sitesi backend'de Python yazılım dilinin Flask kütüphanesini; frontend'de HTML, CSS işaretleme dilleri ile JavaScript'in Jquery kütüphanesini kullanmaktadır. 

### Frontend

Bir karşılama sayfası ve dört ek sayfadan oluşan web sitesinin olabildiğince sade ve kullanıcı dostu tasarlanması hedeflenmiştir. Renk paleti olarak sanatkar.ai [logo](https://github.com/ardauzunoglu/sanatkar.ai/tree/main/logos)sunda yer alan üç temel renk (eflatuni mavi #5e17eb, koyu nane yeşili #39c466 ve dönüşümlü olarak siyah ve beyaz) kullanılmıştır.

### Backend

RNN modellerinin doğal dil üretim işlemlerini ve veritabanı iletişimlerini gerçekleştiren backend bu işlemler için TensorFlow ve SQLAlchemy kütüphanelerinden faydalanmaktadır.

# Contributors
- Yapay zekâ ve backend geliştiricisi: [Arda Uzunoğlu](https://github.com/ardauzunoglu)
- Frontend geliştiricisi: [Ege Dinnen](https://github.com/egedinnen)
