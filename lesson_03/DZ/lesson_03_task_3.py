from address import Address
from mailing import Mailing

to_addr = Address("123456", "Москва", "Ленина", "10", "45")
from_addr = Address("654321", "Санкт-Петербург", "Садовая", "5", "12")

my_mailing = Mailing(to_addr, from_addr, 350, "RU897X45F")

print(f"Отправление {my_mailing.Track} из {my_mailing.From_address.Index}, "
      f"{my_mailing.From_address.City}, {my_mailing.From_address.Street}, "
      f"{my_mailing.From_address.House} - {my_mailing.From_address.Apartment} "
      f"в {my_mailing.To_address.Index}, {my_mailing.To_address.City}, "
      f"{my_mailing.To_address.Street}, {my_mailing.To_address.House} - "
      f"{my_mailing.To_address.Apartment}. Стоимость {my_mailing.Cost} рублей.")