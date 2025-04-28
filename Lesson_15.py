# 1
language = {
    'Swift':'iOS',
    'Java': "Android",
    'HTML':"Web",
    'CSS':"Web",
    'Python':'Backend'}

for key, value in sorted(language.items()):
    print(f"{key.title()} - {value}")

print("********************************************")   
# 2       
davlatlar = {
    "o'zbekiston":'toshkent',
    'aqsh':'washington d.c.',
    'rossiya':'moskva',
    'tojikiston':'dushanbe',
    "qirg'iziston":'bishkek',
    'qozog\'iston':'nursulton',
    'malayziya':'kuala-lumpur',
    'singapur':'sungapur',
    'italiya':'rim'}

print('Dunyo davlatlari:')
for davlat in sorted(davlatlar):
    print(davlat.upper())

print('\nDavlatlarning poytaxtlari')
for poytaxt in sorted(davlatlar.values()):
    print(poytaxt.title())
    
print("********************************************") 