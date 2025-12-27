from smartphone import Smartphone

catalog = [
    Smartphone("Xiaomi", "Redmi", 79123652545),
    Smartphone("Sumsung", "Galexy", 79123652555),
    Smartphone("Motorolla", "At", 79123652544),
    Smartphone("Honor", "GF", 79123652588),
    Smartphone("Pocco", "GH", 79123652547),
 ]

       
for smartphone in catalog:
    print (f"{smartphone.Marka_phone} - {smartphone.Model_phone}. +{smartphone.Number_phone}")