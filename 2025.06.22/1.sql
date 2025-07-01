������� ����������� � PostgreSQL


������� � ������� doctors:

1. ������� ������� ����� (salary) ���� �����������

hospital=# SELECT AVG(salary) FROM hospital.doctors;
         avg
---------------------
 123333.333333333333
(1 row)

2. ������� ������� ������ ��� ���� �����������,
 ��� ����� ���� �������� (����� ����� �������� �� 
���������� ����������� �������)

hospital=# SELECT AVG(premium) AS average_premium_above_avg
hospital-# FROM hospital.doctors
hospital-# WHERE salary > 123333.3;
 average_premium_above_avg
---------------------------
        30000.000000000000
(1 row)

3. ������� � ����������� �� ����������� �������
 ���������� ���� � ������� ��� ������� ���������� �
 ����������� ������� datediff()

# datediff() - � ��� �������  ��� � mysql - ������� ����� ������, 
� �� ����� ����� ������� � ������� � ������� ����� � �������


hospital=# SELECT
hospital-#     doctor_id,
hospital-#     d.last_name || ' ' || d.first_name || ' ' || d.patr_name AS full_name,
hospital-#     AVG(end_date - start_date)::INT AS avg_vacation_days
hospital-# FROM
hospital-#     hospital.vacations v
hospital-# JOIN
hospital-#     hospital.doctors d ON v.doctor_id = d.id
hospital-# GROUP BY
hospital-#     doctor_id, d.last_name, d.first_name, d.patr_name
hospital-# ORDER BY
hospital-#     avg_vacation_days ASC;
 doctor_id |        full_name        | avg_vacation_days
-----------+-------------------------+-------------------
         2 | ������� ����� ��������� |                13
         1 | ������ ���� ��������    |                14
(2 rows)





4. ������� ��� ������� ���������� ����� ������ ��� ������� � ����� ������� ��� ������� � ����������� �� ����������� �������� ����� ����� ����� ����������

hospital=# SELECT
hospital-#     v.doctor_id,
hospital-#     d.last_name || ' ' || d.first_name || ' ' || COALESCE(d.patr_name, '') AS full_name,
hospital-#     MIN(EXTRACT(YEAR FROM v.start_date)) AS first_vacation_year,
hospital-#     MAX(EXTRACT(YEAR FROM v.start_date)) AS last_vacation_year,
hospital-#     (MAX(EXTRACT(YEAR FROM v.start_date)) - MIN(EXTRACT(YEAR FROM v.start_date))) AS years_diff
hospital-# FROM
hospital-#     hospital.vacations v
hospital-# JOIN
hospital-#     hospital.doctors d ON v.doctor_id = d.id
hospital-# GROUP BY
hospital-#     v.doctor_id, d.last_name, d.first_name, d.patr_name
hospital-# ORDER BY
hospital-#     years_diff ASC;
 doctor_id |        full_name        | first_vacation_year | last_vacation_year | years_diff
-----------+-------------------------+---------------------+--------------------+------------
         2 | ������� ����� ��������� |                2023 |               2023 |          0
         1 | ������ ���� ��������    |                2023 |               2024 |          1
(2 rows)





������� � ������� donations:

5. ������� ����� ������������� �� �� ����� ��� ������� ��������� � 
����������� �� ����������� ������� ���������

hospital=# SELECT
hospital-#     d.id AS department_id,
hospital-#     d.name AS department_name,
hospital-#     SUM(dn.amount) AS total_donations
hospital-# FROM
hospital-#     hospital.donations dn
hospital-# JOIN
hospital-#     hospital.departments d ON dn.dep_id = d.id
hospital-# GROUP BY
hospital-#     d.id, d.name
hospital-# ORDER BY
hospital-#     d.id ASC;
 department_id | department_name | total_donations
---------------+-----------------+-----------------
             1 | �������         |       500000.00
             2 | ��������        |       750000.00
             3 | �����������     |      1000000.00
(3 rows)



6. ������� ����� ������������� �� ������ ��� ��� ������� �������� 
� ����������� �� ����������� ������� ��������� � �����

hospital=# SELECT
hospital-#     d.sponsor_id,
hospital-#     EXTRACT(YEAR FROM d.date) AS year,
hospital-#     SUM(d.amount) AS total_amount
hospital-# FROM
hospital-#     hospital.donations d
hospital-# GROUP BY
hospital-#     d.sponsor_id, EXTRACT(YEAR FROM d.date)
hospital-# ORDER BY
hospital-#     d.sponsor_id ASC,
hospital-#     year ASC;
 sponsor_id | year | total_amount
------------+------+--------------
          1 | 2023 |   1500000.00
          2 | 2023 |    750000.00
(2 rows)