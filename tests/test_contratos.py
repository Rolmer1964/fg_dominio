from dataclasses import fields

from fg_dominio import ResultadoRisco, ResultadoTriagem


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


def test_dataclasses_comparam_por_valor():
    a = ResultadoTriagem("Outros", "Não Identificado", "Neutro", "Baixa", "")
    b = ResultadoTriagem("Outros", "Não Identificado", "Neutro", "Baixa", "")
    assert a == b
