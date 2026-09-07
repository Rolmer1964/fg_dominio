from datetime import timedelta

from fg_dominio import TZ_BRT, agora_brt


def test_tz_brt_e_utc_menos_3():
    assert TZ_BRT.utcoffset(None) == timedelta(hours=-3)


def test_agora_brt_tem_fuso():
    agora = agora_brt()
    assert agora.tzinfo is TZ_BRT
    assert agora.utcoffset() == timedelta(hours=-3)
