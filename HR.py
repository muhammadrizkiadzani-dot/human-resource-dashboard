import pandas as data_hr
from sqlalchemy import create_engine

df = data_hr.read_excel( r"D:\Latihan Data Engineer\Data Set\hr_employee_dataset_5000_48_locations_clean.xlsx")

print("Jumlah data kosong")
print(df.isnull().sum())

print("Data Tabel")
df.info()

print("\n 5 baris pertama")
print(df.head(5))

print("\n Data Statistik")
print(df.describe())

print("\n baris dan kolom")
print(df.shape)

#data kosong di kolom tanggal keluar dengan dikasih tanda
df['termination_date'] = df["termination_date"].fillna('N/A')

#mengisi data kosong didalam alasan keluar 
df['termination_reason'] = df["termination_reason"].fillna('Still Employed')

df['education_level'] = df["education_level"].fillna('Unknown')

#menghitung nilai median job satisfaction
median_satisfaction = df['job_satisfaction'].median()

#mengisi nilai kosong dengan nilai median 
df['job_satisfaction'] = df["job_satisfaction"].fillna(median_satisfaction)

#menghitung nilai tengah kolom work_life_balance
median_wlb = df['work_life_balance'].median()

#mengisi data koosng dengan nilai median
df["work_life_balance"] = df["work_life_balance"].fillna(median_wlb)

#melakukan standarisasi kolom (mengecilkan huruf, ganti spasi dengan _)
df.columns = df.columns.str.lower().str.replace(' ', '_').str.strip()

#membersihkan spasi gaib disemua teks
target_cols = df.select_dtypes(include=['object', 'string']).columns

#isi data kosong dengan 'Unknown'
for col in target_cols:
    df[col] = df[col].astype(str).str.strip()

# Menggunakan target_cols yang sama agar tidak memicu warning lagi
df[target_cols] = df[target_cols].fillna("Unknown")

# Pengecekan ulang apakah data sudah bersih atau belum
print(" jumlah data kosong per kolom")
print(df.isna().sum())

# melihat sisa jumlah data duplikat
print(" jumlah data duplikat")
print(df.duplicated().sum())

#melihat data bersih 5 baris pertama
print(" 5 Baris pertama Bersih")
print(df.head(5))

print("tipe data")
df.info()

df.to_excel(r"D:\Latihan Data Engineer\Data Set\hr_employee_dataset_5000_48_locations_clean_2.xlsx", index=False)
print("data baru berhasil disimpan")

# Save ke database
engine = create_engine(
    "postgresql://postgres:Rizki17%40@localhost:5432/hr_db"
)

df.to_sql(
    "hr",
    engine,
    if_exists="replace",
    index=False
)

print("berhasil dikirim ke warehouse")