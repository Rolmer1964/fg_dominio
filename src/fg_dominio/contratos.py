"""Contratos de resultado — os DTOs que um passo do pipeline produz e outro consome.

Ficam aqui, e não no pacote que os produz, para que nenhuma folha da família
precise importar outra: `fg_risco` recebe um `ResultadoTriagem` sem depender de
`fg_triagem`. Quem costura os passos é o orquestrador (`fg_core`).

Zero dependências — apenas dataclasses. Campos obrigatórios: a fachada que produz
o resultado é responsável por preencher defaults antes de construir.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass
class ResultadoTriagem:
    """Saída da triagem inicial (Claude Haiku). Produzido por `fg_triagem`."""

    categoria: str
    produto: str
    sentimento: str
    urgencia: str
    resumo: str


@dataclass
class ResultadoRisco:
    """Saída da avaliação de risco (Claude Sonnet + RAG). Produzido por `fg_risco`."""

    nivel: str
    justificativa: str
    acoes_recomendadas: list[str]
    trechos_rag_usados: int
