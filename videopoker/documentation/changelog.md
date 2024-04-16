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
- päivitetty käyttöliittymää siten, että käyttäjälle näytetään oletuspelin tiedot ja maksutaulukko ennen kuin
  peli alkaa
