{{
    config(
        materialized='incremental'
        ,unique_key='id'
        ,dist='auto'
        ,sort='id'
        ,tags=["health"]
    )
}}

select 
    *
from {{ref('stg_health')}}
where id >= 1