<?php
//header("Content-type: application/json");
$curl = curl_init();

curl_setopt($curl, CURLOPT_URL,"https://balneabilidade.ima.sc.gov.br/relatorio/historico");
curl_setopt($curl, CURLOPT_POST, 1);
curl_setopt($curl, CURLOPT_POSTFIELDS, "municipioID=24&localID=40&ano=2019&redirect=true");

curl_setopt($curl, CURLOPT_SSL_VERIFYHOST, false);
curl_setopt($curl, CURLOPT_SSL_VERIFYPEER, false);

curl_setopt($curl, CURLOPT_RETURNTRANSFER, true);

$html = curl_exec($curl);
$erro = curl_error($curl); 

echo $html;