# test_soliditycore.py
"""
Tests for SolidityCore module.
"""

import unittest
from soliditycore import SolidityCore

class TestSolidityCore(unittest.TestCase):
    """Test cases for SolidityCore class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = SolidityCore()
        self.assertIsInstance(instance, SolidityCore)
        
    def test_run_method(self):
        """Test the run method."""
        instance = SolidityCore()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
