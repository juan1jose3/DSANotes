<?php
class VehicleList{
    private $name;
    private $brand;
    private $model;
    private $year;
    private $color;
    private $price;
    private $image_path;
    private $pdo;

    function __construct($name,$brand,$model,$year,$color,$price,$image_path,$pdo)
    {
        $this->name = $name;
        $this->brand = $brand;
        $this->model = $model;
        $this->year = $year;
        $this->color = $color;
        $this->price = $price;
        $this->image_path = $image_path;
        $this->pdo = $pdo;
    }

    public function insert(){
        $query = $this->pdo->prepare("INSERT INTO vehicleList (name, brand, model, year, color, price, image_path) 
        VALUES(:name, :brand, :model, :year, :color, :price, :image_path)");

        $query->bindParam(":name",$this->name);
        $query->bindParam(":brand",$this->brand);
        $query->bindParam(":model",$this->model);
        $query->bindParam(":year",$this->year);
        $query->bindParam(":color",$this->color);
        $query->bindParam(":price",$this->price);
        $query->bindParam(":image_path",$this->image_path);

        $query->execute();
    }

    public function edit($id){
        $query = $this->pdo->prepare("UPDATE vehicleList SET name = :name , brand = :brand, model = :model, year = :year, 
        color = :color, price = :price , image_path = :image_path WHERE id = :id");

        $query->bindParam(":name",$this->name);
        $query->bindParam(":brand",$this->brand);
        $query->bindParam(":model",$this->model);
        $query->bindParam(":year",$this->year);
        $query->bindParam(":color",$this->color);
        $query->bindParam(":price",$this->price);
        $query->bindParam(":image_path",$this->image_path);
        $query->bindParam(":id",$id);
        
        $query->execute();
    }

}