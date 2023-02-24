#!/usr/bin/env python3

#########################
# CSC 720               #
# Homework 1            #
# Problem 9c            #
#########################

# Convert our transition table from JFLAP to a nested dictionary
transition_table = {
        'q0' : {
            'alphanum' : 'q0',
            '@' : 'q1',
            '.' : 'q6'
            },
        'q1' : {
            'alphanum' : 'q1',
            '@' : 'q6',
            '.' : 'q2'
            },
        'q2' : {
            'alphanum' : 'q3',
            '@' : 'q6',
            '.' : 'q6'
            },
        'q3' : {
            'alphanum' : 'q4',
            '@' : 'q1',
            '.' : 'q6'
            },
        'q4' : {
            'alphanum' : 'q5',
            '@' : 'q6',
            '.' : 'q2'
            },
        'q5' : {
            'alphanum' : 'q6',
            '@' : 'q6',
            '.' : 'q2'
            },
        'q6' : {
            'alphanum' : 'q6',
            '@' : 'q6',
            '.' : 'q6'
            }
        }

# Check our address
def check_address(address_input):
    
    # Initialize the current state to q0
    current_state = 'q0'
    
    # Initialize the current character type
    char_type = ''
    
    # Check character type
    for char in address_input:
        if char.isalnum():
            char_type = 'alphanum'
        elif char == '@':
            char_type = '@'
        elif char == '.':
            char_type = '.'
        
        # Check transition table and move to next state
        current_state = transition_table[current_state][char_type]

        # Debugging statement
        ##print("Moving to state: {}".format(current_state))
    
    # Check to see if we end up in a final state
    final_states = ['q4', 'q5']
    
    if current_state in final_states:
        print("Email address {} is valid".format(address_input))
    else:
        print("Email address {} is NOT valid".format(address_input))



# Main program
if __name__ == "__main__":

    # Get an email address from our user
    user_input = input("Enter email address: ")

    # Check whether or not the email address is valid
    check_address(user_input)