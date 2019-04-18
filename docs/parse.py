import json
import glob

jsonpath = "./contracts/*.json"
prefix = "./contracts"

def parse():
  for filepath in glob.glob(jsonpath):
    print(filepath)
    outpath = filepath.replace("json", "rst")

    with open(filepath, "r") as jsonfile:
      data = json.load(jsonfile)
      _template(data, outpath)
      jsonfile.close()

def _template(data, out):
  with open(out, "w") as outfile:
    outfile.write(_template_meta(data))
    outfile.write(_template_structs(data))
    outfile.write(_template_constants(data))
    outfile.write(_template_states(data))
    outfile.write(_template_events(data))
    outfile.write(_template_external_functions(data))

  outfile.close()

def _template_meta(data):
  return f'''
{data['name']}
{'=' * len(data['name'])}

{data.get('description', '')}
'''

def _template_structs(data):
  structs = data.get('structs', [])
  if len(structs) == 0: return "\n"

  ret = '''
Struct
------
'''


  for struct in structs:
    ret += f'''
{struct['name']}
{'^' * len(struct['name'])}

{struct.get('description', '')}

Members
"""""""
'''
    for param in struct.get('members', []):
      ret += _template_variable(param['type'], param.get('name', ''), param.get('description', ''))

  return ret

def _template_events(data):
  events = data.get('events', [])
  if len(events) == 0: return "\n"

  ret = '''
Events
------
'''

  for event in events:
    ret += f'''
{event['name']}
{'^' * len(event['name'])}

{event.get('description', '')}

Parameters
""""""""""

'''
    params = event.get('params', [])
    if len(params) == 0:
      ret += "None\n"
    else:
      for param in params:
        ret += _template_variable(param['type'], param.get('name', ''), param.get('description', ''))

  return ret


def _template_external_functions(data):
  funcs = data.get('external-functions', [])
  if len(funcs) == 0: return "\n"

  ret = '''
External Functions
------------------

'''

  for func in funcs:
    ret += f'''
{func['name']}
{'^' * len(func['name'])}

{func.get('description', '')}

Parameters
""""""""""

'''
    params = func.get('params', [])
    if len(params) == 0:
      ret += "None\n"
    else:
      for param in params:
        ret += _template_variable(param['type'], param.get('name', ''), param.get('description', ''))

    ret += '''
Returns
"""""""

'''

    params = func.get('returns', [])
    if len(params) == 0:
      ret += "None\n"
    else:
      for param in params:
        ret += _template_variable(param['type'], param.get('name', ''), param.get('description', ''))

  return ret


def _template_constants(data):
  constants = data.get('public-constants', [])
  if len(constants) == 0: return "\n"

  ret = '''
Constants
---------

'''
  for param in constants:
    ret += _template_variable(param['type'], param.get('name', ''), param.get('description', ''))

  return ret

def _template_states(data):
  variables = data.get('public-state-variables', [])
  if len(variables) == 0: return "\n"

  ret = '''
Public State Variables
----------------------

'''
  for param in variables:
    ret += _template_variable(param['type'], param.get('name', ''), param.get('description', ''))

  return ret



def _template_variable(var_type, name, description):
  if len(description) != 0:
    description = f': {description}'

  if len(name) == 0:
    return f'- ``<{var_type}>``{description}\n'
  return f'- ``{name} <{var_type}>``{description}\n'

if __name__ == '__main__':
    parse()
