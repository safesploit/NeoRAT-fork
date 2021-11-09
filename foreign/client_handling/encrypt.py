from foreign.global_state import state


def encrypt(filename, decrypt):
  if decrypt:
    with open(filename, 'rb') as rf:
      filedata = state['settings']['encryption'].do_decrypt(rf.read())
    
    with open(filename, 'wb') as wf:
      wf.write(filedata)
    
    return {'message': f'{filename} successfully decrypted', 'text_mode': 'success'}
  else:
    with open(filename, 'rb') as rf:
      filedata = state['settings']['encryption'].do_encrypt(rf.read())

    with open(filename, 'wb') as wf:
      wf.write(filedata)
    
    return {'message': f'{filename} successfully encrypted', 'text_mode': 'success'}