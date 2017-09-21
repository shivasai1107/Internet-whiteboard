<?php
require "plug.php"; 
$inuser = $_GET['un'];
$inpass = $_GET['pc'];
$tablename = $_GET['tn'];

if(!empty($inuser)&& !empty($inpass)&& !empty($tablename)){

$inpass = sha1($inpass);
$flag1 =0;
$flag2 =0;
$str = sprintf('SELECT * FROM `%s` WHERE 1;',$tablename);
$mysql_qry = $str;
$result = mysqli_query($conn, $mysql_qry); 
$results = array(); 
while($row = mysqli_fetch_array($result))
{ if($row['user'] == $inuser) $flag1 = 1; 
 if($row['passcode'] == $inpass) $flag2 = 1; }
if($flag1 == 1 & $flag2 == 1) 
    jsonify(200,"Login Success",NULL);

else jsonify(206,"Login Failure",NULL);
}

else 
      jsonify(400,"Incomplete Arguments",NULL);
$conn->close();
?>