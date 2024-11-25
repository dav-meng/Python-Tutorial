import r_exchange_rates

def convert_gbp_to_eur(amount):
    return amount*r_exchange_rates.GBP_TO_EUR

def convert_gbp_to_usd(amount):
    return amount*r_exchange_rates.GBP_TO_USD

def convert_gbp_to_jyp(amount):
    return amount*r_exchange_rates.GBP_TO_JYP

def convert_gbp_to_cny(amount):
    return amount*r_exchange_rates.GBP_TO_CNY

def main():
    gbp_amount=100

    eur_amount=convert_gbp_to_eur(gbp_amount)
    usd_amount=convert_gbp_to_usd(gbp_amount)
    jyp_amount=convert_gbp_to_jyp(gbp_amount)
    cny_amount=convert_gbp_to_cny(gbp_amount)

    print(f" GBP {gbp_amount} is equivalent to: ")
    print(f" USD {usd_amount}")
    print(f" JYP {jyp_amount}")
    print(f" CNY {cny_amount}")

if __name__ == "__main__":
    main()







 

