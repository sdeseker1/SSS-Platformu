Üniversite SSS Platformu
1. Proje Hakkında Genel Bilgi
Bu proje, Django web çatısı kullanılarak geliştirilen bir “Üniversite Sıkça Sorulan Sorular (SSS) Platformu”dur. Amacı, üniversite öğrencileri ve adaylarının sık karşılaştıkları sorulara kolay ve hızlı bir şekilde erişmesini sağlamaktır.

2. Kullanılan Teknolojiler
•	Python 3
•	Django 3.2.9
•	SQLite (veritabanı)
•	HTML/CSS (Temel arayüz)
•	Django Templates

3. Projenin Temel Özellikleri
Özellik	Açıklama
Kullanıcı Kayıt:	Kullanıcılar kayıt formu üzerinden hesap oluşturabilir.
Giriş / Çıkış:	Django’nun kimlik doğrulama sistemi ile kullanıcı girişi yapılabilir.
SSS Listeleme:	Mevcut sorular listelenir, arama ve kategoriye göre filtreleme yapılabilir.
Soru Sorma:	Kayıtlı kullanıcılar sistem üzerinden yeni soru talebinde bulunabilir.
Admin Panel:	Yetkili kullanıcılar (personel) gelen soruları görebilir, cevaplayabilir, silebilir.
API Hazırlığı:	API ile veri erişimi planlanabilir şekilde yapı kurulmuştur.
Veritabanı:                    	Proje, dbsql adlı veritabanı kullanılarak yapılandırılmıştır. Django ORM ile tüm veriler bu veritabanında yönetilir ve saklanır.


4. Sistem Mimarisi
Django, MTV (Model-Template-View) mimari desenini kullanır. Bu desen, birçok kişi tarafından MVC (Model-View-Controller) ile karıştırılsa da, Django’ya özgü bazı farklar içerir.
Aşağıda Django’nun MTV mimarisi detaylı şekilde açıklanmıştır:
•	Modeller (models.py)
Veritabanı ile ilgili her şeyi temsil eder.
Veritabanı tablolarını ve onların ilişkilerini tanımlar.
models.py dosyasında yer alır.
Category: Soru kategorilerini tutar.
            Question: Onaylanmış, herkese açık sorular.
            QuestionRequest: Kullanıcıların yönelttiği ve henüz onaylanmamış sorular.
•	Template
Kullanıcıya gösterilecek HTML dosyalarıdır.
Dinamik içerik göstermek için Django Template Language (DTL) kullanılır.
templates/ klasöründe yer alır.
•	Görünümler (views.py)
İş mantığını barındırır.
HTTP isteklerini karşılar ve gerekli işlemleri yaparak uygun templatei döner.
views.py dosyasında yer alır.
            home, register_view, custom_login_view: Giriş ve ana sayfa işlemleri.
            ask_question: Kullanıcıların soru gönderme alanı.
            admin_panel, answer_question, delete_question: Admin yetkili işlemleri.
            sss_view: SSS sayfası, arama ve kategori filtreleme ile birlikte.
•	URL Yönlendirme (urls.py)
           Tüm view fonksiyonları ile bağlantılı yol tanımları.


5. Yazılım Tasarım İlkeleri ile Uyum Analizi
5.1 SRP – Single Responsibility Principle (Tek Sorumluluk İlkesi)
Açıklama: Her sınıf ya da modül yalnızca tek bir sorumluluğa sahip olmalı.
Durum:
•	models.py sadece veritabanı yapısını tanımlar.
•	views.py sadece iş mantığını barındırır.
•	forms.py, urls.py, templates/ gibi yapılar ayrı sorumluluklara sahiptir.
Uygun.
5.2 OCP – Open/Closed Principle (Açık/Kapalı İlkesi)
Açıklama: Kod, genişlemeye açık ama değişikliğe kapalı olmalı.
Durum:
•	Yeni view, model, form veya URL route eklenebilir.
•	Var olan yapılar değiştirilmeden genişletilebilir.
Uygun.
5.3 LSP – Liskov Substitution Principle (Yerine Geçme İlkesi)
Açıklama: Alt sınıflar, üst sınıfların yerine sorunsuzca kullanılabilmelidir.
Durum:
•	UserCreationForm → RegisterForm örneği bu ilkeyi destekliyor.
•	Django'nun sınıfları genişletilmeye uygun.
 Uygun.
5.4 ISP – Interface Segregation Principle (Arayüz Ayrımı İlkesi)
Açıklama: Sınıflar sadece ihtiyaç duyduğu metotları içermeli.
Durum:
•	Django'da view, model ve form yapıları ihtiyaca göre yazılır.
•	Kullanılmayan işlevsellik sisteme yüklenmez.
•	Uygun.
5.5 Cohesion (Bağlılık/Tutarlılık)
Açıklama: İlgili işler bir arada, ilgisiz işler ayrı tutulmalı.
Durum:
•	Django’nun dosya yapısı bu konuda çok net: Her şey ayrı ayrı ve anlamlı klasörlerde.
 Uygun.
 5.6 Coupling (Bağımlılık)
Açıklama: Bir bileşenin diğerine olan bağımlılığı ne kadar azsa o kadar iyidir.
Durum:
•	Django bileşenleri loosely coupled’dır (gevşek bağlı).
•	Ancak ORM ile view arasında doğal bir bağ vardır.
 Kabul edilebilir düzeyde.
5.7 Robustness – Postel’s Law (Sağlamlık İlkesi)
Açıklama: “Girdi konusunda hoşgörülü, çıktı konusunda katı olun.”
Durum:
•	Django form yapıları validasyonlarıyla bu ilkeye uygundur.
•	Geçerli olmayan veriler temizlenmeden kaydedilmez.
 Uygun.
 5.8 Demeter’s Law (Demeter İlkesi)
Açıklama: “Sadece tanıdığın nesnelerle konuş.”
Durum:
•	Django view’ları genelde doğrudan modelle çalışır ve veri katmanlarına fazla karışmaz.
•	Fonksiyonlar birbirleriyle fazla iç içe değildir.
 Uygun.

 6. Kullanıcı Rolleri
          Rol	                                               Yetki
Standart Kullanıcı:	SSS’leri görüntüleyebilir, soru sorabilir.
Yetkili Kullanıcı (Admin)	: Yeni soruları cevaplayabilir, silebilir, onaylayarak yayınlayabilir.

7. Yazılımsal ve Sistemsel Gereksinimler
7.1 Esneklik (Flexibility)
Sistem, yeni özelliklerin eklenmesine ve mevcut yapıların değiştirilmeden genişletilmesine uygun bir şekilde geliştirilmiştir. Örneğin:
•	Yeni kategori eklemek için sadece Category modeline yeni bir kayıt eklemek yeterlidir.
•	Yeni soru tipi veya kullanıcı rolü eklenebilir yapıdadır.
•	Kodlar fonksiyonel ve modüler yazılmış, her bileşen (view, model, form) ayrı çalışmaktadır.
7.2 Güvenlik (Security)
•	Kullanıcı girişi ve kimlik doğrulama, Django’nun yerleşik auth sistemi ile sağlanmaktadır.
•	Sadece yetkili kullanıcılar (admin) yeni soruları onaylayabilir veya silebilir.
•	Django’nun CSRF, XSS ve SQL Injection’a karşı korumaları aktif olarak çalışmaktadır.
•	Form doğrulama işlemleri (clean, is_valid()) ile veri bütünlüğü korunur.
7.3 Kullanılabilirlik (Usability)
•	Kullanıcı arayüzü sade ve işlevseldir.
•	Sorulara ulaşım, kategoriye göre filtreleme ve arama gibi kullanıcı dostu özellikler sunulmuştur.
•	Başarılı işlem sonrası bilgilendirme mesajları (messages.success) gösterilerek kullanıcı yönlendirilmiştir.
7.4 Performans
•	Küçük-orta ölçekli sistemler için yeterli performansı sağlar.
•	Veri filtreleme işlemleri (filter, icontains) sade ve optimize edilmiştir.
•	Gereksiz sorgulardan kaçınılmıştır.
7.5 Taşınabilirlik (Portability)
•	Django’nun platform bağımsız yapısı sayesinde sistem, Linux/Windows/MacOS gibi ortamlarda çalıştırılabilir.
•	SQLite kullanılması, küçük projeler için dosya temelli kurulum kolaylığı sağlar.
7.6 Sürdürülebilirlik (Maintainability)
•	Kodlar okunabilir, mantıksal olarak gruplanmış ve iyi yapılandırılmıştır.
•	Her işlev ayrı fonksiyonlara bölünerek yazılmıştır (ask_question, answer_question vb.).
•	Yeni geliştiriciler için kolayca adapte olunabilir yapıdadır.


