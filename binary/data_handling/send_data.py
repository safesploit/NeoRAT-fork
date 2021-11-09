import pickle
import zlib


def send_data(conn, data, settings, extra_data={}):
	encryption, encoding, headersize = settings
	data.update(extra_data)

	pickled_msg = pickle.dumps(data)
	compressed_msg = zlib.compress(pickled_msg, 5)
	encrypted_msg = encryption.do_encrypt(compressed_msg)
	final_msg = bytes(f'{len(encrypted_msg):<{headersize}}', encoding) + encrypted_msg
	conn.send(final_msg)