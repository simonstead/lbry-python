import requests
import json

base_url = "http://127.0.0.1:5279/lbryapi/"


def _request(method_name, body={}, **opt_params):
    payload = { "method": method_name }
    if body != {}:
        payload["params"] = body
    r = requests.post(base_url, data=json.dumps(payload))
    if r.status_code != 200:
        print "Bad Status Code"
        print r
    j = r.json()
    if 'result' in j:
        return j['result']
    else:
        return r

def channel_list_mine():
    method_name = "channel_list_mine"
    return _request(method_name)


def wallet_balance():
    method_name = "wallet_balance"
    return _request(method_name)

#  LBRY JSON-RPC API Documentation blob_announce_all
#  Announce all blobs to the DHT
# Args: None
#  Returns:
#      (str) Success/fail message
def blob_announce_all():
    return _request("blob_announce_all")


# Delete a blob
#  Args:
#      'blob_hash': (str) hash of blob to get
#  Returns:
#      (str) Success/fail message
def blob_delete(blob_hash):
    method_name = "blob_delete"
    return _request(method_name, { "blob_hash": blob_hash })


# Download and return a blob
#
# Args:
#     'blob_hash': (str) blob hash of blob to get
#     'timeout'(optional): (int) timeout in number of seconds
#     'encoding'(optional): (str) by default no attempt at decoding is made,
#                          can be set to one of the following decoders:
#                          'json'
#     'payment_rate_manager'(optional): if not given the default payment rate manager
#                                      will be used. supported alternative rate managers:
#                                      'only-free'
# Returns
#     (str) Success/Fail message or (dict) decoded data
def blob_get(blob_hash, **opt_params):
    method_name = "blob_get"
    return _request(method_name, { "blob_hash": blob_hash }, **opt_params)


#  Returns blob hashes. If not given filters, returns all blobs known by
#  Args:
#      'uri' (optional): (str) filter by blobs in stream for winning clai
#      'stream_hash' (optional): (str) filter by blobs in given stream ha
#      'sd_hash' (optional): (str) filter by blobs in given sd hash
#      'needed' (optional): (bool) only return needed blobs
#      'finished' (optional): (bool) only return finished blobs
#      'page_size' (optional): (int) limit number of results returned
#      'page' (optional): (int) filter to page x of [page_size] results
#  Returns:
#      (list) List of blob hashes
def blob_list(**opt_params):
    method_name = "blob_get"
    return _request(method_name, { }, **opt_params)


# blob_refect_all
# Reflects all saved blobs
#
# Args:
#     None
# Returns:
#     (bool) true if successful
def blob_refect_all():
    return _request("blob_refect_all")



# Get contents of a block
#
# Args:
#     'blockhash': (str) hash of the block to look up
# Returns:
#     (dict) Requested block
def block_show(blockhash):
    method_name = "block_show"
    return _request(method_name, { "blockhash": blockhash })


# Get my channels
#
# Returns:
#     (list) ClaimDict
def channel_list_mine():
    return _request("channel_list_mine")


# Generate a publisher key and create a new certificate claim
#
# Args:
#     'channel_name': (str) '@' prefixed name
#     'amount': (float) amount to claim name
#
# Returns:
#     (dict) Dictionary containing result of the claim
#     {
#         'tx' : (str) hex encoded transaction
#         'txid' : (str) txid of resulting claim
#         'nout' : (int) nout of the resulting claim
#         'fee' : (float) fee paid for the claim transaction
#         'claim_id' : (str) claim ID of the resulting claim
#     }
def channel_new(channel_name, amount):
    method_name = "channel_new"
    return _request(method_name, { "channel_name": channel_name, "amount": amount })


# Abandon a name and reclaim credits from the claim
#
# Args:
#     'claim_id': (str) claim_id of claim
# Return:
#     (dict) Dictionary containing result of the claim
#     {
#         txid : (str) txid of resulting transaction
#         fee : (float) fee paid for the transaction
#     }
def claim_abandon(claim_id):
    method_name = "claim_abandon"
    return _request(method_name, { "claim_id": claim_id })



#
#    Get claims for a name
#  Args:
#      'name': (str) search for claims on this name
#  Returns
#      (dict) State of claims assigned for the name
#      {
#          'claims': (list) list of claims for the name
#          [
#              {
#              'amount': (float) amount assigned to the claim
#              'effective_amount': (float) total amount assigned to the c
#                                  including supports
#              'claim_id': (str) claim ID of the claim
#              'height': (int) height of block containing the claim
#              'txid': (str) txid of the claim
#              'nout': (int) nout of the claim
#              'supports': (list) a list of supports attached to the clai
#              'value': (str) the value of the claim
# }, ]
#          'supports_without_claims': (list) supports without any claims
#          'last_takeover_height': (int) the height of last takeover for
#      }
def claim_list(name):
    method_name = "claim_list"
    return _request(method_name, { "name": name })



# List my name claims
#
# Args:
#     None
# Returns
#     (list) List of name claims owned by user
#     [
#         {
#             'address': (str) address that owns the claim
#             'amount': (float) amount assigned to the claim
#             'blocks_to_expiration': (int) number of blocks until it expires
#             'category': (str) "claim", "update" , or "support"
#             'claim_id': (str) claim ID of the claim
#             'confirmations': (int) number of blocks of confirmations for the claim
#             'expiration_height': (int) the block height which the claim will expire
#             'expired': (bool) true if expired, false otherwise
#             'height': (int) height of the block containing the claim
#             'is_spent': (bool) true if claim is abandoned, false otherwise
#             'name': (str) name of the claim
#             'txid': (str) txid of the cliam
#             'nout': (int) nout of the claim
#             'value': (str) value of the claim
#         },
#    ]
def claim_list_mine():
    method_name = "claim_list_mine"
    return _request(method_name)


#  Support a name claim
#  Args:
#      'name': (str) name
#      'claim_id': (str) claim ID of claim to support
#      'amount': (float) amount to support by
#  Return:
#      (dict) Dictionary containing result of the claim
#      {
#          txid : (str) txid of resulting support claim
#          nout : (int) nout of the resulting support claim
#          fee : (float) fee paid for the transaction
# }
def claim_new_support(name, claim_id, amount):
    method_name = "claim_new_support"
    body = { "name": name, "claim_id": claim_id, "amount": amount }
    return _request(method_name, body)

#  Resolve claim info from a LBRY name
#  Args:
#      'name': (str) name to look up, do not include lbry:// prefix
#      'txid'(optional): (str) if specified, look for claim with this txi
#      'nout'(optional): (int) if specified, look for claim with this nou
#      'claim_id'(optional): (str) if specified, look for claim with this
#  Returns:
#      (dict) Dictionary contaning claim info, (bool) false if claim is n
# resolvable
#      {
#          'txid': (str) txid of claim
#          'nout': (int) nout of claim
#          'amount': (float) amount of claim
#          'value': (str) value of claim
#          'height' : (int) height of claim takeover
#          'claim_id': (str) claim ID of claim
#      'supports': (list) list of supports associated with claim
# d t
# claim_id ot
#          'supports': (list) list of supports associated with claim
#      }
# commands
#  Return a list of available commands
#  Returns:
#      (list) list of available commands
def claim_show(name, **opt_params):
    method_name = "claim_show"
    body = { "name": name }
    return _request(method_name, body, **opt_params)


#  Stop lbrynet-daemon
#  Returns:
#      (string) Shutdown message
def daemon_stop():
    method_name = "daemon_stop"
    return _request(method_name)


#  Download and return a sd blob
#  Args:
#      'sd_hash': (str) hash of sd blob
#      'timeout'(optional): (int) timeout in number of seconds
#      'payment_rate_manager'(optional): (str) if not given the default p
#                                       will be used. supported alternati
#                                       only-free
#  Returns
#      (str) Success/Fail message or (dict) decoded data
def descriptor_get(sd_hash, **opt_params):
    method_name = "descriptor_get"
    body = { "sd_hash": sd_hash }
    return _request(method_name, body, **opt_params)


#  Delete a lbry file
#  Args:
#      'name' (optional): (str) delete file by lbry name,
#         'sd_hash' (optional): (str) delete file by sd hash,
# ayment rate
# ve rate mana
# m g
#      'sd_hash' (optional): (str) delete file by sd hash,
#      'file_name' (optional): (str) delete file by the name in the downl
#      'stream_hash' (optional): (str) delete file by stream hash,
#      'claim_id' (optional): (str) delete file by claim ID,
#      'outpoint' (optional): (str) delete file by claim outpoint,
#      'rowid': (optional): (int) delete file by rowid in the file manage
#      'delete_target_file' (optional): (bool) delete file from downloads
#                                      defaults to true if false only the
#                                      db entries will be deleted
#  Returns:
#      (bool) true if deletion was successful
def file_delete(**opt_params):
    method_name = "file_delete"
    return _request(method_name, {}, **opt_params)


#  List files limited by optional filters
#  Args:
#      'name' (optional): (str) filter files by lbry name,
#      'sd_hash' (optional): (str) filter files by sd hash,
#      'file_name' (optional): (str) filter files by the name in the down
#      'stream_hash' (optional): (str) filter files by stream hash,
#      'claim_id' (optional): (str) filter files by claim id,
#      'outpoint' (optional): (str) filter files by claim outpoint,
#      'rowid' (optional): (int) filter files by internal row id,
#      'full_status': (optional): (bool) if true populate the 'message' a
#  Returns:
#      (list) List of files
# [
# {
#     'completed': (bool) true if download is completed,
# 'file_name': (str) name of file,
# 'download_directory': (str) download directory,
# 'points_paid': (float) credit paid to download file,
# 'stopped': (bool) true if download is stopped,
# 'stream_hash': (str) stream hash of file,
# 'stream_name': (str) stream name ,
# 'suggested_file_name': (str) suggested file name,
# 'sd_hash': (str) sd hash of file,
# 'name': (str) name claim attached to file
# 'outpoint': (str) claim outpoint attached to file
# 'claim_id': (str) claim ID attached to file,
# 'download_path': (str) download path of file,
# 'mime_type': (str) mime type of file,
# 'key': (str) key attached to file,
# 'total_bytes': (int) file size in bytes, None if full_status is false
# oads folder,
# r
#  folder,
#  blobs and
# loads folder
# nd 'size' fi
# ,
# e
# 'download_path': (str) download path of file,
# us is false
#              'total_bytes': (int) file size in bytes, None if full_stat
#              'written_bytes': (int) written size in bytes
#              'message': (str), None if full_status is false
#              'metadata': (dict) Metadata dictionary
# }, ]
def file_list(**opt_params):
    method_name = "file_list"
    return _request(method_name, {}, **opt_params)


#  Start or stop downloading a file
#  Args:
#      'status': (str) "start" or "stop"
#      'name' (optional): (str) start file by lbry name,
#      'sd_hash' (optional): (str) start file by the hash in the name cla
#      'file_name' (optional): (str) start file by its name in the downlo
#  Returns:
#      (str) Confirmation message
def file_set_status(status, **opt_params):
    method_name = "file_set_status"
    body = { "status": status }
    return _request(method_name, body, **opt_params)

# Download stream from a LBRY name.
#
# Args:
#     'uri': (str) lbry uri to download
#     'file_name'(optional): (str) a user specified name for the downloaded file
#     'timeout'(optional): (int) download timeout in number of seconds
#     'download_directory'(optional): (str) path to directory where file will be saved
# Returns:
#     (dict) Dictionary contaning information about the stream
#     {
#         'completed': (bool) true if download is completed,
#         'file_name': (str) name of file,
#         'download_directory': (str) download directory,
#         'points_paid': (float) credit paid to download file,
#         'stopped': (bool) true if download is stopped,
#         'stream_hash': (str) stream hash of file,
#         'stream_name': (str) stream name,
#         'suggested_file_name': (str) suggested file name,
#         'sd_hash': (str) sd hash of file,
#         'name': (str) name claim attached to file
#         'outpoint': (str) claim outpoint attached to file
#         'claim_id': (str) claim ID attached to file,
#         'download_path': (str) download path of file,
#         'mime_type': (str) mime type of file,
#         'key': (str) key attached to file,
#         'total_bytes': (int) file size in bytes, None if full_status is false
#         'written_bytes': (int) written size in bytes
#         'message': (str), None if full_status is false
#         'metadata': (dict) Metadata dictionary
#     }
def get(uri, **opt_params):
    method_name = "get"
    body = { "uri": uri }
    return _request(method_name, body, **opt_params)



# Get stream availability for lbry uri
#
# Args:
#     'uri' : (str) lbry uri
#     'sd_timeout' (optional): (int) sd blob download timeout
#     'peer_timeout' (optional): (int) how long to look for peers
#
# Returns:
#     (float) Peers per blob / total blobs
def get_availability(uri, **opt_params):
    method_name = "get_availability"
    body = { "uri": uri }
    return _request(method_name, body, **opt_params)


# Return a useful message for an API command
#
# Args:
#     'command'(optional): (str) command to retrieve documentation for
# Returns:
#     (str) if given a command, returns documentation about that command
#     otherwise returns general help message
def help(**opt_params):
    return _request("help", {},**opt_params)


# Get peers for blob hash
#
# Args:
#     'blob_hash': (str) blob hash
#     'timeout'(optional): (int) peer search timeout in seconds
# Returns:
#     (list) List of contacts
def peer_list(blob_hash, **opt_params):
    method_name = "peer_list"
    body = { "blob_hash": blob_hash }
    return _request(method_name, body, **opt_params)


# Make a new name claim and publish associated data to lbrynet,
# update over existing claim if user already has a claim for name.
#
# Fields required in the final Metadata are:
#     'title'
#     'description'
#     'author'
#     'language'
#     'license',
#     'nsfw'
#
# Metadata can be set by either using the metadata argument or by setting individual arguments
# fee, title, description, author, language, license, license_url, thumbnail, preview, nsfw,
# or sources. Individual arguments will overwrite the fields specified in metadata argument.
#
# Args:
#     'name': (str) name to be claimed
#     'bid': (float) amount of credits to commit in this claim,
#     'metadata'(optional): (dict) Metadata to associate with the claim.
#     'file_path'(optional): (str) path to file to be associated with name. If provided,
#                             a lbry stream of this file will be used in 'sources'.
#                             If no path is given but a metadata dict is provided, the source
#                             from the given metadata will be used.
#     'fee'(optional): (dict) Dictionary representing key fee to download content:
#                       {currency_symbol: {'amount': float, 'address': str, optional}}
#                       supported currencies: LBC, USD, BTC
#                       If an address is not provided a new one will be automatically
#                       generated. Default fee is zero.
#     'title'(optional): (str) title of the file
#     'description'(optional): (str) description of the file
#     'author'(optional): (str) author of the file
#     'language'(optional): (str), language code
#     'license'(optional): (str) license for the file
#     'license_url'(optional): (str) URL to license
#     'thumbnail'(optional): (str) thumbnail URL for the file
#     'preview'(optional): (str) preview URL for the file
#     'nsfw'(optional): (bool) True if not safe for work
#     'sources'(optional): (dict){'lbry_sd_hash':sd_hash} specifies sd hash of file
#     'channel_name' (optional): (str) name of the publisher channel
#
# Returns:
#     (dict) Dictionary containing result of the claim
#     {
#         'tx' : (str) hex encoded transaction
#         'txid' : (str) txid of resulting claim
#         'nout' : (int) nout of the resulting claim
#         'fee' : (float) fee paid for the claim transaction
#         'claim_id' : (str) claim ID of the resulting claim
#     }
def publish(name, bid, **opt_params):
    method_name = "publish"
    body = { "name": name, "bid": bid }
    return _request(method_name, body, **opt_params)



# Reflect a stream
#
# Args:
#     'sd_hash': (str) sd_hash of lbry file
# Returns:
#     (bool) true if successful
def reflect(sd_hash, **opt_params):
    method_name = "reflect"
    body = { "sd_hash": sd_hash }
    return _request(method_name, body, **opt_params)


# Report a bug to slack
#
# Args:
#     'message': (str) message to send
# Returns:
#     (bool) true if successful
def report_bug(message):
    method_name = "report_bug"
    body = { "message": message }
    return _request(method_name, body)




# Resolve a LBRY URI
#
# Args:
#     'uri': (str) uri to download
# Returns:
#     None if nothing can be resolved, otherwise:
#     If uri resolves to a channel or a claim in a channel:
#         'certificate': {
#             'address': (str) claim address,
#             'amount': (float) claim amount,
#             'effective_amount': (float) claim amount including supports,
#             'claim_id': (str) claim id,
#             'claim_sequence': (int) claim sequence number,
#             'decoded_claim': (bool) whether or not the claim value was decoded,
#             'height': (int) claim height,
#             'depth': (int) claim depth,
#             'has_signature': (bool) included if decoded_claim
#             'name': (str) claim name,
#             'supports: (list) list of supports [{'txid': txid,
#                                                  'nout': nout,
#                                                  'amount': amount}],
#             'txid': (str) claim txid,
#             'nout': (str) claim nout,
#             'signature_is_valid': (bool), included if has_signature,
#             'value': ClaimDict if decoded, otherwise hex string
#         }
#     If uri resolves to a channel:
#         'claims_in_channel': [
#             {
#                 'address': (str) claim address,
#                 'amount': (float) claim amount,
#                 'effective_amount': (float) claim amount including supports,
#                 'claim_id': (str) claim id,
#                 'claim_sequence': (int) claim sequence number,
#                 'decoded_claim': (bool) whether or not the claim value was decoded,
#                 'height': (int) claim height,
#                 'depth': (int) claim depth,
#                 'has_signature': (bool) included if decoded_claim
#                 'name': (str) claim name,
#                 'supports: (list) list of supports [{'txid': txid,
#                                                      'nout': nout,
#                                                      'amount': amount}],
#                 'txid': (str) claim txid,
#                 'nout': (str) claim nout,
#                 'signature_is_valid': (bool), included if has_signature,
#                 'value': ClaimDict if decoded, otherwise hex string
#             }
#         ]
#     If uri resolves to a claim:
#         'claim': {
#             'address': (str) claim address,
#             'amount': (float) claim amount,
#             'effective_amount': (float) claim amount including supports,
#             'claim_id': (str) claim id,
#             'claim_sequence': (int) claim sequence number,
#             'decoded_claim': (bool) whether or not the claim value was decoded,
#             'height': (int) claim height,
#             'depth': (int) claim depth,
#             'has_signature': (bool) included if decoded_claim
#             'name': (str) claim name,
#             'channel_name': (str) channel name if claim is in a channel
#             'supports: (list) list of supports [{'txid': txid,
#                                                  'nout': nout,
#                                                  'amount': amount}]
#             'txid': (str) claim txid,
#             'nout': (str) claim nout,
#             'signature_is_valid': (bool), included if has_signature,
#             'value': ClaimDict if decoded, otherwise hex string
#         }
#     }
def resolve(uri):
    method_name = "resolve"
    body = { "uri": uri }
    return _request(method_name, body)


# Resolve stream info from a LBRY name
#
# Args:
#     'name': (str) name to look up, do not include lbry:// prefix
# Returns:
#     (dict) Metadata dictionary from name claim, None if the name is not
            # resolvable
def resolve_name(name):
    method_name = "resolve_name"
    body = { "name": name }
    return _request(method_name, body)



# Send credits to an address
#
# Args:
#     'amount': (float) the amount to send
#     'address': (str) the address of the recipient in base58
# Returns:
#     (bool) true if payment successfully scheduled
def send_amount_to_address(amount, address):
    method_name = "send_amount_to_address"
    body = { "amount": amount, "address": address }
    return _request(method_name, body)



# Get daemon settings
#
# Returns:
#     (dict) Dictionary of daemon settings
#     See ADJUSTABLE_SETTINGS in lbrynet/conf.py for full list of settings
def settings_get():
    method_name = "settings_get"
    return _request(method_name)


#  Set daemon settings
#  Args:
#      'run_on_startup': (bool) currently not supported
#      'data_rate': (float) data rate,
#      'max_key_fee': (float) maximum key fee,
#      'download_directory': (str) path of where files are downloaded,
#      'max_upload': (float), currently not supported
#      'max_download': (float), currently not supported
#      'download_timeout': (int) download timeout in seconds
#      'search_timeout': (float) search timeout in seconds
#      'cache_time': (int) cache timeout in seconds
#  Returns:
#      (dict) Updated dictionary of daemon settings
# status
#  Return daemon status
#  Args:
#      'session_status' (optional): (bool) true to return session status,
#          default is false
#  Returns:
#      (dict) Daemon status dictionary
def settings_set(data_rate, max_key_fee, download_directory, download_timeout, search_timeout, cache_time):
    method_name = "settings_set"
    body = { "data_rate": data_rate, "max_key_fee": max_key_fee, "download_directory": download_directory, "download_timeout": download_timeout, "search_timeout": search_timeout, "cache_time": cache_time }
    return _request(method_name, body)



# Return daemon status
#
# Args:
#     'session_status' (optional): (bool) true to return session status,
#         default is false
# Returns:
#     (dict) Daemon status dictionary
def status(**opt_params):
    return _request("status", **opt_params)


# Get estimated cost for a lbry stream
#
# Args:
#     'name': (str) lbry name
#     'size' (optional): (int) stream size, in bytes. if provided an sd blob
#                         won't be downloaded.
# Returns:
#     (float) Estimated cost in lbry credits, returns None if uri is not
#         resolveable
def stream_cost_estimate(name, **opt_params):
    method_name = "stream_cost_estimate"
    body = { "name": name }
    return _request(method_name, body, **opt_params)



# List transactions belonging to wallet
#
# Args:
#     None
# Returns:
#     (list) List of transactions
def transaction_list():
    method_name = "transaction_list"
    return _request(method_name)


# Get a decoded transaction from a txid
#
# Args:
#     'txid': (str) txid of transaction
# Returns:
#     (dict) JSON formatted transaction
def transaction_show(txid):
    return _request("transaction_show", { 'txid': txid })


#  Get lbry version information
# Args: None
#  Returns:
#      (dict) Dictionary of lbry version information
#      {
#          'build': (str) build type (e.g. "dev", "rc", "release"),
#          'ip': (str) remote ip, if available,
#          'lbrynet_version': (str) lbrynet_version,
#          'lbryum_version': (str) lbryum_version,
#          'lbryschema_version': (str) lbryschema_version,
#          'os_release': (str) os release string
#          'os_system': (str) os name
#          'platform': (str) platform string
#          'processor': (str) processor type,
#          'python_version': (str) python version,
# }
#
def version():
    method_name = "version"
    return _request(method_name)

#  Return the balance of the wallet
#  Args:
#      'address' (optional): If address is provided only that balance wil
#      'include_unconfirmed' (optional): If set unconfirmed balance will
#       the only takes effect when address is also provided.
#  Returns:
#      (float) amount of lbry credits in wallet
def wallet_balance(**opt_params):
    method_name = "wallet_balance"
    return _request(method_name, {}, **opt_params)


#  Checks if an address is associated with the current wallet.
#  Args:
#      'address': (str) address to check in base58
#  Returns:
#      (bool) true, if address is associated with current wallet
def wallet_is_address_mine(address):
    method_name = "wallet_is_address_mine"
    body = { "address": address }
    return _request(method_name, body)


#  List wallet addresses
# Args: None
#  Returns:
#      List of wallet addresses
def wallet_list():
    method_name = "wallet_list"
    return _request(method_name)

# Generate a new wallet address
#
# Args:
#     None
# Returns:
#     (str) New wallet address in base58addresses
def wallet_new_address():
    method_name = "wallet_new_address"
    return _request(method_name)


#  Get public key from wallet address
#  Args:
#      'address': (str) wallet address in base58
#  Returns:
#      (list) list of public keys associated with address.
#          Could contain more than one public key if multisig.
def wallet_public_key():
    method_name = "wallet_public_key"
    return _request(method_name)


# Return an address containing no balance, will create
# a new address if there is none.
#
# Args:
#     None
# Returns:
#     (str) Unused wallet address in base58
def wallet_unused_address():
    method_name = "wallet_unused_address"
    return _request(method_name)
