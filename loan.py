def check_loan_status(credit_score, has_unpaid_debt):
    """
    Checks if a user qualifies for an instant wallet loan.
    Requires credit_score >= 70 AND has_unpaid_debt == False.
    """
    # Use your open-book strategy. Look at how 'and' combines with '==' or 'not'
    if credit_score >= 70 and has_unpaid_debt == False: # YOUR CODE HERE
        return "Approved"
    else:
        return "Rejected"

# --- TEST YOUR CODE BELOW ---
# Test 1: Good credit score, but has unpaid debt
print("User 1 Loan Status:", check_loan_status(85, True))
# EXPECTED OUTPUT: Rejected

# Test 2: Good credit score AND has no unpaid debt
print("User 2 Loan Status:", check_loan_status(75, False))
# EXPECTED OUTPUT: Approved

