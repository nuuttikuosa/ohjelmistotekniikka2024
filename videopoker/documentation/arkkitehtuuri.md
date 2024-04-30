# Arkkitehtuurikuvaus

Ohjelman rakenne noudattelee kolmikerrosarkkitehtuuria, ja koodin pakkausrakenne on seuraava:

![Pakkausrakenne](./kuvat/arkkitehtuuri-pakkaus.png)

Pakkaus _ui_ sisältää käyttöliittymäkoodin, _services_ sovelluslogiikan ja _repositories_ tietojen pysyväistallennuksesta vastaavan koodin. Pakkaus _entities_ sisältää luokkia, jotka kuvaavat sovelluksen käsitteellisiä objekteja.

## Käyttöliittymä

Käyttöliittymä sisältää kolme erillistä näkymää:

- Kirjautuminen
- Videopokeri pelin

Kaikki äkymät on toteuteuttu omina luokkinaan. Näkymistä yksi on aina kerrallaan näkyvänä. Näkymien näyttämistä koordinoi [UI](../src/ui/ui.py)-luokka. Käyttöliittymä on pyritty eristämään täysin sovelluslogiikasta, joka on palvelukerroksessa. Käyttöliittymä kutsuu [TodoService](../src/services/todo_service.py)-luokan metodeja.

Sovelluksen pelaaminen on hyvin samanlaista eri käyttäjille, vain käyttäen pelitilin saldo on käyttäjäkohtainen. Yksi kierros peliä maksaa yhden yksikön ja voitot määräytyvät voittotaulukon mukaan.

## Päätoiminnallisuudet

Kuvataan seuraavaksi sovelluksen toimintalogiikka  päätoiminnallisuuden osalta sekvenssikaaviona.

Alussa käyttäjä kirjautuu sovellukseen antamalla nimensä. Sovellus hakee tietokannasta käyttäjän pelitilin saldon. Seuraavaksi sovellus hakee tietokannasta oletuspelin, _jätkä tai parempi_ tiedot ja voittotaulukon. 

Käyttäjä päättää pelata kierroksen videopokeria. Ohjelma jakaa hänelle käden ja arvioi käden korttiyhdistelmät. Käyttää voi halutessaan vaihtaa kortteja kädessä ja ohjelma vaihtaa kortit, arvioi kortityhdistelmät ja laskee käyttäjän voiton ja päivittää käyttäjän pelitilin saldon.
![Sekvenssikaavio](./kuvat/sekvenssi-pelin_kulku.png)

Kehitysversiossa kortit käytetään käyttöliittymällä kirjainyhdistelminä, mutta seuraavassa versiossa otetaan käyttöön png-tyyppiset kuvat pelikorteille.

## Rakenne

Ohjelman luokkakaavio on seuraavanlainen:

![Luokkakaavio](./kuvat/arkkitehtuuri-luokkakaavio.png)

## Ohjelman rakenteeseen jääneet heikkoudet

## Videopokerikäsien arviointi
Keskeinen arviointifunktio on hieman liian pitkä ja monimutkainen. Pylint ilmoittaa liian pitkistä ja monimutkaisista metodeista luokan PokerHandEvaluator metodissa basic_evaluation. Evaluointi on kuitenkin logiikaltaan sellainen, että jos se jaettaisiin kahteen funktioon, niin koodin looginen ymmärrettävyys kärsisi, joten olen pitänyt tämän toiminnallisuuden yhtenä kokonaisuutena. Periaatteessa suorien ja värien arvioinnin voi eriyttää muutta käden arvioinnista. 

### Käyttöliittymä

Käyttöliittymän tyhmittelyä voisi parantaa rajattomasti, mutta koska en ole kovinkaan visuaalinen henkilö. Oikeassa ohjelmistoprojektissa käyttöliittymän viilaus olisi UX designerin eikä toteuttajan tehtävä.
