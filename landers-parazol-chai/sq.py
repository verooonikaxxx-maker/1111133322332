# -*- coding: utf-8 -*-
import sys; sys.path.insert(0,'/tmp/claude-0/tea')
from repl import apply
A = "['’ʼ]"   # прямой и типографский апостроф

R = [
 (r'Përbërja e kapsulave natyrore Parazol sipas',            'Përbërja e çajit bimor Parazol sipas'),
 (r'në kapsula natyrore të arritshme për të gjithë',         'në çaj bimor të arritshëm për të gjithë'),
 (r'— kapsula natyrore që veprojnë pikërisht atje ku duhet', '— çaj bimor që pihet dhe vepron pikërisht atje ku duhet'),
 (r'Në përbërjen e kapsulave Parazol',                       'Në përbërjen e çajit Parazol'),
 (r'Rezultati — kapsula që veprojnë',                        'Rezultati — një çaj që vepron'),
 (r'I merrni dy herë në ditë',                               'E pini dy herë në ditë'),
 (r'te kapsulat Parazol është se ato jo vetëm i lehtësojnë simptomat — por aktivizojnë',
                                                             'te çaji Parazol është se ai jo vetëm i lehtëson simptomat — por aktivizon'),
 (r'Kapsulat merren, dhe mikroekstraktet',                   'Çaji pihet, dhe mikroekstraktet'),
 (r'Që nga kapsula e parë',                                  'Që nga gota e parë'),
 (r'u mundëson kapsulave t' + A + r'i çojnë lëndët aktive',  'i mundëson çajit t’i çojë lëndët aktive'),
 (r'Merrni kapsulat dy herë në ditë',                        'Pini çajin dy herë në ditë'),
 (r'i sillte kapsulat Parazol nga',                          'i sillte çajin Parazol nga'),
 (r'Dy muaj marrje —',                                       'Dy muaj pirje —'),
 (r'Me kapsulat Parazol — 30 ditë marrje',                   'Me çajin Parazol — 30 ditë pirje'),
 (r'Merrte kapsulat Parazol çdo ditë',                       'Pinte çajin Parazol çdo ditë'),
 (r'paketime të kapsulave Parazol posaçërisht',              'paketime të çajit Parazol posaçërisht'),
 (r'kapsulat Parazol të rezervuara për ju do t' + A + r'i ofrohen të radhësit',
                                                             'çaji Parazol i rezervuar për ju do t’i ofrohet të radhësit'),
 (r'Dhjetë ditë i marr kapsulat në mëngjes',                 'Dhjetë ditë e pi çajin në mëngjes'),
 (r'I marr kapsulat prej 5 javësh',                          'E pi çajin prej 5 javësh'),
 (r'pas fillimit të marrjes së kapsulave',                   'pas fillimit të pirjes së çajit'),
 (r'Por kapsulat Parazol — kjo është krejt tjetër gjë',      'Por çaji Parazol — kjo është krejt tjetër gjë'),
 (r'Vazhdoj t' + A + r'i marr, por tashmë',                  'Vazhdoj ta pi, por tashmë'),
 (r'Fillova t' + A + r'i marr kapsulat Parazol dy herë në ditë',
                                                             'Fillova ta pi çajin Parazol dy herë në ditë'),
 (r'Më jep kapsula çdo mëngjes e mbrëmje',                   'Më bën çaj çdo mëngjes e mbrëmje'),
 (r'Tri javë me kapsulat dhe u ndjeva',                      'Tri javë me çajin dhe u ndjeva'),
 (r'të provonim kapsulat Parazol',                           'të provonim çajin Parazol'),
 (r'I jepja dy herë në ditë',                                'Ia bëja dy herë në ditë'),
 (r'Menjëherë fillova t' + A + r'i marr kapsulat',           'Menjëherë fillova ta pi çajin'),
 (r'Menjëherë fillova me i marrë kapsulat',                  'Menjëherë fillova me e pi çajin'),
 (r'Dy javë i marr dy herë në ditë',                         'Dy javë e pi dy herë në ditë'),
 (r'Kapsulat Parazol janë e vetmja gjë që më dha',           'Çaji Parazol është e vetmja gjë që më dha'),
 (r'TË VËRTETË — i marr dy herë në ditë',                    'TË VËRTETË — e pi dy herë në ditë'),
 (r'I marr kapsulat Parazol prej 50 ditësh',                 'E pi çajin Parazol prej 50 ditësh'),
 (r'më porositi kapsulat Parazol dhe më detyroi të provoja — m' + A + r'i jepte në mëngjes dhe në mbrëmje',
                                                             'më porositi çajin Parazol dhe më detyroi të provoja — ma bënte në mëngjes dhe në mbrëmje'),
 (r'Mora tre paketime kapsulash, për kurën e plotë',         'Mora tre paketime çaji, për kurën e plotë'),
]
U='/root/.claude/uploads/ebcc1709-ea34-5dd5-ad04-bda3b7359ce7/'
apply(U+'44e5c951-index.html', '/tmp/claude-0/tea/AL.html', R)
print()
apply(U+'384172fa-index.html', '/tmp/claude-0/tea/XK.html', R)
