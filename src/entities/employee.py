#!/usr/bin/env python3

"""
TODO
"""

from dataclasses import dataclass


@dataclass
class Employee:
	"""
	TODO
	"""

	name: str
	employee_id: int
	pay_rate: float = 100.0
	hours_worked: float = 0.0
	employer_cost: float = 1000.0
	has_comission: bool = True
	comission: float = 100.0
	contracts_landed: int = 0

	def compute_payout(self) -> float:
		"""Compute how much must be paid to an employee"""
		payout: float = self.pay_rate * self.hours_worked
		payout += self.employer_cost

		if self.has_comission:
			payout += self.comission * self.contracts_landed

		return payout
