from datetime import date
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
import pypyodbc
from django.utils.text import slugify


data = {   
    "sliders": [
        {
            "slider_image": "slider1.png",
            "url": "film-adi-1"
        },
         {
            "slider_image": "slider2.png",
            "url": "film-adi-2"
        },
         {
            "slider_image": "slider3.png",
            "url": "film-adi-3"
        }
    ]
}
data1 = {   
    1: "1.png",
    2: "2.png"  
}
conn=pypyodbc.connect(
    'Driver={SQL Server};'
    'Server=DESKTOP-HC3S402\SQLEXPRESS;'
    'Database=Scooter'
)
cursor = conn.cursor()







def scooter_bilgi():
    
    query = """
    SELECT s.ScooterID, m.Marka, mo.Model
    FROM Scooter s
    JOIN Marka m ON s.MarkaID = m.MarkaID
    JOIN Model mo ON s.ModelID = mo.ModelID
    ORDER BY s.ScooterID
    """

    cursor = conn.cursor()
    cursor.execute(query)

     # Verileri 'scooter' isimli sözlükte toplama
    scooterbilgi = {}
    for row in cursor:
        scooter_id = row[0]  # ScooterID sütununun indeksi
        marka = row[1]       # Marka sütununun indeksi
        model = row[2]       # Model sütununun indeksi

    slug = slugify(f"{scooter_id}")
    
    resim_url = 'img/' + str(scooter_id) + '.png'

    if scooter_id not in scooterbilgi:
        scooterbilgi[scooter_id] = {'Marka': marka, 'Model': model, 'Slug':slug, 'Resim': resim_url}
    

    return scooterbilgi

def scooter_detay():
    
    query = """
    SELECT s.ScooterID,
       g.MotorGucumax, g.Menzilmax, g.Hizmax, g.TasimaKapasitesi, tt.TekerlekTipi, g.TekerlekSayisi, g.LastikEbati, g.Katlanabilme,
       ft.FrenTeknolojisi, o.Onfren, af.ArkaFren, t.BataryaVoltaji, t.BataryaAkimi, t.TirmanmaAcisi, kst.KorumaSertifikasyonu, r.Renk, t.Agirlik
    FROM Scooter s
    JOIN GenelOzellik g ON s.ScooterID = g.ScooterID
    JOIN TeknikOzellik t ON s.ScooterID = t.ScooterID
    JOIN TekerlekTipi tt ON g.TekerlekTipiID = tt.TekerlekTipiID
    JOIN FrenTeknolojisi ft ON t.FrenTeknolojisiID = ft.FrenTeknolojisiID
    JOIN OnFren o ON t.ÖnFrenID = o.OnfrenID
    JOIN ArkaFren af ON t.ArkaFrenID = af.ArkaFrenID
    JOIN KorumaSertifikasyonu kst ON t.KorumaSertifikasyonuID = kst.KorumaSertifikasyonuID
    JOIN Renk r ON t.RenkID = r.RenkID
    """

    cursor = conn.cursor()
    cursor.execute(query)

     # Verileri 'scooter' isimli sözlükte toplama
    scooterdetay = {}
    for row in cursor:
        scooter_id = row[0]
        scooterdetay[scooter_id] = {
            'Ozellikler': {
                'MotorGucumax': row[1],
                'Menzilmax': row[2],
                'Hizmax': row[3],
                'TasimaKapasitesi': row[4],
                'TekerlekID': row[5],
                'TekerlekSayisi': row[6],
                'LastikEbati': row[7],
                'Katlanabilme': row[8],
                'FrenTeknolojisiID': row[9],
                'ÖnFrenID': row[10],
                'ArkaFrenID': row[11],
                'BataryaVoltaji': row[12],
                'BataryaAkimi': row[13],
                'TirmanmaAcisi': row[14],
                'KorumaSertifikasyonuID': row[15],
                'RenkID': row[16],
                'Agirlik': row[17]
            }
        }
    return scooterdetay

def scooter_fiyat():
    
    query = """
    SELECT fl.ScooterID, f.Fiyat, s.Site, f.FiyatLink
    FROM Fiyatlar fl
    JOIN Fiyat f ON fl.FiyatlarID = f.FiyatlarID
    JOIN Site s ON f.SiteID = s.SiteID
    ORDER BY fl.ScooterID
    """

    cursor = conn.cursor()
    cursor.execute(query)

    scooterfiyat = {}
    for row in cursor:
        scooter_id = row[0]
        fiyat_bilgisi = {
            'Fiyat': row[1],
            'Site': row[2],
            'FiyatLink': row[3]
        }

        if scooter_id not in scooterfiyat:
            scooterfiyat[scooter_id] = []
        scooterfiyat[scooter_id].append(fiyat_bilgisi)
    return scooterfiyat

def scooter_renk():
    
    query = """
    SELECT RenkID, Renk FROM Renk
    """
    cursor = conn.cursor()
    cursor.execute(query)
    colors = cursor.fetchall()

    return colors

def scooter_marka():
    
    query = """
    SELECT MarkaID, Marka FROM Marka
    """
    cursor = conn.cursor()
    cursor.execute(query)
    colors = cursor.fetchall()

    return colors

def scooter_sertifikasyon():
    
    query = """
    SELECT KorumaSertifikasyonuID, KorumaSertifikasyonu FROM KorumaSertifikasyonu
    """
    cursor = conn.cursor()
    cursor.execute(query)
    colors = cursor.fetchall()

    return colors

def scooter_tekerlek():
    
    query = """
    SELECT TekerlekTipiID, TekerlekTipi FROM TekerlekTipi
    """
    cursor = conn.cursor()
    cursor.execute(query)
    colors = cursor.fetchall()

    return colors

def scooter_onfren():

    
    query = """
    SELECT OnFrenID, OnFren FROM OnFren
    """
    cursor = conn.cursor()
    cursor.execute(query)
    colors = cursor.fetchall()

    return colors

def scooter_arkafren():

    
    query = """
    SELECT ArkaFrenID, ArkaFren FROM ArkaFren
    """
    cursor = conn.cursor()
    cursor.execute(query)
    colors = cursor.fetchall()

    return colors

def scooter_fren():

    
    query = """
    SELECT FrenTeknolojisiID, FrenTeknolojisi FROM FrenTeknolojisi
    """
    cursor = conn.cursor()
    cursor.execute(query)
    colors = cursor.fetchall()

    return colors

def scooter_site(): 
    query = """
    SELECT SiteID, Site FROM Site
    """
    cursor = conn.cursor()
    cursor.execute(query)
    colors = cursor.fetchall()

    return colors

def scooter_sil(scooter_id):
    try:
        # İlişkili tablolardaki verileri silin
        cursor.execute("DELETE FROM Fiyatlar WHERE ScooterID = ?", scooter_id)
        cursor.execute("DELETE FROM TeknikOzellik WHERE ScooterID = ?", scooter_id)
        cursor.execute("DELETE FROM GenelOzellik WHERE ScooterID = ?", scooter_id)

        # Ana Scooter tablosundan kaydı silin
        cursor.execute("DELETE FROM Scooter WHERE ScooterID = ?", scooter_id)

        conn.commit()
    except Exception as e:
        print("Bir hata oluştu: ", e)
        conn.rollback()  # Hata durumunda yapılan işlemleri geri al

def scooter_maxfiyat(scooter_id):
    try:
        # En yüksek fiyatı bulma sorgusu
        cursor.execute("""
            SELECT MAX(Fiyat)
            FROM Fiyatlar
            INNER JOIN Fiyat ON Fiyatlar.FiyatlarID = Fiyat.FiyatlarID
            WHERE Fiyatlar.ScooterID = ?
        """, scooter_id)

        highest_price = cursor.fetchone()[0]
        return highest_price
    except Exception as e:
        print("Bir hata oluştu: ", e)
        return None

def scooter_fiyatguncelle(scooter_id, new_price):
    try:
        # İlgili FiyatlarID'leri bul
        cursor.execute("""
            SELECT FiyatlarID
            FROM Fiyatlar
            WHERE ScooterID = ?
        """, scooter_id)
        fiyatlar_ids = cursor.fetchall()

        # Her bir FiyatlarID için Fiyat tablosunu güncelle
        for fiyatlar_id in fiyatlar_ids:
            cursor.execute("""
                UPDATE Fiyat
                SET Fiyat = ?
                WHERE FiyatlarID = ?
            """, (new_price, fiyatlar_id[0]))

        conn.commit()
    except Exception as e:
        print("Bir hata oluştu: ", e)
        conn.rollback()



def index(request):
    scooter_adı = scooter_bilgi()
    sliders = data["sliders"]
    resimler=data1
    
    return render(request, 'index.html', {
        "scooter": scooter_adı,
        "sliders": sliders,
        "resimler":resimler,
    
    })

def scooter(request):
    scooteradı = scooter_bilgi()
    return render(request, 'scooter.html', {
        "scooter": scooteradı
    })

def scooter_details(request, slug):
    scooterlar = scooter_bilgi()
    scooterfiyatlar=scooter_fiyat()
    scooterozellik=scooter_detay()
    
    # Eşleşen scooter_id'yi bulma
    scooter_id = next((id for id, detaylar in scooterlar.items() if detaylar['Slug'] == slug), None)

    if scooter_id is not None:
        
        scooteradı = scooterlar[scooter_id]['Marka']+scooterlar[scooter_id]['Model']
        scooterresim = scooterlar[scooter_id]['Resim']
        scooterozellik = scooterozellik[scooter_id]
        scooterfiyat = scooterfiyatlar[scooter_id]


        # scooterfiyat ve diğer detayları da burada ekleyebilirsiniz

        return render(request, 'scooter-details.html', {
            "Scooter": scooteradı,
            "Resim": scooterresim,
            "Fiyatlar":scooterfiyat,
            "Ozellik":scooterozellik,
            
            # Diğer context bilgileri
        })
    else:
        # Eğer scooter bulunamazsa hata mesajı gösterilebilir veya başka bir sayfaya yönlendirme yapılabilir
        return HttpResponse("Scooter bulunamadı")

def form(request):
    renk = scooter_renk()
    marka = scooter_marka()
    sertifikasyon=scooter_sertifikasyon()
    tekerlek=scooter_tekerlek()
    onfren=scooter_onfren()
    arkafren=scooter_arkafren()
    fren=scooter_fren()
    site=scooter_site()


    if request.method == 'POST':
        # Formdan gelen verileri al
        marka_id = request.POST.get('marka')  # 'marka' formdaki input/select ismi
        model_id = request.POST.get('model')  # 'model' formdaki input/select ismi
        motor_gucu_max = request.POST.get('motor_gucu_max')
        menzil_max = request.POST.get('menzil_max')
        hiz_max = request.POST.get('hiz_max')
        tasima_kapasitesi = request.POST.get('tasima_kapasitesi')
        tekerlek_id = request.POST.get('tekerlek')
        tekerlek_sayisi = request.POST.get('tekerlek_sayisi')
        lastik_ebati = request.POST.get('lastik_ebati')
        katlanabilme = request.POST.get('katlanabilme')
        fren_teknolojisi_id = request.POST.get('fren_teknolojisi')
        on_fren_id = request.POST.get('on_fren')
        arka_fren_id = request.POST.get('arka_fren')
        batarya_voltaji = request.POST.get('batarya_voltaji')
        batarya_akimi = request.POST.get('batarya_akimi')
        tirmanma_acisi = request.POST.get('tirmanma_acisi')
        koruma_sertifikasyonu_id = request.POST.get('koruma_sertifikasyonu')
        renk_id = request.POST.get('renk')
        agirlik = request.POST.get('agirlik')

        print(renk)
        
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO Scooter (MarkaID, ModelID) 
            VALUES (?, ?)
        """, (marka_id, model_id))
        conn.commit()

        # Son eklenen ScooterID'yi almak
        cursor.execute("SELECT SCOPE_IDENTITY()")
        scooter_id = cursor.fetchone()[0]

        # GenelOzellik tablosuna veri ekleme
        cursor.execute("""
            INSERT INTO GenelOzellik (ScooterID, MotorGucumax, Menzilmax, Hizmax, TasimaKapasitesi, TekerlekID, TekerlekSayisi, LastikEbati, Katlanabilme) 
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (scooter_id, motor_gucu_max, menzil_max, hiz_max, tasima_kapasitesi, tekerlek_id, tekerlek_sayisi, lastik_ebati, katlanabilme))
        conn.commit()

        # TeknikOzellik tablosuna veri ekleme
        cursor.execute("""
            INSERT INTO TeknikOzellik (ScooterID, FrenTeknolojisiID, ÖnFrenID, ArkaFrenID, BataryaVoltaji, BataryaAkimi, TirmanmaAcisi, KorumaSertifikasyonuID, RenkID, Agirlik) 
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (scooter_id, fren_teknolojisi_id, on_fren_id, arka_fren_id, batarya_voltaji, batarya_akimi, tirmanma_acisi, koruma_sertifikasyonu_id, renk_id, agirlik))
        conn.commit()

        
        return redirect('/scooter')
        

    return render(request, 'form.html', {
        'Renk': renk,
        'Marka':  marka,
        'Sertifikasyon': sertifikasyon,
        'Tekerlek': tekerlek,
        'Arkafren': arkafren,
        'Onfren': onfren,
        'Fren': fren,
        'Site': site,

        })

 