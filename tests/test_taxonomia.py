from fg_dominio import (
    CATEGORIAS,
    NIVEIS_RISCO_ORDEM_EXIBICAO,
    PRODUTOS,
    SLA_POR_URGENCIA,
    URGENCIAS_ORDEM_EXIBICAO,
    normalizar_risco,
    normalizar_urgencia,
)


def test_normalizar_urgencia():
    assert normalizar_urgencia("CRÍTICA") == "Crítica"
    assert normalizar_urgencia("critico") == "Crítica"
    assert normalizar_urgencia("média") == "Média"
    assert normalizar_urgencia("Alta") == "Alta"
    assert normalizar_urgencia("xpto") is None
    assert normalizar_urgencia(None) is None


def test_normalizar_risco():
    assert normalizar_risco("Alto") == "Alto"
    assert normalizar_risco("baixíssimo") == "Baixo"
    assert normalizar_risco("MÉDIO") == "Médio"
    assert normalizar_risco("") is None


def test_sla_cobre_todas_as_urgencias():
    assert set(SLA_POR_URGENCIA) == {"Crítica", "Alta", "Média", "Baixa"}
    assert SLA_POR_URGENCIA["Crítica"] == "4 horas"


def test_ordens_de_exibicao_sao_decrescentes():
    assert URGENCIAS_ORDEM_EXIBICAO[0] == "Crítica"
    assert NIVEIS_RISCO_ORDEM_EXIBICAO[0] == "Crítico"


def test_conjuntos_de_vocabulario():
    assert "Não Identificado" in PRODUTOS
    assert "Fraude/Segurança" in CATEGORIAS
    assert len(CATEGORIAS) == 6
