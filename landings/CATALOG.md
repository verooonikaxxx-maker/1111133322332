# Каталог транзитных страниц

## Сводка

- **Всего уникальных**: 25 (из 27 загруженных, 2 дубля отброшены)
- **Тип VSL**: 14 страниц
- **Тип Advertorial**: 11 страниц
- **Гео**: AT, BA×2, BG×4, CR, CZ×2, DE×2, FR, HR, HU, ID, MK, PL×2, PT, RO, RS×3, SI
- **Суб-вертикали**: incontinence (8), joints (9), parasites (5), prostate (1)

## По офферам

### Cystiolla (VSL, incontinence) — 6 гео
| ID | GEO | SID | Язык | Видео | Цена |
|----|-----|-----|------|-------|------|
| hr_nutra_cystiolla | HR | 2443 | hr | HR666.mp4 | 78→39 EUR |
| cz_nutra_cystiolla | CZ | 1353 | cs | CZ1.mp4 | 1840→920 CZK |
| fr_nutra_cystiolla | FR | 3729 | fr | FR1.mp4 | 78→39 EUR |
| pt_nutra_cystiolla | PT | 2565 | pt | PT1111.mp4 | 78→39 EUR |
| pl_nutra_cystiolla | PL | 1385 | pl | PL1.mp4 | 310→155 PLN |
| de_nutra_cystiolla | DE | 3354 | de | DE11.mp4 | 78→39 EUR |

### Flexosamine (VSL, joints) — 2 гео
| ID | GEO | SID | Язык | Видео | Цена |
|----|-----|-----|------|-------|------|
| de_nutra_flexosamine | DE | 2461 | de | preview.ink/…mp4 | 98→49 EUR |
| cr_nutra_flexosamine | CR | 3874 | es | media/video.mp4 | 49980→24990 CRC |

### Nautubone (VSL, joints) — 1 гео
| ID | GEO | SID | Цена |
|----|-----|-----|------|
| ba_nutra_nautubone | BA | 2835 | 110→55 KM |

### CY-Relief (VSL, incontinence) — 1 гео
| ID | GEO | SID | Цена |
|----|-----|-----|------|
| ba_nutra_cyrelief | BA | 2735 | 110→55 KM |

### Uro UP Forte (VSL, prostate) — 1 гео
| ID | GEO | SID | Цена |
|----|-----|-----|------|
| at_nutra_uroupforte | AT | 2662 | 78→39 EUR |

### Parazol (VSL, parasites) — 1 гео
| ID | GEO | SID | Цена |
|----|-----|-----|------|
| bg_nutra_parazol | BG | 2722 | 78→39 EUR |

### Femino Plus (VSL, incontinence) — 1 гео
| ID | GEO | SID | Цена |
|----|-----|-----|------|
| rs_nutra_feminoplus | RS | 4695 | 2980→1490 RSD |

### Advertorial — parasites (4 страницы)
| ID | GEO | SID | Формат |
|----|-----|-----|--------|
| bg_nutra_parasites01 | BG | 2722 | article |
| rs_nutra_parasites01 | RS | 2691 | article |
| rs_nutra_parasites02 | RS | 2691 | article |
| si_nutra_parasites01 | SI | 2720 | article |

### Advertorial — joints (7 страниц)
| ID | GEO | SID | Формат |
|----|-----|-----|--------|
| pl_nutra_joints01 | PL | 1397 | article |
| hu_nutra_incontinence01 | HU | 2542 | article |
| bg_nutra_joints01 | BG | 2804 | article |
| bg_nutra_joints02 | BG | 2804 | article |
| ro_nutra_joints01 | RO | 2828 | article |
| mk_nutra_joints01 | MK | 2694 | article |
| id_nutra_joints01 | ID | 2897 | article |
| cz_nutra_joints01 | CZ | 2406 | article |

## Структурные паттерны

### VSL-страницы (14 шт.)
- Видео-элемент (autoplay, без controls)
- Форма заказа → `/order.php` с трекерными макросами (`{fbpx}`, `{subid}`, `{campaign_id}`, `{hash}`)
- Блок ТВ-логотипов ("Как видели на ТВ")
- Фейковые Facebook-комментарии (5-15 шт.)
- Обратный отсчёт / таймер
- Скидка -50%, отображение старой/новой цены
- Фейковый дефицит ("Осталось 17 упаковок")
- Клоак-скрипт (у 12 из 14): редирект для ru-locale + direct traffic

### Advertorial-страницы (11 шт.)
- Формат фейковой новостной статьи
- Вымышленные/реальные врачи с полными именами
- Фейковые отзывы пациентов
- Без видео, без блока комментариев
- Трекерные макросы в формах
- Без клоак-скриптов

## Дубли (отброшены)
- `bad50da4` = дубль `10af924a` (hr_nutra_cystiolla)
- `ad7c1cf1` = дубль `9d5c6b1f` (mk_nutra_joints01)
