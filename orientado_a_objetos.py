# ═══════════════════════════════════════════════
# PARADIGMA ORIENTADO A OBJETOS – Folha de Pagamento
# ═══════════════════════════════════════════════

class Funcionario:
    """Representa um funcionário com seus dados salariais."""

    PERCENTUAL_BONUS = 0.10  

    def __init__(self, nome: str, cargo: str, salario_bruto: float):
        self.nome          = nome
        self.cargo         = cargo
        self.salario_bruto = salario_bruto

    def calcular_bonus(self) -> float:
        """Retorna o valor absoluto do bônus."""
        return self.salario_bruto * self.PERCENTUAL_BONUS

    def salario_com_bonus(self) -> float:
        """Retorna o salário bruto acrescido do bônus."""
        return self.salario_bruto + self.calcular_bonus()

    def __repr__(self) -> str:
        return f"Funcionario({self.nome!r}, {self.cargo!r}, R${self.salario_bruto:,.2f})"


class GerenciadorFolha:
    """Gerencia a lista de funcionários e processa a folha."""

    def __init__(self, funcionarios: list):
        self._funcionarios = funcionarios

    def filtrar_acima_de(self, limiar: float) -> list:
        """Retorna funcionários com salário bruto > limiar."""
        return [f for f in self._funcionarios if f.salario_bruto > limiar]

    def calcular_custo_total_bonus(self, funcionarios: list) -> float:
        """Soma os bônus de todos os funcionários recebidos."""
        return sum(f.calcular_bonus() for f in funcionarios)

    def relatorio(self, limiar: float) -> None:
        """Imprime o relatório completo de bônus."""
        elegiveis = self.filtrar_acima_de(limiar)
        total     = self.calcular_custo_total_bonus(elegiveis)

        print("=== PARADIGMA ORIENTADO A OBJETOS ===")
        print(f"Funcionários com bônus: {len(elegiveis)}")
        print(f"Custo total do bônus  : R$ {total:,.2f}")
        for f in elegiveis:
            print(
                f"  {f.nome:15s} | Cargo: {f.cargo:15s}"
                f" | Bônus: R$ {f.calcular_bonus():>8,.2f}"
                f" | Total: R$ {f.salario_com_bonus():>9,.2f}"
            )


funcionarios = [
    Funcionario("Ana Lima",     "Engenheira",    8500.00),
    Funcionario("Bruno Costa",  "Analista",      3200.00),
    Funcionario("Carla Souza",  "Gerente",      12000.00),
    Funcionario("Diego Melo",   "Desenvolvedor", 5700.00),
    Funcionario("Elena Rocha",  "Designer",      3800.00),
    Funcionario("Felipe Nunes", "Arquiteto",     9100.00),
]

gerenciador = GerenciadorFolha(funcionarios)
gerenciador.relatorio(limiar=4000.00)
