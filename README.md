# PyTest'in Yaygın Dekoratörleri ve Açıklamaları

1. **@pytest.mark.parametrize**:
   Bu dekoratör, bir test fonksiyonunu birden fazla veri seti ile çalıştırmanıza olanak tanır. Farklı girişler ve beklenen çıkışlar sağlayarak testlerinizi çeşitlendirebilirsiniz.

2. **@pytest.fixture**:
   Test fonksiyonlarına belirli bir veri veya durumu sağlayan bir yapılandırma işlevi tanımlar. Bu, tekrarlanan hazırlık işlemlerini merkezi bir yerden yönetmeyi sağlar.

3. **@pytest.mark.skip**:
   Belirli bir testin atlanmasını sağlar. Genellikle bir testin geçici olarak çalıştırılmaması gerektiğinde kullanılır.

4. **@pytest.mark.skipif**:
   Belirli bir koşula bağlı olarak testin atlanmasını sağlar. Koşul sağlandığında test atlanır.

5. **@pytest.mark.xfail**:
   Beklenen bir hata durumu olduğunda kullanılır. Testin başarısız olması beklenir ve başarısız olursa test süitini kırmaz.

6. **@pytest.mark.usefixtures**:
   Test sınıfları veya modüller için belirli fikstürlerin otomatik olarak kullanılmasını sağlar.

Bu dekoratörler, testlerinizi daha esnek ve yönetilebilir hale getirmek için kullanışlı araçlardır. Testlerinizi yazarken hangi dekoratörlerin ihtiyaçlarınıza uygun olduğunu belirlemek, daha etkili bir test süreci oluşturmanıza yardımcı olabilir.

