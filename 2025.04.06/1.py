def strong_password(password: str,*):
    score_lower = 0
    score_upper = 0
    score_digit = 0
    score_alnum = 0

    
    if len(password) > 7:
        check_len = 1
    else:
        check_len = 0

    for simbol in password:
        if simbol.islower():
            score_lower += 1
        elif simbol.isupper():
            score_upper += 1
        if simbol.isdigit():
            score_digit += 1
        if not simbol.isalnum():
            score_alnum += 1 

    
    if check_len + (score_lower > 0) + (score_upper > 0) + (score_digit > 1) + (score_alnum > 0) == 5:
        return True
    else:
        return False
    

# >>> strong_password('aP3:kD_l3')
# True
# >>> strong_password('password')
# False
# >>> strong_password('Qq123123/')
# True
# >>>


