# Requirements for video poker application

## Purpose of application 

With the video poker application user can analyze different video pokers and their pay-out tables and calculate their return to player. User can also play those video pokers.
In future releases application will recommend optimal play. The motivation for the application is that there are progressive video pokers 
in some casinos and when a progressive pot is high enough then the game can have a positive expected value like the lotto can have a positive EV, 
if no one has won the jackpot for a long time. 

## Users

In the first version, there is only one user role: user. In the future versions admin user might be added.

## User Interface

There will be two main screens. One is to modify payouts for different videopokers. User can load, create, and update payout tables on this screen. On another screen, the user can play selected video poker.

The application will open to the screen where user can select different video pokers - different payout. From here user can select a pay-out table to play or create a new one or modify an existing one.

The application has a graphical user interface where user can see graphical cards and select which ones to keep and which ones to discard and draw new ones. 

## Functionality of the first version

- User can create payout table for new video poker
- User can modify the pay-out table existing video poker
- User can select existing payout table
- user can play selected video poker
- user can calculate the expected value for the selected pay-out table 

## Possible development ideas for the future releases
- The application will propose the best possible play:
which cards to keep and which to discard. This depends on the payout table. e.g. if Royal Flush has a very high pay-out then drawing it whit with one card can be profitable. Or if flush has a very high payout, some 2 card flush draws might be profitable.
    
