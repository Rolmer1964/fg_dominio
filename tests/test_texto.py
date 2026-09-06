from fg_dominio import mascarar_palavroes


def test_censura_palavrao():
    out = mascarar_palavroes("que porra é essa, que merda de atendimento")
    assert "porra" not in out and "merda" not in out
    assert "***" in out


def test_preserva_termos_uteis():
    txt = "Vou processar o banco e reclamar no Banco Central sobre esse golpe."
    assert mascarar_palavroes(txt) == txt


def test_none_e_vazio():
    assert mascarar_palavroes(None) == ""
    assert mascarar_palavroes("") == ""


def test_versao_censurada_com_asteriscos():
    assert "p*rra" not in mascarar_palavroes("isso é uma p*rra")
