# ATENÇÃO! Os cálculos ainda não está atualizado com as regras do IR 2026

# Calculadora PJ para Simples Nacional

O objetivo deste projeto é auxiliar trabalhadores autônomos, especialmente desenvolvedores, que prestam serviço como PJ e escolhem o Simples Nacional.

Aqui é possível calcular os descontos e o salário líquido. Neste caso, é feita uma simulação, considerando para o [Fator R](https://www.contabilizei.com.br/contabilidade-online/fator-r-simples-nacional/), o enquadramento do anexo III e no anexo V. Desta forma é possível compará-los a fim de escolher o mais vantajoso.

## 🚀 Como usar

### Pré-requisitos

- Python
- Git (para clonar o repositório)

### Execução

1. **Clonando o repositório:**
   ```bash
   git clone https://github.com/jeffRayneres/calculadora-pj-simples-nacional.git
   cd calculadora-pj-simples-nacional
   ```

2. **Rodando a calculadora:**
   ```bash
   python main.py
   ```

### Como funciona

1. Execute o comando `python main.py`
2. Digite o valor do seu salário bruto mensal
3. O programa calculará automaticamente:
   - Pro labore
   - Desconto INSS
   - Desconto IR (Imposto de Renda sobre o pro labore)
   - Impostos do Simples Nacional (Anexo III e V)
   - Salário líquido para ambas as opções

### Exemplo de uso

```
Digite o salário bruto: 10000

Salário bruto: 10000.00

========== ANEXO III ==========
Pro labore: 2800.00
Desconto INSS: 308.00
Desconto IR: 17.46
Pro labore líquido: 2474.54

Imposto Anexo III: 600.00
Salário líquido Anexo III: 9074.54

=========== ANEXO V ===========
Imposto Anexo V: 1550.00
Salário líquido Anexo V: 8450.00
```

## 📋 Estrutura do projeto

```
calculadora-pj-simples-nacional/
├── main.py                 # Arquivo principal e interface do usuário
├── calculator.py           # Lógica de cálculos fiscais
├── IRTaxTableEnum.py       # Tabela de Imposto de Renda
├── RFactorTaxEnum.py       # Tabelas do Simples Nacional (Anexos III e V)
├── README.md              # Documentação do projeto
└── LICENSE                # Licença MIT
```

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## 👨‍💻 Autor

**Jefferson Rayneres Silva Cordeiro**

---

*Este projeto provê apenas uma simulação geral, procure sempre um contador para orientações mais detalhadas*
