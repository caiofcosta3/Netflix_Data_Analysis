import pandas as pd

df = pd.read_csv(r'C:\01_Projetos\Netflix_data_analysis\Data\netflix_titles.csv')
print("Linhas: ", df.shape[0])
print("Colunas: ", df.shape[1])
print(df.columns.tolist())

duplicados = df["title"].duplicated().sum()
print("Títulos duplicados:", duplicados)

titulos_repetidos = df.loc[df["title"].duplicated(), "title"].unique()
print("Exemplos de títulos repetidos:", titulos_repetidos[:20])

print("tipo da coluna date_added: ",df["date_added"].dtype)

print(df["duration"].head(10))

tem_multiplos_country = df["country"].dropna().str.contains(",", regex=False).any()
print("country tem múltiplos?", tem_multiplos_country)

tem_multiplos_listed_in = df["listed_in"].dropna().str.contains(",", regex=False).any()
print("listed_in tem múltiplos?", tem_multiplos_listed_in)


print(df["date_added"].head(10))