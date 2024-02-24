SELECT A.AUTHOR_ID, B.AUTHOR_NAME, A.CATEGORY, SUM(A.TOTAL_PRICE) AS TOTAL_PRICE
FROM 
(
    SELECT BOOK.BOOK_ID, BOOK.AUTHOR_ID,  BOOK.CATEGORY, BOOK.PRICE * BOOK_SALES.SALES      AS TOTAL_PRICE 
    FROM BOOK 
    JOIN BOOK_SALES 
    ON BOOK.BOOK_ID = BOOK_SALES.BOOK_ID
    WHERE SALES_DATE LIKE "2022-01-%"
    
) A
JOIN AUTHOR B
ON A.AUTHOR_ID = B.AUTHOR_ID
GROUP BY A.CATEGORY, B.AUTHOR_ID
ORDER BY B.AUTHOR_ID, A.CATEGORY DESC

# 저자별 카테고리별 합계

# 1ST
# 책 => 가격
# 책에서 카테고리로 묶는다. => 카테고리 별 판매수... 합이 나온다. 

#2ND
# BOOK_ID별 합산 가격 구한 테이블 만들기
#