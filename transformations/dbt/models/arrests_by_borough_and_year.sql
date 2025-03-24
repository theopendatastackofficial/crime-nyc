SELECT 
    arrest_boro AS borough,
    year,
    COUNT(*) AS total_arrests
FROM {{ source('main', 'crime_nypd_arrests') }}
GROUP BY 
    arrest_boro, year
ORDER BY 
    year, total_arrests DESC
