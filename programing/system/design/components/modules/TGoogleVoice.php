<?
#########################               
#component TGoogleVoise##
#Avtor = Max95         ##
#Ver.  = 1.0           ##
#########################
///////////Божественный костыль с переменными GLOBAL/////////
$GLOBALS['FileFlac'];//Путь до Flac файла
$GLOBALS['TextVoice'];//Сюда пишем распознанный текст
///////Спасибо Denfer'у за класс Thread/////////////
 Class Thread
{
    Public $self;
    Protected $Thread;
    
   
    
    Public Function __construct()
    {
        $this->self = strtoupper(uniqid());
        
        $this->Thread = new TThread;
        $this->Thread->onExecute = 'Thread::_Execute';
        $this->Thread->_self = $this;
        
        $GLOBALS['___thread'][$this->self] = $this;
    }
    
    Public Function __destruct()
    {
        $this->Stop();
    }
    
    Function __set($Key, $Value)
    {
        $this->Thread->{$Key} = $Value;
    }
    
    Function __get($Key)
    {
        return $this->Thread->{$Key};
    }
    
    Static Function _Execute($Pointer)
    {
        $thread = TThread::get($Pointer);
        $self = $thread->_self;
        $self->Execute($Pointer);
    }
    
    Function Execute($Pointer)
    {
        IF( $Pointer != NULL )
        {
            $self = TThread::get($Pointer);
            $Func = Array( $this, OnExecute );
            IF( is_callable( $Func ) )
                return @call_user_func ( $Func );
        }
        return null;
    }
    
    Public Function Start()
    {
        $this->Thread->resume();
    }
    
    Public Function Pause()
    {
        $this->Suspend();
    }
    
    Public Function Stop()
    {
        $this->Pause();
        $this->Terminate();
        $this->Free();
    }
    
    Public Function Suspend()
    {
        $this->Thread->suspend();
    }
    
    Public Function Terminate()
    {
        $this->Thread->terminate();
    }
    
    Public Function Free()
    {
        $this->Thread->free();
    }
    
    Public Function OnExecute(){}
}

///Отправляем данные в поток
function GetFile()
  { 
    return $GLOBALS['FileFlac'] ;
  }
///Вывод из потока
function GetVoise($Voise)
  { 
   $GLOBALS['TextVoise'] = $Voise;

  }





class ThreadFileWritter extends Thread
{
   
    
    function OnExecute(){
	
	
	$res = syncEx('GetFile', array());
	$flac = file_exists($res);
    
     if(!$flac){sync('GetVoise', array('File error'));}
        else
             {
      
       
      $file = file_get_contents(getFileName($res));
      $socket = fsockopen('www.google.com', 80, $errno, $errstr, 30);
      fwrite($socket, "POST /speech-api/v1/recognize?xjerr=1&client=chromium&lang=ru-RU HTTP/1.1\r\n");
      fwrite($socket, "Host: www.google.com\r\n");
      fwrite($socket,"Content-Type: audio/x-flac; rate=16000\r\n");
      fwrite($socket,"Content-length:".strlen($file)."\r\n");
      fwrite($socket,"Connection:Close\r\n");
      fwrite($socket,"\r\n");
      fwrite($socket,"$file\r\n");
      fwrite($socket,"\r\n");
    for ($i = 1; $i <= 13; $i++)
        {
        $s = fgets($socket,512);
        $r[] = $s;
        }
         
         $res = json_decode($r[12])->hypotheses[0]->utterance;
         $res = iconv("utf-8", "windows-1251", $res);
         sync('GetVoise', array($res));
              }
     
 
 
    }
}

//Автор Max95 v1.0
class TGoogleVoice extends __TNoVisual {
    
    public $class_name_ex = __CLASS__;
    
    
    
    public function __inspectProperties(){
	
	return array('FlacFile', 'Voice');//свойства
    }
    
    public function __initComponentInfo(){
        
        parent::__initComponentInfo();
	
       
          
          
    }
    
    public function __construct($onwer=nil,$init=true,$self=nil){
	parent::__construct($onwer, $init, $self);
	
        if ($init)
	{
	   
           
           
	}
    }
     
    ///распознаём голос
    public function VoiceRecognition()
    {
        $GLOBALS['TextVoice'] = 'Loading';
	$GLOBALS['FileFlac'] = $this->FlacFile;
	
        $GetVoise = new ThreadFileWritter;//Создаём поток
	$GetVoise->Start();
    }
    
    
    public function TextVoice() {return $GLOBALS['TextVoise'];}  // возвращаем в ДС
    
    //синтез речи Русский(Ж)
    public function Text_to_speech($text)
    {
  $uagent = "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/15.0.872.0 Safari/535.2";
  $text = iconv('cp1251','utf-8',$text);
  $url= 'http://translate.google.com/translate_tts?tl=ru&q='.urlencode($text).'';
  $ch = curl_init( $url );
  curl_setopt($ch, CURLOPT_URL, $url);
  curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
  curl_setopt($ch, CURLOPT_HEADER, 0);
  curl_setopt($ch, CURLOPT_FOLLOWLOCATION, 1);
  curl_setopt($ch, CURLOPT_ENCODING, "");
  curl_setopt($ch, CURLOPT_USERAGENT, $uagent);
  curl_setopt($ch, CURLOPT_CONNECTTIMEOUT, 120);
  curl_setopt($ch, CURLOPT_TIMEOUT, 120);
  curl_setopt($ch, CURLOPT_MAXREDIRS, 10);
  $content = curl_exec( $ch );
  file_put_contents( $this->Voice ,  $content );
  
  curl_close( $ch );
	
    }
    
    public function Rec_Flac_File()
    {
	shell_exec("rec.exe -q -c 1 -r 16000 zapis.flac");
    }
    
    public function StopRec_Flac_File()
    {
	shell_exec("TASKKILL /F /IM rec.exe");  
    }
    
    
}


?>



