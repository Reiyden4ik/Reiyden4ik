<?


class ev_fmOpenDVS_shape2 {
	
	function onMouseDown(){
			global $curX, $curY, $formX, $formY, $fmOpenDVSTimer;
			$curX = cursor_pos_x();
			$curY = cursor_pos_y();
			$formX = c("fmOpenDVS")->x;
			$formY = c("fmOpenDVS")->y;
			$code = '
				global $curX, $curY, $formX, $formY;
				c("fmOpenDVS")->x = $formX - ($curX - cursor_pos_x());
				c("fmOpenDVS")->y = $formY - ($curY - cursor_pos_y());
			';
			$fmOpenDVSTimer = setTimer(1, $code);
    }
	
	function onMouseUp(){
			global $fmOpenDVSTimer;
			$fmOpenDVSTimer->free();
    }
	
}