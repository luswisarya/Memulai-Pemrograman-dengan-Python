batas_diskon = 500000
persentase_diskon = 10  # 10%
if dico > batas_diskon:
    diskon = (persentase_diskon / 100) * dico
else:
    diskon = 0

total_harga = dico - diskon
print(total_harga)
