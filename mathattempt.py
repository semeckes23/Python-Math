def abs(abs_target):
    if(abs_target < 0):
        abs_target = abs_target - abs_target*2
    return abs_target

def pwr(base,power):
    result_pwr = base
    if (not is_float(power)):
        if(power > 0):
            for i in range(power-1):
                result_pwr = result_pwr * base
        elif(power <= 0):
            power = abs(power)
            for j in range(power+1):
                result_pwr = result_pwr/base
    else:
        result_pwr = "Error, not coded yet"
    return result_pwr

def is_float(number_check_f):
    remainder_f = number_check_f % 1
    state_f = remainder_f > 0
    return state_f

def log_x(base_l,x):
    attempt_counter = 0
    attempt = x
    tried = False
    while(attempt != base_l or not tried):
        if (attempt >= base_l):
            attempt = attempt / base_l
            attempt_counter += 1
        else:
            attempt = attempt * base_l/attempt
            tried = True
    return attempt_counter

def e():
    n = 36517 
    e_base = 1 + 1/n
    e_val = pwr(e_base,n)
    return e_val

def exp(e_power):
    e_x = pwr(e(),e_power)
    return e_x


