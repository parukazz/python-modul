# Mad libs

# cerita dengan beberapa kata yang hilang
# isi kata berikut sesuai dengan jenisnya

"""
 First Story
"""

kata_sifat = input("Kata Sifat: ")
tempat_bumi = input("Nama Tempat di Bumi: ")
superhero = input("Nama Superhero: ")
superpowers = input("Kekuatan Super: ")
villain = input("Nama Villain: ")
important_stuff = input("Benda Penting: ")
kata_kerja = input("Kata Kerja: ")

title = f"Petualangan {kata_sifat} di {tempat_bumi}"

paragraf1 = f"Pada suatu hari yang {kata_sifat}, para Avengers sedang bersantai di markas mereka di {tempat_bumi}. Tiba-tiba, {superhero} menerima panggilan darurat dari Nick Fury. Ternyata, {villain} telah mencuri {important_stuff} dan berencana menggunakannya untuk {kata_kerja} dunia!"

paragraf2 = f"Para Avengers segera bersiap untuk menghadapi ancaman ini. {superhero} memimpin tim dengan keberaniannya yang {kata_sifat}, sementara {superhero} menggunakan {superpowers} untuk melawan musuh. Pertarungan berlangsung sengit, dengan ledakan {kata_sifat} dan aksi {kata_sifat} yang memukau."

paragraf3 = f"Akhirnya, dengan kerjasam tim yang {kata_sifat}, para Avengers berhasil mengalahkan {villain} dan merebut kembali {important_stuff}. Dunia pun terselamatkan, dan para Avengers kembali ke markas mereka dengan perasaan {kata_sifat}."

print(title)
print(paragraf1)
print(paragraf2)
print(paragraf3)