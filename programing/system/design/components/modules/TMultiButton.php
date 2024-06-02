<?

//**************************************************//
//********************TMultiButton******************//
//********************By Roman**********************//
//**************************************************//

class TMultiButton extends TLabel{

   public $class_name_ex = __CLASS__;
   function __construct($onwer=nil,$init=true,$self=nil){
   parent::__construct($onwer,$init,$self);
   if ($init){
	    $this->ColorOne = 16763904;
        $this->ColorTwo = 10110244;
		$this->font->color = clWhite;
		$this->font->style = fsBold;
		$this->font->size = 10;
	}
	$this->color = $this->colorOne;
	$this->transparent= false;
	$this->alignment= taCenter;
	$this->autoSize = false;
    $this->layout   =  tlCenter;
	
    }
    public function __initComponentInfo(){
    $this->transparent= false;
	$this->alignment= taCenter;
	$this->autoSize = false;
    $this->layout   =  tlCenter;
	$obj = $this;
	$this->onMouseLeave = function()use($obj){
    $obj->Color = $obj->ColorOne;
	};
	$this->onMouseEnter = function()use($obj){
    $obj->Color = $obj->ColorTwo;
	};
   }
}