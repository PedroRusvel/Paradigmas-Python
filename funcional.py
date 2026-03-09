# ═══════════════════════════════════════════════
# PARADIGMA FUNCIONAL – Folha de Pagamento
# ═══════════════════════════════════════════════
from functools import reduce

funcionarios = (
    {"nome": "Ana Lima",     "cargo": "Engenheira",    "salario": 8500.00},
    {"nome": "Bruno Costa",  "cargo": "Analista",      "salario": 3200.00},
    {"nome": "Carla Souza",  "cargo": "Gerente",       "salario": 12000.00},
    {"nome": "Diego Melo",   "cargo": "Desenvolvedor", "salario": 5700.00},
    {"nome": "Elena Rocha",  "cargo": "Designer",      "salario": 3800.00},
    {"nome": "Felipe Nunes", "cargo": "Arquiteto",     "salario": 9100.00},
)

LIMIAR = 4000.00
BONUS  = 0.10

def acima_do_limiar(limiar: float):
    """Retorna predicado que verifica salário > limiar."""
    return lambda func: func["salario"] > limiar

def aplicar_bonus(percentual: float):
    """Retorna transformação que acrescenta o bônus ao registro (imutável)."""
    return lambda func: {
        **func,
        "salario_original": func["salario"],
        "bonus":            func["salario"] * percentual,
        "salario_final":    func["salario"] * (1 + percentual),
    }

def somar_bonus(acumulador: float, func: dict) -> float:
    """Função redutora: acumula o valor de bônus."""
    return acumulador + func["bonus"]

elegiveis   = list(filter(acima_do_limiar(LIMIAR), funcionarios))
com_bonus   = list(map(aplicar_bonus(BONUS), elegiveis))
total_bonus = reduce(somar_bonus, com_bonus, 0.0)

print("=== PARADIGMA FUNCIONAL ===")
print(f"Funcionários com bônus: {len(com_bonus)}")
print(f"Custo total do bônus  : R$ {total_bonus:,.2f}")
for f in com_bonus:
    print(
        f"  {f['nome']:15s} | Salário orig.: R$ {f['salario_original']:>9,.2f}"
        f" | Bônus: R$ {f['bonus']:>8,.2f} | Final: R$ {f['salario_final']:>9,.2f}"
    )
