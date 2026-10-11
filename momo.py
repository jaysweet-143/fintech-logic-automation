def calculate_total_momo_cost(amount_sent):
    """
    Calculates the final cost for a MoMo transaction.
    Takes the amount being sent, adds a 1% fee, and subtracts a GH₵ 0.50 cashback.
    """
    momo_fee = amount_sent * 0.01
    total_cost = (amount_sent + momo_fee) - 0.50
    final_rounded_cost = round(total_cost, 2)
    return final_rounded_cost

#--- TEST CASES ---
print("Testing GH₵ 250 transaction...")
print("Total deducted from wallet:", calculate_total_momo_cost(250.00))
#EXPECTED OUTPUT: 252.0


