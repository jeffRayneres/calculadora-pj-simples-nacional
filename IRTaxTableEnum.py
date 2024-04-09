from enum import Enum

class IRTaxTableEnum(Enum):
    BRACKET_1 = {'lower': 0, "upper": 2259.20, 'tax_rate': 0}
    BRACKET_2 = {'lower': 2259.21, "upper": 2826.65, 'tax_rate': 0.075, 'cumulative_tax': 42.59 }
    BRACKET_3 = {'lower': 2826.66, "upper": 3751.05, 'tax_rate': 0.15, 'cumulative_tax': 181.29 }
    BRACKET_4 = {'lower': 3751.06, "upper": 4664.68, 'tax_rate': 0.225, 'cumulative_tax': 386.79 }
    BRACKET_5 = {'lower': 4664.69, "upper": 1000000000, 'tax_rate': 0.275}
