# Arkkitehtuurikuvaus

Ohjelman rakenne noudattelee kolmikerrosarkkitehtuuria, ja koodin pakkausrakenne on seuraava:

![Pakkausrakenne](./kuvat/arkkitehtuuri-pakkaus.png)

Pakkaus _ui_ sisältää käyttöliittymäkoodin, _services_ sovelluslogiikan ja _repositories_ tietojen pysyväistallennuksesta vastaavan koodin. Pakkaus _entities_ sisältää luokkia, jotka kuvaavat sovelluksen käsitteellisiä objekteja.

## Käyttöliittymä

Käyttöliittymä sisältää kolme erillistä näkymää:

- Peliprofiilin valinta
- Videopokeri pelin

Kaikki näkymät on toteuteuttu omina luokkinaan. Näkymistä yksi on aina kerrallaan näkyvänä. Näkymien näyttämistä koordinoi [UI](../src/ui/ui.py)-luokka. Käyttöliittymä on pyritty eristämään täysin sovelluslogiikasta, joka on palvelukerroksessa. Käyttöliittymä kutsuu [VideoPokerService](../src/services/videopokerservice.py)-luokan metodeja.

Sovellus on Videopokeri, jonka pelaaminen on monille tuttua huoltoasemilta ja marketeista.

Kun pelikortteja vaihdetaan eli kun jaetaan uusi käsi tai kädessä vaihdetaan kortteja, niin kutsutaan sovelluksen [initialize_hand_view](https://github.com/nuuttikuosa/ohjelmistotekniikka2024/blob/main/videopoker/src/ui/video_poker_view.py) metodia, joka renderöi korttinäkymän uudelleen palvelukerrokselta saamiensa pelikorttien perusteella,

Sovelluksen pelaaminen on hyvin samanlaista eri käyttäjille, vain käyttäjien pelitilin saldo on käyttäjäkohtainen. Yksi kierros peliä maksaa yhden yksikön ja voitot määräytyvät voittotaulukon mukaan.

## Sovelluslogiikka
Sovelluksen loogisen tietomallin muodostavat luokat:
- [PlayingCard](https://github.com/nuuttikuosa/ohjelmistotekniikka2024/blob/main/videopoker/src/entities/card.py), joka kuvaa pelikorttia
- [Dealer](https://github.com/nuuttikuosa/ohjelmistotekniikka2024/blob/main/videopoker/src/entities/dealer.py), joka kuvaa korttipelin jakajaa ja jaka käden ja uudet pelikortit.
- [Deck](https://github.com/nuuttikuosa/ohjelmistotekniikka2024/blob/main/videopoker/src/entities/deck.py), joka kuvaa korttipakkaa
- [Game](https://github.com/nuuttikuosa/ohjelmistotekniikka2024/blob/main/videopoker/src/entities/game.py), joka kuvaa tiettyä videopokeria ja sen sääntöjä ja voittotaulukkoa.
- [PokerHand](https://github.com/nuuttikuosa/ohjelmistotekniikka2024/blob/main/videopoker/src/entities/hand.py), joka kuvaa pokerikättä eli joukkoa pelikortteja.
- [HandValue](https://github.com/nuuttikuosa/ohjelmistotekniikka2024/blob/main/videopoker/src/entities/hand_value.py), joka kuvaa käden arvoa. esim. suora, väri, kaksi paria tai hai.
- [PayoutTable](https://github.com/nuuttikuosa/ohjelmistotekniikka2024/blob/main/videopoker/src/entities/payout_table.py), joka kuvaa tietyn videopokerin voittoaulukkoa
- [PokerHandEvaluator](https://github.com/nuuttikuosa/ohjelmistotekniikka2024/blob/main/videopoker/src/entities/pokerevaluator.py), joka kuvaa käden arviointisääntöjä eli pelin sääntöjä.
- [User](https://github.com/nuuttikuosa/ohjelmistotekniikka2024/blob/main/videopoker/src/entities/user.py), joka kuvaa pelaajaa

Ohjelman luokkien väliset suhteet ovat:
```mermaid
 classDiagram
PokerHand "1" -- "5" PlayingCard
Deck "1" -- "52" PlayingCard
VideoPokerService "1" -- "1" Deck
VideoPokerService "1" -- "1" PokerHand
VideoPokerService "1" -- "1" Dealer
VideoPokerService "1" -- "n" PokerHandEvaluator
VideoPokerService "1" -- "1" UserRepository
VideoPokerService "1" -- "1" GameRepository
PokerHandEvaluator "1" -- "n" HandValue
GameRepository "1" -- "n" HandValue
UserInterface  "1"--"1" ImageRepository
UserInterface  "1"--"1" VideoPokerService
User "1" -- "1" VideoPokerService
User "n" -- "1" UserRepository
Game "1" -- "1" VideoPokerService
Game "n" -- "1" GameRepository
Game "1" -- "1" PayoutTable
PayoutTable "n" -- "1" GameRepository
```

Toiminnallisista kokonaisuuksista vastaa luokan [VideoPokerService](../src/services/videopokerservice.py) ainoa olio. Luokka tarjoaa kaikille käyttäliittymän toiminnoille oman metodin. Näitä ovat esimerkiksi:

- `login(user)`
- `deal(count)`
- `get_hand()`
- `select_card(card_id)`
- `replace_cards()`
- `logout()`

VideoPokerService pääsee käsiksi pelaajaprofiileihin, peleihin ja  voittotaulukkoihin pysyväistietojen säilytyksestä vastaavien luokkien [GameRepository](https://github.com/nuuttikuosa/ohjelmistotekniikka2024/blob/main/videopoker/src/repositories/game_repository.py) ja [UserRepository](https://github.com/nuuttikuosa/ohjelmistotekniikka2024/blob/main/videopoker/src/repositories/user_repository.py) kautta. Nämä sijaitsevat pakkauksessa _repositories_. Luokkien toteutus injektoidaan sovelluslogiikalle konstruktorikutsun yhteydessä.

## Tietojen pysyväistallennus

Pakkauksen _repositories_ luokat `GameRepository` ja `UserRepository` huolehtivat tietojen tallettamisesta. Molemmat luokat käyttävät SQLite-tietokantaa, joka alustetaan [initialize_database.py](https://github.com/nuuttikuosa/ohjelmistotekniikka2024/blob/main/videopoker/src/initialize_database.py)-tiedostossa.


### Kuvatiedostot
Pelikortit näytetään kuvina graafisella käyttöliittymällä. Käyttöliittymä käyttää pakkauksen _repositories_ luokkaa `ImageRepository` kuvien lukemiseen levyltä. Luokka noudattaa Repository suunnittelumallia ja kuvatiedostot voidaan tulevaisuudessa ladata vaikka tietokannasta tai internetissä olevasta hakemistosta, jos toteutusta muutetaan.


## Päätoiminnallisuudet

Kuvataan seuraavaksi sovelluksen toimintalogiikka  päätoiminnallisuuden osalta sekvenssikaaviona.

Alussa sovellus avaa peliprofiilin valintanäytön, johon on haettu tietokannasta siellä olevat peliprofiilit (pelaajan nimi ja pelitilin saldo). Käyttäjä voi valita olemassaolevat peliprofiilin tai luoda uuden.

### Peliprofiilin valitseminen

Kun peliprofiilinäkymän syötekenttään kirjoitetaan peliprofiilin nimi, jota ei ole vielä tietokannassa ja jonka jälkeen klikataan painiketta _Pelaa_, niin sovelluksen kontrolli etenee seuraavasti:

```mermaid

sequenceDiagram
  actor Player
  participant UI
  participant VideoPokerService
  participant UserRepository
  Player->>UI: painaa "Pelaa" painiketta
  UI->>VideoPokerService: login("Nuutti")
  VideoPokerService->>UserRepository: get_players()
  UserRepository-->>VideoPokerService: players
  VideoPokerService->>User: User(user, 1000)
  User-->> VideoPokerService: player
  VideoPokerService->>UserRepository: create_player(user)
  UserRepository-->> VideoPokerService:  player created
  VideoPokerService->>UI: player created
  UI->UI: show_video_poker_view()
```

Seuraavaksi sovellus hakee tietokannasta oletuspelin, _jätkä tai parempi_ tiedot ja voittotaulukon.

 Ohjelma jakaa hänelle käden ja arvioi käden korttiyhdistelmät. Käyttää voi halutessaan vaihtaa kortteja kädessä ja ohjelma vaihtaa kortit, arvioi korttiyhdistelmät ja laskee käyttäjän voiton ja päivittää käyttäjän pelitilin saldon.

### Uuden käden jakaminen pelaajalle

Kun Pelaaja painaa videopokerin pelaamisnäytöllä "Jaa uusi käsi", niin sovelluksen kontrolli etenee seuraavasti:

```mermaid
sequenceDiagram
  actor Player
  participant UI
  participant VideoPokerService
  participant Deck
  participant Playingcard
  Player->>UI: painaa "Jaa uusi käsi" painiketta
  UI->>UI:handle_deal_cards
  UI->>VideoPokerService: deal_hand()
  VideoPokerService->>VideoPokerService: init_deck()
  VideoPokerService->>Deck: Deck()
  Deck-->>VideoPokerService: deck
  VideoPokerService->>Playingcard: PlayingCard(i)
  Playingcard-->>VideoPokerService: playing card
  VideoPokerService->>Deck: add_card()
  Deck-->>VideoPokerService: card added
  VideoPokerService->>Dealer: deal_hand(count)
  Dealer->PokerHand:PokerHand()
  PokerHand-->>Dealer:hand
  Dealer->>Deck: number_of_cards()
  Deck-->>Dealer: number of card in deck
  Dealer->>Deck: get_card(card_number)
  Deck-->> Dealer: card
  Dealer->>PokerHand: add_card(card)
  PokerHand-->> Dealer: card added
  Dealer-->>VideoPokerService: hand
  VideoPokerService -->>VideoPokerService: lokita jaettu käsi onnistuneesti
  VideoPokerService ->> User: reduce_balance(PRICE_OF_GAME_ROUND)
  User-->>VideoPokerService: pelitilin saldoa vähennetty
  VideoPokerService->>UI: Käsi jaettu
  UI->UI: initialize_hand_view()
```
### Muut toiminnallisuudet

Sama periaate toistuu sovelluksen kaikissa toiminnallisuuksissa, käyttöliittymän tapahtumakäsittelijä kutsuu sopivaa sovelluslogiikan metodia, sovelluslogiikka kutsuu palvelukerrosta. Kontrollin palatessa käyttöliittymään, päivitetään tarvittaessa videopokeri näkymä  sekä aktiivinen näkymä.

## Ohjelman sisäiset tietotyypit

Ohjelmassa käsitellään pelikortteja kaksimerkkisinä stringeinä. Esimerkiksi pokerikäsi voi olla:
JS AC KH 8C 9S

Tässä toinen kirjain viittaa kortin maahan ja sen englanninkieliseen nimeen:
s = Spades
C = Clubs
H = Hearts
D = Diamonds
ja ensimmäinen kirjain kortin suuruuteen:
2,3,4,5,6,7,8,9,T,J,Q,K ja A, jossa T = 10, J = jätkä, Q = kuningatar, K = kuningas ja A on ässä.

## Lokitus

Ohjelmassa käytetään loguru lokitusviitekehystä toiminnalliseen lokitukseen. Tällöin jaetut kortit ja korttien valuaatiot lokitetaan, jotta jälkikäteen voidaan validoida pelaajien väitteitä mahdollisesti virheellisestä jaetuista tai jakamattomista voitoista.

## Ohjelman rakenteeseen jääneet heikkoudet

### Videopokerikäsien arviointi
Keskeinen arviointifunktio on hieman liian pitkä ja monimutkainen. Pylint ilmoittaa liian pitkistä ja monimutkaisista metodeista luokan PokerHandEvaluator metodissa basic_evaluation. Evaluointi on kuitenkin logiikaltaan sellainen, että jos se jaettaisiin kahteen funktioon, niin koodin looginen ymmärrettävyys kärsisi, joten olen pitänyt tämän toiminnallisuuden yhtenä kokonaisuutena. Periaatteessa suorien ja värien arvioinnin voi eriyttää muutta käden arvioinnista.

### Käyttöliittymä

Käyttöliittymän ryhmittelyä voisi parantaa rajattomasti, mutta koska en ole kovinkaan visuaalinen henkilö. Oikeassa ohjelmistoprojektissa käyttöliittymän viilaus olisi UX designerin eikä toteuttajan tehtävä.
