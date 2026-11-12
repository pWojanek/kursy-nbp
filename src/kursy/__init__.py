from decimal import Decimal

import httpx


def main() -> None:
    data = httpx.get(
        "https://api.nbp.pl/api/exchangerates/rates/a/usd/?format=json"
    ).json(parse_float=Decimal)
    print(f"Kurs dolara to: {data['rates'][0]['mid']}")
