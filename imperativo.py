# ═══════════════════════════════════════════════
# PARADIGMA IMPERATIVO – Folha de Pagamento
# ═══════════════════════════════════════════════

funcionarios = [
    ("Ana Lima",     "Engenheira",    8500.00),
    ("Bruno Costa",  "Analista",      3200.00),
    ("Carla Souza",  "Gerente",      12000.00),
    ("Diego Melo",   "Desenvolvedor", 5700.00),
    ("Elena Rocha",  "Designer",      3800.00),
    ("Felipe Nunes", "Arquiteto",     9100.00),
]

LIMIAR = 4000.00   
BONUS  = 0.10     

filtrados = []
for func in funcionarios:
    nome, cargo, salario = func
    if salario > LIMIAR:
        filtrados.append(func)

com_bonus = []
for func in filtrados:
    nome, cargo, salario = func
    novo_salario = salario * (1 + BONUS)
    com_bonus.append((nome, cargo, salario, novo_salario))

total_bonus = 0.0
for func in com_bonus:
    nome, cargo, salario_orig, salario_novo = func
    total_bonus += salario_novo - salario_orig

print("=== PARADIGMA IMPERATIVO ===")
print(f"Funcionários com bônus: {len(com_bonus)}")
print(f"Custo total do bônus  : R$ {total_bonus:,.2f}")
for f in com_bonus:
    print(f"  {f[0]:15s} | Salário: R$ {f[2]:>9,.2f} | Com bônus: R$ {f[3]:>9,.2f}")
