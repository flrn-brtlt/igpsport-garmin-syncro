# iGPSPORT Garmin Sync

Automatische Synchronisation von Aktivitäten von iGPSPORT zu Garmin Connect über GitHub Actions.

## Features

- Automatischer Login bei iGPSPORT
- Download neuer FIT-Dateien
- Upload nach Garmin Connect
- Automatische Ausführung über GitHub Actions
- Keine lokale Hardware erforderlich
- Kostenlos nutzbar

## Voraussetzungen

- iGPSPORT Account
- Garmin Connect Account
- GitHub Account

## Installation

### 1. Repository forken

Forke dieses Repository in deinen eigenen GitHub-Account.

### 2. GitHub Secrets anlegen

Öffne:

Settings → Secrets and variables → Actions

Lege folgende Secrets an:

| Name | Beschreibung |
|--------|--------|
| IGPSPORT_USER | iGPSPORT Benutzername |
| IGPSPORT_PASSWORD
