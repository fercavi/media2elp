<?php

//file_put_contents ("logServidor.txt","Servidor:" . var_export($_POST ,true) . "\n", FILE_APPEND);
function getUpdateId(){
  $id = -1;
  $file = fopen("id.txt","r");
  $id = fread($file,filesize("id.txt"));
  fclose($file);
  $id = $id + 1;
  $file = fopen("id.txt","w");
  fwrite($file,$id);
  return $id;
}

$command = $_POST["command"];


if (isset($command)){
  if ($command == 'render'){
      $id = getUpdateId();
      echo json_encode(array("collection_id"=>$id,"state"=>"finished"));
      $llibre = var_export($_POST["metabook"],true);
      file_put_contents ($id . ".txt",$llibre,FILE_APPEND);
  }
  if ($command == 'render_status'){
      $id = $_POST["collection_id"];
      echo json_encode(array("state"=>"finished","collection_id"=>$id,"url"=>"http://localhost/prova/" . $id . ".txt"));
  }

}

//echo json_encode(array("state"=>"finished","collection_id"=>"666","url"=>"http://localhost/prova/666.txt"));
//file_put_contents ("logClient.txt","Template:" . json_encode($_POST) . "\n", FILE_APPEND . FILE_USE_INCLUDE_PATH);
?>
