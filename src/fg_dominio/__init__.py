"""fg_dominio — vocabulário compartilhado da família FinGuard.

Zero dependências. Constantes de taxonomia, o mapa de SLA da POL-SAC-001, os
normalizadores e os contratos de resultado (DTOs) que triagem, risco, relatórios
e a UI precisam concordar. É a única área comum: uma folha pode importar
`fg_dominio`, nunca outra folha.
"""

from .contratos import ResultadoRisco, ResultadoTriagem
from .taxonomia import (
    CATEGORIAS,
    NIVEIS_RISCO,
    NIVEIS_RISCO_ORDEM_EXIBICAO,
    PRODUTOS,
    SENTIMENTOS,
    SLA_POR_URGENCIA,
    URGENCIAS,
    URGENCIAS_ORDEM_EXIBICAO,
    normalizar_risco,
    normalizar_urgencia,
)
from .texto import PALAVROES, mascarar_palavroes

__version__ = "0.2.0"

__all__ = [
    "CATEGORIAS",
    "NIVEIS_RISCO",
    "NIVEIS_RISCO_ORDEM_EXIBICAO",
    "PALAVROES",
    "PRODUTOS",
    "ResultadoRisco",
    "ResultadoTriagem",
    "SENTIMENTOS",
    "SLA_POR_URGENCIA",
    "URGENCIAS",
    "URGENCIAS_ORDEM_EXIBICAO",
    "__version__",
    "mascarar_palavroes",
    "normalizar_risco",
    "normalizar_urgencia",
]
