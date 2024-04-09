from enum import Enum


class RFactorTaxEnum(Enum):
    ANNEX_III = {
        "bracket_1": {
            "limit": 180000,
            "tax_rate": 0.06,
            "deductible_amount": 0
        },

        "bracket_2": {
            "limit": 360000,
            "tax_rate": 0.112,
            "deductible_amount": 9360
        },

        "bracket_3": {
            "limit": 720000,
            "tax_rate": 0.135,
            "deductible_amount": 17640
        },

    }

    ANNEX_V = {
        "bracket_1": {
            "limit": 180000,
            "tax_rate": 0.155,
            "deductible_amount": 0
        },

        "bracket_2": {
            "limit": 360000,
            "tax_rate": 0.18,
            "deductible_amount": 4500
        },

        "bracket_3": {
            "limit": 720000,
            "tax_rate": 0.195,
            "deductible_amount": 9900
        }
    }
