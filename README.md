## ЗАДАНИЕ 1

---

## ЗАДАНИЕ 2

---

## ЗАДАНИЕ 3

**В базе данных есть следующие таблицы:**

***city***:
city_id;
client_city_id;
city;
client_city

***client***:
client_id;
client_city_id;
birth_date;
registration

***promotion***:
promotion_id;
category_id;
promotion_name;
category_name;
partner_id;
partner_name

***purchase***:
purchase_id;
partner_id;
client_id;
city_id;
promotion_id;
category_id;
purchase_date;
price;
quantity;
status


**Необходимо написать запрос, чтобы получить такую таблицу:**

purchase_date – дата покупки

purchase_id – id покупки

client_id – id покупателя

client_age – возраст покупателя

client_registration_age – как долго человек пользуется вашими магазинами

client_category – содержит new или old, если это первая или последующая покупка соответственно

promotion_name – акция

category_name – категория

partner_name – партнёр

client_city – город, где находится покупатель

city – город

revenue – сумма выручки

quantity – число проданных единиц


**Дополнительные условия:**

1. В таблице должны присутствовать только значения, где в поле status стоит значение 1. 

2. И те значения, где purchase_date находится в диапазоне от 01.05.2020 до 01.08.2020.


**Решение:** <td><a href="https://github.com/IanaSerezhkina/KarpovCourse/blob/main/%D0%97%D0%B0%D0%B4%D0%B0%D0%BD%D0%B8%D0%B5%203" target="_blank"><b>Задание 3</b></a></td>

Для получения необходимой таблицы были сделаны следующие шаги:
- на основе таблицы ***client*** созданы столбцы client_age (разница между текущей датой и днем рождения клиента) и client_registration_age (разница между текущей датой и датой регистрации клиента);
- на основе таблицы ***purchase*** создан столбец revenue как произведение стоимости товара на количество;
- объединены таблицы ***purchase*** и ***promotion*** по переменной partner_id; объединены таблицы ***client*** и ***city*** по переменной client_city_id; получившиеся две таблицы объединены между собой по переменной client_id;

