# Käyttöohje

Lataa projektin viimeisimmän [releasen](https://github.com/ohjelmistotekniikka-hy/python-todo-app/releases) lähdekoodi valitsemalla _Assets_-osion alta _Source code_.

## Konfigurointi

Tallennukseen käytettävän tietokannan nimeä ja lokitiedostojen nimiä voi muuttaa muokkaamalla käynnistyshakemistossa olevaa _.env_-tiedostoa. Tietokanta luodaan _data_-hakemistoon build komennolla, jos sitä ei ole. Lokitiedostot sijaitsevat _logs_-hakemistossa  Konfiguraation muoto on seuraava:

```
DATABASE_FILENAME=game_database.sqlite
GAME_EVENT_LOG_FILENAME = game_event_log.log
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

```bash
poetry run invoke start
```

## Pelitilin valinta

Sovellus käynnistyy Peliprofiilinäkymään:

![](./kuvat/login-ikkuna.png)

Ikkunassa näkyy tietokannassa olevat pelaajaprofiilit ja niiden pelitilien saldot. On mahdollista valita olemassa oleva pelaajaprofiili kirjoittamalla pelaajaprofiilin nimi tai voidaan luoda uusi pelaajaprofiili kirjoittamalla uuden pelaajaprofiilin nimi.

Pelaaminen alkaa painamalla "Play"-painiketta.

## Videopokerin pelaaminen

Pelaajaprofiilin valitsemisen jälkeen siirrytään videopokerin pelaus näkymään:

![](./kuvat/videopokerin-pelaaminen-kierros-yksi.png)

Näytön yläkulmassa näkyy peliprofiilin nimi ja profiilin pelitilin saldo.

Peli jakaa käyttäjälle viisi korttia, joista jokaisen alla on lukitsemispainike "Valitse", jolla lukitaan ne kortit, jotka halutaan pitää toiselle kierrokselle. Valittu kortti voidaan vapauttaa eli poistaa valituista painamalla "Vapauta"

Eri korttiyhdistelmien voitot näkyvät pelikorttien alla olevassa ikkunassa. Esim. kuninkaallisesta värisuorasta (värisuora ässästä kymppiin) saa 800 kolikkoa ja jätkäparista tai isommasta saa yhden kolikon.

Kun painetaan "Vaihda Kortteja" ikkunan oikeassa alakulmassa, niin halutut kortit vaihdetaan ja paras korttiyhdistelmä arvioidaan:

![](./kuvat/videopokerin-pelaaminen-kierros-kaksi.png)

Nyt ikkunan alalaidassa näkyy, voitettiinko jotain ja jos voitettiin, niin kuinka paljon.

Kun painetaan "Jaa uusi käsi", niin ohjelma jakaa pelaajalle 5 uutta korttia.

## Videopokerin pelaamisen lopettaminen

Painamalla ikkunan oikeassa yläkulmassa olevaa "Lopeta Pelaaminen" painiketta käyttäjä voi lopettaa pelaamisen. Tällöin sovellus palaa peliprofiilinäkymään.

Kun käyttäjä lopettaa videopokerin pelaamisen, niin sovellus tallentaa pelitilin saldon tietokantaa seuraavaa pelisessiota varten.
