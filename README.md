# Fintech & Telecom Logic Scripts 💳

A collection of lightweight Python scripts I built to automate basic transaction and compliance logic.

## 📱 Project 1: MoMo Fee Calculator (`momo.py`)
Calculates standard transaction fees while subtracting user cashback rewards.
* **Logic:** Functions, basic math, and rounding numbers.
* **Input:** Amount being sent.
* **Output:** Total deduction from the user wallet.

## 🚨 Project 2: Instant Loan Approver (`loan.py`)
An automated check that approves or rejects mini-loans based on account history.
* **Logic:** If/Else conditional checking and Boolean logic.
* **Rules:** Requires a credit score >= 70 and zero unpaid debts.

## 📊 Project 3: Data Bundle Bonus (`bundle.py`)
Calculates a flat 15% bonus data allowance whenever a customer buys a bundle.
* **Logic:** Floating-point math and precision rounding.
* **Input:** Base data size purchased (GB).
* **Output:** Final rounded bonus data credited.

## 👑 Project 4: Account Tier Flag (`tier.py`)
Automatically flags user wallets as "Premium" or "Standard" based on activity volume.
* **Logic:** Compound logic tracking using the 'and' operator.
* **Rules:** Flags as Premium if volume > GHS 5,000 AND transactions > 10.

