<?php
require "plug.php";

$u= $_GET['un'];
$x= $_GET['pc'];
$t= $_GET['ut'];
$w= $_GET['tn'];
$y = sha1($x);
if(!empty($u) && !empty($x) && !empty($t) && !empty($w)){
$str = sprintf("INSERT INTO user_table (user, passcode, user_type) VALUES ('%s', '%s', '%s')",$u,$y,$t);
$sql = $str;
if(mysqli_query($conn,$sql)){
     jsonify(200,"New record created successfully",NULL);
}
else{
	$state = sprintf("%s",mysqli_error($conn));
     jsonify(206,"Failed to Register",NULL);
}
}
else
     jsonify(400,"Incomplete Arguments",NULL);

$conn->close();


?>