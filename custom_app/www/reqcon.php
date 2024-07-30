<?php

use PHPMailer\PHPMailer\PHPMailer;
use PHPMailer\PHPMailer\Exception;

require 'phpmailer/src/Exception.php';
require 'phpmailer/src/PHPMailer.php';
require 'phpmailer/src/SMTP.php';

header('Content-Type: application/json'); // Set content type to JSON

if(isset($_POST["send"])){ 
    // Create a new PHPMailer instance
    $mail = new PHPMailer(true);

    // Configure SMTP settings
    $mail->isSMTP();
    $mail->Host = 'smtp.gmail.com';
    $mail->SMTPAuth = true;
    $mail->Username = '360ithub.developers@gmail.com'; // Your Gmail email address
    $mail->Password = 'vldv ough vzqb yxtq'; 
    $mail->SMTPSecure = 'ssl';
    $mail->Port = 465;

    $mail->setFrom($_POST["email"]); // Sender's email address
    $mail->addAddress('360ithub.developers@gmail.com'); // Your shop's email address

    $mail->isHTML(true);

    // Construct message body
    $message = "<strong>First Name:</strong> " . $_POST["firstName"] . "<br>";
    $message .= "<strong>Last Name:</strong> " . $_POST["lastName"] . "<br>";
    $message .= "<strong>Email:</strong> " . $_POST["email"] . "<br>";
    $message .= "<strong>Phone Number:</strong> " . $_POST["phone"] . "<br>";
    $message .= "<strong>Message:</strong><br>" . nl2br($_POST["message"]);

    $mail->Subject = "Callback Request";
    $mail->Body = $message;

    if ($mail->send()) {  
        echo json_encode(['success' => true]);
    } else {
        echo json_encode(['success' => false, 'error' => $mail->ErrorInfo]);
    }
}
?>
