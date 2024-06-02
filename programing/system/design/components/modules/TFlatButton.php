<?

//TFlatButton by OnericOzelot
//Class for DevelStudio 4.0

class TFlatButton extends TLabel {

	public $class_name_ex = __CLASS__;
	
		public function set_onMouseDown($v){
	
			event_set($this->self, 'onMouseDown', 'TFlatButton::onMouseDown');
			
    	}
    
    	public function set_onMouseUp($v){
	
			event_set($this->self, 'onMouseUp', 'TFlatButton::onMouseUp');
			
    	}

	public function __initComponentInfo(){

		event_set($this->self, 'onMouseDown', 'TFlatButton::onMouseDown');
		event_set($this->self, 'onMouseUp', 'TFlatButton::onMouseUp');
	
	}
	
	public function __construct($owner = nil, $init = true, $self = nil){
		parent::__construct($owner, $init, $self);
		
		if ( $init ){
		
			$this->caption = "FlatButton";
			$this->fontColor = clWhite;
			$this->color = 10271770;
			$this->pressedColor = 8757270;
			$this->transparent = false;
			$this->alignment = taCenter;
			$this->layout = tlCenter;
		
		}
	}
	
		public static function onMouseDown($self, $button){
		
			if ( !$button ){
				global $oldColor;
				$oldColor = c($self)->color;
				c($self)->color = c($self)->pressedColor;
			}
			
		}
		
		public static function onMouseUp($self, $button){
		
			if ( !$button ){
				global $oldColor;
				c($self)->color = $oldColor;
			}
			
		}
}