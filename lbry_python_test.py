import unittest
import requests
import lbry

class LbryPythonTests(unittest.TestCase): 
  
  base_url = "http://127.0.0.1:5279/lbryapi/"
  
  def test_should_make_any_request(self):
    r = requests.get("http://google.com")
    self.assertEqual(r.status_code,200)

  def test_should_make_req_to_lbry(self):
    r = requests.get("http://127.0.0.1:5279/lbryapi")
    self.assertEqual(r.status_code,200)

  def test_raw_lbry_method_get(self):
    url = self.base_url + "get"
    self.assertEqual(url, "http://127.0.0.1:5279/lbryapi/get")
  
  def test_lbry_module_base_url(self):
    url  = lbry.base_url
    self.assertEqual(url, self.base_url)

  def test_lbry_module_get(self):
    r = lbry.get()
    self.assertEqual(r.status_code, 200)
