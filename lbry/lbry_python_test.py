import unittest
import requests
import lbry

class LbryPythonTests(unittest.TestCase):
    def test_lbry_channel_list_mine(self):
        r = lbry.channel_list_mine()
        assert isinstance(r, list)

    def test_lbry_method_claim_list_mine(self):
        r = lbry.claim_list_mine()
        assert isinstance(r, list)

    @unittest.skip("Test skip")
    def test_lbry_method_blob_delete(self):
        blob_hash = "TEST_BLOB_HASH"
        r = lbry.blob_delete(blob_hash)
        print r
        assert r

    @unittest.skip("Test skip")
    def test_lbry_method_blob_get(self):
        r = lbry.blob_get(blob_hash)
        print r
        assert r == 0

    def test_lbry_method_blob_list(self):
        r = lbry.blob_list()
        assert r > 0

    def test_lbry_method_block_show(self):
        blockhash = "5487da044e5bb671d10e4329a7026a9bc27c1196c8ab5ce5ab4fb864686f61ed"
        r = lbry.block_show(blockhash)
        assert r > 0

    def test_lbry_method_channel_list_mine(self):
        r = lbry.channel_list_mine()
        assert isinstance(r, list)

    @unittest.skip("Test skip")
    def test_lbry_method_channel_new(self):
        channel_name = "CHANNEL_TEST_NAME"
        amount = 0.0
        r = lbry.channel_new(channel_name, amount)
        assert r

    @unittest.skip("Test skip")
    def test_lbry_method_claim_abandon(self):
        r = lbry.claim_abandon(claim_id)
        assert r

    def test_lbry_method_claim_list(self):
        r = lbry.claim_list("princess-bubblegum")
        self.assertIn('claims', r)

    def test_lbry_method_claim_list_mine(self):
        r = lbry.claim_list_mine()
        assert isinstance(r, list)

    @unittest.skip("Test skip")
    def test_lbry_method_claim_new_support(self):
        name = "princess-bubblegum"
        claim_id = "claim_id"
        amount = 0.0
        r = lbry.claim_new_support(name, claim_id, amount)
        assert r

    def test_lbry_method_claim_show(self):
        name = "princess-bubblegum"
        r = lbry.claim_show(name)
        assert r

    def test_lbry_method_claim_show_opt(self):
        name = "princess-bubblegum"
        opt_params = { "txid": "4479d2913ecf706b46181e9ff139ed486fef400b01b85b11d642b76be547e6d8", "nout": 0 }
        r = lbry.claim_show(name, **opt_params)
        print r
        assert r

    @unittest.skip("Test skip")
    def test_lbry_method_daemon_stop(self):
        r = lbry.daemon_stop()
        assert r > 0

    @unittest.skip("Test skip")
    def test_lbry_method_descriptor_get(self):
        sd_hash = "sd_hash"
        r = lbry.descriptor_get(sd_hash)

    @unittest.skip("Test skip")
    def test_lbry_method_file_delete(self):
        params = { "name": "princess-bubblegum" }
        r = lbry.file_delete(params)
        assert r > 0

    def test_lbry_method_file_list(self):
        opt_params = { "name": "princess-bubblegum" }
        r = lbry.file_list(**opt_params)
        assert r > 0

    @unittest.skip("Test skip")
    def test_lbry_method_file_set_status(self):
        status = "stop"
        optionals = { "name": "princess-bubblegum" }
        r = lbry.file_set_status(status, optionals)
        assert r > 0

    @unittest.skip("Test skip")
    def test_lbry_method_get(self):
        uri = "princess-bubblegum"
        r = lbry.get(uri)
        assert r > 0

    def test_lbry_method_get_availability(self):
        uri = "princess-bubblegum"
        r = lbry.get_availability(uri)
        assert r > 0

    @unittest.skip("Test skip")
    def test_lbry_method_peer_list(self):
        blob_hash = "blob_hash"
        r = lbry.peer_list(blob_hash)
        assert r > 0

    @unittest.skip("Test skip")
    def test_lbry_method_publish(self):
        name = "princess-bubblegum"
        bid = 0
        r = lbry.publish(name, bid)
        assert r > 0

    @unittest.skip("Test skip")
    def test_lbry_method_reflect(self):
        sd_hash = "sd_hash"
        r = lbry.reflect(sd_hash)
        assert r > 0

    @unittest.skip("Test skip")
    def test_lbry_method_report_bug(self):
        message = "Hi there, I'm testing out the LBRY API Wrapper for python. Have a great day."
        r = lbry.report_bug(message)
        assert r > 0

    def test_lbry_method_resolve(self):
        uri = "princess-bubblegum"
        r = lbry.resolve(uri)
        self.assertIn("4479d2913ecf706b46181e9ff139ed486fef400b01b85b11d642b76be547e6d8", str(r))

    def test_lbry_method_resolve_name(self):
        name = "princess-bubblegum"
        r = lbry.resolve_name(name)
        assert r > 0

    def test_lbry_method_send_amount_to_address(self):
        amount = 0
        address = "TEST_LBRY_ADDRESS"
        r = lbry.send_amount_to_address(amount, address)
        assert r > 0

    def test_lbry_method_settings_get(self):
        r = lbry.settings_get()
        assert r > 0

    @unittest.skip("Test skip")
    def test_lbry_method_settings_set(self):
        data_rate = 0.0
        max_key_fee = 0.0
        download_directory = "TEST_DOWNLOAD_DIRECTORY"
        download_timeout = 600
        search_timeout = 600
        cache_time = 600
        r = settings_set(data_rate, max_key_fee, download_directory, download_timeout, search_timeout, cache_time)
        assert r > 0

    def test_lbry_method_stream_cost_estimate(self):
        name = "princess-bubblegum"
        r = lbry.stream_cost_estimate(name)
        assert r > 0

    @unittest.skip("Test skip")
    def test_lbry_method_transaction_list(self):
        r = lbry.transaction_list()
        assert isinstance(r, list)

    @unittest.skip("Test skip")
    def test_lbry_method_version(self):
        r = lbry.version()
        self.assertTrue("lbryum_version" in str(r))

    def test_lbry_method_wallet_balance(self):
        r = lbry.wallet_balance()
        assert r >= 0

    def test_lbry_method_wallet_is_address_mine(self):
        wallet_address = "MY_WALLET_ADDRESS"
        r = lbry.wallet_is_address_mine(wallet_address)
        assert r == False

    def test_lbry_method_wallet_list(self):
        r = lbry.wallet_list()
        assert r > 0

    @unittest.skip("Test skip")
    def test_lbry_method_wallet_new_address(self):
        r = lbry.wallet_new_address()
        assert isinstance(r, list)

    def test_lbry_method_wallet_public_key(self):
        r = lbry.wallet_public_key()
        assert r > 0

    @unittest.skip("Test skip")
    def test_lbry_method_wallet_unused_address(self):
        r = lbry.wallet_unused_address()
        assert isinstance(r, list)

    def test_lbry_method_status_with_optional_params(self):
        r = lbry.status(session_status=True)
        self.assertTrue("session_status" in str(r))
        r2 = lbry.status(session_status=False)
        self.assertFalse("session_status" in str(r2))
