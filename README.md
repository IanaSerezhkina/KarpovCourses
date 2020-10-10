## ЗАДАНИЕ 1

В таблице содержится информация о покупках. Необходимо, воспользовавшись этими данными, выяснить, какие пары товаров пользователи чаще всего покупают вместе. 

**Решение:** <td><a href="https://github.com/IanaSerezhkina/KarpovCourses/blob/main/%D0%97%D0%B0%D0%B4%D0%B0%D0%BD%D0%B8%D0%B5%201.ipynb" target="_blank"><b>Задание 1</b></a></td>

Для решения я использовала библиотеку mlxtend и её модуль apriori. 

**Выводы**: 
- Наиболее часто встречаемые пары товаров состоят преимущественно из овощей, самая распространенная пара это "огурцы и укроп". Вероятно это связано с тем, что это самые распространенные ингредиенты для летнего салата. 
- В топ-5 пар попал паттерн "огурцы и арбуз", скорее всего это связано с сезонностью: конец лета - время нового урожая овощей и арбузов. 
- Также стоит отметить, что чаще всего одним из товаров в паре являются "огурцы", что можно объяснить тем, что данный овощ является самым распространенным в продуктовой корзине в принципе. 

---

## ЗАДАНИЕ 2

**Вопрос следующий:** К вам поступила информация о числе заказов за прошедшие 3 месяца (январь-март) с разрешением по неделям. Постройте (если это возможно) прогноз продаж на следующие 3 месяца, с учётом того, что в неделю с 2020-02-02 по 2020-02-09 была проведена массивная акция, повысившая число заказов на 7%.

**Решение:** 

Так как данные представленны только объемом продаж за неделю (без независимых переменных), то прогноз продаж можно было бы построить с применением метода скользящего среднего, однако в данном случае прогноз осуществить невозможно, так как:
- во-первых, у нас нет данных за предыдущие года, чтобы установить основной тренд продаж (идет снижение или повышение)
- во-вторых, из-за отсутствия данных за предыдущие года мы не можем оценить влияние сезонности на продажи 

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
- на основе таблицы ***purchase*** <s>через костыли</s> создана колонка client_category: сначала путем агрегации я нашла первую дату покупки каждого клиента и через CASE добавила туда колонку client_category с записью 'new', затем объединила через FULL JOIN эту таблицу с изначальной purchase и заполнила пропуски в client_category как 'old';
- на основе таблицы ***client*** созданы столбцы client_age (разница между текущей датой и днем рождения клиента) и client_registration_age (разница между текущей датой и датой регистрации клиента);
- на основе таблицы ***purchase*** создан столбец revenue как произведение стоимости товара на количество;
- объединены таблицы ***purchase*** и ***promotion*** по переменной partner_id; объединены таблицы ***client*** и ***city*** по переменной client_city_id; получившиеся две таблицы объединены между собой по переменной client_id

