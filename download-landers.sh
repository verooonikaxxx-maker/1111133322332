#!/usr/bin/env bash
# Выгрузка транзиток на суставы с сервера Keitaro (pro1.trk.dev).
# Тянет каждую директорию /lander/... целиком: index.html + images/ + js/.
# Запуск:  bash download-landers.sh [папка-назначения]
# По умолчанию складывает в ./landers-sustavy

set -uo pipefail

BASE="https://pro1.trk.dev"
DEST="${1:-./landers-sustavy}"

# offer_id|ГЕО|краткое имя|путь к директории
LANDERS=(
"33384|MK|nautubone-te-kto-ne-verit-v2-TSL|/lander/sustavi-mk-nautubone-te--cto-ne-verit-v-silu-prirodi-v2--mba-_1785501219/"
"34440|BG|nautubone-padre-v4-gel-TSL|/lander/019e8dd7-906b-758a-ac83-b37645bab49b_1786198368/"
"33381|BA|nautubone-kemal-dizdarevic-VSL|/lander/9da651d2-5d49-4987-949a-1fd8118c43ae_1785500964/"
"34677|CR|flexosamine-carlos-estrada-v3-VSL|/lander/925bb0cc-4f8f-4a65-9e03-825a242f5bcd_1786441669/"
"34439|CZ|arthrovia-padre-v3-gel-TSL|/lander/-30771--sustavi-cz-arthrovia-molodoy-vrach-v-dome-prestarelih-v3--ika-_1786198355/"
"34437|RO|jointerra-102-letniy-ortoped-v4-TSL|/lander/sustavi-ro-jointerra-102-letniy-ortoped-v4-yda--capsuli_1786196248/"
"34676|DE|flexosamine-drosten-v2|/lander/019d4d9a-050a-78be-bc63-6151060ad540_1786441578/"
)

mkdir -p "$DEST"

have() { command -v "$1" >/dev/null 2>&1; }

if have wget; then
  MODE=wget
elif have curl; then
  MODE=curl
else
  echo "Нужен wget или curl. На маке: brew install wget" >&2
  exit 1
fi

echo "Режим: $MODE   →   $DEST"
echo

ok=0; fail=0

for row in "${LANDERS[@]}"; do
  IFS='|' read -r id geo slug path <<< "$row"
  out="$DEST/${id}_${geo}_${slug}"
  mkdir -p "$out"
  echo "── $id  $geo  $slug"

  if [ "$MODE" = wget ]; then
    # зеркалим всю директорию лендера
    wget -q --show-progress -r -np -nH -e robots=off \
         --cut-dirs=2 -P "$out" -R "index.html?*" \
         "$BASE$path" || true
  else
    # curl: тянем index.html и все относительные ссылки из него
    if ! curl -fsSL "$BASE$path" -o "$out/index.html"; then
      echo "   ! index.html не скачался"; fail=$((fail+1)); continue
    fi
    grep -Eo '(src|href)[[:space:]]*=[[:space:]]*"[^"]+"' "$out/index.html" \
      | sed -E 's/^[^"]*"//; s/"$//' \
      | grep -Ev '^(https?:|//|data:|#|mailto:|javascript:)' \
      | sort -u \
      | while read -r rel; do
          mkdir -p "$out/$(dirname "$rel")"
          curl -fsSL "$BASE$path$rel" -o "$out/$rel" || echo "   ! $rel"
        done
  fi

  n=$(find "$out" -type f | wc -l | tr -d ' ')
  if [ "$n" -gt 0 ]; then
    echo "   ok, файлов: $n"
    ok=$((ok+1))
  else
    echo "   ! пусто"
    fail=$((fail+1))
  fi
  echo
done

echo "Готово. Успешно: $ok, с ошибками: $fail"
echo "Папка: $DEST"
echo
echo "Примечание: страницы подключают jQuery 3.6.0 с cdnjs — для локального"
echo "просмотра нужен интернет, либо скачайте jquery.min.js и поправьте путь."
