<?
Class TServer Extends __TNoVisual{
public $class_name_ex = __CLASS__;

Function Check($url){
   $get = @Get_HEADERS($url);
   IF(Preg_Match("/200/i",$get[0]))
   {
    Return "True";
   } Else {
    Return "False";
   }
}

Function Get($url){
 Return File_get_contents($url);
}

Function Put($url,$data,$continue = false){
   $arr = Explode(" | ",$data);
   $arr = implode("&",$arr);
   $arr = str_replace(array("->","-> "," ->"," = "," =","= ","="),"=",$arr);
   $post = "$url?$arr";
   IF($continue == ""){ $continue = true;} else { $continue = $continue; }
   IF($continue == true){File_get_contents($post);}
   Return($post);
}

Function Alternate($fx,$url){
   if($this->alternate == ""){$url = $url;}else{$url = $this->alternate;}
   $fx = base64_encode(base64_encode(base64_encode( $fx )));
   $post = "$url?set=$fx";
   File_get_contents($post);
   Return $post;
}

Public Function __construct($owner=nil,$init=true,$self=nil){
        parent::__construct($owner,$init,$self);}
}