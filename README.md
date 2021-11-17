# Interface em Python para o [API do Portal da Transparência](https://www.portaltransparencia.gov.br/api-de-dados)

O `portaldatransparencia` é um módulo que faz interface com o API do portal 
da transparência do governo federal. 

# Documentação
O `portaldatransparencia` foi desenvolvido na imagem e semelhança do próprio API do portal, 
então seguindo as indicações da [documentação original](http://api.portaldatransparencia.gov.br/) 
já dá uma ideia de como usar esse módulo. Porém o próprio módulo tem a documentação da página. 
Ainda assim, aqui tem alguns exemplos para ficar mais claro.

# Como usar
Primeiro, é necessário [cadastrar uma conta `gov.br`](http://portaldatransparencia.gov.br/api-de-dados/cadastrar-email) 
e gerar um token pessoal. Lembrando que para gerar o token é necessário que a conta tenha 2FA configurado. 
Depois, basta importar o `PortalDaTransparencia` do `portaldatransparencia` e criar os objetos que vão solicitar os dados do API:

```python
from portaldatransparencia import PortalDaTransparencia
token = '<seu token>'
portal = PortalDaTransparencia(token)

# Transferências realizadas para Florianópolis em Jan/2021 visando auxiliar no combate contra o COVID-19
result = portal.coronavirus.transferencias(mesAno=202101,codigoIbge='4205407')

# Lista de JSONs com dados sobre as transferências do período consultado
print(result)
```

O `PortalDaTransparencia` nada mais é que um aglomerado de outros portais, como o `Coronavirus`, ou o `DespesasPublicas`. 
Também é possível importar somente o portal de interesse:

```python
from portaldatransparencia import DespesasPublicas
token = '<seu token>'
portal = DespesasPublicas(token)

# Primeira página da consulta para os recursos recebidos do governo de pessoas físicas
result = portal.recursos_recebidos(mesAnoInicio='01/2020',mesAnoFim='01/2021')

# Lista de JSONs com dados sobre os recursos recebidos dentro do período consultado
print(result)
```

# Limites
*Texto de http://portaldatransparencia.gov.br/api-de-dados/cadastrar-email*

> A fim de garantir a estabilidade do ambiente, os seguintes limites são definidos:
> - De 00:00 às 06:00: até 700 requisições por minuto
> - Nos demais horários: 400 requisições por minuto
> - APIs restritas: 180 requisições por minuto.
> 
> As APIs restritas são:
> - /api-de-dados/despesas/documentos-por-favorecido
> - /api-de-dados/bolsa-familia-disponivel-por-cpf-ou-nis
> - /api-de-dados/bolsa-familia-por-municipio
> - /api-de-dados/bolsa-familia-sacado-por-nis
> - /api-de-dados/auxilio-emergencial-beneficiario-por-municipio
> - /api-de-dados/auxilio-emergencial-por-cpf-ou-nis
> - /api-de-dados/auxilio-emergencial-por-municipio
> - /api-de-dados/seguro-defeso-codigo
>
> Usos acima desses limites terão o token suspenso por 8 hora(s).

# Disclaimer

A maior parte do código escrito no `transpyrantportal` foi gerado automaticamente 
através de webscraping da página de documentação (`scraping.py`)

# Licença

O `transpyrantportal` está licensiado sobre a licença do MIT.
