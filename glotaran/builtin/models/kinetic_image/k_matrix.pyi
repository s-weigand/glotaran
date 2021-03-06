from __future__ import annotations

from typing import Any

import numpy as np

from glotaran.builtin.models.kinetic_image.initial_concentration import InitialConcentration
from glotaran.model import model_attribute
from glotaran.parameter import Parameter

class KMatrix:
    @classmethod
    def empty(cls: Any, label: str, compartments: list[str]) -> KMatrix: ...
    def involved_compartments(self) -> list[str]: ...
    def combine(self, k_matrix: KMatrix) -> KMatrix: ...
    def matrix_as_markdown(
        self, compartments: list[str] = ..., fill_parameters: bool = ...
    ) -> str: ...
    def a_matrix_as_markdown(self, initial_concentration: InitialConcentration) -> str: ...
    def reduced(self, compartments: list[str]) -> np.ndarray: ...
    def full(self, compartments: list[str]) -> np.ndarray: ...
    def eigen(self, compartments: list[str]) -> tuple[np.ndarray, np.ndarray]: ...
    def rates(self, initial_concentration: InitialConcentration) -> np.ndarray: ...
    def a_matrix(self, initial_concentration: InitialConcentration) -> np.ndarray: ...
    def a_matrix_non_unibranch(
        self, initial_concentration: InitialConcentration
    ) -> np.ndarray: ...
    def a_matrix_unibranch(self, initial_concentration: InitialConcentration) -> np.array: ...
    def is_unibranched(self, initial_concentration: InitialConcentration) -> bool: ...
    @property
    def matrix(self) -> dict[tuple[str, str], Parameter]: ...
