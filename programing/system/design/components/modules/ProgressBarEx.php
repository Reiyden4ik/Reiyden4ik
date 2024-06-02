<?

//**************************************************//
//********************ProgressBarEx2.2**************//
//********************By Roman**********************//
//**************************************************//

class ProgressBarEx extends TScrollBox{

   public $class_name_ex = __CLASS__;
   function __construct($onwer=nil,$init=true,$self=nil){
    parent::__construct($onwer,$init,$self);
	if ($init){
      $this->ColorOne;
	  $this->proc = true;
	  $this->image = false;
	  $this->rand = rand(0, 9999);
   }
	}
	public function __initComponentInfo(){
	 global $image, $color, $label, $yes, $file;
	 $this->doubleBuffered = true;
	 $this->autoScroll = false;
	 $this->borderStyle = bsNone;
	 $this->text = '';
	 $this->parent = $this->parent;
	 if ($this->image == true){  
	 $image[$this->rand] = new TMImage;
	 $image[$this->rand]->parent = $this;
	 $image[$this->rand]->h = $this->h + 1;
	 $image[$this->rand]->w = 0;
	 $image[$this->rand]->y = 0;
	 $image[$this->rand]->autoSize = false;
	 $image[$this->rand]->mosaic = true;
	 $image[$this->rand]->proportional = false;
	 }else{
	 $image[$this->rand] = new TShape;
	 $image[$this->rand]->parent = $this;
	 $image[$this->rand]->h = $this->h + 1;
	 $image[$this->rand]->w = 0;
	 $image[$this->rand]->x = 0;
	 $image[$this->rand]->y = 0;
     $image[$this->rand]->brushColor = $this->ColorOne;
	 $image[$this->rand]->penStyle = psClear;
	 }
	 $label[$this->rand] = new TLabel;
	 if ($this->proc == true){
	 $label[$this->rand]->caption = '0%';
	 }
	 $label[$this->rand]->align = alClient;
	 $label[$this->rand]->parent = $this;
	 $label[$this->rand]->alignment = taCenter;
	 $label[$this->rand]->layout = tlCenter;
	 $label[$this->rand]->font->color = $this->font->color;
	 $label[$this->rand]->font->style = $this->font->style;
	 $label[$this->rand]->font->size = $this->font->size;
	 }
    public function load_image( $filel ){
	global $file, $yes;
	  $file = $filel;
	  return $file;
	}
    public function progress($max, $pos){
	 global $image, $label, $file;
	 err_no();
	 if ($this->image == true){
	 $image[$this->rand]->loadFromFile( $file );
	 }
	 $this->doubleBuffered = true;
	 $this->borderStyle = bsNone;
	 $w = $this->w;
     $x = $pos;
     $y = $w;
     $t = $max;
     $pr = $y*$x/$t;
     $pr = floor($pr);
	 $cv = new TControlCanvas( $image );
     $image[$this->rand]->w = $pr;
	 $cv = new TControlCanvas( $image );
	 if ($this->end == true){
	   if ($max == $pos){
	 $image[$this->rand]->w = 0;
	 }
	 }
	 if ($this->proc == true){
	 $x = $pos;
     $y = 100;
     $t = $max;
     $pr = $y*$x/$t;
     $pr = floor($pr);
     $label[$this->rand]->caption = "$pr%";
	 if ($max == $pos){
	 $cv = new TControlCanvas( $image );
	 $cv = new TControlCanvas( $image );
	 if ($this->end == true){
	 $label[$this->rand]->caption = "0%";
	 }
	 }
	 }
    }
}