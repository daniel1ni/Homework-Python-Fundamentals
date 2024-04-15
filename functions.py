def dollarizer(some_string):
    return (f"Dollarizer: {some_string.replace('s', '$')}")

def eurizer(some_string):
    return (f"Eurizer: {some_string.replace('e', '€')}")
  
def replacer(some_string):
    return (f"Replacer: {some_string.replace('l', '£')}")
    
def wonky_text(some_string):
    dollarized_String = dollarizer(some_string)
    euro_string = eurizer(dollarized_String)
    replaced_string = replacer(euro_string)
    return(f"Wonky text: {replaced_string}")

#print(wonky_text("testcaselivetoliftlive"))

def celsius_to_fahrenheit(celsius):
    return(f"Celsius to Fahrenheit: {int(celsius) * 9/5 +32}")

def age_in_days(years):
    return(f"Age in days: {years * 365}")

def simple_interest(principal, rate, time):
    return (f"Simple interest: {(principal * rate * time) / 100}")

def plan_finances(Principal_amount, rateofInterest, time_in_years, final_amount_after_rateofInterest):
    real_amount = Principal_amount * (1 + (rateofInterest/100)) * time_in_years
    if real_amount >= final_amount_after_rateofInterest: 
        return(True)
    else:
        return(False)
    

