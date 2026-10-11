def calculate_data_bonus(data_bought):
    """
    Calculates a 15% data bundle bonus.
    Rounds the final bonus size to 1 decimal place.
    """
    bonus_data = data_bought * 0.15
    rounded_bonus = round(bonus_data, 1)
    return rounded_bonus

# --- TEST CASES ---
print("Testing 25 GB bundle purchase...")
print("Bonus Data earned (GB):", calculate_data_bonus(25.0))

