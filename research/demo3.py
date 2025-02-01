cols = ['person_age', 'person_gender', 'person_education', 'person_income', 'person_emp_exp',
        'person_home_ownership', 'loan_amnt', 'loan_intent', 'loan_int_rate', 'credit_score',
        'previous_loan_defaults_on_file']

# Initialize the input_array with None values
input_array = [None] * len(cols)

for i in range(len(cols)):
    print(cols[i])
    # Prompt for input and convert it to an integer
    input_array[i] = input("Enter value of " + cols[i] + ": ")

# Output the collected input values
print("Input Array:", input_array)
