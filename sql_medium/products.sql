with y2019 as (select company_name,count(product_name) cnt1 from car_launches where year = 2019 group by company_name),
 y2020 as (select company_name,count(product_name) cnt2 from car_launches where year = 2020 group by company_name)

select y.company_name, cnt2 - cnt1 from y2020 y
join y2019 x on y.company_name = x.company_name