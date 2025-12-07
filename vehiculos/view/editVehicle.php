<?php
include("../config/connection.php");
$id = $_GET["txtID"];

if ($id) {

    $select = $pdo->prepare("SELECT * FROM vehicleList WHERE id = :id");

    $select->bindParam(':id', $id);
    $select->execute();
    $dataSet = $select->fetch(PDO::FETCH_ASSOC);

    $name = $dataSet["name"];
    $brand = $dataSet["brand"];
    $model = $dataSet["model"];
    $year = $dataSet["year"];
    $color = $dataSet["color"];
    $price = $dataSet["price"];
    $image_path = $dataSet["image_path"];
}


?>



<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="https://code.jquery.com/mobile/1.4.5/jquery.mobile-1.4.5.min.css">
    <script src="https://code.jquery.com/jquery-1.11.3.min.js"></script>
    <script src="https://code.jquery.com/mobile/1.4.5/jquery.mobile-1.4.5.min.js"></script>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Urbanist:ital,wght@0,100..900;1,100..900&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="../styles/main.css">
    <title>editVehicle</title>
</head>

<body>
    <div data-role="page">
        <div data-role="header" data-theme="b">
            <a href="vehicleList.php" data-icon="back" data-theme="b">Volver</a>
            <h1>Editar Vehiculo</h1>
        </div>

        <div data-role="content">
            <div data-role="collapsible" data-collapsed="false" data-theme="b" data-content-theme="b">
                <h3>Formulario de Edición</h3>
                <form action="../controller/controller.php" method="POST">
                    <input type="hidden" name="id" value="<?php echo htmlspecialchars($id); ?>">

                    <label for="name">Nombre:</label>
                    <input type="text" name="name" id="name" value="<?php echo htmlspecialchars($name); ?>">

                    <label for="brand">Marca:</label>
                    <input type="text" name="brand" id="brand" value="<?php echo htmlspecialchars($brand); ?>">

                    <label for="model">Model:</label>
                    <input type="text" name="model" id="model" value="<?php echo htmlspecialchars($model); ?>">

                    <label for="year">Año:</label>
                    <input type="text" name="year" id="year" value="<?php echo htmlspecialchars($year); ?>">

                    <label for="color">Color:</label>
                    <input type="text" name="color" id="color" value="<?php echo htmlspecialchars($color); ?>">

                    <label for="price">Precio:</label>
                    <input type="number" name="price" id="price" value="<?php echo htmlspecialchars($price); ?>">

                    <label for="image_path">Imagen:</label>
                    <input type="text" name="image_path" id="image_path" value="<?php echo htmlspecialchars($image_path); ?>">

                    <div class="ui-grid-a">
                        <div class="ui-block-a">
                            <button type="submit" name="action" value="update" data-icon="check" data-theme="b">Guardar Cambios</button>
                        </div>
                        <div class="ui-block-b">
                            <button type="reset" data-icon="delete" data-theme="b">Limpiar</button>
                        </div>
                    </div>
                </form>
            </div>
        </div>

        <div data-role="footer" data-position="fixed" data-theme="b">
            <h4>Vehicle CRUD System - jQuery Mobile</h4>
        </div>
    </div>

</body>

</html>