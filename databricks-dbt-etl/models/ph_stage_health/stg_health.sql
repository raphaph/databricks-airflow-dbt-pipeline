{{
    config(
        tags=["health"]
    )
}}

select 
    id::bigint as id,
    diagnosis::varchar(1) as diagnosis,
    radius_mean::float as radius_mean,
    from_utc_timestamp(current_timestamp(), 'America/Sao_Paulo') as update_date

from {{source('ph_health','breast_cancer')}}