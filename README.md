# fg_dominio

Vocabulário compartilhado da família FinGuard. **Zero dependências.**

Existe para que `fg_triagem`, `fg_risco`, `fg_relatorios` e a UI concordem nos
mesmos strings — sem drift de digitação entre o prompt do LLM e os mapas
downstream.

## Conteúdo

| Símbolo | O que é |
|---|---|
| `CATEGORIAS`, `PRODUTOS`, `SENTIMENTOS`, `URGENCIAS`, `NIVEIS_RISCO` | listas/conjuntos de valores permitidos |
| `URGENCIAS_ORDEM_EXIBICAO`, `NIVEIS_RISCO_ORDEM_EXIBICAO` | ordem decrescente para painéis |
| `SLA_POR_URGENCIA` | mapa `{urgência: prazo}` — §4 da POL-SAC-001 |
| `normalizar_urgencia(s)`, `normalizar_risco(s)` | texto livre → valor canônico (ou `None`) |
| `mascarar_palavroes(texto)` | filtro local de profanidade (preserva "Banco Central", "golpe", etc.) |

## Uso

```python
from fg_dominio import PRODUTOS, SLA_POR_URGENCIA, normalizar_urgencia, mascarar_palavroes

normalizar_urgencia("CRÍTICA")          # "Crítica"
SLA_POR_URGENCIA["Alta"]                # "24 horas"
"Cartão de Crédito" in PRODUTOS         # True
mascarar_palavroes("que merda")         # "que ***"
```

## Testes

```bash
pip install -e ".[dev]"
pytest -q
ruff check src tests
```
