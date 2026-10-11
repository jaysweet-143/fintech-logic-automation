def check_user_tier(total_amount, transaction_count):
    """
    Checks if a user qualifies for the Premium tier.
    Requires total_amount > 5000 AND transaction_count > 10.
    """
    if total_amount > 5000 and transaction_count > 10: # YOUR CODE HERE
        return "Premium"
    else:
        return "Standard"

# --- TEST CASES ---
print("User 1 Tier:", check_user_tier(6000.00, 5))
print("User 2 Tier:", check_user_tier(7500.00, 12))


