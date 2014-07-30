select ar.id,
       race_id,
       r.`qualifier_id`,
       r.name,
       year,
       age,
       athlete_id,
       TIME_TO_SEC(final_time) as 'final_time',
       high_temp,
       low_temp,
       high_humidity,
       low_humidity,
       starting_elevation,
       gross_elevation_gain
from athlete_races ar join races r on ar.`race_id` = r.`id`
and r.`race_type` like 'Ironman'
and ar.`age` between 40 and 49
and ar.`final_time` != 0
and ar.`athlete_id` in (
select athlete_id
from athlete_races ar join races r on ar.`race_id` = r.`id`
and ar.age != 0
and ar.`age` between 40 and 49
and r.`race_type` like 'Ironman'
and ar.`final_time` != 0
and ar.`m_f` like 'M'
and ar.athlete_id != 1109
group by athlete_id
having count(*) > 10)
order by athlete_id;
