WITH offense_counts AS (
    SELECT 
        ofns_desc AS offense_description,
        year,
        COUNT(*) AS total_arrests
    FROM {{ source('main', 'crime_nypd_arrests') }}
    GROUP BY ofns_desc, year
)
SELECT 
    offense_description,
    year,
    total_arrests
FROM offense_counts
QUALIFY ROW_NUMBER() OVER (PARTITION BY year ORDER BY total_arrests DESC) <= 10
ORDER BY year, total_arrests DESC
