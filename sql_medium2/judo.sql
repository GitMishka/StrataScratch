select team, avg(weight) from olympics_athletes_events where (age between 20 and 30) and sport = 'Judo'
group by team