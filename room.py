from time import sleep

def universal_sleep(x):
    return sleep(x)

class Room:
    def starting_room(self):
        print("Gözlerini araladığında, her şey sessiz. Bir soğukluk seni sarıyor.")
        universal_sleep(2.4)
        print("Vücudun ağır, başın zonkluyor, ama hala hayattasın. Burada bir şeyler yanlış.")
        universal_sleep(2.4)
        print("Etrafa bakıyorsun. Taş zemin, soğuk ve kaygan. Adımların yankılanıyor.")
        universal_sleep(2.4)
        print("Zemin, bir tür kemik yığınıyla dolu. Ama bu kemikler, seninkiler gibi değil.")
        universal_sleep(2.4)
        print("Bir anda, etrafındaki alanın sınırları kayboluyor, sanki başka bir dünyaya adım atmış gibisin.")
        universal_sleep(2.4)
        print("Düşüncelerinin dağılmasına izin veremiyorsun. Buradan çıkmak zorundasın.")
        universal_sleep(2.4)
        print("Yavaşça ayağa kalkıyorsun, etrafındaki kemikleri bir kenara bırakıp, ilerlemeye karar veriyorsun.")
        universal_sleep(2.4)
        print("Bilinmeyen bir yol seni bekliyor, ama geriye dönüş yok. Tek yol ileri.")
        universal_sleep(2.4)
        print("Yavaşça adımını atıyorsun. Nereye gittiğini bilmiyorsun, ama ilerlemekten başka çaren yok.")
        universal_sleep(2.4)
    def describe_fountain_room(self):
        print("Soğuk taş duvarların yankı yaptığı, kasvetli bir zindan odasındasın.")
        universal_sleep(2)
        print("Odanın ortasında, solgun mavi ışıklar saçan eski bir taş çeşme duruyor.")
        universal_sleep(2)
        print("Çeşmeden dökülen su, sessizliği delen tek ses kaynağı gibi yankılanıyor.")
        universal_sleep(2)
        print("Zeminde biriken su, karanlıkta parlayan küçük yansımalar yaratıyor.")
        universal_sleep(2)
        print("Odanın büyüklüğü seni hem büyülüyor hem de huzursuz ediyor; sanki bu boşlukta yalnız değilsin.")
        universal_sleep(2)
        print("Nemli hava boğazını yakıyor, ama aynı zamanda çeşmeden yükselen o hafif serinlik bir nebze rahatlatıyor.")
        universal_sleep(2)
        print("İçindeki ses, buranın sırlarla dolu olduğunu fısıldıyor. Adımlarını dikkatli atmalı, gözünü dört açmalısın.")
        universal_sleep(2)

    def describe_statue_room(self):
        print("Taş duvarlarla çevrili bu geniş odada, hava durgun ama yoğun bir enerji hissediliyor.")
        universal_sleep(2)
        print("Odanın ortasında yükselen büyük bir taş heykel, yüzyıllardır burada bekliyormuş gibi duruyor.")
        universal_sleep(2)
        print("Heykelin önünde üç farklı sembol kazınmış taş levha sıralanmış: biri dairesel, biri köşeli, diğeri çatallı bir işaret taşıyor.")
        universal_sleep(2)
        print("Duvarlara asılı meşaleler odayı titrek sarı ışıklarla aydınlatıyor.")
        universal_sleep(2)
        print("Adımlarını dikkatli atarak heykele yaklaştıkça, meşalelerin rengi yavaş yavaş sarıdan maviye dönmeye başlıyor.")
        universal_sleep(2)
        print("Alevler artık neredeyse hayaletimsi bir parıltıyla yanıyor; mavi ışık heykelin yüz hatlarını daha da korkutucu kılıyor.")
        universal_sleep(2)
        print("Sanki oda da seninle birlikte nefes alıyor, seni izliyor.")
        universal_sleep(2)

        # Nesne 1: İksir
        print("İlk taş levhanın önünde, camı kararmış gibi görünen garip bir iksir duruyor.")
        universal_sleep(2)
        print("İksirin içi, sanki sonsuz bir boşluğu barındırıyor gibi; içinde kıpırdayan karanlık, minyatür bir kara delik gibi dönüyor.")
        universal_sleep(2)

        # Nesne 2: Bıçak
        print("İkinci taş levhanın önünde, paslanmamış ve hâlâ keskin görünen eski bir bıçak var.")
        universal_sleep(2)
        print("Bıçağın kabzasında kurumuş kan izleri var ve ucu heykele doğru bakıyor.")
        universal_sleep(2)
        print("Açıkça belli ki bu bıçak, kullanıcısının kendi kanını sunması için burada duruyor.")
        universal_sleep(2)

        # Nesne 3: Kılıç
        print("Üçüncü levhanın önündeyse, biçimi dünyaya ait olmayan bir kılıç yerleştirilmiş.")
        universal_sleep(2)
        print("Bıçağı dalgalı, rengi tanımlanamaz şekilde değişken; eline almak bir yemin vermek gibi hissettiriyor.")
        universal_sleep(2)

        print("Seçimin ne olursa olsun, dönüşü olmayacak gibi hissediyorsun.")
        universal_sleep(2)
        print("\n1 - İksir\t 2 - Hançer\t 3 - Kılıç")

    def statue_room_after_choice(self):
        print("Seçimini yaptıktan sonra, odadaki her şey bir anlığına sessizliğe gömülüyor.")
        universal_sleep(2.2)
        print("Heykelin gözleri kısa bir süre için parlıyor; hangi duyguyu taşıdığı belirsiz.")
        universal_sleep(2.2)
        print("Ardından, taş zemin ağır bir titreşimle sarsılıyor.")
        universal_sleep(2.2)
        print("Heykelin arkasındaki duvar yavaşça yukarı doğru kayıyor ve ardında karanlık bir geçit açılıyor.")
        universal_sleep(2.2)
        print("Meşalelerin mavi alevleri tekrar sarıya dönmeye başlıyor.")
        universal_sleep(2.2)
        print("Oda yeniden ilk haline dönüyor gibi; tanıdık ama yine de huzursuz edici bir sessizlik hâkim.")
        universal_sleep(2.2)
        print("Kapı şimdi açık dikkatli adımlarla odadan ayırılıyorsun...")
        universal_sleep(2.2)

    def last_room(self):
        print("Odanın kapısını açtığında, gözlerin bir anda karanlıkla sarılı bir alanla karşılaşıyor.")
        universal_sleep(2.4)
        print("Işıksız, havasız bir boşluk gibi hissediyorsun ama sonra köşeden hafifçe sızan ışık fark ediyorsun.")
        universal_sleep(2.4)
        print("Yavaşça ilerliyorsun, her adımda bir soğuk rüzgarın seni geçiştirdiğini hissediyorsun.")
        universal_sleep(2.4)
        print("Karşında, duvar boyunca yükselen eski, taş merdivenler beliriyor. Havanın ağırlığı, merdivenin yarattığı belirsizlikle birleşiyor.")
        universal_sleep(2.4)
        print("İçinde bir şeyler kıpırdıyor, ama korku yerine bir merak var. Merdivenleri tırmanmaya karar veriyorsun.")
        universal_sleep(2.4)
        print("Her basamağı ağır adımlarla çıkarken, sırtındaki soğuk teri hissediyorsun. Havanın boğuculuğu, her adımda seni daha da zorlıyor.")
        universal_sleep(2.4)
        print("Ama bir şekilde, ilerlemeye devam ediyorsun. Tüm vücudun uyanmış gibi, her kasın bir sonraki adımı atmaya odaklanmış.")
        universal_sleep(2.4)
        print("Bir zamanlar tanıdık bir yerden çıkıyor gibi, ama henüz ne olduğunu bilmiyorsun. Tek bildiğin, çıkman gerektiği.")
        universal_sleep(2.4)
        print("Bir sonraki basamağa adım attığında, bir şeyler yerinden oynuyor gibi hissediyorsun. Sanki zindan seni yavaşça yutuyor, ama sen buna karşı duruyorsun.")
        universal_sleep(2.4)
        print("Ve bir adım daha atıyorsun, tek bir düşüncen var: yukarı çıkmak.")
        universal_sleep(2.4)
        print("Merdivenin son basamağına vardığında, odanın kapısı aralanıyor. Işık tam yüzüne vuruyor.")
        universal_sleep(2.4)
        print("Birden her şey netleşiyor. Bu zindan, canavarların ve karanlık güçlerin koruduğu bir yer değil.")
        universal_sleep(2.4)
        print("Zindandakiler, aslında seni hatırlatmaya çalışıyordu. Bu zindanı koruyan varlık, aslında senin geçmişin.")
        universal_sleep(2.4)
        print("Gerçek şu ki, sen bir zamanlar bu zindanın içindeki canavardın. Hafızan silindi, ama şimdi her şey yerine oturuyor.")
        universal_sleep(2.4)
        print("Zindanın derinliklerinde uyuyan o karanlık yaratık, aslında sensin.")
        universal_sleep(2.4)
        print("Bir zamanlar, bu zindanı koruyan bir varlık olarak var olmuştun, ama şimdi eski kimliğini hatırlamaya başlıyorsun.")
        universal_sleep(2.4)
        print("Şimdi, ne yapacağına karar vermen gerekiyor. Ama bir şey kesin: Buradaki her şey, seni bekliyordu.")
        universal_sleep(2.4)