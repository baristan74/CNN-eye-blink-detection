## Proje Konusu:
Engelli bireyler için gözlerden yukarı, aşağı ve enter komutlarının algılanması, 
menü üzerinde sol göz kapalı ise yukarı, sağ göz kapalı ise aşağı, ikisi de kapalı ise enter komutları algılanacaktır.


## Projede Kullanılan Teknolojiler: 
•	Tensorflow
•	Keras
•	Matplotlib
•	Numpy
•	Sklearn
•	OpenCV2


## Proje aşamaları:
######	1. Veri setinin oluşturulması
######	2. Verilerin düzenlenmesi
######	3. Gerekli kütüphanelerin yüklenmesi
######	4. Verilerin train, validation ve test olarak ayrılması
######	5. Verilerin normalize edilmesi
######	6. Veri arttırım işlemlerinin gerçekleştirilmesi
######	7. CNN katmanlarının oluşturulması
######	8. Eğitim işleminin gerçekleştirilmesi
######	9. Webcam üzerinden görüntülerin alınması
######	10. Görüntülerin sınıflandırılması
######	11. Sınıflama üzerinden operasyonların gerçekleştirilmesi

## Veri Setinden Örnek Görüntüler

<p align="center">
  <img width="150" height="200" src="https://user-images.githubusercontent.com/61651202/175304987-38b1c516-5286-4e42-8638-24d56dbc8a04.png">
  <img width="150" height="200" src="https://user-images.githubusercontent.com/61651202/175305375-ddd965fe-9739-423d-bc0e-2ab1b3eb857e.png">
  <img width="150" height="200" src="https://user-images.githubusercontent.com/61651202/175305393-b859f322-d862-4069-bc52-ecdde3905a45.png">
  <img width="150" height="200" src="https://user-images.githubusercontent.com/61651202/175305402-793e788d-1140-46ee-96c3-0fbee0acd0d7.png">
</p>

### CNN Katmanları

<p align="center">
  <img width="400" height="500" src="https://user-images.githubusercontent.com/61651202/175306243-1df266a8-c581-434b-a9ae-270e76d57947.png">
</p>

### Convolution Katmanı: 
-	Bu katman resmin özelliklerini algılamaktan sorumludur. Görüntülerdeki özellikleri algılamak için bazı filtreler uygular. Belirlenen filtre görüntü üzerinde gezdirilir. Gezdirilme işlemi belirlenen stride (adım) değerine göre gerçekleşir. Burada, resim ve filtre matrisi arasındaki indisler birbiri ile çarpılır ve tüm sonuçlar toplanır daha sonra sonuç çıktı matrisinde depolanır. Oluşan çıktı matrisi görüntünün özelliklerini taşır.
- Yukarıdaki görselde görüldüğü gibi projemizde 4 adet Convolution katmanı bulunmaktadır filtre sayıları 16,32,64,128’dir ve bu katmanlardaki filtre boyutları 5x5 ve 3x3 lüktür.

<p align="center">
  <img width="600" height="170" src="https://user-images.githubusercontent.com/61651202/175306837-8ad6618b-5bfc-4b81-912f-5bfd681376e7.png">
</p> 
     
### Pooling Katmanı: 
- Genellikle oluşturulan öznitelik matrislerine uygulanır. Şekilde görüldüğü gibi 4x4 lük öznitelik matrisine 2x2 lik bir max pooling uygulanırsa aşağıdaki gibi çıktı alınır. Genellikle kullanılan yöntem max pooling yöntemidir. Fakat average pooling ve min pooling gibi yöntemler de mevcuttur. Bu katmanın görevi görüntünün boyutunu küçültüp işlem hacmini azaltmaktır.
- Projede 3 adet MaxPooling katmanı bulunmakta ve bu katmanlardaki filtre boyutları 2x2’dir.

<p align="center">
<img width="500" height="150" src="https://user-images.githubusercontent.com/61651202/175307457-98e9ef1d-3062-4078-a956-708d30f76a25.png">
</p>
 
### Dropout: 
- Bu işlem eğitim sırasında aşırı öğrenmeyi (overfitting) engellemek için bazı nöronları unutmakta kullanılır. Projede %20 lik dropout uygulanmıştır.

### Flatten: 
- Bu katmanın görevi fully connected katmanı için giriş verilerini hazırlamaktır. Sinir ağları, girişlerini vektörel olarak aldığı için görüntü matrislerini vektörel formata çevirerek bu işlemi gerçekleştirir.


### Fully Connected Katmanı: 
- Bu katman verileri flatten katmanından alır ve oluşturulan sinir ağı ile öğrenme işlemini gerçekleştirir. Öğrenme işlemi, nöronlardaki ağırlıkların güncellenmesiyle gerçekleşir.
- Projede 4 adet gizli katman bulunmaktadır. Sırasıyla bu katmanlarda 64,32,32,16 adet nöron bulunmaktadır. Aktivasyon fonksiyonu olarak ReLU kullanılmıştır. 
- Çıktı katmanında ise sınıf sayısı kadar nöron bulunmaktadır. Aktivasyon fonksiyonu olarak Softmax kullanılmıştır.

### Kullanılan Aktivasyon Fonksiyonları:
-	ReLU : [0,+ ∞) arasında değer alır. Bu aktivasyon fonksiyonunun avantajı aynı anda tüm nöronları aktive etmemesidir. Yani bir nöron negatif değer üretirse, aktive edilmeyeceği anlamına gelir. Bu da diğer aktivasyon fonksiyonlarından daha verimli ve hızlı çalışmasını sağlar bu nedenle ReLU çok katmanlı sinir ağlarında daha çok tercih edilir.

<p align="center">
  <img width="300" height="150" src="https://user-images.githubusercontent.com/61651202/175308140-14ae1114-12ad-44a7-8133-1de4997238b0.png">
</p> 

- Softmax : Çoğu zaman çoklu Sigmoid olarak bilinen bu fonksiyon, çok sınıflı hedef değişken içeren sınıflandırma problemleri için uygun bir aktivasyon fonksiyonudur. Softmax çıktı olarak her sınıfa ait olasılık sonucu döndürür. Örneğin 3 sınıflı bir tahmin yapıyorsak 3 adet olasılık sonucu döndürür.

<p align="center">
  <img width="200" height="100" src="https://user-images.githubusercontent.com/61651202/175308538-e2ed69f7-7872-49e1-8681-d87fbdf81860.png">
  <img width="200" height="100" src="https://user-images.githubusercontent.com/61651202/175308548-203ab4e2-d878-43ab-90f8-f1f3545f8da1.png">
  <img width="200" height="150" src="https://user-images.githubusercontent.com/61651202/175308551-e0e81631-6bad-4b89-b1ef-e668339a7303.png">
</p> 

### Proje Eğitim Analizi


  
<p align="center">
  <img width="300" height="300" src="https://user-images.githubusercontent.com/61651202/175310240-cead6901-6349-4eb7-939c-62cd121e3a31.png">
  <img width="300" height="300" src="https://user-images.githubusercontent.com/61651202/175310409-0110327c-eea6-42aa-be2b-16e3ac92225d.png">
</p> 

- Dalgalanmalardaki sebeplerden biri batch size’in küçük tutulmasından kaynaklanmaktadır.
  
<p align="center">
  <img width="600" height="75" src="https://user-images.githubusercontent.com/61651202/175310986-4e8b9fa0-6689-4a20-873f-9baba9025442.png">
</p> 
- Eğitim sonucunda elde ettiğimiz accuracy ve loss değerleri görüldüğü gibidir.

### Projeden Görüntüler
- Gözler Açık : Gözler açıkken menü üzerinde herhangi bir işlem gerçekleşmiyor.
<p align="center">
  <img width="600" height="300" src="https://user-images.githubusercontent.com/61651202/175314594-b41f32b4-01e3-4291-87a2-ed96dcde385c.png">
</p> 

- İki Göz Kapalı: İki göz kapalı iken menü üzerinde enter işlemi gerçekleşiyor.
<p align="center">
  <img width="600" height="300" src="https://user-images.githubusercontent.com/61651202/175314575-0beb8e11-ee0c-4664-88c6-d2060917a15c.png">
</p> 

-	Sağ Göz Kapalı: Sağ göz kapalı iken menü üzerinde aşağı hareket sağlanıyor.
<p align="center">
  <img width="600" height="300" src="https://user-images.githubusercontent.com/61651202/175314612-6fdbf71f-a07a-492b-bc3f-0820519c3e6b.png">
</p> 

-	Sol Göz Kapalı: Sol göz kapalı iken menü üzerinde yukarı hareket sağlanıyor.
<p align="center">
  <img width="600" height="300" src="https://user-images.githubusercontent.com/61651202/175314639-499ed770-bf16-400e-a8b8-ee364faeed6d.png">
</p> 
  

## FAYDALANMIŞ OLDUĞUM KAYNAKLAR
-	https://stanford.edu/~shervine/l/tr/teaching/cs-230/cheatsheet-convolutional-neural-networks#layer
-	https://keras.io/api/layers/
-	https://docs.opencv.org/3.4/d8/dfe/classcv_1_1VideoCapture.html#a57c0e81e83e60f36c83027dc2a188e80
-	https://medium.com/deep-learning-turkiye/derin-ogrenme-uygulamalarinda-en-sik-kullanilan-hiper-parametreler-ece8e9125c4
-	https://devdocs.io/matplotlib~3.1/
-	https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html
-	https://machinelearningmastery.com/adam-optimization-algorithm-for-deep-learning/
