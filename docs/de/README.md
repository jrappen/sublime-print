# `print` Erweiterung für [Sublime Text](https://www.sublimetext.com)

> Drucke eine Vorschau deines Sublime Text Codes in deinem Browser.

* [Dokumentation](#dokumentation)
* [Voraussetzungen](#voraussetzungen)
* [Installation](#installation)
* [Verwendung](#verwendung)
* [Quellcode](#quellcode)
* [Spenden](#spenden)

## Dokumentation

> Eine plug-in Dokumentation ist über das Menü oder die Kurzbefehleingabe (command palette) verfügbar.

* Englisch (English):
  <https://github.com/jrappen/sublime-print/blob/master/docs/en/README.md>
* Deutsch:
  <https://github.com/jrappen/sublime-print/blob/master/docs/de/README.md>

### Code of conduct

<https://github.com/jrappen/.github/blob/master/CODE_OF_CONDUCT.md>

### Contributing guide

<https://github.com/jrappen/.github/blob/master/CONTRIBUTING.md>

## Voraussetzungen

print ist als Erweiterung für die **neusten Build** von Sublime Text gedacht und erfordert im Moment **`Build 4074`** oder neuer.

* Lade [Sublime Text](https://www.sublimetext.com) herunter
* Installiere Package Control über den Eintrag `Tools > Install Package Control` im Menü
    * Schließe und öffne Sublime Text nach der Installation von Package Control.

## Installation

Die Verwendung von **Package Control** wird vorausgesetzt, da es deine Erweiterungen (mit ihren Abhängigkeiten) aktuell hält.

### Installation über Package Control

* Öffne die Befehlseingabe (`Tools > Command Palette`).
* Wähle `Preferences: Package Control - User`.

```jsonc
//  Packages/User/Package Control.sublime-settings

{
    "installed_packages":
    [
        "print"
    ],
    "repositories":
    [
        "https://raw.githubusercontent.com/jrappen/sublime-print/master/package_control_channel.json"
    ]
}
```

## Verwendung

print generiert eine Vorschau für das Drucken von Sublime Text Code.

Du kannst:

* eine Vorschau von Markdown als HTML in Sublime erzeugen
* eine Vorschau von Markdown als HTML in deinem Standardbrowser erzeugen
* eine eingefärbte Vorschau deines Codes in deinem Standardbrowser erzeugen
* deinen Code als eingefärbetes HTML Schnipsel in die Zwischenablage kopieren

Du findest die Einträge `Print: ...` in:

* der Befehlszeile (`Tools > Command Palette`)
* oder das Kontextmenü (rechts-Click)

### Bekannte Probleme mit der Markdown Vorschau

* die Vorschau für Markdown ist limitiert auf
  [mini-HTML](https://www.sublimetext.com/docs/minihtml.html)
    * HTML Kommentare brechen die Vorschau (an jenem Punkt)
* [`mdpopups`](https://github.com/facelessuser/sublime-markdown-popups)
  verwendet
  [`python-markdown`](https://github.com/facelessuser/sublime-markdown)
  und
  [`pymdownx`](https://github.com/facelessuser/sublime-pymdownx),
  welche eine Einrückung um 4 Leerzeichen verwenden

## Quellcode

<https://www.github.com/jrappen/sublime-print)>

### Lizenz

<https://github.com/jrappen/sublime-print/blob/master/LICENSE>

### Feedback

Verwende für Feedback bitte die Befehlseingabe (command palette) oder das Menü.

## Spenden

<https://www.paypal.me/jrappen>
