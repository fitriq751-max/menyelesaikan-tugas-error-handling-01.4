class Vehicle:
    def __init__(self, brand, model):
        # Penanganan Error 1: Validasi data kosong
        if not brand or not model:
            raise ValueError("Brand dan Model tidak boleh kosong!")
        self.brand = brand
        self.model = model

    def drive(self):
        print(f"The {self.brand} {self.model} is driving.")

class Car(Vehicle):
    def __init__(self, brand, model, doors):
        super().__init__(brand, model)
        # Penanganan Error 2: Validasi jumlah pintu
        if doors <= 0:
            print("Peringatan: Jumlah pintu harus lebih dari 0. Diset ke default 4.")
            self.doors = 4
        else:
            self.doors = doors

    def honk(self):
        print("Beep! Beep!")

class Truck(Vehicle):
    def __init__(self, brand, model, load_capacity):
        super().__init__(brand, model)
        self.load_capacity = load_capacity

    def load(self, weight):
        # Penanganan Error 4: Cek tipe data menggunakan try-except
        try:
            weight = float(weight)
            # Penanganan Error 3: Cek kapasitas (Overload)
            if weight > self.load_capacity:
                print(f"ERROR: Muatan ({weight}kg) MELEBIHI kapasitas ({self.load_capacity}kg)!")
            elif weight < 0:
                print("ERROR: Berat muatan tidak bisa negatif!")
            else:
                print(f"Berhasil memuat {weight} kg ke dalam truk.")
        except ValueError:
            print(f"ERROR: '{weight}' bukan angka! Masukkan berat dalam angka.")

def main():
    print("Pengujian Sistem Kendaraan")
    
    # 1. Tes Mobil
    my_car = Car("Toyota", "Corolla", 4)
    my_car.drive()
    my_car.honk()

    # 2. Tes Truk Interaktif
    print("Pengujian Truk Interaktif")
    my_truck = Truck("Ford", "F-150", 1000)
    my_truck.drive()
    
    print("Silakan masukkan angka untuk menguji Error Handling:")
    berat_input = input("Masukkan berat muatan yang ingin dimuat ke truk (kg): ") 
    
    # Memproses input melalui metode load
    my_truck.load(berat_input)

if __name__ == "__main__":
    main()
