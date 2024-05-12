# Testausraportti 12.5.2024

Videopokeri-sovellukselle on suoritettu manuaalinen järjestelmätesti. Tämän lisäksi sovellusta on testattu automaattisesti yksikkö- ja integraatiotestein unittestilla ennen jokaista koodin pushausta githubiin.

## Yksikkö- ja integraatiotestaus
### Sovelluslogiikka
Sovelluslogiikasta vastaavaa VideoPokerService-luokkaa testataan TestVideoPokerService-testiluokalla.
Sovelluksessa on käytössä satunnaisuuteen perustuva Dealer-luokka. TodoService-olio alustetaan, niin että sille injektoidaan riippuvuudeksi Dealer-olio, joka on testeissä alustettu aina samalla seed arvolla (seed = 3). Tällä tavalla Dealer-olio jakaa aina samat kortit.
TodoService-luokkaa testataan yksikkötesteissä siten, että sille on injektoitu riippuvuudeksi repositorio-oliot, jotka tallentavat tietoa muistiin pysyväistallennuksen sijaan. Tätä varten testissä on käytössä luokat FakeGameRepository ja FakeUserRepository.

Tämän lisäksi tehdään automatisoitu integraatiotestaus, jossa käytetään TodoService-luokan oliota, jotka käyttää tietokantaan yhteydessä olevia repository-luokkia, jotka palauttavat tiedot testitietokannasta.

Automatisoidussa integraatiotestauksessa käytössä oleva testitietokanta generoidaan aina uudestaan samanlaiseksi ennen testauksen aloittamista.

# Repositorio-luokat
Repositorio-luokkia TodoRepository ja UserRepository testataan ainoastaan testeissä käytössä olevilla tiedostoilla. Tiedostojen nimet on konfiguroitu .env.test-tiedostoon. TodoRepository-luokkaa testataan TestTodoRepository-testiluokalla ja UserRepository-luokkaa TestUserRepository-testiluokalla.
Repositorio-luokkaa ImageRepository luokkaa testataan samoilla kuvatiedostoilla, jotka ovat käytössä myös varsinaisessa sovelluksessa, koska näille suoritetaan ainoastaan lukuoperaatioita.

# Entiteeti-luokat
Sovelluksessa on seuraavat entiteettiluokat: PlayingCard, Dealer, Deck, Game, PokerHandd, HandValue, PayoutTable, PokerHandEvaluator ja User. Näillä on vastaavat testiluokat, jotka sisältävät entiteettien yksikkötestit.


### Testauskattavuus
Käyttöliittymäkerrosta lukuunottamatta sovelluksen testauksen haarautumakattavuus on 99%

![](./kuvat/testuas-testikattavuus.png)

Automaatiotestauksen ulkopuolelle jäivät _build.py_- ja _initialize\_database.py_-tiedostojen suorittaminen komentoriviltä.
