---
title: Yearly Crime Data
---

Analyze yearly crime trends

```sql yearly_arrests
select * from app.arrests_per_year
```

<LineChart
    data={yearly_arrests}
    x=year
    y=num_arrests
    sort=false
/>




```unique
SELECT DISTINCT year
FROM top_offenses_by_year
```

<Dropdown
    name=unique
    data={unique}
    value=year
    title="Select a year" 
    defaultValue=2023
/>

```sql top_offenses_by_year
select * from top_offenses_by_year 
where 
year = '${inputs.unique.value}' 
```
<DataTable data={top_offenses_by_year}/>

<BarChart
    data={top_offenses_by_year}
    x=offense_description
    y=total_arrests
/>





