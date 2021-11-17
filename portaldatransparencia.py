
import requests
import inspect

class PortalDaTransparencia(object):

    def __init__(self, token):
        self.acordos_de_leniencia = AcordosDeLeniencia(token)
        self.auxilio_emergencial = AuxilioEmergencial(token)
        self.bpc = BPC(token)
        self.bolsa_familia = BolsaFamilia(token)
        self.ceis = CEIS(token)
        self.cnep = CNEP(token)
        self.ceaf = CEAF(token)
        self.contratos_pef = ContratosPEF(token)
        self.convenios_pef = ConveniosPEF(token)
        self.coronavirus = Coronavirus(token)
        self.despesas_publicas = DespesasPublicas(token)
        self.emendas_parlamentares = EmendasParlamentares(token)
        self.cepim = CEPIM(token)
        self.garantia_safra = GarantiaSafra(token)
        self.gastos_cartao_de_pagamento = GastosCartaoDePagamento(token)
        self.imoveis_funcionais = ImoveisFuncionais(token)
        self.licitacoes_pef = LicitacoesPEF(token)
        self.peti = Peti(token)
        self.seguro_defeso = SeguroDefeso(token)
        self.servidores_pef = ServidoresPEF(token)
        self.viagens = Viagens(token)
        self.orgaos = Orgaos(token)

class Portal(object):
    base_url = "http://api.portaldatransparencia.gov.br/api-de-dados/{endpoint}"

    def __init__(self, token):
        self._auth = {'chave-api-dados':token}

    def _request(self, query_string, endpoint=None):
        url = self.base_url
        if endpoint is None:
            endpoint = inspect.stack()[1].function.replace('_','-')
        elif endpoint == '':
            url = url.replace('/{endpoint}','{endpoint}')
        else:
            pass
        url = url.format(endpoint=f'{endpoint}{query_string}')
        response = requests.get(url, headers=self._auth)
        if response.ok:
            return response.json()
        else:
            raise requests.RequestException(f"API request resulted in status_code {response.status_code}")
    
    def _query_string(self, data):
        s = '?'
        for key, value in data.items():
            if value is None:
                pass
            elif key == 'self':
                pass
            else:
                if isinstance(value,str):
                    value = value.replace('/','%2F')
                s += f'{key}={value}&'
        return s[:-1]

class AcordosDeLeniencia(Portal):

    #/api-de-dados/acordos-leniencia
    def acordos_leniencia(self, pagina: int=1, cnpjSancionado: str=None, dataFinalSancao: str=None, dataInicialSancao: str=None, nomeSancionado: str=None, situacao: str=None):
        """
        Consulta os registros de Acordos de Leniência por Nome ou CNPJ do Sancionado/Situação/Período
        Parameters
        ----------
        pagina: int
        Página consultada

        cnpjSancionado: str=None
        CNPJ sancionado
        dataFinalSancao: str=None
        Data final da sanção (DD/MM/AAAA)

        dataInicialSancao: str=None
        Data inicial da sanção (DD/MM/AAAA)

        nomeSancionado: str=None
        Nome, nome fantasia ou razão social do sancionado

        situacao: str=None
        Situação do acordo

        """
        query_string = self._query_string(locals().copy())
        return self._request(query_string)

    #/api-de-dados/acordos-leniencia/{id}
    def acordos_leniencia_id(self, id: int):
        """
        Consulta um registro de Acordo de Leniência pelo id
        Parameters
        ----------
        id: int
        ID do registro
        """
        query_string = f'/{id}'
        endpoint = 'acordos-leniencia'
        return self._request(query_string, endpoint)

class AuxilioEmergencial(Portal):

    #/api-de-dados/auxilio-emergencial-beneficiario-por-municipio
    def auxilio_emergencial_beneficiario_por_municipio(self, codigoIbge: str, mesAno: int, pagina: int):
        """
        Consulta os registros dos beneficiários por município e mês/ano
        Parameters
        ----------
        codigoIbge: str
        Código IBGE

        mesAno: int
        Mês e Ano de referência (AAAAMM)

        pagina: int
        Página consultada

        """
        query_string = self._query_string(locals().copy())
        return self._request(query_string)

    #/api-de-dados/auxilio-emergencial-por-cpf-ou-nis
    def auxilio_emergencial_por_cpf_ou_nis(self, pagina: int=1, codigoBeneficiario: str=None, codigoResponsavelFamiliar: str=None):
        """
        Consulta os registros de auxílio emergencial por CPF/NIS
        Parameters
        ----------
        pagina: int
        Página consultada

        codigoBeneficiario: str=None
        CPF/NIS Beneficiário

        codigoResponsavelFamiliar: str=None
        CPF/NIS Responsável Familiar

        """
        query_string = self._query_string(locals().copy())
        return self._request(query_string)

    #/api-de-dados/auxilio-emergencial-por-municipio
    def auxilio_emergencial_por_municipio(self, codigoIbge: str, mesAno: int, pagina: int):
        """
        Consulta os registros de auxílio emergencial por Município
        Parameters
        ----------
        codigoIbge: str
        Código IBGE

        mesAno: int
        Mês e Ano de referência (AAAAMM)

        pagina: int
        Página consultada

        """
        query_string = self._query_string(locals().copy())
        return self._request(query_string)

class BPC(Portal):

    #/api-de-dados/bpc-por-cpf-ou-nis
    def bpc_por_cpf_ou_nis(self, codigo: str, pagina: int):
        """
        Consulta os registros de Benefício de Prestação Continuada por CPF/NIS
        Parameters
        ----------
        codigo: str
        CPF/NIS

        pagina: int
        Página consultada

        """
        query_string = self._query_string(locals().copy())
        return self._request(query_string)

    #/api-de-dados/bpc-por-municipio
    def bpc_por_municipio(self, codigoIbge: str, mesAno: int, pagina: int):
        """
        Consulta os registros de Benefício de Prestação Continuada por Município
        Parameters
        ----------
        codigoIbge: str
        Código IBGE

        mesAno: int
        Mês e Ano de referência (AAAAMM)

        pagina: int
        Página consultada

        """
        query_string = self._query_string(locals().copy())
        return self._request(query_string)

class BolsaFamilia(Portal):

    #/api-de-dados/bolsa-familia-disponivel-por-cpf-ou-nis
    def bolsa_familia_disponivel_por_cpf_ou_nis(self, codigo: str, pagina: int=1, anoMesCompetencia: int=None, anoMesReferencia: int=None):
        """
        Consulta as parcelas disponibilizadas pelo Bolsa Família pelo CPF/NIS
        Parameters
        ----------
        codigo: str
        CPF/NIS (sem máscara, somente números)

        pagina: int
        Página consultada

        anoMesCompetencia: int=None
        Ano e mês de competência (AAAAMM)

        anoMesReferencia: int=None
        Ano e mês de referência (AAAAMM)

        """
        query_string = self._query_string(locals().copy())
        return self._request(query_string)

    #/api-de-dados/bolsa-familia-por-municipio
    def bolsa_familia_por_municipio(self, codigoIbge: str, mesAno: int, pagina: int):
        """
        Consulta as parcelas do Bolsa Família por Município
        Parameters
        ----------
        codigoIbge: str
        Código IBGE

        mesAno: int
        Mês e Ano de referência (AAAAMM)

        pagina: int
        Página consultada

        """
        query_string = self._query_string(locals().copy())
        return self._request(query_string)

    #/api-de-dados/bolsa-familia-sacado-por-nis
    def bolsa_familia_sacado_por_nis(self, nis: str, pagina: int=1, anoMesCompetencia: int=None, anoMesReferencia: int=None):
        """
        Consulta as parcelas sacadas pelo Bolsa Família pelo NIS
        Parameters
        ----------
        nis: str
        NIS (sem máscara, somente números)

        pagina: int
        Página consultada

        anoMesCompetencia: int=None
        Ano e mês de competência (AAAAMM)

        anoMesReferencia: int=None
        Ano e mês de referência (AAAAMM)

        """
        query_string = self._query_string(locals().copy())
        return self._request(query_string)

class CEIS(Portal):

    #/api-de-dados/ceis
    def ceis(self, pagina: int=1, codigoSancionado: str=None, dataFinalSancao: str=None, dataInicialSancao: str=None, nomeSancionado: str=None, orgaoSancionador: str=None):
        """
        Consulta os registros do CEIS por CNPJ ou CPF Sancionado/Órgão Sancionador/Período
        Parameters
        ----------
        pagina: int
        Página consultada

        codigoSancionado: str=None
        CNPJ ou CPF Sancionado
        dataFinalSancao: str=None
        Data Final da Sanção (DD/MM/AAAA)

        dataInicialSancao: str=None
        Data Inicial da Sanção (DD/MM/AAAA)

        nomeSancionado: str=None
        Nome, nome fantasia ou razão social do Sancionado

        orgaoSancionador: str=None
        Órgão Sancionador

        """
        query_string = self._query_string(locals().copy())
        return self._request(query_string)

    #/api-de-dados/ceis/{id}
    def ceis_id(self, id: int):
        """
        Consulta um registro do CEIS pelo id
        Parameters
        ----------
        id: int
        ID do registro
        """
        query_string = f'/{id}'
        endpoint = 'ceis'
        return self._request(query_string, endpoint)

class CNEP(Portal):
    #/api-de-dados/cnep
    def cnep(self, pagina: int=1, codigoSancionado: str=None, dataFinalSancao: str=None, dataInicialSancao: str=None, nomeSancionado: str=None, orgaoSancionador: str=None):
        """
        Consulta os registros do CNEP por CNPJ ou CPF Sancionado/Órgão Sancionador/Período
        Parameters
        ----------
        pagina: int
        Página consultada

        codigoSancionado: str=None
        CNPJ ou CPF do Sancionado
        dataFinalSancao: str=None
        Data Final da Sanção (DD/MM/AAAA)

        dataInicialSancao: str=None
        Data Inicial da Sanção (DD/MM/AAAA)

        nomeSancionado: str=None
        Nome, nome fantasia ou razão social do Sancionado

        orgaoSancionador: str=None
        Órgão Sancionador

        """
        query_string = self._query_string(locals().copy())
        return self._request(query_string)

    #/api-de-dados/cnep/{id}
    def cnep_id(self, id: int):
        """
        Consulta um registro do CNEP pelo id
        Parameters
        ----------
        id: int
        ID do registro
        """
        query_string = f'/{id}'
        endpoint = 'cnep'
        return self._request(query_string, endpoint)

class CEAF(Portal):
    #/api-de-dados/ceaf
    def ceaf(self, pagina: int=1, cpfSancionado: str=None, dataPublicacaoFim: str=None, dataPublicacaoInicio: str=None, nomeSancionado: str=None, orgaoLotacao: str=None):
        """
        Consulta os registros do CEAF por CPF/Órgão de Lotação/Período
        Parameters
        ----------
        pagina: int
        Página consultada

        cpfSancionado: str=None
        CPF do sancionado
        dataPublicacaoFim: str=None
        Data publicação fim (DD/MM/AAAA)

        dataPublicacaoInicio: str=None
        Data publicação início (DD/MM/AAAA)

        nomeSancionado: str=None
        Nome do sancionado
        orgaoLotacao: str=None
        Órgão de lotação

        """
        query_string = self._query_string(locals().copy())
        return self._request(query_string)

    #/api-de-dados/ceaf/{id}
    def ceaf_id(self, id: int):
        """
        Consulta um registro do CEAF pelo id
        Parameters
        ----------
        id: int
        ID do registro
        """
        query_string = f'/{id}'
        endpoint = 'ceaf'
        return self._request(query_string, endpoint)

class ContratosPEF(Portal):

    def __init__(self, token):
        super().__init__(token)
        self.base_url = self.base_url.format(endpoint='contratos/{endpoint}')

    #/api-de-dados/contratos
    def todos(self, codigoOrgao: str, dataFinal: str, dataInicial: str, pagina: int):
        """
        Consulta os todos contratos do Poder Executivo Federal
        Parameters
        ----------
        codigoOrgao: str
        Código do Órgão (SIAFI)

        dataFinal: str
        Data vigência fim (DD/MM/AAAA)

        dataInicial: str
        Data vigência início (DD/MM/AAAA)

        pagina: int
        Página consultada

        """
        query_string = self._query_string(locals().copy())
        endpoint = ''
        return self._request(query_string, endpoint)

    #/api-de-dados/contratos/apostilamento
    def apostilamento(self, id: int):
        """
        Consulta os apostilamentos do contrato pelo id do contrato
        Parameters
        ----------
        id: int
        ID do registro
        """
        query_string = self._query_string(locals().copy())
        return self._request(query_string)

    #/api-de-dados/contratos/cpf-cnpj
    def cpf_cnpj(self, cpfCnpj: str, pagina: int):
        """
        Consulta um contrato do Poder Executivo Federal pelo CPF/CNPJ do Fornecedor
        Parameters
        ----------
        cpfCnpj: str
        CPF/CNPJ do Fornecedor

        pagina: int
        Página consultada

        """
        query_string = self._query_string(locals().copy())
        return self._request(query_string)

    #/api-de-dados/contratos/documentos-relacionados
    def documentos_relacionados(self, id: int):
        """
        Consulta os documentos relacionados a um contrato pelo id do contrato
        Parameters
        ----------
        id: int
        ID do registro
        """
        query_string = self._query_string(locals().copy())
        return self._request(query_string)

    #/api-de-dados/contratos/id
    def id(self, id: int):
        """
        Consulta um contrato do Poder Executivo Federal pelo id
        Parameters
        ----------
        id: int
        ID do registro
        """
        query_string = self._query_string(locals().copy())
        return self._request(query_string)

    #/api-de-dados/contratos/numero
    def numero(self, numero: str, pagina: int):
        """
        Consulta um contrato do Poder Executivo Federal pelo número do contrato
        Parameters
        ----------
        numero: str
        Número do contrato

        pagina: int
        Página consultada

        """
        query_string = self._query_string(locals().copy())
        return self._request(query_string)

    #/api-de-dados/contratos/termo-aditivo
    def termo_aditivo(self, id: int):
        """
        Consulta os termos aditivos do contrato pelo id do contrato
        Parameters
        ----------
        id: int
        ID do registro
        """
        query_string = self._query_string(locals().copy())
        return self._request(query_string)

class ConveniosPEF(Portal):

    def __init__(self, token):
        super().__init__(token)
        self.base_url = self.base_url.format(endpoint='convenios/{endpoint}')
    
    #/api-de-dados/convenios
    def todos(self, pagina: int=1, codigoIBGE: str=None, codigoOrgao: str=None, convenente: str=None, dataFinal: str=None, dataInicial: str=None, dataUltimaLiberacaoFinal: str=None, dataUltimaLiberacaoInicial: str=None, dataVigenciaFinal: str=None, dataVigenciaInicial: str=None, funcao: str=None, numero: str=None, numeroOriginal: str=None, situacao: str=None, subfuncao: str=None, tipoConvenente: str=None, tipoInstrumento: str=None, uf: str=None, valorLiberadoAte: str=None, valorLiberadoDe: str=None, valorTotalAte: str=None, valorTotalDe: str=None):
        """
        Consulta todos convênios do Poder Executivo Federal
        Parameters
        ----------
        pagina: int
        Página consultada

        codigoIBGE: str=None
        Município (Código IBGE)

        codigoOrgao: str=None
        Código do Órgão (SIAFI)

        convenente: str=None
        Convenente
        dataFinal: str=None
        Data referência fim (DD/MM/AAAA)

        dataInicial: str=None
        Data referência início (DD/MM/AAAA)

        dataUltimaLiberacaoFinal: str=None
        Data da última liberação de recurso fim (DD/MM/AAAA)

        dataUltimaLiberacaoInicial: str=None
        Data da última liberação de recurso início (DD/MM/AAAA)

        dataVigenciaFinal: str=None
        Data de vigência fim (DD/MM/AAAA)

        dataVigenciaInicial: str=None
        Data de vigência início (DD/MM/AAAA)

        funcao: str=None
        Código Função

        numero: str=None
        Número do convênio

        numeroOriginal: str=None
        Número original do convênio

        situacao: str=None
        Código Situação

        subfuncao: str=None
        Código Subfunção

        tipoConvenente: str=None
        Tipo de Convenente
        tipoInstrumento: str=None
        Código Tipo de Instrumento

        uf: str=None
        Sigla UF
        valorLiberadoAte: str=None
        Valor liberado até (Formato: 1.000,00)

        valorLiberadoDe: str=None
        Valor liberado de (Formato: 1.000,00)

        valorTotalAte: str=None
        Valor total até (Formato: 1.000,00)

        valorTotalDe: str=None
        Valor total de (Formato: 1.000,00)

        """
        query_string = self._query_string(locals().copy())
        endpoint = ''
        return self._request(query_string, endpoint)

    #/api-de-dados/convenios/id
    def id(self, id: int):
        """
        Consulta um convênio do Poder Executivo Federal pelo id
        Parameters
        ----------
        id: int
        ID do registro
        """
        query_string = self._query_string(locals().copy())
        return self._request(query_string)

    #/api-de-dados/convenios/numero
    def numero(self, numero: str, pagina: int):
        """
        Consulta um convênio do Poder Executivo Federal pelo número do contrato
        Parameters
        ----------
        numero: str
        Número do convênio

        pagina: int
        Página consultada

        """
        query_string = self._query_string(locals().copy())
        return self._request(query_string)

    #/api-de-dados/convenios/numero-original
    def numero_original(self, numeroOriginal: str, pagina: int):
        """
        Consulta um convênio do Poder Executivo Federal pelo número original do contrato
        Parameters
        ----------
        numeroOriginal: str
        Número original do convênio

        pagina: int
        Página consultada

        """
        query_string = self._query_string(locals().copy())
        return self._request(query_string)

    #/api-de-dados/convenios/tipo-instrumento
    def tipo_instrumento(self, ):
        """
        Consulta os tipos de instrumentos usados nos convênios
        Parameters
        ----------
        """
        query_string = self._query_string(locals().copy())
        return self._request(query_string)

class Coronavirus(Portal):

    def __init__(self, token):
        super().__init__(token)
        self.base_url = self.base_url.format(endpoint='coronavirus/{endpoint}')
    
    #/api-de-dados/coronavirus/movimento-liquido-despesa
    def movimento_liquido_despesa(self, mesAnoLancamento: int, pagina: int=1, acao: str=None, elementoDespesa: str=None, funcao: str=None, grupoDespesa: str=None, idPlanoOrcamentario: int=None, modalidadeAplicacao: str=None, programa: str=None, subfuncao: str=None):
        """
        Consulta de movimentação líquida mensal das despesas do Poder Executivo Federal pela classificação funcional programática
        Parameters
        ----------
        mesAnoLancamento: int
        Mês e Ano de lançamento (AAAAMM)

        pagina: int
        Página consultada

        acao: str=None
        Ação (código SIAFI)

        elementoDespesa: str=None
        Elemento Despesa (código SIAFI)

        funcao: str=None
        Função (código SIAFI)

        grupoDespesa: str=None
        Grupo Despesa (código SIAFI)

        idPlanoOrcamentario: int=None
        Id Plano orçamentário

        modalidadeAplicacao: str=None
        Modalidade de Aplicação (código SIAFI)

        programa: str=None
        Programa (código SIAFI)

        subfuncao: str=None
        Subfunção (código SIAFI)

        """
        query_string = self._query_string(locals().copy())
        return self._request(query_string)

    #/api-de-dados/coronavirus/transferencias
    def transferencias(self, mesAno: int, pagina: int=1, codigoIbge: str=None, codigoOrgao: str=None, tipoTransferencia: int=None, uf: str=None):
        """
        Consulta de transferências mensal das despesas do Poder Executivo Federal pela classificação funcional programática
        Parameters
        ----------
        mesAno: int
        Mês e Ano (AAAAMM)

        pagina: int
        Página consultada

        codigoIbge: str=None
        Município

        codigoOrgao: str=None
        Órgão (código SIAFI)

        tipoTransferencia: int=None
        ID do Tipo de Transferência

        uf: str=None
        Sigla UF
        """
        query_string = self._query_string(locals().copy())
        return self._request(query_string)

class DespesasPublicas(Portal):

    def __init__(self, token):
        super().__init__(token)
        self.base_url = self.base_url.format(endpoint='despesas/{endpoint}')

    #/api-de-dados/despesas/api-de-dados/despesas/itens-de-empenho/historico
    def itens_de_empenho_historico(self, codigoDocumento: str, sequencial: int, pagina: int=1):
        """
        Consulta o histórico de um item de empenho
        Parameters
        ----------
        codigoDocumento: str
        Código do empenho (Unidade Gestora + Gestão + Número do documento)

        pagina: int
        Página consultada

        sequencial: int
        Número sequencial do item de empenho

        """
        query_string = self._query_string(locals().copy())
        endpoint = self.base_url.format(endpoint='api-de-dados/despesas/itens-de-empenho/historico')
        return self._request(query_string, endpoint)

    #/api-de-dados/despesas/documentos
    def documentos(self, dataEmissao: str, fase: int, pagina: int=1, gestao: str=None, unidadeGestora: str=None):
        """
        Consulta todos os documentos de despesas
        Parameters
        ----------
        dataEmissao: str
        Data de emissão (DD/MM/AAAA)

        fase: int
        Fase da despesa (1 - Empenho, 2 - Liquidação, 3 - Pagamento)

        pagina: int
        Página consultada

        gestao: str=None
        Gestão (código SIAFI)

        unidadeGestora: str=None
        Unidade gestora emitente (código SIAFI)

        """
        query_string = self._query_string(locals().copy())
        return self._request(query_string)

    #/api-de-dados/despesas/documentos-por-favorecido
    def documentos_por_favorecido(self, ano: int, codigoPessoa: str, fase: int, pagina: int=1, gestao: str=None, ug: str=None):
        """
        Consulta Empenhos, Liquidações e Pagamentos emitidos para um favorecido
        Parameters
        ----------
        ano: int
        Ano de emissão do documento

        codigoPessoa: str
        Código do Favorecido (CPF, CNPJ ou código do SIAFI)

        fase: int
        Fase da despesa (1 - Empenho, 2 - Liquidação, 3 - Pagamento)

        pagina: int
        Página consultada

        gestao: str=None
        Código da gestão do documento

        ug: str=None
        Código da unidade gestora emissora do documento

        """
        query_string = self._query_string(locals().copy())
        return self._request(query_string)

    #/api-de-dados/despesas/documentos-relacionados
    def documentos_relacionados(self, codigoDocumento: str, fase: int):
        """
        Consulta os documentos relacionados a um Empenho, Liquidação ou Pagamento
        Parameters
        ----------
        codigoDocumento: str
        Código do documento (Unidade Gestora + Gestão + Número do documento)

        fase: int
        Fase da despesa (1 - Empenho, 2 - Liquidação, 3 - Pagamento)

        """
        query_string = self._query_string(locals().copy())
        return self._request(query_string)

    #/api-de-dados/despesas/documentos/{codigo}
    def documentos_codigo(self, codigo: str):
        """
        Consulta um documento pelo código (Unidade Gestora + Gestão + Número do documento)
        Parameters
        ----------
        codigo: str
        Código do registro

        """
        query_string = f'/{codigo}'
        endpoint = 'documentos'
        return self._request(query_string)

    #/api-de-dados/despesas/empenhos-impactados
    def empenhos_impactados(self, codigoDocumento: str, fase: int, pagina: int):
        """
        Consulta empenhos impactados por documento/fase
        Parameters
        ----------
        codigoDocumento: str
        Código do documento (Unidade Gestora + Gestão + Número do documento)

        fase: int
        Fase da despesa (2 - Liquidação, 3 - Pagamento)

        pagina: int
        Página consultada

        """
        query_string = self._query_string(locals().copy())
        return self._request(query_string)

    #/api-de-dados/despesas/favorecidos-finais-por-documento
    def favorecidos_finais_por_documento(self, codigoDocumento: str, pagina: int):
        """
        Consulta favorecidos finais por documento
        Parameters
        ----------
        codigoDocumento: str
        Código do documento (Unidade Gestora + Gestão + Número do documento)

        pagina: int
        Página consultada

        """
        query_string = self._query_string(locals().copy())
        return self._request(query_string)

    #/api-de-dados/despesas/itens-de-empenho
    def itens_de_empenho(self, codigoDocumento: str, pagina: int):
        """
        Consulta os itens de um Empenho
        Parameters
        ----------
        codigoDocumento: str
        Código do empenho (Unidade Gestora + Gestão + Número do documento)

        pagina: int
        Página consultada

        """
        query_string = self._query_string(locals().copy())
        return self._request(query_string)

    #/api-de-dados/despesas/plano-orcamentario
    def plano_orcamentario(self, ano: int, pagina: int=1, codPOIdentfAcompanhamento: str=None, codPlanoOrcamentario: str=None, descPlanoOrcamentario: str=None):
        """
        Consulta Plano orçamentário
        Parameters
        ----------
        ano: int
        Ano
        pagina: int
        Página consultada

        codPOIdentfAcompanhamento: str=None
        Identificado de acompanhamento
        codPlanoOrcamentario: str=None
        Código Plano Orçamentária

        descPlanoOrcamentario: str=None
        Descrição Plano Orçamentário

        """
        query_string = self._query_string(locals().copy())
        return self._request(query_string)

    #/api-de-dados/despesas/por-funcional-programatica
    def por_funcional_programatica(self, ano: int, pagina: int=1, acao: str=None, funcao: str=None, programa: str=None, subfuncao: str=None):
        """
        Consulta as despesas do Poder Executivo Federal pela classificação funcional programática
        Parameters
        ----------
        ano: int
        Ano da despesa (AAAA)

        pagina: int
        Página consultada

        acao: str=None
        Ação (código SIAFI)

        funcao: str=None
        Função (código SIAFI)

        programa: str=None
        Programa (código SIAFI)

        subfuncao: str=None
        Subfunção (código SIAFI)

        """
        query_string = self._query_string(locals().copy())
        return self._request(query_string)

    #/api-de-dados/despesas/por-funcional-programatica/movimentacao-liquida
    def por_funcional_programatica_movimentacao_liquida(self, ano: int, pagina: int=1, acao: str=None, elementoDespesa: str=None, funcao: str=None, grupoDespesa: str=None, idPlanoOrcamentario: int=None, modalidadeAplicacao: str=None, programa: str=None, subfuncao: str=None):
        """
        Consulta de movimentação líquida anual das despesas do Poder Executivo Federal pela classificação funcional programática
        Parameters
        ----------
        ano: int
        Ano da despesa (AAAA)

        pagina: int
        Página consultada

        acao: str=None
        Ação (código SIAFI)

        elementoDespesa: str=None
        Elemento Despesa (código SIAFI)

        funcao: str=None
        Função (código SIAFI)

        grupoDespesa: str=None
        Grupo Despesa (código SIAFI)

        idPlanoOrcamentario: int=None
        Id Plano orçamentário

        modalidadeAplicacao: str=None
        Modalidade de Aplicação (código SIAFI)

        programa: str=None
        Programa (código SIAFI)

        subfuncao: str=None
        Subfunção (código SIAFI)

        """
        query_string = self._query_string(locals().copy())
        endpoint = 'por-funcional-programatica/movimentacao-liquida'
        return self._request(query_string)

    #/api-de-dados/despesas/por-orgao
    def por_orgao(self, ano: int, pagina: int=1, orgao: str=None, orgaoSuperior: str=None):
        """
        Consulta as despesas dos órgão do Poder Executivo Federal
        Parameters
        ----------
        ano: int
        Ano da despesa (AAAA)

        pagina: int
        Página consultada

        orgao: str=None
        Órgão/Entidade vinculada (código SIAFI)

        orgaoSuperior: str=None
        Órgão superior (código SIAFI)

        """
        query_string = self._query_string(locals().copy())
        return self._request(query_string)

    #/api-de-dados/despesas/recursos-recebidos
    def recursos_recebidos(self, mesAnoFim: str, mesAnoInicio: str, pagina: int=1, codigoFavorecido: str=None, codigoIBGE: str=None, nomeFavorecido: str=None, orgao: str=None, orgaoSuperior: str=None, tipoFavorecido: str=None, uf: str=None, unidadeGestora: str=None):
        """
        Recebimento de recursos por favorecido
        Parameters
        ----------
        mesAnoFim: str
        Mês ano fim (MM/AAAA)

        mesAnoInicio: str
        Mês ano início (MM/AAAA)

        pagina: int
        Página consultada

        codigoFavorecido: str=None
        CNPJ / CPF / Código do favorecido

        codigoIBGE: str=None
        Município

        nomeFavorecido: str=None
        Nome Favorecido
        orgao: str=None
        Órgão/Entidade vinculada (código SIAFI)

        orgaoSuperior: str=None
        Órgão superior (código SIAFI)

        tipoFavorecido: str=None
        Tipo de favorecido
        uf: str=None
        Sigla UF
        unidadeGestora: str=None
        Unidade gestora (código SIAFI)

        """
        query_string = self._query_string(locals().copy())
        return self._request(query_string)

    #/api-de-dados/despesas/tipo-transferencia
    def tipo_transferencia(self, ):
        """
        Consulta os tipos de transferências usados nas despesas
        Parameters
        ----------
        """
        query_string = self._query_string(locals().copy())
        return self._request(query_string)

class EmendasParlamentares(Portal):

    #/api-de-dados/emendas
    def emendas(self, pagina: int=1, ano: int=None, codigoEmenda: str=None, codigoFuncao: str=None, codigoSubfuncao: str=None, nomeAutor: str=None, numeroEmenda: str=None):
        """
        Consulta as emendas parlamentares
        Parameters
        ----------
        pagina: int
        Página consultada

        ano: int=None
        Ano
        codigoEmenda: str=None
        Código da Emenda

        codigoFuncao: str=None
        Código da função

        codigoSubfuncao: str=None
        Código da subfunção

        nomeAutor: str=None
        Nome do Autor
        numeroEmenda: str=None
        Número da emenda

        """
        query_string = self._query_string(locals().copy())
        return self._request(query_string)

    #/api-de-dados/emendas/documentos/{codigo}
    def documentos_codigo(self, codigo: str, pagina: int):
        """
        Consulta os documentos relacionados à emenda parlamentar pelo código da emenda
        Parameters
        ----------
        codigo: str
        Código da emenda

        pagina: int
        Página consultada

        """
        query_string = f'/{codigo}'
        endpoint = 'emendas/documentos'
        return self._request(query_string)

class CEPIM(Portal):

    #/api-de-dados/cepim
    def cepim(self, pagina: int=1, cnpjSancionado: str=None, nomeSancionado: str=None, orgaoEntidade: str=None, ufSancionado: str=None):
        """
        Consulta os registros do CEPIM por CNPJ ou CPF Sancionado/Órgão superior
        Parameters
        ----------
        pagina: int
        Página consultada

        cnpjSancionado: str=None
        CNPJ do Sancionado
        nomeSancionado: str=None
        Nome, nome fantasia ou razão social do Sancionado

        orgaoEntidade: str=None
        Órgão/Entidade

        ufSancionado: str=None
        UF do Sancionado (sigla)

        """
        query_string = self._query_string(locals().copy())
        return self._request(query_string)

    #/api-de-dados/cepim/{id}
    def cepim_id(self, id: int):
        """
        Consulta um registro do CEPIM pelo id
        Parameters
        ----------
        id: int
        ID do registro
        """
        query_string = f'/{id}'
        endpoint = 'cepim'
        return self._request(query_string)

class GarantiaSafra(Portal):

    #/api-de-dados/safra-codigo-por-cpf-ou-nis
    def safra_codigo_por_cpf_ou_nis(self, codigo: str, pagina: int):
        """
        Consulta os registros Garantia-Safra por CPF/NIS
        Parameters
        ----------
        codigo: str
        CPF/NIS

        pagina: int
        Página consultada

        """
        query_string = self._query_string(locals().copy())
        return self._request(query_string)

    #/api-de-dados/safra-por-municipio
    def safra_por_municipio(self, codigoIbge: str, mesAno: int, pagina: int):
        """
        Consulta os registros Garantia-Safra
        Parameters
        ----------
        codigoIbge: str
        Código IBGE

        mesAno: int
        Mês e Ano de referência (AAAAMM)

        pagina: int
        Página consultada

        """
        query_string = self._query_string(locals().copy())
        return self._request(query_string)

class GastosCartaoDePagamento(Portal):

    #/api-de-dados/cartoes
    def cartoes(self, pagina: int=1, codigoOrgao: str=None, cpfCnpjFavorecido: str=None, cpfPortador: str=None, dataTransacaoFim: str=None, dataTransacaoInicio: str=None, mesExtratoFim: str=None, mesExtratoInicio: str=None, tipoCartao: int=None, valorAte: str=None, valorDe: str=None):
        """
        Consulta os registros de Cartões de Pagamento
        Parameters
        ----------
        pagina: int
        Página consultada

        codigoOrgao: str=None
        Órgão/Entidade (Código SIAFI)

        cpfCnpjFavorecido: str=None
        Favorecido (CPF/CNPJ)

        cpfPortador: str=None
        Portador (CPF)

        dataTransacaoFim: str=None
        Data transação fim (DD/MM/AAAA)

        dataTransacaoInicio: str=None
        Data transação início (DD/MM/AAAA)

        mesExtratoFim: str=None
        Mês extrato fim (MM/AAAA)

        mesExtratoInicio: str=None
        Mês extrato início (MM/AAAA)

        tipoCartao: int=None
        Tipo de cartão (CPGF=1 ou CPCC=2 ou CPDC=3)

        valorAte: str=None
        Valor até (####,##)

        valorDe: str=None
        Valor de (####,##)

        """
        query_string = self._query_string(locals().copy())
        return self._request(query_string)

class ImoveisFuncionais(Portal):

    #/api-de-dados/imoveis
    def imoveis(self, pagina: int=1, cep: str=None, codigoOrgaoSiafiResponsavelGestao: str=None, endereco: str=None, regiao: str=None, situacao: str=None):
        """
        Consulta relação de imóveis
        Parameters
        ----------
        pagina: int
        Página consultada

        cep: str=None
        CEP
        codigoOrgaoSiafiResponsavelGestao: str=None
        Código do Órgão (SIAFI)

        endereco: str=None
        Endereço

        regiao: str=None
        Região

        situacao: str=None
        Situação Imóvel

        """
        query_string = self._query_string(locals().copy())
        return self._request(query_string)

    #/api-de-dados/permissionarios
    def permissionarios(self, pagina: int=1, codigoOrgaoSiafiOcupante: str=None, cpfOcupante: str=None, dataFimOcupacao: str=None, dataInicioOcupacao: str=None):
        """
        Consulta relação de ocupantes
        Parameters
        ----------
        pagina: int
        Página consultada

        codigoOrgaoSiafiOcupante: str=None
        Código do Órgão (SIAFI)

        cpfOcupante: str=None
        CPF Ocupante
        dataFimOcupacao: str=None
        Data fim ocupação (DD/MM/AAAA)

        dataInicioOcupacao: str=None
        Data início ocupação(DD/MM/AAAA)

        """
        query_string = self._query_string(locals().copy())
        return self._request(query_string)

    #/api-de-dados/situacao-imovel
    def situacao_imovel(self):
        """
        Consulta situações dos imóveis funcionais
        Parameters
        ----------
        """
        query_string = self._query_string(locals().copy())
        return self._request(query_string)

class LicitacoesPEF(Portal):

    def __init__(self, token):
        super().__init__(token)
        self.base_url = self.base_url.format(endpoint='licitacoes/{endpoint}')
    
    #/api-de-dados/licitacoes
    def todos(self, codigoOrgao: str, dataFinal: str, dataInicial: str, pagina: int):
        """
        Consulta todas as licitações do Poder Executivo Federal
        Parameters
        ----------
        codigoOrgao: str
        Código do Órgão (SIAFI)

        dataFinal: str
        Data de abertura final (DD/MM/AAAA)

        dataInicial: str
        Data de abertura inicial (DD/MM/AAAA)

        pagina: int
        Página consultada

        """
        query_string = self._query_string(locals().copy())
        endpoint = ''
        return self._request(query_string, endpoint)

    #/api-de-dados/licitacoes/{id}
    def licitacoes_id(self, id: int):
        """
        Consulta uma licitação do Poder Executivo Federal pelo id
        Parameters
        ----------
        id: int
        ID do registro
        """
        query_string = f'/{id}'
        endpoint =''
        return self._request(query_string, endpoint)

    #/api-de-dados/licitacoes/contratos-relacionados-licitacao
    def contratos_relacionados_licitacao(self, codigoModalidade: str, codigoUG: str, numero: str):
        """
        Consulta os contratos relacionados a licitação
        Parameters
        ----------
        codigoModalidade: str
        Código da Modalidade da Licitação

        codigoUG: str
        Código da Unidade Gestora

        numero: str
        Número da Licitação (NNNNNAAAA)

        """
        query_string = self._query_string(locals().copy())
        return self._request(query_string)

    #/api-de-dados/licitacoes/empenhos
    def empenhos(self, codigoModalidade: str, codigoUG: str, numero: str, pagina: int):
        """
        Consulta os empenhos de uma licitação
        Parameters
        ----------
        codigoModalidade: str
        Código da Modalidade da Licitação

        codigoUG: str
        Código da Unidade Gestora

        numero: str
        Número da Licitação (NNNNNAAAA)

        pagina: int
        Página consultada

        """
        query_string = self._query_string(locals().copy())
        return self._request(query_string)

    #/api-de-dados/licitacoes/modalidades
    def modalidades(self, ):
        """
        Consulta as modalidades de licitação
        Parameters
        ----------
        """
        query_string = self._query_string(locals().copy())
        return self._request(query_string)

    #/api-de-dados/licitacoes/participantes
    def participantes(self, codigoModalidade: str, codigoUG: str, numero: str, pagina: int):
        """
        Consulta os participantes de uma licitação
        Parameters
        ----------
        codigoModalidade: str
        Código da Modalidade da Licitação

        codigoUG: str
        Código da Unidade Gestora

        numero: str
        Número da Licitação (NNNNNAAAA)

        pagina: int
        Página consultada

        """
        query_string = self._query_string(locals().copy())
        return self._request(query_string)

    #/api-de-dados/licitacoes/por-ug-modalidade-numero
    def por_ug_modalidade_numero(self, codigoModalidade: str, codigoUG: str, numero: str):
        """
        Consulta uma licitação pelo código da Unidade Gestora, número e modalidade
        Parameters
        ----------
        codigoModalidade: str
        Código da Modalidade da Licitação

        codigoUG: str
        Código da Unidade Gestora

        numero: str
        Número da Licitação (NNNNNAAAA)

        """
        query_string = self._query_string(locals().copy())
        return self._request(query_string)

    #/api-de-dados/licitacoes/ugs
    def ugs(self, pagina: int):
        """
        Consulta as Unidades Gestoras que realizaram licitações
        Parameters
        ----------
        pagina: int
        Página consultada

        """
        query_string = self._query_string(locals().copy())
        return self._request(query_string)

class Peti(Portal):

    #/api-de-dados/peti-por-cpf-ou-nis
    def peti_por_cpf_ou_nis(self, codigo: str, pagina: int):
        """
        Consulta os registros Programa de Erradicação do Trabalho Infantil por CPF/NIS
        Parameters
        ----------
        codigo: str
        CPF/NIS

        pagina: int
        Página consultada

        """
        query_string = self._query_string(locals().copy())
        return self._request(query_string)

    #/api-de-dados/peti-por-municipio
    def peti_por_municipio(self, codigoIbge: str, mesAno: int, pagina: int):
        """
        Consulta os registros Programa de Erradicação do Trabalho Infantil
        Parameters
        ----------
        codigoIbge: str
        Código IBGE

        mesAno: int
        Mês e Ano de referência (AAAAMM)

        pagina: int
        Página consultada

        """
        query_string = self._query_string(locals().copy())
        return self._request(query_string)

class SeguroDefeso(Portal):

    #/api-de-dados/seguro-defeso-codigo
    def seguro_defeso_codigo(self, codigo: str, pagina: int):
        """
        Consulta os registros Seguro Defeso por CPF/NIS
        Parameters
        ----------
        codigo: str
        CPF/NIS

        pagina: int
        Página consultada

        """
        query_string = self._query_string(locals().copy())
        return self._request(query_string)

    #/api-de-dados/seguro-defeso-por-municipio
    def seguro_defeso_por_municipio(self, codigoIbge: str, mesAno: int, pagina: int):
        """
        Consulta os registros Seguro Defeso
        Parameters
        ----------
        codigoIbge: str
        Código IBGE

        mesAno: int
        Mês e Ano de referência (AAAAMM)

        pagina: int
        Página consultada

        """
        query_string = self._query_string(locals().copy())
        return self._request(query_string)

class ServidoresPEF(Portal):

    def __init__(self, token):
        super().__init__(token)
        self.base_url = self.base_url.format(endpoint='servidores/{endpoint}')
    
    #/api-de-dados/servidores
    def todos(self, pagina: int=1, codigoFuncaoCargo: str=None, cpf: str=None, nome: str=None, orgaoServidorExercicio: str=None, orgaoServidorLotacao: str=None, situacaoServidor: int=None, tipoServidor: int=None):
        """
        Consulta todos servidores do Poder Executivo Federal
        Parameters
        ----------
        pagina: int
        Página consultada

        codigoFuncaoCargo: str=None
        Código da Função ou Cargo de Confiança

        cpf: str=None
        CPF do Servidor
        nome: str=None
        Nome do Servidor
        orgaoServidorExercicio: str=None
        Código Órgão Lotação (SIAPE)

        orgaoServidorLotacao: str=None
        Código Órgão Exercício (SIAPE)

        situacaoServidor: int=None
        Situação do Servidor (Ativo=1, Inativo=2 ou Pensionista=3)

        tipoServidor: int=None
        Tipo do Servidor (Civil=1 ou Militar=2)

        """
        query_string = self._query_string(locals().copy())
        endpoint = ''
        return self._request(query_string, endpoint)

    #/api-de-dados/servidores/{id}
    def servidores_id(self, id: int):
        """
        Consulta um servidor do Poder Executivo Federal pelo id
        Parameters
        ----------
        id: int
        ID do registro
        """
        query_string = f'/{id}'
        endpoint = ''
        return self._request(query_string, endpoint)

    #/api-de-dados/servidores/funcoes-e-cargos
    def funcoes_e_cargos(self, pagina: int):
        """
        Código da Função ou Cargo de Confiança
        Parameters
        ----------
        pagina: int
        Página consultada

        """
        query_string = self._query_string(locals().copy())
        return self._request(query_string)

    #/api-de-dados/servidores/por-orgao
    def por_orgao(self, pagina: int=1, licenca: int=None, orgaoExercicio: str=None, orgaoLotacao: str=None, tipoServidor: int=None, tipoVinculo: int=None):
        """
        Consulta de servidores agregados por órgão
        Parameters
        ----------
        pagina: int
        Página consultada

        licenca: int=None
        Licença (Sim: 1; Não: 0)

        orgaoExercicio: str=None
        Código Órgão Lotação (SIAPE)

        orgaoLotacao: str=None
        Código Órgão Exercício (SIAPE)

        tipoServidor: int=None
        Tipo servidor (Civil: 1; Militar: 2)

        tipoVinculo: int=None
        Tipo vínculo (Função: 1; Cargo: 2; Outros: 3; Militares: 4

        """
        query_string = self._query_string(locals().copy())
        return self._request(query_string)

    #/api-de-dados/servidores/remuneracao
    def remuneracao(self, cpf: str, mesAno: int, pagina: int):
        """
        Consulta remunerações de um servidor do Poder Executivo Federal pelo CPF e mês/ano
        Parameters
        ----------
        cpf: str
        CPF do Servidor
        mesAno: int
        Mês e Ano de referência (AAAAMM)

        pagina: int
        Página consultada

        """
        query_string = self._query_string(locals().copy())
        return self._request(query_string)

class Viagens(Portal):

    #/api-de-dados/viagens
    def viagens(self, codigoOrgao: str, dataIdaAte: str, dataIdaDe: str, dataRetornoAte: str, dataRetornoDe: str, pagina: int):
        """
        Consulta viagens por período
        Parameters
        ----------
        codigoOrgao: str
        Código do Órgão (SIAFI)

        dataIdaAte: str
        Data de ida até (DD/MM/AAAA)

        dataIdaDe: str
        Data de ida a partir de (DD/MM/AAAA)

        dataRetornoAte: str
        Data de retorno até (DD/MM/AAAA)

        dataRetornoDe: str
        Data de retorno a partir de (DD/MM/AAAA)

        pagina: int
        Página consultada

        """
        query_string = self._query_string(locals().copy())
        return self._request(query_string)

    #/api-de-dados/viagens-por-cpf
    def viagens_por_cpf(self, cpf: str, pagina: int):
        """
        Consulta viagens por CPF
        Parameters
        ----------
        cpf: str
        CPF
        pagina: int
        Página consultada

        """
        query_string = self._query_string(locals().copy())
        return self._request(query_string)

    #/api-de-dados/viagens/{id}
    def viagens_id(self, id: int):
        """
        Consulta uma viagem pelo ID
        Parameters
        ----------
        id: int
        ID do registro
        """
        query_string = f'/{id}'
        endpoint = 'viagens'
        return self._request(query_string, endpoint)

class Orgaos(Portal):

    #/api-de-dados/orgaos-siafi
    def orgaos_siafi(self, pagina: int=1, codigo: str=None, descricao: str=None):
        """
        Consulta de órgãos cadastrados no Sistema Integrado de Administração Financeira do Governo Federal (SIAFI)
        Parameters
        ----------
        pagina: int
        Página consultada

        codigo: str=None
        Código do Órgão (SIAFI)

        descricao: str=None
        Descrição do Órgão (SIAFI)

        """
        query_string = self._query_string(locals().copy())
        return self._request(query_string)

    #/api-de-dados/orgaos-siape
    def orgaos_siape(self, pagina: int=1, codigo: str=None, descricao: str=None):
        """
        Consulta de órgãos cadastrados no Sistema Integrado de Administração de Pessoal (SIAPE)
        Parameters
        ----------
        pagina: int
        Página consultada

        codigo: str=None
        Código do Órgão (SIAPE)

        descricao: str=None
        Descrição do Órgão (SIAPE)

        """
        query_string = self._query_string(locals().copy())
        return self._request(query_string)
