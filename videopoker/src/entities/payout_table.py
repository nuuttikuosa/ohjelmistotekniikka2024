from entities.hand_value import HandValue


class PayoutTable:
    """Luokka, jona edustaa pelattavan pelin pokerikättä
    """

    def __init__(self):
        """Luokan konstruktori.
        """
        self.table = {}

    def add_payout(self, combination, payout):
        """Lisää voiton maksutaulukkoon.
        Args:
        combination: korttiyhdistelmän numero
        payout: voiton määrä rahana
        """
        self.table[HandValue(combination)] = payout

    def get_payout(self, combination):
        return self.table.get(combination)

    def __str__(self):
        """Return all payouts as a string sorted in descending order by payout.
        Can be used in UI.
        """
        sorted_payouts = sorted(
            self.table.items(), key=lambda x: x[1], reverse=True)
        payouts_str = "\n".join(
            [f"{payout:>5} : {combination.name:} " for combination, payout in sorted_payouts])
        return payouts_str
