import pickle
import zlib


def recv_data(conn, settings, callback=None):
	encryption, headersize = settings
	mode = [True, 0, b'']

	while True:
		client_msg = conn.recv(81920)

		if mode[0]:
			mode[1] = int(client_msg[:headersize])
			mode[0] = False

		mode[2] += client_msg

		if len(mode[2])-headersize == mode[1]:
			decrypted_msg = encryption.do_decrypt(mode[2][headersize:])
			decompressed_msg = zlib.decompress(decrypted_msg)
			client_msg = pickle.loads(decompressed_msg)

			if callback:
				callback(conn, client_msg)

			return client_msg