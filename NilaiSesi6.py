def determine_grade(score):
    if score < 0 or score > 100:
        print("Masukkan nilai antara 0 hingga 100")
    elif score >= 90:
        print("Nilai huruf: A, Predikat: Dengan Pujian")
    elif score >= 80:
        print("Nilai huruf: B, Predikat: Sangat Memuaskan")
    elif score >= 70:
        print("Nilai huruf: C, Predikat: Memuaskan")
    elif score >= 60:
        print("Nilai huruf: D, Predikat: Tidak Memuaskan")
    else:
        print("Nilai huruf: E, Predikat: Tidak Lulus")

try:
    nilai = int(input("Masukkan nilai: "))
    determine_grade(nilai)
except ValueError:
    print("Masukkan harus berupa angka")
