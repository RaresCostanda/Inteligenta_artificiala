
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

pd.set_option('display.max_columns', None)

df = pd.read_csv("C:\Data\Lab_inteligenta_artificiala\data (1).csv")
print("--- Intregul set de date ---")
print(df)

print("\n--- Primii 10 jucatori peste 40 de ani ---")
print(df[df['Age'] > 40].head(10))

print("\n--- Jucatori cu Overall >= 85 si Age < 25 ---")
print(df[(df['Overall'] >= 85) & (df['Age'] < 25)])

print("\n--- Jucatori sortati dupa Skill Moves (descrescator) ---")
print(df.sort_values(by='Skill Moves', ascending=False))

print("\n--- Jucatori cu contract pana in 2021 ---")
print(df[df['Contract Valid Until'] == '2021'])

randuri, coloane = df.shape
print(f"\nSetul de date are {randuri} randuri si {coloane} coloane.")

jucatori_unici = df['Name'].nunique()
print(f"Avem {jucatori_unici} jucatori unici.")

top_5_nationalitati = df['Nationality'].value_counts().head(5)
print("\n--- Top 5 nationalitati ---")
print(top_5_nationalitati)
print(f"Cea mai frecventa nationalitate este: {top_5_nationalitati.index[0]}")

plt.figure(figsize=(8, 8))
top_5_nationalitati.plot.pie(autopct='%1.1f%%', startangle=90, cmap='Pastel1')
plt.title('Top 5 Nationalitati')
plt.ylabel('')
plt.show()

print("\n--- Media SprintSpeed si Acceleration pe nationalitate ---")
print(df.groupby("Nationality")[['SprintSpeed', 'Acceleration']].mean())

df['Position'] = df['Position'].fillna("Unknown")

medie_cluburi = df.groupby('Club')['Overall'].mean()
club_top = medie_cluburi.idxmax()
valoare_top = medie_cluburi.max()
print(f"\nClubul cu cea mai mare medie Overall este {club_top} ({valoare_top:.2f}).")

def parse_currency(value_str):
    if pd.isna(value_str):
        return 0.0
    value_str = str(value_str).replace('€', '')
    if 'M' in value_str:
        return float(value_str.replace('M', '')) * 1000000
    elif 'K' in value_str:
        return float(value_str.replace('K', '')) * 1000
    else:
        return float(value_str)

df['Value'] = df['Value'].apply(parse_currency)
df['Wage'] = df['Wage'].apply(parse_currency)

jucatori_valoare_mare = len(df[df['Value'] > df['Wage']])
print(f"\n{jucatori_valoare_mare} jucatori au valoarea de transfer mai mare decat salariul.")

df['is_underpaid'] = df['Wage'] < (df['Value'] / 100)

df['Scor'] = 0.3 * df['Overall'] + 0.3 * df['Potential'] + 0.2 * df['SprintSpeed']

df_afacere = df[['Name', 'Wage', 'Value']].copy()
df_afacere['difference'] = df_afacere['Value'] - df_afacere['Wage']
df_afacere = df_afacere.sort_values(by='difference', ascending=False)
print("\n--- Top Afaceri Bune ---")
print(df_afacere.head(15))

plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='Value', y='Wage', alpha=0.6, color='blue')
plt.title('Relatia dintre Valoarea jucatorului si Salariu')
plt.xlabel('Valoare')
plt.ylabel('Salariu')
plt.ticklabel_format(style='plain', axis='both')
plt.grid(True)
plt.show()