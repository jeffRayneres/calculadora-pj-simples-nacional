from IRTaxTableEnum import IRTaxTableEnum, IRTaxTableEnum
from RFactorTaxEnum import RFactorTaxEnum


class Calculator:
    def __init__(self):
        pass

    def calculate_IR(self, salary):

        bracket1 = IRTaxTableEnum.BRACKET_1.value
        bracket2 = IRTaxTableEnum.BRACKET_2.value
        bracket3 = IRTaxTableEnum.BRACKET_3.value
        bracket4 = IRTaxTableEnum.BRACKET_4.value
        bracket5 = IRTaxTableEnum.BRACKET_5.value

        IR_tax = 0

        if salary < bracket1['limit']:
            IR_tax = salary * bracket1['tax_rate'] - bracket1['deductible_amount']
        elif salary < bracket2['limit']:
            IR_tax = salary * bracket2['tax_rate'] - bracket2['deductible_amount']
        elif salary < bracket3['limit']:
            IR_tax = salary * bracket3['tax_rate'] - bracket3['deductible_amount']
        elif salary < bracket4['limit']:
            IR_tax = salary * bracket4['tax_rate'] - bracket4['deductible_amount']
        elif salary < bracket5['limit']:
            IR_tax = salary * bracket5['tax_rate'] - bracket5['deductible_amount']
        return IR_tax

    def calculate_INSS(self, value):
        inss_discount = value * 0.11
        return inss_discount

    def calculate_pro_labore(self, salary):
        pro_labore = salary * 0.28
        return pro_labore

    def calculate_tax_R_factor(self, salary, annual_salary, annex):
        tax = 0

        annex3 = RFactorTaxEnum.ANNEX_III.value
        annex5 = RFactorTaxEnum.ANNEX_V.value

        if annex == 3:
            if annual_salary < annex3['bracket_1']['limit']:
                tax = salary * self.calculate_effective_tax_rate(annex3['bracket_1'], salary)
            elif annual_salary < annex3['bracket_2']['limit']:
                tax = salary * self.calculate_effective_tax_rate(annex3['bracket_2'], salary)
            elif annual_salary < annex3['bracket_3']['limit']:
                tax = salary * self.calculate_effective_tax_rate(annex3['bracket_3'], salary)
        elif annex == 5:
            if annual_salary < annex5['bracket_1']['limit']:
                tax = salary * self.calculate_effective_tax_rate(annex5['bracket_1'], salary)
            elif annual_salary < annex5['bracket_2']['limit']:
                tax = salary * self.calculate_effective_tax_rate(annex5['bracket_2'], salary)
            elif annual_salary < annex5['bracket_3']['limit']:
                tax = salary * self.calculate_effective_tax_rate(annex5['bracket_3'], salary)
        return tax

    def calculate_effective_tax_rate(self, bracket_info, salary):
        annual_salary = salary * 12
        effective_tax_rate = (annual_salary * bracket_info['tax_rate'] - bracket_info[
            'deductible_amount']) / annual_salary
        # print("Taxa efetiva: %.2f" % effective_tax_rate)
        return effective_tax_rate