-- 코드를 입력하세요
SELECT 
    FLAVOR
FROM FIRST_HALF
LEFT JOIN (
    SELECT 
        FLAVOR,
        SUM(TOTAL_ORDER) as TOTAL_ORDER_JULY
    FROM JULY
    GROUP BY FLAVOR ) as sub
USING(FLAVOR)
GROUP BY FLAVOR
ORDER BY (SUM(TOTAL_ORDER) + SUM(TOTAL_ORDER_JULY)) DESC
LIMIT 3;
