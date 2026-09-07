"""Fuso horário de Brasília (UTC-3) — `agora_brt()`.

Compartilhado porque relatórios (stems de arquivo, `gerado_em`), traces e a UI
precisam do mesmo horário canônico. Sem horário de verão: o Brasil não observa
DST desde 2019, então UTC-3 fixo.
"""

from datetime import datetime, timedelta, timezone

TZ_BRT = timezone(timedelta(hours=-3))


def agora_brt() -> datetime:
    """`datetime` timezone-aware no fuso de Brasília."""
    return datetime.now(TZ_BRT)
