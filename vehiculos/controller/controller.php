<?php
error_reporting(E_ALL);
ini_set('display_errors', 1);
include("../config/connection.php");
require("../model/Vehicle.php");

if($_SERVER["REQUEST_METHOD"] == "POST"){
    $id = $_POST["id"];
    $name = $_POST["name"];
    $brand = $_POST["brand"];
    $model = $_POST["model"];
    $year = $_POST["year"];
    $color = $_POST["color"];
    $price = $_POST["price"];
    $image_path = $_POST["image_path"];


    $vehicleList = new VehicleList($name,$brand,$model,$year,$color,$price,$image_path,$pdo);

    if($_POST["action"] == "update"){
        $vehicleList->edit($id);
    }elseif($_POST["action"] == "insert"){
        $vehicleList->insert();
    }

    header("Location: ../view/vehicleList.php");
}
