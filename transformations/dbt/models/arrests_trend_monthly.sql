SELECT 
    year,
    month,
    COUNT(*) AS total_arrests
FROM {{ source('main', 'crime_nypd_arrests') }}
GROUP BY year, month
ORDER BY year, month
