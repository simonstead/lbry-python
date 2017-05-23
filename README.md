# Welcome to the LBRY wrapper for Python.

## Example
```python
import lbry
r = lbry.claim_list("princess-bubblegum")
print(r)
```

## Example response
```python
{
  u 'supports_without_claims': [], u 'claims': [{
    u 'claim_sequence': 1,
    u 'has_signature': False,
    u 'name': u 'princess-bubblegum',
    u 'supports': [],
    u 'valid_at_height': 151322,
    u 'hex': u '080110011ac1010801126b080410011a1c496d616765207075626c69736865642066726f6d20737065652e6368221f416e20696d616765207075626c69736865642066726f6d20737065652e63682a0f68747470733a2f2f737065652e6368320d5075626c696320446f6d61696e38004a0052005a001a50080110011a30916dc7eddd36b81eb7693974a97736249a9667231be0a51af3779f0ffe6efccbbc686b253b6ba195fe3397d3809fbc7022186170706c69636174696f6e2f6f637465742d73747265616d',
    u 'amount': 1.0,
    u 'value': {
      u 'version': u '_0_0_1',
      u 'claimType': u 'streamType',
      u 'stream': {
        u 'source': {
          u 'source': u '916dc7eddd36b81eb7693974a97736249a9667231be0a51af3779f0ffe6efccbbc686b253b6ba195fe3397d3809fbc70',
          u 'version': u '_0_0_1',
          u 'contentType': u 'application/octet-stream',
          u 'sourceType': u 'lbry_sd_hash'
        },
        u 'version': u '_0_0_1',
        u 'metadata': {
          u 'description': u 'An image published from spee.ch',
          u 'license': u 'Public Domain',
          u 'author': u 'https://spee.ch',
          u 'title': u 'Image published from spee.ch',
          u 'language': u 'en',
          u 'version': u '_0_1_0',
          u 'nsfw': False,
          u 'licenseUrl': u '',
          u 'preview': u '',
          u 'thumbnail': u ''
        }
      }
    },
    u 'height': 151322,
    u 'depth': 27997,
    u 'effective_amount': 1.0,
    u 'address': u 'bFzJzGfV4VH6bLUD1er8HQC9XfARzBZ1H6',
    u 'nout': 0,
    u 'txid': u '4479d2913ecf706b46181e9ff139ed486fef400b01b85b11d642b76be547e6d8',
    u 'claim_id': u 'bd13c514379ab1bd8d49848254c3b564b16b5399',
    u 'decoded_claim': True
  }], u 'last_takeover_height': 151322
}
```

## Example with optional parameters
```python
opt_params = { "address": "<address>" }
r = lbry.wallet_balance(**opt_params)
print r
```


## To run tests
```bash
$ pytest lbry_python_test.py
```

## List of available methods
channel_list_mine :ballot_box_with_check:

claim_list_mine :ballot_box_with_check:

wallet_balance :ballot_box_with_check:

blob_delete :ballot_box_with_check:

blob_get :ballot_box_with_check:

blob_list :ballot_box_with_check:

block_show :ballot_box_with_check:

channel_list_mine :ballot_box_with_check:

channel_new :ballot_box_with_check:

claim_abandon :ballot_box_with_check:

claim_list :ballot_box_with_check:

claim_list_mine :ballot_box_with_check:

claim_new_support :ballot_box_with_check:

claim_show :ballot_box_with_check:

daemon_stop :ballot_box_with_check:

descriptor_get :ballot_box_with_check:

file_delete :ballot_box_with_check:

file_list :ballot_box_with_check:

file_set_status :ballot_box_with_check:

get :ballot_box_with_check:

get_availability :ballot_box_with_check:

peer_list :ballot_box_with_check:

publish :ballot_box_with_check:

reflect :ballot_box_with_check:

report_bug :ballot_box_with_check:

resolve :ballot_box_with_check:

resolve_name :ballot_box_with_check:

send_amount_to_address :ballot_box_with_check:

settings_get :ballot_box_with_check:

settings_set :ballot_box_with_check:

stream_cost_estimate :ballot_box_with_check:

transaction_list :ballot_box_with_check:

version :ballot_box_with_check:

wallet_balance :ballot_box_with_check:

wallet_is_address_mine :ballot_box_with_check:

wallet_list :ballot_box_with_check:

wallet_new_address :ballot_box_with_check:

wallet_public_key :ballot_box_with_check:

wallet_unused_address :ballot_box_with_check:
