---
title: Crime Data
---

Analyze how well each agency correctly forecasted their 2023 expenses

<Dropdown name=granularity>
    <DropdownOption valueLabel="arrests_by_borough_and_year" value="1" />
    <DropdownOption valueLabel="top_offenses_by_year" value="2" />
    <DropdownOption valueLabel="arrests_by_age_and_gender" value="3" />
    <DropdownOption valueLabel="arrests_trend_monthly" value="4" />
    <DropdownOption valueLabel="arrests_trend_monthly" value="5" />
</Dropdown>

{#if inputs.granularity.value == 1}

```sql arrests_by_borough_and_year
select * from arrests_by_borough_and_year 
```


<DataTable data={arrests_by_borough_and_year}/>


<BarChart
    data={arrests_by_borough_and_year}
    x=year
    y=total_arrests
/>

<BarChart 
    data={arrests_by_borough_and_year}
    x=year
    y=total_arrests
    series=borough
    type=grouped
/>

<BarChart 
    data={arrests_by_borough_and_year}
    x=year
    y=total_arrests
    yFmt=num1k
    series=borough
    type=stacked100
/>


{:else if inputs.granularity.value == 2}


```unique
SELECT DISTINCT year
FROM top_offenses_by_year
```

<Dropdown
    name=unique
    data={unique}
    value=year
    title="Select a year" 
    defaultValue="2023"
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










{:else if inputs.granularity.value == 3}

```unique_year_one
SELECT DISTINCT year
FROM arrests_by_age_and_gender
```

<Dropdown
    name=unique_year_one
    data={unique_year_one}
    value=year
    title="Select a year" 
    defaultValue="2023"
/>


```sql query
select * from arrests_by_age_and_gender 
where 
year = '${inputs.unique_year_one.value}'  
```
<DataTable data={query}/>

<BarChart
    data={query}
    x=gender
    y=total_arrests
/>

<BarChart
    data={arrests_by_age_and_gender}
    x=age_group
    y=total_arrests
/>


<BarChart 
    data={arrests_by_age_and_gender}
    x=year
    y=total_arrests
    series=gender
    type=grouped
/>

<BarChart 
    data={arrests_by_age_and_gender}
    x=year
    y=total_arrests
    yFmt=num1k
    series=gender
    type=stacked100
/>


<BarChart 
    data={arrests_by_age_and_gender}
    x=year
    y=total_arrests
    yFmt=num1k
    series=age_group
    type=stacked100
/>















{:else if inputs.granularity.value == 4}



```sql arrests_by_age_and_gender
select * from arrests_by_age_and_gender 
```
<DataTable data={arrests_by_age_and_gender}/>



{:else }




```sql arrests_trend_monthly
select * from arrests_trend_monthly 
```
<DataTable data={arrests_trend_monthly}/>



{/if}