# Videopokeri

Tämän sovelluksen avulla voi pelata videopokeria. Ohjelma on kirjoitettu Pythonilla.

## Releases
Ohjelman loppujulkaisu (Release) - versio_1.0 löytyy [täältä](https://github.com/nuuttikuosa/ohjelmistotekniikka2024/releases/tag/versio_1.0) 


## Python-versiosta
Ohjelma on testattu Pythonon 3.8. Oletettavasti ei toimi vanhemmilla versioilla.

## Dokumentaatio
- [Käyttöohje](./videopoker/documentation/kayttoohje.md)
- [Vaatimusmäärittely](./videopoker/documentation/requirements.md)
- [Arkkitehtuurikuvaus](./videopoker/documentation/arkkitehtuuri.md)
- [Testausraportti](./videopoker/documentation/testiraportti.MD)
- [Työaikakirjanpito](./videopoker/documentation/working_hours.md)
- [Changelog](./videopoker/documentation/changelog.md)

  
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
```
# Korttikuvien lähde
Pelissä käytetyt pelikorttien kuvat ovat public domain ja kuvien tekijä pyysi mainitsemaan lähteen:
https://tekeye.uk/playing_cards/svg-playing-cards

If you have found these Public Domain SVG Playing Card images useful please 
provide a link to this article, it would be appreciated for the hard work 
that has gone into creating and maintaining this resource. 

Drop me an email, dan@tekeye.uk with information on your completed project 
that uses these playing card images and I will add a link to it.

