-- SQL example to get the average years of service of presidents
SELECT AVG(YRS_SERV) AS average_years_of_service
FROM PRESIDENT;

-- SQL example to get the total number of children of presidents
SELECT SUM(NA_CHILDREN) AS total_number_of_children
FROM PRES_MARRIAGE;

-- SQL example to get the name and birth year of the oldest living president
SELECT PRES_NAME, BIRTH_YR
FROM PRESIDENT
WHERE DEATH_AGE IS NULL
ORDER BY BIRTH_YR ASC
LIMIT 1;

-- SQL example to get the number of presidents from each state
SELECT STATE_BORN, COUNT(*) AS number_of_presidents
FROM PRESIDENT
GROUP BY STATE_BORN;

-- SQL example to get the election years in which the sum of votes was greater than 100 million
SELECT ELECTION_YEAR
FROM ELECTION
GROUP BY ELECTION_YEAR
HAVING SUM(VOTES) > 100000000;

-- SQL example to get the details of the latest election
SELECT *
FROM ELECTION
ORDER BY ELECTION_YEAR DESC
LIMIT 1;

-- ...and so on, until we cover various types of operations and reach the length you require.

