#!/usr/bin/env bash
# Re-export every .drawio source in this directory to .png and .svg.
# Run after editing any .drawio file here.
#
# --svg-theme light is required: drawio's default (auto) emits CSS
# light-dark()/color-scheme, which makes the diagram invert colors
# under a dark OS/browser theme. Sphinx has no dark-mode support, so
# the exported SVG must stay pinned to the light palette.
set -euo pipefail
cd "$(dirname "$0")"

DRAWIO=$(command -v drawio || echo /opt/drawio/drawio)

for src in *.drawio; do
  base="${src%.drawio}"
  "$DRAWIO" --export --format png --embed-diagram --output "${base}.png" "$src"
  "$DRAWIO" --export --format svg --svg-theme light --embed-diagram --output "${base}.svg" "$src"
done
