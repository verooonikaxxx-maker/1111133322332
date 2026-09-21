# -*- coding: utf-8 -*-
import sys, re, os, html, importlib
sys.path.insert(0,'/tmp/claude-0/ro'); sys.path.insert(0,'/tmp/claude-0/st')
from nodes import index
WS=re.compile(r'^(\s*)(.*?)(\s*)$', re.S)
SRC='/root/.claude/uploads/ebcc1709-ea34-5dd5-ad04-bda3b7359ce7/43ee5151-index.html'

def build(mod, lang, country, dst, ph=None, alt=None):
    T=importlib.import_module(mod).T
    src,nodes,bad=index(SRC); assert not bad and len(nodes)==208
    assert sorted(T)==list(range(208)), mod
    imgs_b=re.findall(r'<img[^>]*src="([^"]*)"',src)
    out=src
    for i in sorted(T, reverse=True):
        o,l,orig=nodes[i]
        ol,_,ot=WS.match(orig).groups(); ml,core,mt=WS.match(T[i]).groups()
        out=out[:o]+((ml or ol)+html.escape(core,quote=False)+(mt or ot) if core else (ml or ol)+(mt or ot))+out[o+l:]
    out=re.sub(r'(<html[^>]*\blang=")[^"]*(")', lambda m:m.group(1)+lang+m.group(2), out, count=1)
    out=out.replace('name="country" value="HU"','name="country" value="%s"'%country)
    for a,b in (ph or {}).items(): out=out.replace('placeholder="%s"'%a,'placeholder="%s"'%b)
    for a,b in (alt or {}).items(): out=out.replace('alt="%s"'%a,'alt="%s"'%b)
    os.makedirs(os.path.dirname(dst),exist_ok=True)
    open(dst,'w',encoding='utf-8').write(out)
    s2,n2,b2=index(dst)
    imgs_a=re.findall(r'<img[^>]*src="([^"]*)"',s2)
    assert len(n2)==208 and not b2, mod
    assert imgs_a==imgs_b, 'пути к картинкам изменились: '+mod
    for tag in ('<img','<form','<input','<button','<script','<style','<table','<tr','<td','<th','<li','<h1','<h2'):
        assert src.count(tag)==s2.count(tag), '%s: %s %d→%d'%(mod,tag,src.count(tag),s2.count(tag))
    hu=len(re.findall(r'\b(?:hogy|nem|van|amely|ízület|magyar|Magyarország|és|egy|ezt|akik)\b',s2))
    print('%-3s узлов %d | теги ок | картинки ок | lang=%s country=%s sid=%s | венгерских слов осталось: %d'%(
      country,len(n2),
      re.search(r'<html[^>]*lang="([^"]*)"',s2).group(1),
      re.search(r'name="country" value="([^"]*)"',s2).group(1),
      re.search(r'name="sid" value="([^"]*)"',s2).group(1), hu))
    return s2
