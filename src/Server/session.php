<?php
require "plug.php";

$sql = "SELECT user,loggedin FROM `user_table` where loggedin = 'YES'";
$userarray=array();
$result = $conn->query($sql);
if($result){
if ($result->num_rows > 0) {
    while($row = $result->fetch_assoc()) {
        array_push($userarray,$row["user"]);
    }

    	jsonify(200,"The Active Users are ",$userarray);
}
else jsonify(200,"NO USERS FOUND ",NULL);
}
else
	jsonify(400,"Couldn't Access Mysql",NULL);

$conn->close();
?>	