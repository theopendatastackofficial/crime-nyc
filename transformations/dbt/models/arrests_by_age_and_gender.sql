
SELECT 
    age_group,
    perp_sex AS gender,
    year,
    COUNT(*) AS total_arrests
FROM {{ source('main', 'crime_nypd_arrests') }}
GROUP BY age_group, gender, year
ORDER BY year, age_group, total_arrests DESC
