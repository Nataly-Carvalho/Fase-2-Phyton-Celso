import dadosTemporais

arquivo = 'dados_temporais/dados_temporais.csv'
df = dadosTemporais.ler_dados_arquivo(arquivo)
df = dadosTemporais.calcular_media_movel(df)
dadosTemporais.plotar_grafico(df)
