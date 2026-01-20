# test_scancrawlerchain.py
"""
Tests for ScanCrawlerChain module.
"""

import unittest
from scancrawlerchain import ScanCrawlerChain

class TestScanCrawlerChain(unittest.TestCase):
    """Test cases for ScanCrawlerChain class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = ScanCrawlerChain()
        self.assertIsInstance(instance, ScanCrawlerChain)
        
    def test_run_method(self):
        """Test the run method."""
        instance = ScanCrawlerChain()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
