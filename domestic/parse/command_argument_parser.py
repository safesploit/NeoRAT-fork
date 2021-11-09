def command_argument_parser(message):
  arguments = message.split('--')
  first = arguments[0]

  if first.endswith(' '):
    first = first[:-1]

  arguments_dict = {'message': first}

  for argument in arguments[1:]:
    key_value_list = [y for y in argument.split(' ') if y != '']

    key = key_value_list[0]
    value = key_value_list[1:]

    if len(key_value_list) == 1:
      arguments_dict[key] = True
    else:
      arguments_dict[key] = ' '.join(value)
  
  return arguments_dict