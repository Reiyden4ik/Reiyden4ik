<?

$result = array();

$result[] = array(
                  'CAPTION'=>t('LoadFromFile'),
                  'PROP'=>'LoadFromFile',
                  'INLINE'=>'LoadFromFile ( $file )',
                  );

$result[] = array(
                  'CAPTION'=>t('saveToFile'),
                  'PROP'=>'saveToFile',
                  'INLINE'=>'saveToFile ( $file )',
                  );

return $result;