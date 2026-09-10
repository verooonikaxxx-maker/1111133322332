#!/usr/bin/env bash
# Выкачивает картинки для RO-адаптаций. Запускать НА СВОЕЙ машине —
# в облачной сессии Claude Code исходящий трафик режется allow-list'ом.
#
#   bash fetch-images.sh <папка-с-index.html> <база>
#
# <база> — URL каталога, где лежит исходный ленд, например:
#   https://pro1.trk.dev/lander/sustavi-mk-nautubone-.../
# Скрипт читает пути прямо из index.html, так что ничего не надо перечислять руками.

set -uo pipefail

DIR="${1:?укажите папку с index.html}"
BASE="${2:-}"
HTML="$DIR/index.html"
[ -f "$HTML" ] || { echo "нет файла $HTML"; exit 1; }

get() { # $1 url, $2 dest
  mkdir -p "$(dirname "$2")"
  if command -v wget >/dev/null 2>&1; then
    wget -q --tries=3 --timeout=25 -O "$2" "$1"
  else
    curl -fsSL --retry 3 --max-time 25 -o "$2" "$1"
  fi
}

ok=0; fail=0

# --- внешние картинки (static.joxi.pro и прочие) ---
grep -oE 'src="https?://[^"]+\.(jpg|jpeg|png|webp|gif)"' "$HTML" \
  | sed 's/^src="//; s/"$//' | sort -u | while read -r url; do
    name="images/ext/$(basename "${url%%\?*}")"
    if get "$url" "$DIR/$name"; then echo "OK   $url"; else echo "FAIL $url"; fi
  done

# --- локальные картинки: тянем из каталога исходного ленда ---
if [ -n "$BASE" ]; then
  BASE="${BASE%/}"
  grep -oE 'src="(images|js)/[^"]+"' "$HTML" | sed 's/^src="//; s/"$//' | sort -u | while read -r rel; do
    if [ -f "$DIR/$rel" ]; then echo "SKIP $rel (уже есть)"; continue; fi
    if get "$BASE/$rel" "$DIR/$rel"; then echo "OK   $rel"; else echo "FAIL $rel"; fi
  done
else
  echo
  echo "Второй аргумент (база) не задан — локальные images/ не качались."
  echo "Нужно: bash fetch-images.sh \"$DIR\" https://pro1.trk.dev/lander/<папка>/"
fi

echo
echo "Готово. Проверка недостающих:"
grep -oE 'src="(images|js)/[^"]+"' "$HTML" | sed 's/^src="//; s/"$//' | sort -u | while read -r rel; do
  [ -f "$DIR/$rel" ] || echo "  нет: $rel"
done
