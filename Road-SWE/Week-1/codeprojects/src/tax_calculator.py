# src/calculator.py

from tax_rules import calculate_taxable_income, get_tax_rate


class IncomeTaxCalculator:
    """
    Income Tax Calculator for UK (2024/2025).
    """

    def __init__(self, gross_income: float):
        self.gross_income = gross_income

    def taxable_income(self) -> float:
        return calculate_taxable_income(self.gross_income)

    def tax_rate(self) -> float:
        return get_tax_rate(self.taxable_income())

    def tax_due(self) -> float:
        return self.taxable_income() * self.tax_rate()
