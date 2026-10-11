def calculate_total_momo_cost(amount_sent):
    """
    Calculates the final cost for a MoMo transaction.
    Takes the amount being sent, adds a 1% fee, and subtracts a GH₵ 0.50 cashback.
    """
# 1. Calculate the 1% fee based on the amount_sent
# Hint: 1% is written as 0.01 in decimal math
    momo_fee = amount_sent * 0.01

# 2. Calculate the total cost by adding the fee to the amount_sent,
# then subtracting the GH₵ 0.50 cashback reward
    total_cost = (amount_sent + momo_fee) - 0.50

# 3. Round the final total cost to 2 decimal places using a built-in function
    final_rounded_cost = round(total_cost, 2)

    return final_rounded_cost

#--- TEST YOUR CODE BELOW ---
#Let's check what happens when a user wants to send GH₵ 250.00
print("Testing GH₵ 250 transaction...")
print("Total deducted from wallet:", calculate_total_momo_cost(250.00))
#EXPECTED OUTPUT: 252.0


