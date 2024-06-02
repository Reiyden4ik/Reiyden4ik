<?

$result = array();

$result[] = array(
                  'CAPTION'=>t('Путь до файла записи(.flac)'),
                  'TYPE'=>'text',
                  'PROP'=>'FlacFile',
                  );

$result[] = array(
                  'CAPTION'=>t('Файл синтеза голоса'),
                  'TYPE'=>'text',
                  'PROP'=>'Voice',
                  );

return $result;