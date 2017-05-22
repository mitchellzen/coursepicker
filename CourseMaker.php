<?php

/*
 * This file is purely to inject sample data into the database; courses generated at random
 */
define("NUMBER_OF_COURSES", 2);


function random_lipsum($amount = 1, $what = 'paras', $start = 0) {
    return simplexml_load_file("http://www.lipsum.com/feed/xml?amount=$amount&what=$what&start=$start")->lipsum;
}

$courses = random_lipsum(NUMBER_OF_COURSES);
$db = new SQLite3('backend/db.sqlite3');
foreach($courses as $key=>$course){
	$words = explode(" ", $course);
	$name = $words[0];
	$professor = $words[1];
	$professor_insert = sprintf('INSERT INTO course_picker_professor (id, name) VALUES ("%d, %s")',$key,$professor);
	echo $professor_insert;
	//$db->exec($professor_insert);

	//todo: randomly generate cost
	$cost = 3233;
	$course_insert = sprintf('INSERT INTO course_picker_course (name, cost, description) VALUES ("%d, %s, %d, %s")',$key,$name, $cost, $course);
	echo $course_insert;
	//$db->exec($course_insert);

	//todo: randomly generate dates
	$start_date = date('Y-m-d H:i:s');
	//todo: add 1 hour for end date
	$end_date = date('Y-m-d H:i:s');
	$session_insert = sprintf('INSERT INTO course_picker_session (course, start_date, end_date) VALUES ("%d, %s, %s")',$key,$start_date,$end_date);
	echo $session_insert;
	//$db->exec($session_insert);
	$teaching_insert = sprintf('INSERT INTO course_picker_professor_courses (professor_id, course_id) VALUES ("%d, %d")',$key,$key);
	echo $teaching_insert;
	//$db->exec($teaching_insert);

}


?>