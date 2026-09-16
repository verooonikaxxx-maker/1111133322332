# -*- coding: utf-8 -*-
"""Меняем ТОЛЬКО форму препарата: капсулы -> чай. Работаем внутри текстовых узлов,
имена, города, цены, разметку и всё остальное не трогаем."""
import sys, re, io, html
sys.path.insert(0, '/tmp/claude-0/ro')
from nodes import index

WS = re.compile(r'^(\s*)(.*?)(\s*)$', re.S)
AP = "['’ʼ]"          # обычный и типографский апостроф


def apply(src_path, dst_path, rules, probe=r'kapsul'):
    src, nodes, bad = index(src_path)
    assert not bad
    targets = [i for i, (o, l, d) in enumerate(nodes) if re.search(probe, d, re.I)]
    out = src
    hits = {}
    for i in sorted(targets, reverse=True):
        o, l, orig = nodes[i]
        lead, core, tail = WS.match(orig).groups()
        new = core
        for pat, rep in rules:
            new2 = re.sub(pat, rep, new)
            if new2 != new:
                hits[pat] = hits.get(pat, 0) + 1
                new = new2
        if new == core:
            continue
        out = out[:o] + lead + html.escape(new, quote=False) + tail + out[o + l:]
    io.open(dst_path, 'w', encoding='utf-8').write(out)

    s2, n2, b2 = index(dst_path)
    left = [(i, ' '.join(d.split())[:90]) for i, (o, l, d) in enumerate(n2) if re.search(probe, d, re.I)]
    unused = [p for p, _ in rules if p not in hits]
    print('%-22s узлов %d->%d | сбитых %d | тегов <img> %d->%d | правил сработало %d/%d'
          % (dst_path.split('/')[-1], len(nodes), len(n2), len(b2),
             src.count('<img'), s2.count('<img'), len(hits), len(rules)))
    if unused:
        print('   ПРАВИЛА БЕЗ СРАБАТЫВАНИЯ:', unused)
    print('   осталось упоминаний «%s»: %d' % (probe, len(left)))
    for i, t in left:
        print('      %3d | %s' % (i, t))
    return len(left), unused
