<?php 
require "plug.php"; 
$mysql_qry = 'SELECT count(*) FROM Table_1';
$result = mysqli_query($conn, $mysql_qry); 
if($result){
if($row = mysqli_fetch_array($result))
	jsonify(200,"Number of events",$row[0]);
else
	jsonify(206,"Couldn't Retrieve",NULL);
}
else
	jsonify(400,"Failed to Process Query",NULL);
$conn->close();
?>