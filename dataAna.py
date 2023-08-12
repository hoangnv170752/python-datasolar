import matplotlib.pyplot as plt

f = open("DataNV.csv", "r", encoding="utf8")
header = f.readline()
data = f.readlines()
f.close()

ten = []
vitri = []
diadiem = []
tuoi = []
ngaybatdau = []

for i in data:
    i = i.split(",")
    ten.append(i[0])
    vitri.append(i[1])
    diadiem.append(i[2])
    tuoi.append(i[3])
    ngaybatdau.append(i[4])

print(ten)

def phanTich():
    for i in range(len(tuoi)):
        tuoi[i] = int(tuoi[i])
    tong = 0
    for i in tuoi:
        tong += i
    trungbinh = tong/len(tuoi)
    nhomtuoi = {"Duoi20":0, "20-40": 0}
    for i in tuoi:
        if i < 20:
            nhomtuoi["Duoi20"] += 1
        if 20 <= i <= 40:
            nhomtuoi["20-40"] += 1
    plt.figure(figsize= (10,5))
    hang = list(nhomtuoi.keys()) 
    caccot = list(nhomtuoi.values())
    ax = plt.gca()
    label = caccot
    bar = plt.bar(hang, caccot)
    for idx,rect in enumerate(bar):
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width()/2., 1.001*height,
                list(label)[idx],
                ha='center', va='bottom')
    plt.title("Bieu do theo nhom tuoi nhan vien")
    plt.ylabel("So luong")
    plt.xlabel("Nhom tuoi")
    plt.show()
# phanTich()
def vietTat(chuoi):
    ketqua = chuoi[0]
    while chuoi.find(" ") != -1:
        vt = chuoi.find(" ")
        ketqua = ketqua + chuoi[vt + 1].upper()
        chuoi = chuoi[0:vt] + chuoi[vt + 1:]
    return ketqua

print(vietTat("Ki su phan mem"))

def phanTichViTri():
    nhomViTri = {}
    for i in vitri:
        i = vietTat(i)
        if i not in nhomViTri: 
            nhomViTri[i] = 0
        nhomViTri[i] += 1
    print(nhomViTri)
    hang = list(nhomViTri.keys()) 
    caccot = list(nhomViTri.values())
    ax = plt.gca()
    label = caccot
    bar = plt.bar(hang, caccot)

    for idx,rect in enumerate(bar):
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width()/2., 1.001*height,
                list(label)[idx],
                ha='center', va='bottom')
    plt.title("Bieu do theo nhom tuoi nhan vien")
    plt.ylabel("So luong")
    plt.xlabel("Nhom tuoi")
    plt.show()
phanTichViTri()