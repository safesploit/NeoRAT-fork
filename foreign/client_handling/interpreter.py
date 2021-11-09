import contextlib
import io


def interpreter(execute):
  try:
    with io.StringIO() as stdout, contextlib.redirect_stdout(stdout):
      exec_data = exec(execute)
      return {'message': f'Python successfully interpreted', 'result': stdout.getvalue().strip(), 'text_mode': 'success'}
  except Exception as err:
    return {'message': f'Python could not be interpreted\nError message: \'{err}\'', 'text_mode': 'danger'}