PERSONAL_ALLOWANCE =12_570
BASIC_RATE_LIMIT = 50_270
HIGHER_RATE_LIMIT = 125_140

BASIC_RATE = 0.20
HIGHER_RATE = 0.40
ADDITIONAL_RATE = 0.45

def calculate_taxable_income(gross_income: float) -> float:
    """
    Calculate taxable income after personal allowance.
    """
    taxable = gross_income - PERSONAL_ALLOWANCE
    return max(taxable, 0.0)

def get_tax_rate(taxable_income: float) -> float:
    if taxable_income <= 0:
        return 0.0
    elif taxable_income <= BASIC_RATE_LIMIT - PERSONAL_ALLOWANCE:
        return BASIC_RATE
    elif taxable_income <= HIGHER_RATE_LIMIT - PERSONAL_ALLOWANCE:
        return HIGHER_RATE
    else:
        return ADDITIONAL_RATE
