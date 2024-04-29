select distinct(stars) from yelp_reviews;

SELECT 
    business_name,
    review_id,
    user_id,
    CAST(stars AS INT) AS stars,
    review_date,
    review_text,
    funny,
    useful,
    cool
FROM yelp_reviews
WHERE 
    stars <> '?'