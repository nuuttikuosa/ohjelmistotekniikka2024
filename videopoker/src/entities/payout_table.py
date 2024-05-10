from entities.hand_value import HandValue

class PayoutTable:
    def __init__(self):
       self.table = {}

    def add_payout(self, combination, payout):
        self.table[HandValue(combination)] = payout

    def get_payout(self, combination):
        return self.table.get(combination)

    def __str__(self):
        """Return all payouts as a string sorted in descending order by payout."""
        sorted_payouts = sorted(self.table.items(), key=lambda x: x[1], reverse=True)
        payouts_str = "\n".join([f"{payout:>5} : {combination.name:} " for combination, payout in sorted_payouts])
        return payouts_str