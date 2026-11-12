from decimal import Decimal

import httpx


def get_current_rate(currency: str) -> Decimal:
    data = httpx.get(
        f"https://api.nbp.pl/api/exchangerates/rates/a/{currency}/?format=json"
    ).json(parse_float=Decimal)

    return data["rates"][0]["mid"]
