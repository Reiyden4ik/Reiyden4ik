<?

$result = array();

$result[] = array(
                  'CAPTION'=>t('File name'),
                  'TYPE'=>'text',
                  'PROP'=>'skinPath',
                  );
				  
$result[] = array(
                  'CAPTION'=>t('DevelStudio path'),
                  'TYPE'=>'text',
                  'PROP'=>'DSPath',
                  );
				  
$result[] = array(
                  'CAPTION'=>t('Enable skin'),
                  'TYPE'=>'check',
                  'PROP'=>'skinEnable',
                  );

return $result;