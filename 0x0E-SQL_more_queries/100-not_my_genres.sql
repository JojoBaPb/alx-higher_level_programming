-- Lists all genres of the database hbtn_0d_tvshows
-- those that are not linked to the show Dexter.
-- Records are sorted by asc genre name.
SELECT DISTINCT `name`
FROM `tv_genres` AS g
INNER JOIN `tv_show_genres` AS s
ON g.`id` = s.`genre_id`

INNER JOIN `tv_shows` AS t
ON s.`show_id` = t.`id`
WHERE g.`name` NOT IN
(SELECT `name`
	FROM `tv_genres` AS g
	INNER JOIN `tv_show_genres` AS s
	ON g.`id` = s.`genre_id`

	INNER JOIN `tv_shows` AS t
	ON s.`show_id` = t.`id`
	WHERE t.`title` = "Dexter")
ORDER BY g.`name`;
