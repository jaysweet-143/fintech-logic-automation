def calculate_data_bonus(data_bought):
    """
    Calculates a 15% data bundle bonus.
    Rounds the final bonus size to 1 decimal place.
    """
    # 1. Calculate the 15% bonus data
    # Hint: 15% is written as 0.15 in decimal math
    bonus_data = data_bought * 0.15
    
    # 2. Round the bonus_data to 1 decimal place
    rounded_bonus = round(bonus_data, 1)
    
    return rounded_bonus

# --- TEST YOUR CODE BELOW ---
# Let's check the bonus when a user buys a 25 GB data bundle
print("Testing 25 GB bundle purchase...")
print("Bonus Data earned (GB):", calculate_data_bonus(25.0))
# EXPECTED OUTPUT: 3.8

