# Requirements for video poker application

## Purpose of the application

With the video poker application user can play video poker.
In future releases application it will be possible to select from many different video pokers with different payout tables. Application will recommend optimal play. The motivation for the application is that there are progressive video pokers
in some casinos and when a progressive pot is high enough then the game can have a positive expected value like the lotto can have a positive EV,
if no one has won the jackpot for a long time.

## Users

In the first version, player can select from existing user profiles or create a new one.

## User Interface

There will be two main screens. On the first screen user can select player profile. On another screen, the user can play selected video poker.

The application will open to the screen where user can player profile with game account balance.

The application has a graphical user interface where user can see graphical cards and select which ones to keep and which ones to discard and draw new ones.

## Functionality of the first version

- User can create payout table for new video poker (can create these in db using sql)
- User can modify the pay-out table of existing video poker (can edit these in db using sql)
- User can select existing payout table (can edit these in code setting DEFAULT_GAME to wanted payout table type)
- user can play Jacks or better Video (GUI implemented, graphic playing cards)
- user can create player profile or select player profile from db - amount of winnings will be updated to db after playing. (Done)

## Possible development ideas for the future releases
- The application will propose the best possible play for current hand, what cards to select and what to keep.:

which cards to keep and which to discard. This depends on the payout table. e.g. if Royal Flush has a very high pay-out then drawing it whit with one card can be profitable. Or if flush has a very high payout, some 2 card flush draws might be profitable.
