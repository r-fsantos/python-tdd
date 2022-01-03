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
	pay_rate: float = 100.00
	hours_worked: int = 0
	employer_cost: float = 1000.00
	has_comission: bool = True
	comission: float = 100.00
	contracts_landed: int = 0

	def compute_payout(self) -> float:
		"""Compute how much must be paid to an employee"""
		raise NotImplementedError()
	
	