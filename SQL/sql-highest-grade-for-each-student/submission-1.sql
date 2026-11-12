-- Write your query below
/*
SELECT DISTINCT ON (student_id)
    student_id,
    exam_id,
    score
FROM exam_results
ORDER BY student_id, score DESC, exam_id;
*/
SELECT student_id, exam_id, score
FROM (
    SELECT 
        student_id, 
        exam_id, 
        score,
        ROW_NUMBER() OVER (
            PARTITION BY student_id 
            ORDER BY score DESC, exam_id ASC
        ) as rn
    FROM exam_results
) AS ranked_exams
WHERE rn = 1
ORDER BY student_id;