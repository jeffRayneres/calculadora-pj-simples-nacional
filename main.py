from calculator import Calculator

class bcolors:
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    RED = "\033[91m"
    RESET = "\033[0m"

class Main:
    def __init__(self) -> None:
        calc = Calculator()
        salary = float(input("Digite o salário bruto: "))
        annual_salary = salary * 12

        pro_labore = calc.calculate_pro_labore(salary)
        inss_discount = calc.calculate_INSS(pro_labore)
        salary_IR_base = pro_labore - inss_discount
        IR_tax = calc.calculate_IR(salary_IR_base)
        net_pro_labore = pro_labore - inss_discount - IR_tax

        R_factor_tax_annex_III = calc.calculate_tax_R_factor(salary, annual_salary, 3)
        R_factor_tax_annex_V = calc.calculate_tax_R_factor(salary, annual_salary, 5)

        net_salary_annex_III = salary - R_factor_tax_annex_III - inss_discount - IR_tax
        net_salary_annex_V = salary - R_factor_tax_annex_V

        print("Salário bruto: %.2f\n" % salary)

        print(bcolors.YELLOW+"========== ANEXO III =========="+bcolors.RESET)
        print("Pro labore: %.2f" % round(pro_labore, 2))
        print("Desconto INSS: %.2f" % round(inss_discount, 2))
        print("Desconto IR: %.2f" % round(IR_tax, 2))
        print("Pro labore líquido: %.2f\n" % net_pro_labore)

        print("Imposto Anexo III: %.2f" % round(R_factor_tax_annex_III, 2))
        print("Salário líquido Anexo III: %.2f\n" % net_salary_annex_III)

        print(bcolors.YELLOW+"=========== ANEXO V ==========="+bcolors.RESET)
        print("Imposto Anexo V: %.2f" % round(R_factor_tax_annex_V, 2))
        print("Salário líquido Anexo V: %.2f" % net_salary_annex_V)


main = Main()
