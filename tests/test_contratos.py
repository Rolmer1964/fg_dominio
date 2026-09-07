from dataclasses import fields

from fg_dominio import ResultadoConsolidado, ResultadoRisco, ResultadoTriagem


def test_resultado_triagem_campos():
    r = ResultadoTriagem(
        categoria="Fraude/Segurança",
        produto="Cartão de Crédito",
        sentimento="Crítico",
        urgencia="Crítica",
        resumo="Cliente relata transações não reconhecidas.",
    )
    assert [f.name for f in fields(r)] == ["categoria", "produto", "sentimento", "urgencia", "resumo"]
    assert r.produto == "Cartão de Crédito"


def test_resultado_risco_campos():
    r = ResultadoRisco(
        nivel="Alto",
        justificativa="Indício de fraude conforme §2.3 da POL-SAC-001.",
        acoes_recomendadas=["Bloquear cartão", "Abrir chamado de fraude"],
        trechos_rag_usados=4,
    )
    assert [f.name for f in fields(r)] == ["nivel", "justificativa", "acoes_recomendadas", "trechos_rag_usados"]
    assert r.trechos_rag_usados == 4


def test_resultado_consolidado_campos_e_opcional():
    r = ResultadoConsolidado(
        categoria="Cobrança Indevida",
        produto="Cartão de Crédito",
        sentimento="Negativo",
        urgencia="Alta",
        resumo="cobrança em duplicidade",
        prazo_resposta="24 horas",
        area_responsavel="Gerência de Cartões",
        nivel_risco="Alto",
        justificativa_risco="conforme §2.3 da POL-SAC-001",
        acoes_recomendadas=["Estornar em 24h"],
    )
    assert r.nivel_risco_original is None
    assert [f.name for f in fields(r)] == [
        "categoria", "produto", "sentimento", "urgencia", "resumo",
        "prazo_resposta", "area_responsavel", "nivel_risco", "justificativa_risco",
        "acoes_recomendadas", "nivel_risco_original",
    ]


def test_dataclasses_comparam_por_valor():
    a = ResultadoTriagem("Outros", "Não Identificado", "Neutro", "Baixa", "")
    b = ResultadoTriagem("Outros", "Não Identificado", "Neutro", "Baixa", "")
    assert a == b
