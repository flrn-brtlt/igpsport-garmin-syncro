name: iGPSPORT Sync

on:
  schedule:
    - cron: '*/30 * * * *'

  workflow_dispatch:

jobs:
  sync:
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v4

      - name: Python installieren
        uses: actions/setup-python@v5
        with:
          python-version: '3.11'

      - name: Pakete installieren
        run: pip install -r requirements.txt

      - name: Sync starten
        env:
          IGPSPORT_USER: ${{ secrets.IGPSPORT_USER }}
          IGPSPORT_PASSWORD: ${{ secrets.IGPSPORT_PASSWORD }}
          GARMIN_USER: ${{ secrets.GARMIN_USER }}
          GARMIN_PASSWORD: ${{ secrets.GARMIN_PASSWORD }}
        run: python sync.py
