# Käyttöohje

Lataa projektin viimeisimmän [releasen](https://github.com/ohjelmistotekniikka-hy/python-todo-app/releases) lähdekoodi valitsemalla _Assets_-osion alta _Source code_.

## Konfigurointi

Tallennukseen käytettävän tietokannan nimeä voi konfiguroida muokkaamalla käynnistyshakemistossa olevaa _config.py_-tiedostoa. Tietokanta luodaan _data_-hakemistoon, jos sitä ei ole. Konfiguraation muoto on seuraava:

```
DATABASE_FILENAME = "game_database.sqlite"
```

## Ohjelman käynnistäminen

Ennen ohjelman käynnistämistä, asenna riippuvuudet komennolla:

```bash
poetry install
```

Jonka jälkeen suorita alustustoimenpiteet komennolla:

```bash
poetry run invoke build
```

Nyt ohjelman voi käynnistää komennolla tekstikäyttöliittymään:

```
poetry run invoke start
```
ja graafiseen käyttöliittymään:

```
poetry run invoke startGUI
```

## Kirjautuminen

Sovellus käynnistyy kirjautumisnäkymään:

![](./kuvat/kayttoohje-kirjautuminen.png)

Kirjautuminen onnistuu kirjoittamalla gamename syötekenttään ja painamalla "Login"-painiketta.

## Videopokerin pelaaminen

Peli jakaa käyttäjälle viisi korttia, joista jokaisen alla on lukitsemispainike, jollla lukitaan ne kortit jotka halutaa pitää toiselle kierrokselle.

## Videopokerin pelaamisen lopettaminen
Kun käyttäjä päättää lopettaa videopokerin pelaamisen, niin sovellus tallentaa pelitilin saldon tietkantaa seuraavaa pelisessiota varten.
