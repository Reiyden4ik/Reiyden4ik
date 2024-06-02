<?


class ev_fmNewProject_btn_demos {
    
    function onClick(){
        
        run(dirname(EXE_NAME).'/demos/');
    }
    
}

class ev_fmNewProject_shape2 {
	
	function onMouseDown(){
			global $curX, $curY, $formX, $formY, $fmProjectTimer;
			$curX = cursor_pos_x();
			$curY = cursor_pos_y();
			$formX = c("fmNewProject")->x;
			$formY = c("fmNewProject")->y;
			$code = '
				global $curX, $curY, $formX, $formY;
				c("fmNewProject")->x = $formX - ($curX - cursor_pos_x());
				c("fmNewProject")->y = $formY - ($curY - cursor_pos_y());
			';
			$fmProjectTimer = setTimer(1, $code);
    }
	
	function onMouseUp(){
			global $fmProjectTimer;
			$fmProjectTimer->free();
    }
	
}