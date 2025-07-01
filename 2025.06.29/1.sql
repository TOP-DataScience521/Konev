Запросы к таблицам схемы world

1. Вывести названия стран и названия сопоставленных им столиц

world=# SELECT
world-#     TRIM(c.Name) AS country_name,
world-#     TRIM(ct.Name) AS capital_name
world-# FROM
world-#     country c
world-# JOIN
world-#     city ct ON c.Capital = ct.ID
world-# ORDER BY
world-#     c.Name;
    country_name    | capital_name
--------------------+--------------
 France             | Paris
 Germany            | Berlin
 Russian Federation | Moscow
 United Kingdom     | London
 United States      | Washington
(5 rows)



2. Сравнить по регионам сумму населения стран и сумму населения городов

world=# SELECT
world-#     c.Region,
world-#     SUM(c.Population) AS total_country_population,
world-#     SUM(ci.Population) AS total_city_population,
world-#     ROUND(SUM(ci.Population) * 100.0 / NULLIF(SUM(c.Population), 0), 2) AS urbanization_percentage
world-# FROM
world-#     country c
world-# LEFT JOIN
world-#     city ci ON c.Code = ci.CountryCode
world-# GROUP BY
world-#     c.Region
world-# ORDER BY
world-#     urbanization_percentage DESC;
           region           | total_country_population | total_city_population | urbanization_percentage
----------------------------+--------------------------+-----------------------+-------------------------
 Northern Europe            |                 67220000 |               8982000 |                   13.36
 Eastern Europe             |                146700000 |              12655000 |                    8.63
 Western Europe             |                150590000 |               5917000 |                    3.93
 Northern America           |                331000000 |                702455 |                    0.21
(4 rows)



3. Вывести десять языков, на которых разговаривает больше всего людей

world=# SELECT
world-#     cl.Language,
world-#     ROUND(SUM(c.Population * cl.Percentage / 100)) AS total_speakers
world-# FROM
world-#     countrylanguage cl
world-# JOIN
world-#     country c ON cl.CountryCode = c.Code
world-# WHERE
world-#     cl.Percentage > 0
world-# GROUP BY
world-#     cl.Language
world-# ORDER BY
world-#     total_speakers DESC
world-# LIMIT 10;
            language            | total_speakers
--------------------------------+----------------
 English                        |      337156060
 Russian                        |      125721900
 German                         |       79527540
 French                         |       63077040
 Spanish                        |       42699000
 Tatar                          |        4694400
 Turkish                        |        2163200
 Welsh                          |         604980
(8 rows)




Запросы к таблицам схемы hospital

4. Вывести названия специальностей и суммарное количество дней отпусков, в которых были врачи каждой специальности; отсортировать по возрастанию суммарного количества дней отпуска

hospital=# SELECT
hospital-#     TRIM(s.name) AS specialization,
hospital-#     COALESCE(SUM((v.end_date - v.start_date + 1)), 0) AS total_vacation_days
hospital-# FROM
hospital-#     hospital.specializations s
hospital-# LEFT JOIN
hospital-#     hospital.doctors_specs ds ON s.id = ds.spec_id
hospital-# LEFT JOIN
hospital-#     hospital.vacations v ON ds.doctor_id = v.doctor_id
hospital-# GROUP BY
hospital-#     s.id, s.name
hospital-# ORDER BY
hospital-#     total_vacation_days ASC;
 specialization | total_vacation_days
----------------+---------------------
 Кардиолог      |                   0
 Хирург         |                  14
 Терапевт       |                  29
(3 rows)




5. Вывести округлённую до целого сумму средств, которую можно выделить на одну палату этого отделения 
(в зависимости от количества палат в отделении), от всех пожертвований каждому отделению; отсортировать 
по убыванию найденной суммы

hospital=# SELECT
hospital-#     d.id AS department_id,
hospital-#     TRIM(d.name) AS department_name,
hospital-#     COUNT(w.id) AS ward_count,
hospital-#     SUM(dn.amount) AS total_donations,
hospital-#     ROUND(SUM(dn.amount) / NULLIF(COUNT(w.id), 0)) AS donation_per_ward
hospital-# FROM
hospital-#     hospital.departments d
hospital-# LEFT JOIN
hospital-#     hospital.wards w ON d.id = w.dep_id
hospital-# LEFT JOIN
hospital-#     hospital.donations dn ON d.id = dn.dep_id
hospital-# GROUP BY
hospital-#     d.id, d.name
hospital-# ORDER BY
hospital-#     donation_per_ward DESC;
 department_id | department_name | ward_count | total_donations | donation_per_ward
---------------+-----------------+------------+-----------------+-------------------
             3 | Кардиология     |          1 |      1000000.00 |           1000000
             2 | Хирургия        |          1 |       750000.00 |            750000
             1 | Терапия         |          2 |      1000000.00 |            500000
(3 rows)



  =========================
