import pandas as pd
import matplotlib.pyplot as plt


def ler_dados_arquivo(arquivo):
    df = pd.read_csv(arquivo, parse_dates=['data'])
    return df


def calcular_media_movel(df, dias=5):
    df['media_movel'] = df['ocorrencias'].rolling(window=dias).mean()
    return df


def plotar_grafico(df):
    plt.figure(figsize=(10, 5))
    plt.plot(df['data'], df['ocorrencias'], label='Ocorrências Diárias', marker='o')
    plt.plot(df['data'], df['media_movel'], label='Média Móvel ', linestyle='--', color='orange')

    plt.title('Ocorrências Diárias e Média Móvel ')
    plt.xlabel('Data')
    plt.ylabel('Ocorrências')
    plt.legend()
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


