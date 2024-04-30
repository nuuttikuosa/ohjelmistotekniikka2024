# Videopokeri

Tämän sovelluksen avulla voi pelata videopokeria. Ohjelma on kirjoitettu Pythonilla.

## Releases
Ohjelman toinen julkaisu (Release) - viikko6 löytyy [täältä](https://github.com/nuuttikuosa/ohjelmistotekniikka2024/releases/tag/viikko5) 

## Koodikatselmointi

[Nostettu issue löytyy täältä](https://github.com/iita-mari/ot-harjoitustyo/issues/1)


## Python-versiosta
Ohjelma on testattu Pythonon 3.8. Oletettavasti ei toimi vanhemmilla versioilla.

## Dokumentaatio
- [Vaatimusmäärittely](./videopoker/documentation/requirements.md)
- [Arkkitehtuurikuvaus](./videopoker/documentation/arkkitehtuuri.md)
- [Työaikakirjanpito](./videopoker/documentation/working_hours.md)
- [Changelog](./videopoker/documentation/changelog.md)
- [Käyttöohje](./videopoker/documentation/kayttoohje.md)
  
## Asennus

1. Asenna riippuvuudet komennolla:

```bash
poetry install
```

2. Suorita vaadittavat alustustoimenpiteet komennolla:

```bash
poetry run invoke build
```

3. Käynnistä sovellus komennolla:
```bash
poetry run invoke start
```
4. Tai vaihtoehtoisesti alustava graafisen käyttöliittymän versio komennolla
```bash
poetry run invoke startGUI
```

## Komentorivitoiminnot

### Ohjelman suorittaminen

Ohjelman pystyy suorittamaan komennolla:

```bash
poetry run invoke start
```
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
