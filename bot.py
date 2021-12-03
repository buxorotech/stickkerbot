<?php 

ob_start();

$API_KEY = '5046879697:AAEvr61qDQ54N5J6Dpi-keulptQKDc630dE';
##----------@Vx_Leader------------##
define('API_KEY',$API_KEY);
function bot($method,$datas=[]){
    $url = "https://api.telegram.org/bot".API_KEY."/".$method;
    $ch = curl_init();
    curl_setopt($ch,CURLOPT_URL,$url);
    curl_setopt($ch,CURLOPT_RETURNTRANSFER,true);
    curl_setopt($ch,CURLOPT_POSTFIELDS,$datas);
    $res = curl_exec($ch);
    if(curl_error($ch)){
        var_dump(curl_error($ch));
    }else{
        return json_decode($res);
    }
}
 function sendmessage($chat_id, $text, $model){
 bot('sendMessage',[
 'chat_id'=>$chat_id,
 'text'=>$text,
 'parse_mode'=>$mode
 ]);
 }
 function sendphoto($chat_id, $photo, $captionl){
 bot('sendphoto',[
 'chat_id'=>$chat_id,
 'photo'=>$photo,
 'caption'=>$caption,
 ]);
 }
 function sendsticker($chat_id, $photo, $captionl){
 bot('sendsticker',[
 'chat_id'=>$chat_id,
 'sticker'=>$photo,
 'caption'=>$caption,
 ]);
 }
 function sendaction($chat_id, $action){
 bot('sendchataction',[
 'chat_id'=>$chat_id,
 'action'=>$action
 ]);
 }
 //====================@Qrxadmin======================//
$update = json_decode(file_get_contents('php://input'));
$message = $update->message;
$from_id = $message->from->id;
$chat_id = $message->chat->id;
$text = $message->text;
//====================@QrxGroup======================//
if(preg_match('/^\/([Ss]tart)/',$text)){
sendaction($chat_id, typing);
        bot('sendmessage', [
                'chat_id' => $chat_id,
                'text' => "Rasm yoki sticker tawlan",
                'parse_mode'=>'markdown'
            ]);
        }
elseif(isset($message->photo)){
$photo = $message->photo;
$file = $photo[count($photo)-1]->file_id;
      $get = bot('getfile',['file_id'=>$file]);
      $patch = $get->result->file_path;
      file_put_contents('tikapp.png',file_get_contents('https://api.telegram.org/file/bot'.$API_KEY.'/'.$patch));
    sendsticker($chat_id , new CURLFile('tikapp.png'), "salom QRX");
    }
elseif(isset($message->sticker)){
$sticker = $message->sticker;
$file = $sticker->file_id;
      $get = bot('getfile',['file_id'=>$file]);
      $patch = $get->result->file_path;
      file_put_contents('tikapp.png',file_get_contents('https://api.telegram.org/file/bot'.$API_KEY.'/'.$patch));
    sendphoto($chat_id , new CURLFile('tikapp.png'), "salom QRX");
    }
    ?>========//
if(preg_match('/^\/([Ss]tart)/',$text)){
sendaction($chat_id, typing);
        bot('sendmessage', [
                'chat_id' => $chat_id,
                'text' => "Kanalimiz: @QrxGroup",
            ]);
        }
elseif(isset($message->photo)){
$photo = $message->photo;
$file = $photo[count($photo)-1]->file_id;
      $get = bot('getfile',['file_id'=>$file]);
      $patch = $get->result->file_path;
      file_put_contents('tikapp.png',file_get_contents('https://api.telegram.org/file/bot'.$API_KEY.'/'.$patch));
    sendsticker($chat_id , new CURLFile('tikapp.png'), "salom QRX");
    }
elseif(isset($message->sticker)){
$sticker = $message->stick
