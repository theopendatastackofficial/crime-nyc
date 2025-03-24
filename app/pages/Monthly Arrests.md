---
title: Monthly Arrests
---

Analyze how well each agency correctly forecasted their 2023 expenses


```unique
SELECT DISTINCT year
FROM arrests_trend_monthly
```

<Dropdown
    name=unique
    data={unique}
    value=year
    title="Select a year" 
    defaultValue=2023
/>

```sql arrests_trend_monthly
select * from arrests_trend_monthly 
where 
year = '${inputs.unique.value}'
```
<DataTable data={arrests_trend_monthly}/>


<LineChart
    data={arrests_trend_monthly}
    x=month
    y=total_arrests
    sort=false
/>



