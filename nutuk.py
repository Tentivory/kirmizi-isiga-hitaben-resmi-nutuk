#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Kırmızı ışığa resmi nutuk. Gerçekten çalışır, gerçekten işe yaramaz."""

from __future__ import annotations

import sys
import time

BASLIK = "T.C. HAYALÎ TRAFİK DİPLOMASİSİ GENEL MÜDÜRLÜĞÜ"

NUTUK = [
    "Sayın Kırmızı Işık,",
    "Bu kavşağın eşit vatandaşı olarak huzurunuzdayım.",
    "Siz durdursunuz diye duruyoruz; bu bir itaat değil, protokoldür.",
    "Yeşil ışık vaat eder. Siz ise söz vermezsiniz. Bu yüzden daha dürüstsünüz.",
    "Komisyon toplanmış, çay demlenmiş, tutanak açılmıştır.",
    "Karar: geçiş, şartlı ve geçicidir.",
    "Lütfen yeşile dönünüz. Dönmezseniz yine bekleriz. Bu da bir tür vatandaşlıktır.",
]


def yaz(satir: str, bekle: float = 0.45) -> None:
    print(satir)
    sys.stdout.flush()
    time.sleep(bekle)


def nutuk_oku() -> None:
    yaz("=" * 52, 0.2)
    yaz(BASLIK, 0.4)
    yaz("Konu: Kırmızı ışığa hitaben resmi nutuk", 0.4)
    yaz("=" * 52, 0.3)
    yaz("", 0.2)
    for satir in NUTUK:
        yaz(satir, 0.7)
    yaz("", 0.2)
    yaz("Komisyon düşünüyor...", 1.2)
    for i in range(7, 0, -1):
        yaz(f"  [bekleyiş süzülmesi] {i}", 0.35)
    yaz("", 0.2)
    yaz("KARAR: Işık hayali olarak YEŞİL ilan edilmiştir.", 0.6)
    yaz("Geçiş izni: VERİLDİ (sanal).", 0.4)
    yaz("Gerçek kavşakta hâlâ kırmızıysa durunuz.", 0.4)
    yaz("=" * 52, 0.2)


def main() -> int:
    nutuk_oku()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
