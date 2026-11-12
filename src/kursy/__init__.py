from kursy.nbp import get_current_rate


def main() -> None:

    print(f"Kurs dolara to: {get_current_rate('usd')}")
    print(f"Kurs Euro to: {get_current_rate('eur')}")
