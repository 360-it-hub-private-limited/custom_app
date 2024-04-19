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
    $message = "<strong>Name:</strong> " . $_POST["name"] . "<br>";
    $message .= "<strong>Email:</strong> " . $_POST["email"] . "<br>";
    $message .= "<strong>Mobile Number:</strong> " . $_POST["phone"] . "<br>";
    $message .= "<strong>Message:</strong><br>" . nl2br($_POST["message"]);

    $mail->Subject = "Book A Demo Request from Website";
    // $mail->Subject = "Customer: " . $_POST["phone"];
    $mail->Body = $message;
    $mail->Body = "
    <html>
        <head>
            <style>
                body { font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; color: #333; }
                .container { width: 100%; max-width: 650px; margin: 20px auto; border: 1px solid #ddd; box-shadow: 0 0 10px rgba(0,0,0,0.1); }
                .header { background-color: #ffffff; padding: 20px; text-align: center; }
                .header img { height: 50px; }
                .footer { background-color: #f8f9fa; padding: 15px; text-align: center; font-size: 14px; color: #666; }
                .content { padding: 30px; line-height: 1.6; }
                .content h2 { color: #007bff; }
                .button {
                    background-color: #28a745; 
                    border: none;
                    color: white;
                    padding: 10px 20px;
                    text-align: center;
                    text-decoration: none;
                    display: inline-block;
                    font-size: 16px;
                    border-radius: 5px;
                    margin: 15px 0;
                    cursor: pointer;
                }
                .info-item { margin-bottom: 10px; }
                .info-label { font-weight: bold; }
            </style>
        </head>
        <body>
            <div class='container'>
                <div class='header'>
                    <img src='https://360ithub.com/wp-content/uploads/2023/04/logo.png' alt='Logo' />
                </div>
                <div class='content'>
                    <h2>Contact Information</h2>
                    <div class=\"info-item\"><span class=\"info-label\">Name:</span> {$_POST['name']}</div>
                    <div class=\"info-item\"><span class=\"info-label\">Email:</span> {$_POST['email']}</div>
                    <div class=\"info-item\"><span class=\"info-label\">Mobile Number:</span> {$_POST['phone']}</div>
                    

                    <div class=\"info-item\"><span class=\"info-label\">Message:</span><br>" . nl2br($_POST['message']) . "</div>
                </div>
                <div class='footer'>
                    <p>Thank you for contacting us!</p>
                </div>
            </div>
        </body>
</html>";

    if ($mail->send()) {  
        echo json_encode(['success' => true]);
    } else {
        echo json_encode(['success' => false, 'error' => $mail->ErrorInfo]);
    }
}
?>
