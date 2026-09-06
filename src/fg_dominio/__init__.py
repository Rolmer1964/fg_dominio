"""fg_dominio — vocabulário compartilhado da família FinGuard.

Zero dependências. Constantes de taxonomia, o mapa de SLA da POL-SAC-001 e os
normalizadores que triagem, risco, relatórios e a UI precisam concordar.
"""

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

__version__ = "0.1.0"

__all__ = [
    "CATEGORIAS",
    "NIVEIS_RISCO",
    "NIVEIS_RISCO_ORDEM_EXIBICAO",
    "PALAVROES",
    "PRODUTOS",
    "SENTIMENTOS",
    "SLA_POR_URGENCIA",
    "URGENCIAS",
    "URGENCIAS_ORDEM_EXIBICAO",
    "__version__",
    "mascarar_palavroes",
    "normalizar_risco",
    "normalizar_urgencia",
]
