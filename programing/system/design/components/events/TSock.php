<?

$result = array();

$result[] = array(
                  'CAPTION'=>'��������� ����������',
                  'EVENT'=>'OnData',
                  'INFO'=>'%func%($self, $connectionId, $Data, $Type)',
                  'ICON'=>'TSock_Data',
                  );

$result[] = array(
                  'CAPTION'=>'����������� �������',
                  'EVENT'=>'OnConnect',
                  'INFO'=>'%func%($self, $connectionId)',
                  'ICON'=>'TSock_Connect',
                  );

$result[] = array(
                  'CAPTION'=>'���������� �������',
                  'EVENT'=>'OnDisconnect',
                  'INFO'=>'%func%($self, $connectionId)',
                  'ICON'=>'TSock_Disconnect',
                  );



return $result;

?>