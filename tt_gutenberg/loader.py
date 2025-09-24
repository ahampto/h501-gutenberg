import pandas as pd

def load_lang_alias():
    df_auth = pd.read_csv('https://raw.githubusercontent.com/rfordatascience/tidytuesday/main/data/2025/2025-06-03/gutenberg_authors.csv')
    df_lang = pd.read_csv("https://raw.githubusercontent.com/rfordatascience/tidytuesday/main/data/2025/2025-06-03/gutenberg_languages.csv")
    df_meta = pd.read_csv("https://raw.githubusercontent.com/rfordatascience/tidytuesday/main/data/2025/2025-06-03/gutenberg_metadata.csv")
    df = pd.merge(df_meta, df_lang, on=["gutenberg_id"], how='inner')
    df = df.dropna()
    df = pd.merge(df, df_auth, on=["gutenberg_author_id"], how='inner')
    df = df.drop_duplicates()
    df2 = df.groupby(['total_languages','author_x']).size().sort_values(ascending=False).reset_index(name='count of translations')
    return df2['author_x'].tolist()

def load_just_lang():
    df_auth = pd.read_csv('https://raw.githubusercontent.com/rfordatascience/tidytuesday/main/data/2025/2025-06-03/gutenberg_authors.csv')
    df_lang = pd.read_csv("https://raw.githubusercontent.com/rfordatascience/tidytuesday/main/data/2025/2025-06-03/gutenberg_languages.csv")
    df_meta = pd.read_csv("https://raw.githubusercontent.com/rfordatascience/tidytuesday/main/data/2025/2025-06-03/gutenberg_metadata.csv")
    df = pd.merge(df_meta, df_lang, on=["gutenberg_id"], how='inner')
    df = df.dropna()
    df = pd.merge(df, df_auth, on=["gutenberg_author_id"], how='inner')
    df = df.drop_duplicates()
    df2 = df.groupby(['total_languages','author_x']).size().sort_values(ascending=False).reset_index(name='count of translations')  

    return list(zip(df2['author_x'], df2['count of translations']))
    

def just_alias():
    df_auth = pd.read_csv('https://raw.githubusercontent.com/rfordatascience/tidytuesday/main/data/2025/2025-06-03/gutenberg_authors.csv')
    df_lang = pd.read_csv("https://raw.githubusercontent.com/rfordatascience/tidytuesday/main/data/2025/2025-06-03/gutenberg_languages.csv")
    df_meta = pd.read_csv("https://raw.githubusercontent.com/rfordatascience/tidytuesday/main/data/2025/2025-06-03/gutenberg_metadata.csv")
    df = pd.merge(df_meta, df_lang, on=["gutenberg_id"], how='inner')
    df = df.dropna()
    df = pd.merge(df, df_auth, on=["gutenberg_author_id"], how='inner')
    df = df.drop_duplicates()
    df1 = df[['title','author_x']].value_counts().reset_index(name='count of title')
    return df1['author_x'].unique().tolist()


def no_lang_alias():
    df_auth = pd.read_csv('https://raw.githubusercontent.com/rfordatascience/tidytuesday/main/data/2025/2025-06-03/gutenberg_authors.csv')
    df_lang = pd.read_csv("https://raw.githubusercontent.com/rfordatascience/tidytuesday/main/data/2025/2025-06-03/gutenberg_languages.csv")
    df_meta = pd.read_csv("https://raw.githubusercontent.com/rfordatascience/tidytuesday/main/data/2025/2025-06-03/gutenberg_metadata.csv")
    df = pd.merge(df_meta, df_lang, on=["gutenberg_id"], how='inner')
    df = df.dropna()
    df = pd.merge(df, df_auth, on=["gutenberg_author_id"], how='inner')
    df = df.drop_duplicates()
    df1 = df[['title','author_x']].value_counts().reset_index(name='count of title')
    return list(zip(df1['author_x'], df1['count of title']))