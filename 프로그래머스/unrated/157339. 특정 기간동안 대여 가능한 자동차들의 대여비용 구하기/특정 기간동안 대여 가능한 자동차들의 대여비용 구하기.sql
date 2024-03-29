/*
table - CAR, RENTAL_HISTORY, DISCOUNT_PLAN
*/

-- 코드를 입력하세요

WITH car AS (
SELECT 
    CAR_ID, 
    CAR_TYPE, 
    DAILY_FEE
FROM CAR_RENTAL_COMPANY_CAR as a
LEFT JOIN CAR_RENTAL_COMPANY_RENTAL_HISTORY as b
USING (CAR_ID)
WHERE a.CAR_TYPE IN ('SUV','세단')
GROUP BY CAR_ID
HAVING MAX(END_DATE) <= '2022-11-01'
)

# SELECT *
# FROM car

SELECT 
    CAR_ID, 
    CAR_TYPE, 
    ROUND(DAILY_FEE * (100-DISCOUNT_RATE) *0.01 * 30, 0) AS FEE
FROM car 
LEFT JOIN (SELECT * 
           FROM CAR_RENTAL_COMPANY_DISCOUNT_PLAN 
           WHERE duration_type = '30일 이상') AS discount
USING (CAR_TYPE)
WHERE 
    ROUND(DAILY_FEE * (100-DISCOUNT_RATE) * 0.01 * 30, 0) >= 500000 AND 
    ROUND(DAILY_FEE * (100-DISCOUNT_RATE) * 0.01 * 30, 0) < 2000000
ORDER BY
    FEE DESC,
    CAR_TYPE ASC,
    CAR_ID DESC
    
    

# 1. 세단이나 suv인차 중
# 2. 2022년 11월 1일 부터 11월 30일까지 대여 가능  
# 1과 2는 car id

# 3. 30일간의 대여금액이 50만원 이상 200만원 미만
# 1과 3은 car_type