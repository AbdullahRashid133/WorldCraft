# test_worldcraft.py
"""
Tests for WorldCraft module.
"""

import unittest
from worldcraft import WorldCraft

class TestWorldCraft(unittest.TestCase):
    """Test cases for WorldCraft class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = WorldCraft()
        self.assertIsInstance(instance, WorldCraft)
        
    def test_run_method(self):
        """Test the run method."""
        instance = WorldCraft()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
