"""fg_dominio — vocabulário compartilhado da família FinGuard.

Zero dependências. Constantes de taxonomia, o mapa de SLA da POL-SAC-001, os
normalizadores, o fuso BRT e os contratos de resultado (DTOs) que triagem, risco,
relatórios e a UI precisam concordar. É a única área comum: uma folha pode
importar `fg_dominio`, nunca outra folha.
"""

from .contratos import ResultadoConsolidado, ResultadoRisco, ResultadoTriagem
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
from .tempo import TZ_BRT, agora_brt
from .texto import PALAVROES, mascarar_palavroes

__version__ = "0.3.0"

__all__ = [
    "CATEGORIAS",
    "NIVEIS_RISCO",
    "NIVEIS_RISCO_ORDEM_EXIBICAO",
    "PALAVROES",
    "PRODUTOS",
    "ResultadoConsolidado",
    "ResultadoRisco",
    "ResultadoTriagem",
    "SENTIMENTOS",
    "SLA_POR_URGENCIA",
    "TZ_BRT",
    "URGENCIAS",
    "URGENCIAS_ORDEM_EXIBICAO",
    "__version__",
    "agora_brt",
    "mascarar_palavroes",
    "normalizar_risco",
    "normalizar_urgencia",
]
