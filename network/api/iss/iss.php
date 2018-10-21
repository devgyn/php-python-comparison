<?php

// API Request example in PHP

$req = file_get_contents('http://api.open-notify.org/iss-pass.json?lat=44.6134227&lon=1.1366893');
$api = json_decode($req);

if ($api->message == 'success') {

	foreach ($api->response as $issRes)
		        {
		$issDuration = round($issRes->duration / 60) . ' minutes';
		$issDate = date('Y-m-d H:i:s', $issRes->risetime);
		
		echo "
            	Duration: $issDuration \n
            	Date: $issDate\n
		==============================\n
		";
    }

}

