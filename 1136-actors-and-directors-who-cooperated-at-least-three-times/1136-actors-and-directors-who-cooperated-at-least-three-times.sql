 /*all pairs aid,did
 atleast 3 times
 */

 select actor_id,director_id
 from ActorDirector
 group by actor_id,director_id
 having  count(actor_id)>=3


-- select actor_id,director_id
-- from cte
-- where count(actor_id)>=3