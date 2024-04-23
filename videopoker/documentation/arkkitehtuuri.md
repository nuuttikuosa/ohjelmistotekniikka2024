# Arkkitehtuurikuvaus

## Päätoiminnallisuudet

Kuvataan seuraavaksi sovelluksen toimintalogiikka  päätoiminnallisuuden osalta sekvenssikaaviona.

Käyttäjä päättää pelata kierroksen videopokeria. Ohjelma jakaa hänelle käden ja arvioi käden korttiyhdistelmät. Käyttää voi halutessaan vaihtaa kortteja kädessä ja ohjelma vaihtaa kortit, arvioi kortityhdistelmät ja laskee käyttäjän voiton ja päivittää käyttäjän pelitilin saldon.
![Sekvenssikaavio](./kuvat/sekvenssi-pelin_kulku.png)

## Rakenne

Ohjelman rakenne noudattelee kolmitasoista kerrosarkkitehtuuria, ja ohjelman luokkakaavio on seuraavanlainen:

![Luokkakaavio](./kuvat/arkkitehtuuri-luokkakaavio.png)
