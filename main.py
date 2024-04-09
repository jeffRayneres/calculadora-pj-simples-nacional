from calculator import Calculator


class Main:
    def __init__(self) -> None:
        calc = Calculator()
        salary = 10000
        annual_salary = salary * 12
        print("Salário bruto: %.2f" % salary)
        print("")

        pro_labore = calc.calculate_pro_labore(salary)
        print("Pro labore: %.2f" % round(pro_labore, 2))

        inss_discount = calc.calculate_INSS(pro_labore)
        print("Desconto INSS: %.2f" % round(inss_discount, 2))
        salary_IR_base = pro_labore - inss_discount

        IR_tax = calc.calculate_IR(salary_IR_base)
        print("Desconto IR: %.2f" % round(IR_tax, 2))

        net_pro_labore = pro_labore - inss_discount - IR_tax
        print("Pro labore líquido: %.2f" % net_pro_labore)
        print("")

        R_factor_tax_annex_III = calc.calculate_tax_R_factor(salary, annual_salary, 3)
        print("Imposto Anexo III: %.2f" % round(R_factor_tax_annex_III, 2))

        R_factor_tax_annex_V = calc.calculate_tax_R_factor(salary, annual_salary, 5)
        print("Imposto Anexo V: %.2f" % round(R_factor_tax_annex_V, 2))

        net_salary_annex_III = salary - R_factor_tax_annex_III - inss_discount - IR_tax
        net_salary_annex_V = salary - R_factor_tax_annex_V

        print("")
        print("Salário líquido Anexo III: %.2f" % net_salary_annex_III)
        print("Salário líquido Anexo V: %.2f" % net_salary_annex_V)

        pass


main = Main()
