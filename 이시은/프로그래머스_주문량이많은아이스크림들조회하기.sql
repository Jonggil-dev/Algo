-- inner join 이용 -> 가로로 합침
SELECT FLAVOR FROM 
(SELECT F.FLAVOR, F.TOTAL_ORDER + J.TOTAL_ORDER AS TOTAL_ORDER 
FROM FIRST_HALF F
INNER JOIN (
    SELECT FLAVOR, SUM(TOTAL_ORDER) AS TOTAL_ORDER FROM JULY
    GROUP BY FLAVOR
) J ON J.FLAVOR = F.FLAVOR
ORDER BY TOTAL_ORDER DESC) NEW_TABLE
LIMIT 3;

-- union all 이용 -> 중복을 허용하면서 세로로 합침
select flavor from (
select flavor, total_order from first_half
union all
select flavor, total_order from july
) new_table
group by flavor
order by sum(total_order) desc
limit 3;