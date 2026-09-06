"""Taxonomia e mapas de política — o vocabulário que os módulos precisam concordar."""

CATEGORIAS: list[str] = [
    "Cobrança Indevida",
    "Atendimento",
    "Fraude/Segurança",
    "Produto/Serviço",
    "Cancelamento",
    "Outros",
]

# Lista permitida de produtos (validação pós-triagem).
PRODUTOS: set[str] = {
    "Cartão de Crédito",
    "Conta Corrente",
    "Empréstimo",
    "Investimentos",
    "Seguros",
    "Não Identificado",
}

SENTIMENTOS: list[str] = ["Positivo", "Neutro", "Negativo", "Crítico"]

# Ordem crescente de severidade.
URGENCIAS: list[str] = ["Baixa", "Média", "Alta", "Crítica"]
NIVEIS_RISCO: list[str] = ["Baixo", "Médio", "Alto", "Crítico"]

# Ordem de exibição (decrescente) usada nos painéis decisórios.
URGENCIAS_ORDEM_EXIBICAO: list[str] = ["Crítica", "Alta", "Média", "Baixa"]
NIVEIS_RISCO_ORDEM_EXIBICAO: list[str] = ["Crítico", "Alto", "Médio", "Baixo"]

# SLA derivado da urgência (§4 da POL-SAC-001). Fonte única.
SLA_POR_URGENCIA: dict[str, str] = {
    "Crítica": "4 horas",
    "Alta": "24 horas",
    "Média": "3 dias úteis",
    "Baixa": "5 dias úteis",
}


def normalizar_urgencia(u: str | None) -> str | None:
    s = (u or "").lower()
    if "crít" in s or "crit" in s:
        return "Crítica"
    if "alt" in s:
        return "Alta"
    if "méd" in s or "med" in s:
        return "Média"
    if "baix" in s:
        return "Baixa"
    return None


def normalizar_risco(r: str | None) -> str | None:
    s = (r or "").lower()
    if "crít" in s or "crit" in s:
        return "Crítico"
    if "alt" in s:
        return "Alto"
    if "méd" in s or "med" in s:
        return "Médio"
    if "baix" in s:
        return "Baixo"
    return None
