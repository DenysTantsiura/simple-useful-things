/*
Оцінки студентів у певній групі з певного предмета на останньому занятті.
*/ 
SELECT
  a.value_ AS Assessment, 
  s.name AS Student,
  g.group_name AS Group_,
  sub.subject AS Subject,
  DATE(a.date_of) AS Date_of -- --CONVERT(varchar, a.date_of,2) AS [YYYY-MM.DD]
FROM
  assessments AS a
  JOIN
  subjects AS sub
	  ON a.subject_id = sub.id
  JOIN
  students AS s
	  ON a.student_id = s.id
  JOIN
  groups_ AS g
	  ON s.group_id = g.id
WHERE g.id = 3 AND sub.id = 2 -- Group_ = "Group-2" AND Subject = "History" --AND a.date_of = MAX(a.date_of)
GROUP BY Student, Group_, Subject, Date_of, Assessment  -- bug ? no grouping by Student
ORDER BY Student, Date_of DESC;

/*
SELECT
  a.value_ AS Assessment, 
  s.name AS Student,
  g.group_name AS Group_,
  sub.subject AS Subject,
  DATE(a.date_of) AS Date_of -- --CONVERT(varchar, a.date_of,2) AS [YYYY-MM.DD]
FROM
  assessments AS a
  JOIN
  subjects AS sub
	  ON a.subject_id = sub.id
  JOIN
  students AS s
	  ON a.student_id = s.id
  JOIN
  groups_ AS g
	  ON s.group_id = g.id
WHERE g.id = 3 AND sub.id = 2 and a.date_of in (
	select a.date_of 
	from assessments AS a
		join students AS s
	  		ON a.student_id = s.id
	  	join groups_ AS g
	  		ON s.group_id = g.id
	where a.subject_id = 2 and g.id = 3 --and a.date_of = max(a.date_of)
	--group by s.id
	order by a.date_of desc
	--limit 1
)-- Group_ = "Group-2" AND Subject = "History" --AND a.date_of = MAX(a.date_of)
--GROUP BY Student, Group_, Subject, Date_of, Assessment  -- bug ? no grouping by Student
--ORDER BY Student, Date_of DESC;
GROUP BY Student, a.value_, g.group_name, sub.subject, a.date_of
ORDER BY Date_of DESC;


*/
