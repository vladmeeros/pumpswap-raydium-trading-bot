# test_tokenvault.py
"""
Tests for TokenVault module.
"""

import unittest
from tokenvault import TokenVault

class TestTokenVault(unittest.TestCase):
    """Test cases for TokenVault class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = TokenVault()
        self.assertIsInstance(instance, TokenVault)
        
    def test_run_method(self):
        """Test the run method."""
        instance = TokenVault()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
