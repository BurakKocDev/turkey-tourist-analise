import pandas as pd
import warnings
warnings.filterwarnings("ignore")
import seaborn as sb
import matplotlib.pyplot as plt
sb.set(style="white", color_codes=True)


data = pd.read_csv("tourist_numbers_Turkey.csv")
print(data)

print(data.shape)

for _data in data.columns:
    print(_data)

#Verileri tarihe göre yeniden eskiye sırala ve yeni dosyaya yaz.

sorted_data = data.sort_values(by=["Date"], ascending=False)
sorted_data.to_csv('SortedFile_Tourist_Numbers_Turkey.csv', index=False)
sorted_data=pd.read_csv('tourist_numbers_Turkey.csv')
sorted_data.head()

# 1-Veride null deger var mı kontrol ediliyor.

data.isnull().values.any()

#1-Date bilgisi object ten datetime formatina cevrildi

data['Date']=pd.to_datetime(data['Date'])
print(data.dtypes)

# 3 - Veride yer alan ekstra 00 lar temizleniyor

data.iloc[:,1:]=((data.iloc[:,1:])/100).astype('int')

# 4-Baslık satırındaki verilerde bosluklar vardı, indeksle erisimde sorun olmaması icin temizlendi.

#data.columns = data.columns.to_series().apply(lambda x: x.strip())
data.columns = data.columns.str.strip()
data.head()

# Yil ve ay bazında gruplama yapabilmek icin dataframe verisine yil ve ay bilgisi ekleniyor.

from warnings import simplefilter
simplefilter(action="ignore", category=pd.errors.PerformanceWarning)


data['Year'] = pd.DatetimeIndex(data.Date).year
data['Month'] = pd.DatetimeIndex(data.Date).month
print(data)

# Belirli ülkeler için tüm verileri listeleme

belirliUlkelerTumData = data[['Date','ALMANYA','BELCIKA','ESTONYA']]
print(belirliUlkelerTumData)


# En yüksek turist sayısına sahip 14 kayıttan 4-14 arasını getir. İlk 4 kayıt genel toplamı ifade eden kayıtlara ait oldugu icin dahil edilmedi.

enCokTuristIlk10Ulke= data.sum(numeric_only=True).nlargest(14)[4:14]
print(enCokTuristIlk10Ulke)

# enCokTuristIlk10Ulke= data.drop(['Date','Year','Month'],axis=1).sum().sort_values(ascending=False).head(14)[4:14]

"""En
cok
turist
gelen
10
ulke
ve
sayıları
bulunup
yeni
bir
dataFrame
olusturuluyor."""

enCokTuristIlk10Ulke = {
    "Country": ["ALMANYA", "RUSYA", "INGILTERE", "BULGARISTAN", "IRAN", "GURCISTAN", "HOLLANDA", "AMERICA", "UKRAYNA",
                "FRANSA"]
    , "Visitors": [59329922, 51876544, 29183629, 23310568, 21004970, 20137812, 14366875, 13251904, 13161806, 11355850]
}

enCokTuristIlk10Ulke = pd.DataFrame(enCokTuristIlk10Ulke)
print(enCokTuristIlk10Ulke)


#görselleştirme(en çok gelen ilk 10 ülke)

"""plt.figure(figsize = (16,8))
sb.set_palette("pastel")

ax = sb.barplot(x = 'Country', y = 'Visitors',data = enCokTuristIlk10Ulke, hue = 'Country',dodge = False,)
ax.set_xticklabels(ax.get_xticklabels(),rotation = 45)

ax.set_title('Top Ten Country', size = 20)

ax.set_xlabel('Country',size = 15)
ax.set_ylabel('Total Number of Tourist', size = 15)
#plt.legend(ncol=3) #plt.legend(loc='lower right')
plt.show()
#plt.savefig('TopTenCountryPicture.png')"""






# Yillara Gore GenelToplam

plt.figure(figsize=(16, 8))
# There are several predefined styles ('darkgrid', 'whitegrid', 'dark', 'white' and 'ticks')
sb.set_theme(style="darkgrid")

genelToplam = sb.lineplot(x='Year', y='GTOPLAM', data=data, palette='Set2', hue='Month', linewidth=2.5)
genelToplam.set_title('Total Number of Tourists by Years', size=30)
genelToplam.set_xlabel('Year', size=15)
genelToplam.set_ylabel('Tourist Count', size=15)
plt.show()
# General_Trend.legend(loc='upper left',ncol=4) #plt.legend(loc='lower right')





"""# Belirli bir tarihteki tüm verileri listeleme. Bu örnekte 2018,2019

data20181920 = data.loc[(data.Year == 2018) | (data.Year == 2019) | (data.Year == 2020)]

# data20181920
plt.figure(figsize=(10, 6))
# There are several predefined styles ('darkgrid', 'whitegrid', 'dark', 'white' and 'ticks')
sb.set_theme(style="whitegrid", palette="pastel")

GenelToplam_20181920 = sb.lineplot(x='Month', y='GTOPLAM', data=data20181920, palette='Set2', hue='Year')
GenelToplam_20181920.set_title('Total Number of Tourists by Years for 2018 and 2020', size=15)
GenelToplam_20181920.set_xlabel('Month', size=10)
GenelToplam_20181920.set_ylabel('Tourist Count', size=10)
plt.show()"""