# Rank Takip

Valorant gibi rank sistemli oyunlarda günlük maç sonuçlarını ve RR değişimlerini takip etmek için yazdığım basit bir Python uygulaması.

## Özellikler

- Maç ekleme (kazanıldı/kaybedildi + RR)
- Gün sonunda toplu giriş
- Bugünün özeti (maç sayısı, kazanma oranı, net RR)
- Günlük geçmiş tablosu
- Genel istatistikler
- Son maçı silme

## Kurulum ve Çalıştırma

Bilgisayarında Python 3 kurulu olması yeterli, ek kütüphane gerekmiyor.

```
python rank_takip.py
```

Veriler aynı klasörde `maclar.json` dosyasına kaydedilir.

## Kullanım

Program açılınca menüden bir seçenek seçilir. Örneğin `1` ile maç eklerken sonucu `k` (kazandım) ya da `y` (yenildim) olarak girip RR miktarını sadece sayı olarak yazıyorsun. Kaybedilen maçlarda eksi işaretini program kendisi ekler.

## Notlar

Python öğrenirken yaptığım bir proje.
