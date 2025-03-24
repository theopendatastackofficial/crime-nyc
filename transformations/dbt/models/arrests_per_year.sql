SELECT 
    year,
    COUNT(*) AS num_arrests
FROM {{ source('main', 'crime_nypd_arrests') }}
GROUP BY year
ORDER BY year
