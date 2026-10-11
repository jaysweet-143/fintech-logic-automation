def check_user_tier(total_amount, transaction_count):
    """
    Checks if a user qualifies for the Premium tier.
    Requires total_amount > 5000 AND transaction_count > 10.
    """
    # Use an if-else statement combined with the 'and' operator
    if total_amount > 5000 and transaction_count > 10: # YOUR CODE HERE
        return "Premium"
    else:
        return "Standard"

# --- TEST YOUR CODE BELOW ---
# Test 1: High amount, but low transaction count
print("User 1 Tier:", check_user_tier(6000.00, 5))
# EXPECTED OUTPUT: Standard

# Test 2: High amount AND high transaction count
print("User 2 Tier:", check_user_tier(7500.00, 12))
# EXPECTED OUTPUT: Premium

