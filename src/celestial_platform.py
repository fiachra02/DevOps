"""
CelestialPlatform Module

This module provides functionality to manage a celestial platform
that can hold orbs and calculate gravity based on their weight.
"""

class CelestialPlatform:
    """
    Represents a celestial platform that holds orbs and calculates gravity
    based on their weight and the platform's maximum capacity.
    """

    def __init__(self, max_weight):
        """
        Initialize the platform with a maximum weight capacity.

        Args:
            max_weight (float): The maximum weight capacity of the platform.
        """
        self.max_weight = max_weight
        self.orbs = []  # List to hold orbs on the platform

    def add_orb(self, orb_weight):
        """
        Adds an orb to the platform and recalculates gravity.

        Args:
            orb_weight (float): The weight of the orb to add.

        Returns:
            float: The updated gravity after adding the orb.

        Raises:
            ValueError: If adding the orb exceeds the maximum weight capacity.
        """
        total_weight = self.get_total_weight() + orb_weight
        if total_weight > self.max_weight:
            raise ValueError("Weight exceeds platform capacity!")
        self.orbs.append(orb_weight)
        return self.calculate_gravity()

    def remove_orb(self, orb_weight):
        """
        Removes an orb from the platform and recalculates gravity.

        Args:
            orb_weight (float): The weight of the orb to remove.

        Returns:
            float: The updated gravity after removing the orb.

        Raises:
            ValueError: If the orb is not found on the platform.
        """
        if orb_weight not in self.orbs:
            raise ValueError("Orb not found on the platform!")
        self.orbs.remove(orb_weight)
        return self.calculate_gravity()

    def get_total_weight(self):
        """
        Returns the total weight of orbs on the platform.

        Returns:
            float: The total weight of orbs.
        """
        return sum(self.orbs)

    def calculate_gravity(self):
        """
        Calculates gravity based on weight distribution.

        Returns:
            float: The gravity based on the total weight of orbs.
        """
        total_weight = self.get_total_weight()
        if total_weight == 0:
            return 1.0  # Default gravity
        gravity = 1.0 + (total_weight / self.max_weight)
        return round(gravity, 2)


# Example Usage
platform = CelestialPlatform(max_weight=100)
print(platform.add_orb(30))  # Adds an orb of weight 30
print(platform.add_orb(40))  # Adds an orb of weight 40
print(platform.remove_orb(30))  # Removes the orb of weight 30
