# -*- coding: utf-8 -*-
"""
Created on Tue Nov 16 15:26:35 2021

@author: Guilherme Zanotelli
"""

from bs4 import BeautifulSoup
from more_itertools import sort_together

with open("api-docs.html", encoding='utf-8') as f:
    soup = BeautifulSoup(f, 'html.parser')
    
endpoints = {}

for endpoint in soup.find_all('div','opblock opblock-get is-open'):
    endpoint_name = endpoint.div.find_all('span')[1].a.text
    params = {'arg types':[],'description':[],'arg names':[], 'arg description':[]}
    for param in endpoint.find_all('tr','parameters'):
        if param.td.div.text.startswith('chave-api'):
            continue
        params['arg names'].append(param.td.div.text)
        params['arg types'].append(param.find('div','parameter__type').text)
        params['arg description'].append(param.find('td','col parameters-col_description').div.text)
    params['description'] = endpoint.div.div.text
    endpoints[endpoint_name]=params

full_text = ''

for endpoint, args_data in endpoints.items():
    path = endpoint.split('/')
    func = path[-2]+'_'+path[-1][1:-1] if path[-1].startswith(r'{') else path[-1]
    func = func.replace('-','_')
    args = []
    for arg, type_ in zip(args_data['arg names'], args_data['arg types']):
        type_ = type_[:3]
        default = '=None'
        if arg.endswith('*'):
            arg = f'AAA{arg[:-2]}'
            default = ''
        args.append(f'{arg}: {type_}{default}')
    
    try:
        args, descs = sort_together([args, args_data['arg description']])
    except ValueError:
        args, descs = [], []
    args = [arg.replace('AAA','') for arg in args]
    docstring = f'"""\n\t\t{args_data["description"]}\n\t\tParameters\n\t\t----------\n\t\t'
    for arg, desc in zip(args, descs):
        docstring += f'{arg}\n\t\t{desc}\n\t\t'
    docstring += '"""'
    args = ', '.join(args)
    full_text += f"\t#{endpoint}\n\tdef {func}(self, {args}):\n\t\t{docstring}\n\t\tquery_string = self._query_string(locals().copy())\n\t\treturn self._request(query_string)\n\n"

full_text.replace('\t','    ')
    