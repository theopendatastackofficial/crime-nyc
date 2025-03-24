SELECT 
    date_trunc('month', arrest_date) AS arrest_month,
    law_cat_cd AS crime_level,
    COUNT(*) AS num_arrests
FROM {{ source('main', 'crime_nypd_arrests') }}
GROUP BY arrest_month, crime_level
ORDER BY arrest_month, crime_level
