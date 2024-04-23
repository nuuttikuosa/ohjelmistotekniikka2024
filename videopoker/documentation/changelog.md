## Viikko 3

- Tehty seuraavat luokat: PlayingCard, Dealer, Deck, PokerHand, PokerHandEvaluator ja
  VideoPokerService.
- lisätty VideoPokerService-luokka, joka vastaa sovelluslogiikan koodista
- tehty yksinkertainen tekstipohjainen käyttöliittymä tiedostoon index.py
- kirjoitettu yksikötestit luokalle card, tämän luokan osalta testikattavuus 100%.

## Viikko 4
- Tehty GameRepository luokka, joka käyttää sqlite tietokantaa, johon eri videopokerityyppien voittotaulukot
  on tallennettu. Tehty kannanluontilauseet ja tiedon insertointilauseet jätkä tai parempi videopokerille,
  jossa huonoin pari, josta maksetaan voitto on jätkäpari. Toistaiseksi tietokannasta vain haetaan tietoa.
- Lisätty VideoPokerService luokkaan toiminnallisuutta, että hakee GameRepository luokasta kaikki tallennetut
  maksutaulukot eli pelit ja niihin liittyvät yksityiskohtaiset maksutaulukot.
- päivitetty käyttöliittymää siten, että käyttäjälle näytetään oletuspelin tiedot ja maksutaulukko ennen kuin peli alkaa

## Viikko 5
- Laajennettu käsien evaluaatiota lisäämällä säännöt isoille pareille (Jacks or Better). Näistä voi saada eri palkinnon kuin tavallisesta parista.
- lisättu käyttäjä repository käyttäjäprofiileille. Käyttäjä voi valita aikaisemman käyttäjäprofiilin tai luoda uuden käyttäjän. Käyttäjän pelitilin saldo päivitetään repositoryyn, kun käyttäjä lopettaa pelaamisen.
- lisätty VideoPokerService luokkaan user reposlitory toiminallisuutta ja refaktoroitu koodin rakenne eri loogisiin "pakkauksiin" eli hakemistoihin esimerkkisovelluksen mallin mukaisesti.
- käyttöliittymä on toteutettu väliaikaisesti index.py tiedostoon. Ensiviikolla eriytän käyttäliittymän erilliseen graafiseen UI komponenttiin. Tähän asti on ollut tarkoituksena rakentaan sovelluksen "back-end" toiminnallisuus ja varmistaa väliaikaisen käyttöliittymä kautta että luokat integroituvat toisiinsa ja perustoiminnallisuus on virheetön.
