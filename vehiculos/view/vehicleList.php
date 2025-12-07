<?php
include("../config/connection.php");

function isMobileDevice() {
    $userAgent = isset($_SERVER['HTTP_USER_AGENT']) ? $_SERVER['HTTP_USER_AGENT'] : '';
    return preg_match("/(android|avantgo|blackberry|bolt|boost|cricket|docomo|fone|hiptop|mini|mobi|palm|phone|pie|tablet|up\.browser|up\.link|webos|wos)/i", $userAgent);
}

$query = $pdo->prepare("SELECT * FROM vehicleList");
$query->execute();
$dataSet = $query->fetchAll(PDO::FETCH_ASSOC);

$commentsQuery = $pdo->prepare("SELECT c.*, v.name as vehicle_name FROM comments c LEFT JOIN vehicleList v ON c.vehicle_id = v.id ORDER BY c.created_at DESC LIMIT 10");
$commentsQuery->execute();
$comments = $commentsQuery->fetchAll(PDO::FETCH_ASSOC);

if (isset($_GET["txtID"])) {
    $id = $_GET["txtID"];
    $delete = $pdo->prepare("DELETE FROM vehicleList WHERE id=:id");
    $delete->bindParam(":id", $id);
    $delete->execute();
    header("Location:vehicleList.php");
}

if (isset($_POST["submit_comment"])) {
    $vehicle_id = $_POST["vehicle_id"];
    $comment = $_POST["comment"];
    $username = !empty($_POST["username"]) ? $_POST["username"] : 'Anonymous';
    
    $insertComment = $pdo->prepare("INSERT INTO comments (vehicle_id, username, comment, created_at) VALUES (:vehicle_id, :username, :comment, NOW())");
    $insertComment->bindParam(":vehicle_id", $vehicle_id);
    $insertComment->bindParam(":username", $username);
    $insertComment->bindParam(":comment", $comment);
    $insertComment->execute();
    
    header("Location:vehicleList.php#preview");
    exit();
}

$isMobile = isMobileDevice();
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
    <title><?php echo $isMobile ? 'Vehicle Gallery' : 'Vehicle Management System'; ?></title>
    <style>
        .comment-box {
            background: #f5f5f5;
            padding: 10px;
            margin: 10px 0;
            border-radius: 8px;
            border-left: 4px solid #1e90ff;
        }
        .comment-header {
            font-weight: bold;
            margin-bottom: 5px;
            color: #333;
        }
        .comment-meta {
            font-size: 0.85em;
            color: #666;
            margin-bottom: 8px;
        }
        .comment-text {
            color: #444;
        }
        .comment-form {
            background: #fff;
            padding: 15px;
            border-radius: 8px;
            margin-top: 15px;
        }
    </style>
</head>

<body>

    <div data-role="page">

        <div data-role="header" data-theme="b">
            <h1><?php echo $isMobile ? 'Vehicle Gallery' : 'Vehicle Management System'; ?></h1>
        </div>

        <div data-role="content">

            <?php if (!$isMobile): ?>
            <div data-role="collapsible" data-collapsed="false" data-theme="b" data-content-theme="b">
                <h3>Insertar vehiculos</h3>
                <div>
                    <form action="../controller/controller.php" method="POST">
                        <input type="hidden" name="id" value="<?php echo isset($id) ? htmlspecialchars($id) : ''; ?>">

                        <div class="ui-grid-b">
                            <div class="ui-block-a">
                                <label for="name">Nombre:</label>
                                <input type="text" name="name" id="name" required>

                                <label for="brand">Marca:</label>
                                <input type="text" name="brand" id="brand" required>

                                <label for="model">Model:</label>
                                <input type="text" name="model" id="model" required>
                            </div>

                            <div class="ui-block-b">
                                <label for="year">Año:</label>
                                <input type="text" name="year" id="year" required>

                                <label for="color">Color:</label>
                                <input type="text" name="color" id="color" required>
                            </div>

                            <div class="ui-block-c">
                                <label for="price">Precio:</label>
                                <input type="number" name="price" id="price" required>

                                <label for="image_path">Imagen:</label>
                                <input type="text" name="image_path" id="image_path" required>
                            </div>
                        </div>

                        <div class="ui-grid-a">
                            <div class="ui-block-a">
                                <button type="submit" name="action" value="insert" data-icon="check" data-theme="b">Guardar Cambios</button>
                            </div>
                            <div class="ui-block-b">
                                <button type="reset" data-icon="delete" data-theme="b">Cancelar</button>
                            </div>
                        </div>
                    </form>
                </div>
            </div>

            <div data-role="collapsible" data-collapsed="false" data-theme="b" data-content-theme="b">
                <h3>Lista Vehiculos</h3>
                <div style="overflow-x:auto;">
                    <table data-role="table" class="ui-responsive table-stroke" data-mode="reflow">
                        <thead>
                            <tr>
                                <th>id</th>
                                <th>name</th>
                                <th>brand</th>
                                <th>model</th>
                                <th>year</th>
                                <th>color</th>
                                <th>price</th>
                                <th>image_path</th>
                                <th>Editar</th>
                                <th>Borrar</th>
                            </tr>
                        </thead>
                        <tbody>
                            <?php foreach ($dataSet as $data): ?>
                                <tr>
                                    <td><?php echo $data["id"] ?></td>
                                    <td><?php echo $data["name"] ?></td>
                                    <td><?php echo $data["brand"] ?></td>
                                    <td><?php echo $data["model"] ?></td>
                                    <td><?php echo $data["year"] ?></td>
                                    <td><?php echo $data["color"] ?></td>
                                    <td><?php echo $data["price"] ?></td>
                                    <td><?php echo $data["image_path"] ?></td>
                                    <td>
                                        <a href="../view/editVehicle.php?txtID=<?php echo $data['id']; ?>"
                                            data-ajax="false"
                                            data-role="button"
                                            data-mini="true"
                                            data-icon="edit"
                                            data-theme="a">Editar</a>
                                    </td>
                                    <td>
                                        <a href="../view/vehicleList.php?txtID=<?php echo $data['id']; ?>"
                                            data-ajax="false"
                                            data-role="button"
                                            data-mini="true"
                                            data-icon="delete"
                                            data-theme="c">Borrar</a>
                                    </td>
                                </tr>
                            <?php endforeach ?>
                        </tbody>
                    </table>
                </div>
            </div>

            <div data-role="collapsible" data-collapsed="false" data-theme="b" data-content-theme="b">
                <h3>Recent Comments</h3>
                <div>
                    <?php if (count($comments) > 0): ?>
                        <?php foreach ($comments as $comment): ?>
                            <div class="comment-box">
                                <div class="comment-header"><?php echo htmlspecialchars($comment['username']); ?></div>
                                <div class="comment-meta">
                                    Vehicle: <?php echo htmlspecialchars($comment['vehicle_name']); ?> | 
                                    <?php echo date('M d, Y H:i', strtotime($comment['created_at'])); ?>
                                </div>
                                <div class="comment-text"><?php echo htmlspecialchars($comment['comment']); ?></div>
                            </div>
                        <?php endforeach; ?>
                    <?php else: ?>
                        <p>No comments yet.</p>
                    <?php endif; ?>
                </div>
            </div>
            <?php endif; ?>

            <div data-role="collapsible" data-collapsed="false" data-theme="b" data-content-theme="b" id="preview">
                <h3><?php echo $isMobile ? 'Nuestros Vehículos' : 'Preview'; ?></h3>
                <div style="display: flex; flex-wrap: wrap; gap: 20px; justify-content: center;">
                    <?php foreach ($dataSet as $data): ?>
                        <div style="flex: 0 1 calc(33.333% - 20px); min-width: 280px;">
                            <div class="ui-body ui-body-b" style="text-align: center; padding: 15px;">
                                <img src="../<?php echo $data["image_path"] ?>" alt="<?php echo htmlspecialchars($data["name"]) ?>" style="max-width:100%; border-radius:15px;">
                                <h4><?php echo $data["name"] ?></h4>
                                <p><strong>Marca:</strong> <?php echo $data["brand"] ?> <strong>Modelo:</strong> <?php echo $data["model"] ?></p>
                                <p><strong>Año:</strong> <?php echo $data["year"] ?></p>
                                <p><strong>Color:</strong> <?php echo $data["color"] ?></p>
                                <p><strong>Precio:</strong> $<?php echo number_format($data["price"], 2) ?></p>
                                
                                <?php if ($isMobile): ?>
                                <div class="comment-form">
                                    <form method="POST" action="vehicleList.php" data-ajax="false">
                                        <input type="hidden" name="vehicle_id" value="<?php echo $data['id']; ?>">
                                        
                                        <label for="username_<?php echo $data['id']; ?>">Tu Nombre (opcional):</label>
                                        <input type="text" name="username" id="username_<?php echo $data['id']; ?>" placeholder="Anonymous">
                                        
                                        <label for="comment_<?php echo $data['id']; ?>">Comentario:</label>
                                        <textarea name="comment" id="comment_<?php echo $data['id']; ?>" required></textarea>
                                        
                                        <button type="submit" name="submit_comment" data-icon="comment" data-theme="b">Enviar Comentario</button>
                                    </form>
                                </div>
                                <?php endif; ?>
                            </div>
                        </div>
                    <?php endforeach; ?>
                </div>
            </div>

        </div>

        <div data-role="footer" data-position="fixed" data-theme="b">
            <h4>Vehicle <?php echo $isMobile ? 'Gallery' : 'CRUD System'; ?> - jQuery Mobile</h4>
        </div>

    </div>

</body>

</html>