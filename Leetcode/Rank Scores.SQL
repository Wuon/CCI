SELECT
    s2.Score as Score,
    (
        SELECT
            (COUNT(DISTINCT Score) + 1 )
        FROM
            Scores as s1
        WHERE
            s2.Score < s1.Score
    ) as Rank
FROM
    Scores as s2
ORDER BY
    Score DESC
;
