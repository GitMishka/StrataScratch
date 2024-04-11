SELECT MAX(score)-MIN(score) AS difference_in_scores
FROM
  (SELECT student,
          SUM(assignment1+assignment2+assignment3) AS score
   FROM box_scores
   GROUP BY student) a;