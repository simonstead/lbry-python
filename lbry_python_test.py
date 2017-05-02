import unittest
import requests
import lbry

class LbryPythonTests(unittest.TestCase):
    def shallow_check(self, r):
        self.assertEqual(r.status_code, 200)
        j = r.json()
        self.assertIn('result', j)
        self.assertIn('jsonrpc', j)
        self.assertIn('id', j)

    def test_lbry_method_channel_list_mine(self):
        r = lbry.channel_list_mine()
        assert isinstance(r, list)

    def test_lbry_method_claim_list_mine(self):
        r = lbry.claim_list_mine()
        assert isinstance(r, list)

    def test_lbry_method_wallet_balanace(self):
        r = lbry.wallet_balance()
        assert r >= 0
