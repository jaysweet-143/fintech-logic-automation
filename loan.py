def check_loan_status(credit_score, has_unpaid_debt):
    """
    Checks if a user qualifies for an instant wallet loan.
    Requires credit_score >= 70 AND has_unpaid_debt == False.
    """
    if credit_score >= 70 and has_unpaid_debt == False: # YOUR CODE HERE
        return "Approved"
    else:
        return "Rejected"

# --- TEST CASES ---
print("User 1 Loan Status:", check_loan_status(85, True))
print("User 2 Loan Status:", check_loan_status(75, False))


