<?php

$dsn = "mysql:host=localhost;dbname=vehicles";
$dbusername = "root";
$password = "";

try{
    $pdo = new PDO($dsn,$dbusername,$password);
    //echo "conectado";

}catch (PDOException $e){
    echo "Error en la conexión ". $e;

}