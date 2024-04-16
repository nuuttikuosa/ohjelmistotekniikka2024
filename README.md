# Videopokeri

Tämän sovelluksen avulla voi pelata videopokeria. Ohjelma on kirjoitettu Pythonilla.

## Python-versiosta
Ohjelma on testattu Pythonon 3.8. Oletettavasti ei toimi vanhemmilla versioilla.

## Dokumentaatio
- [Vaatimusmäärittely](./videopoker/documentation/requirements.md)
- [Arkkitehtuurikuvaus](./videopoker/documentation/arkkitehtuuri.md)
- [Työaikakirjanpito](./videopoker/documentation/working_hours.md)
- [Changelog](./videopoker/documentation/changelog.md)

## Asennus

1. Asenna riippuvuudet komennolla:

```bash
poetry install
```
2. Käynnistä sovellus komennolla:
```bash
poetry run invoke start
```

## Komentorivitoiminnot

### Testaus

Testit suoritetaan komennolla:

```bash
poetry run invoke test
```

### Testikattavuus

Testikattavuusraportti generoidaan komennolla:

```bash
poetry run invoke coverage-report
```

Raportti löytyy _htmlcov_-hakemistosta.

### Pylint

Tiedoston [.pylintrc](./videopoker/.pylintrc) määrittelemät tarkistukset voi suorittaa komennolla:

```bash
poetry run invoke lint