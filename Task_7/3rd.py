# P(A∣B) = ( P(B∣A) × P(A) ) / P(B)

prior_a = float(input("Enter the prior probability of A: "))

prior_b = float(input("Enter the prior probability of B: "))

conditional_b_given_a = float(input("Enter the conditional probability of B given A: "))

print((conditional_b_given_a * prior_a) / prior_b)