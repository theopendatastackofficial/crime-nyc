descriptions_crime_nypd_arrests = {
    "arrest_key": "Randomly generated persistent ID for each arrest.",
    "arrest_date": "Exact date of arrest for the reported event.",
    "pd_cd": "Three-digit internal classification code (more granular than Key Code).",
    "pd_desc": "Description of internal classification corresponding with PD code (more granular than Offense Description).",
    "ky_cd": "Three-digit internal classification code (more general category than PD code).",
    "ofns_desc": "Description of internal classification corresponding with KY code (more general category than PD description).",
    "law_code": "Law code charges corresponding to the NYS Penal Law, VTL, and other various local laws.",
    "law_cat_cd": "Level of offense: felony, misdemeanor, or violation.",
    "arrest_boro": "Borough of arrest: B (Bronx), S (Staten Island), K (Brooklyn), M (Manhattan), Q (Queens).",
    "arrest_precinct": "Precinct where the arrest occurred.",
    "jurisdiction_code": "Jurisdiction responsible for arrest. Codes 0 (Patrol), 1 (Transit), and 2 (Housing) represent NYPD; codes 3 and higher represent non-NYPD jurisdictions.",
    "age_group": "Perpetrator’s age within a category.",
    "perp_sex": "Perpetrator’s sex description.",
    "perp_race": "Perpetrator’s race description.",
    "x_coord_cd": "Midblock X-coordinate for New York State Plane Coordinate System, Long Island Zone, NAD 83, units feet (FIPS 3104).",
    "y_coord_cd": "Midblock Y-coordinate for New York State Plane Coordinate System, Long Island Zone, NAD 83, units feet (FIPS 3104).",
    "latitude": "Latitude coordinate for Global Coordinate System, WGS 1984, decimal degrees (EPSG 4326).",
    "longitude": "Longitude coordinate for Global Coordinate System, WGS 1984, decimal degrees (EPSG 4326).",
    "lon_lat": "Georeferenced Point Column based on Longitude and Latitude fields."
}


# Automatically generate table_descriptions
table_descriptions = {
    var_name.replace('descriptions_', ''): var_value
    for var_name, var_value in globals().items()
    if var_name.startswith('descriptions_')
}
