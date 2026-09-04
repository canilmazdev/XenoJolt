# test_xenojolt.py
"""
Tests for XenoJolt module.
"""

import unittest
from xenojolt import XenoJolt

class TestXenoJolt(unittest.TestCase):
    """Test cases for XenoJolt class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = XenoJolt()
        self.assertIsInstance(instance, XenoJolt)
        
    def test_run_method(self):
        """Test the run method."""
        instance = XenoJolt()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
