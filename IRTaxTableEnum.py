from enum import Enum


class IRTaxTableEnum(Enum):
    BRACKET_1 = {
        "limit": 2259.20,
        'tax_rate': 0,
        'deductible_amount': 0
    }

    BRACKET_2 = {
        "limit": 2826.65,
        'tax_rate': 0.075,
        'deductible_amount': 169.44
    }

    BRACKET_3 = {
        "limit": 3751.05,
        'tax_rate': 0.15,
        'deductible_amount': 381.44
    }

    BRACKET_4 = {
        "limit": 4664.68,
        'tax_rate': 0.225,
        'deductible_amount': 662.77
    }

    BRACKET_5 = {
        "limit": 1000000000,  # Placeholder for "above 4664.68"
        'tax_rate': 0.275,
        'deductible_amount': 896.00
    }
