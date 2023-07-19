import pickle

def check_progress():
    saved_progress = load_game()

    if saved_progress:
        print("Kaydedilen ilerleme bulundu.")
        print("Karakter Adı:", saved_progress['character_name'])
        print("Karakter Cinsiyeti:", saved_progress['character_gender'])
        print("Karakter Sınıfı:", saved_progress['character_class'])
        print("Level:", saved_progress['level'])


    else:
        print("Kaydedilen ilerleme bulunamadı.")



def start_new_game():
    character_name = input("Karakter Adınızı Giriniz.: ")
    character_gender = input("Karakter Cinsiyetini Seçiniz. (Erkek/Kadın): ")
    character_class = input("Karakterinizin Sınıfını Seçiniz. (Suikastçi/Büyücü/Savaşçı/Ölü Dirilten):")
    character_level = 1


    progress = {
        'level': character_level ,
        'character_gender': character_gender ,
        'character_name': character_name ,
        'character_class': character_class ,


    }
    return progress






def save_game(progress):
    with open("savefile.pickle", "wb") as file:
        pickle.dump(progress, file)


def load_game():
    try:
        with open("savefile.pickle", "rb") as file:
            progress = pickle.load(file)
            return progress
    except FileNotFoundError:
        return None


def main_game_loop():
    print("Cehenneme hoş geldin. \nCehenneme hoş geldin. \nCehenneme hoş geldin. \nCehenneme hoş geldin. \nCehenneme hoş geldin. \nCehenneme hoş geldin. ")
    print("\n")
    print("Kendine geldiğinde bu ses kafanda yankılanıyordu.")
    print("\n")
    print("Yoğun bir baş ağrısı ve açlıktan kazınan bir mideyle gözlerini açtın. ")
    print("\n")
    print("Etrafına bakındığında yıkık dökük bir evin içinde bulunan bir eski bir yatağın içindeydin. ")
    print("\n")
    print("Tek hatırladığın gece bir oyun oynadığındı.")
    print("\n")


    character_level = 1

    saved_progress = load_game()

    if saved_progress:

        print("Bir önceki oyununuz bulundu!")
        choice = input("Kaydedilen oyununuzu devam ettirmek ister misiniz? (E/H): ")

        if choice.upper() == "E":

            progress = saved_progress
            print("Kaydedilen ilerleme yüklendi.")
        else:

            progress = start_new_game()
            print("Yeni bir oyun başladı.")
    else:


        print("Yeni bir oyun başladı.")

    # Ana oyun döngüsünü başlatın
    while True:

        if character_level == 1:

            print("\n")
            print("Seçeneklerin şunlar:")
            print("\n")
            print("1) Elini yüzünü yıka.")
            print("\n")
            print("2) Kahvaltı yap.")
            print("\n")
            print("3) Dışarıya Çık.")
            print("\n")
            print("4) Evin içerisini incele.")
            print("\n")
            print("5) Uyumaya Devam et.")
            print("\n")
            seçenek1 = input("Ne yapmak İstiyorsun (1/2/3/4/5): ")
            if seçenek1=="1":
                print("Elini yüzünü buz gibi suda yıkadın ve biraz su içtin.")
                print("\n")
                print("Soğuk suyun etkisiyle kendine geldin ferahlamış hissediyorsun.")
                print("\n")
                print("Şimdi ne yapmak istersin.")
                print("\n")
                print("1) Kahvaltı yap. \n2) Dışarıya Çık. \n3) Evin içerisini incele.")
                seçenek1_1 = input("(1/2/3): ")
                if seçenek1_1=="1":
                    print("Dolabı açtın ve dolabın bomboş olduğunu farkettin.")
                    print("\nUyarı: Uzun süreli açlık ve susuzluk karakterinizin ölümüne yol açabilir.")
                    print("\nCan: Sağlıklı(10/10) - Açlık: Açlıktan midesi kazınıyor(2/10) - Su ihtiyacı: Susamamış(10/10) ")
                    print("\n10/10 seviyeleri gösterir: 10/10 en iyi seviye, 0/10 en düşük seviyedir.")
                    print("\nNe yapmak istersin:")
                    print("\n1) Dışarıya çık ve yiyecek bişeyler ara.")
                    print("\n2) Evin içerisini araştır.")
                    seçenek1_1_2 = input("(1/2): ")
                    if seçenek1_1_2=="1":
                        print("Evin kapısını açıp dışarıya çıktın.")
                        print("\nEtrafına baktığında küçücük bir kasabada olduğunu ve etrafın karla kaplı olduğunu farkettin.")
                        print("\nBir anda üşümeye başladın.")
                        print("\nSıcaklık: Soğuk(3/10).")
                        print("\n5/10 normal - 1/10 aşırı soğuk - 10/10 aşırı sıcağı temsil eder")
                        print("\nAşırı soğuk veya aşırı sıcak havalarda gerekli ekipmanlar olmadan bulunmak karakterinizin ölümüne sebep olabilir.")
                        print("\nKasabaya doğru baktığında bazı dükkanların olduğunu görebiliyorsun.")
                        print("\nNe yapmak istersin:")
                        print("\n1) Gördüğün dükkanlara doğru yürümeye başla.")
                        print("\n2) Eve girip evin içerisini araştır.")
                        seçenek1_1_3 = input("(1/2): ")
                    if seçenek1_1_2=="2":
                        print("Evin içerisini detaylıca araştırdın.")
                        print("\nEnerji: 9/10.")
                        print("\nUyarı: Enerji 0 a düştüğünde bayılırsınız.")
                        print("\nEvin içinde 3 bronz sikke ve yırtıklarla dolu bir kazak buldun.")




            elif seçenek1=="2":
                print("Dolabı açtın ve dolabın bomboş olduğunu farkettin.")
                print("\nUyarı: Uzun süreli açlık ve susuzluk karakterinizin ölümüne yol açabilir.")
                print("\nCan: Sağlıklı(10/10) - Açlık: Açlıktan midesi kazınıyor(2/10) - Su ihtiyacı: Susamış(4/10 ")
                print("\n3/3 seviyeleri gösterir 10/10 en iyi seviye 0/10 en düşük seviyedir.")
                print("\nNe yapmak istersin:")
                print("\n1) Dışarıya çık ve yiyecek bişeyler ara.")
                print("\n2) Evin içerisini araştır.")
                print("\n3) Elini yüzünü yıka.")
                print("\n4) Uyumaya Devam et.")
            else :
                print("Devamı Kodlanmadı.")

        else:
            print("Geçerli bir tercih yapmadınız. Lütfen tekrar deneyin.")
            continue






        choice = input("Bir seçenek girin: ")


        if choice == "q":
            break
        if choice == "c":

            check_progress()
            break



    save_game(progress)


main_game_loop()
