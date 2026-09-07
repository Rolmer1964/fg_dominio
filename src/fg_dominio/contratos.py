"""Contratos de resultado — os DTOs que um passo do pipeline produz e outro consome.

Ficam aqui, e não no pacote que os produz, para que nenhuma folha da família
precise importar outra: `fg_risco` recebe um `ResultadoTriagem` sem depender de
`fg_triagem`. Quem costura os passos é o orquestrador.

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


@dataclass
class ResultadoConsolidado:
    """Triagem + risco após os overrides determinísticos da POL-SAC-001.

    Produzido por `fg_relatorios.consolidar`. `urgencia`, `nivel_risco` e
    `justificativa_risco` já refletem os overrides (canal regulatório, risco
    crítico). `nivel_risco_original` só é preenchido quando um override elevou o
    risco — guarda o valor que o modelo havia atribuído.
    """

    categoria: str
    produto: str
    sentimento: str
    urgencia: str
    resumo: str
    prazo_resposta: str
    area_responsavel: str
    nivel_risco: str
    justificativa_risco: str
    acoes_recomendadas: list[str]
    nivel_risco_original: str | None = None
