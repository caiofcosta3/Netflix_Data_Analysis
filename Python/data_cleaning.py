import pandas as pd

df = pd.read_csv(r"C:\01_Projetos\Netflix_data_analysis\Data\netflix_titles.csv")
processed = df.copy(deep=True)

print("Shape inicial:", processed.shape)

# tratar nulos

print("\nNulos por coluna:")
print(processed.isna().sum().sort_values(ascending=False))

# remover apenas colunas essenciais
colunas_essenciais = ["title", "type", "date_added", "duration"]
processed = processed.dropna(subset=colunas_essenciais)

# tratar duplicados

processed = processed.drop_duplicates()
processed = processed.drop_duplicates(subset=["title", "type"], keep="first")

# tratar date_added

processed["date_added_clean"] = (
    processed["date_added"]
    .astype("string")
    .str.replace("\u00a0", " ", regex=False)
    .str.strip()
    .str.replace(r"\s+", " ", regex=True)
)

processed["date_added"] = pd.to_datetime(
    processed["date_added_clean"],
    errors="coerce"
)


# criar colunas derivadas
processed["year_added"] = processed["date_added"].dt.year
processed["month_added"] = processed["date_added"].dt.month
processed["month_name"] = processed["date_added"].dt.month_name()
processed["year_month"] = processed["date_added"].dt.to_period("M").astype(str)

print("\nTipos após conversão:")

print(processed["year_added"].head(5), processed["month_added"].head(5), processed["month_name"].head(5), processed["year_month"].head(5))



print("Shape final:", processed.shape)
# Para salvar base processada
# processed.to_csv(r'C:\01_Projetos\Netflix_data_analysis\Data\netflix_titles_processed.csv', index=False)