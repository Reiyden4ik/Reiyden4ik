<?php

################################
#                              #
#  HTML Engine class           #
#                              #
#  By OnericOzelot             #
#  Special for DevelStudio CE  #
#                              #
################################

class HTMLEngine {
	
	function start(){
		global $myProject, $_FORMS, $projectFile;
		
		mkdir(dirname($projectFile) . "/html");
		mkdir(dirname($projectFile) . "/html/images");
		foreach ($_FORMS as $form){
			myUtils::saveForm($form);
			self::compileForm(dirname($projectFile) . "/" . $form . ".dfm", dirname($projectFile) . "/html/");
		}
		
		run(dirname($projectFile) . "/html/" . $_FORMS[0] . ".html", false);
		
	}
	
	function compileForm($file, $dir = false){
		$dfm = createForm($file);
		if ($dir){
			//mkdir($dir);
			$hname = $dir . basenameNoExt($file) . ".html";
		} else {
			$hname = basenameNoExt($file) . ".html";
		}
		$fsize = $dfm->font->size + 5;
		$formname = strtolower(basenameNoExt($file));
		$events = eventEngine::$DATA;
		
		file_put_contents($hname, '<html>
			<head>
				<meta http-equiv="Content-Type" content="text/html; charset=windows-1251">
				<title>' . $dfm->caption . '</title>
				<style type="text/css">
				body
				{
					background-color: ' . strtoupper("#" . dechex($dfm->color)) . ';
					color: #000000;
					font-family: ' . $dfm->font->name . ';
					font-size: ' . $fsize . 'px;
					margin: 0;
					padding: 0;
				}
				</style>
			</head>
			<body>
			<form name="' . $formname . '" method="get" action="events.php" enctype="text/plain" target="_self" id="' . $formname . '">');
			
		file_put_contents($dir . "/events.php", "<?php\n\n");

		foreach ($dfm->componentList as $object){
			switch ( get_class($object) ){
				case "TLabel":
					$fsize = $object->fontSize + 5;
					switch ($object->alignment){
						case taLeftJustify:
							$ta = "left";
						break;
						case taRightJustify:
							$ta = "right";
						break;
						case taCenter:
							$ta = "center";
						break;
					}
					$add = '
			<div id="' . $object->name . '" style="position:absolute;left:' . $object->x . 'px;top:' . $object->y . 'px;width:' . $object->w . 'px;height:' . $object->h . 'px;z-index:0;text-align:' . $ta . ';">
			<span style="color:#000000;font-family:' . $object->font->name . ';font-size:' . $fsize . 'px;">' . $object->caption . '</span>
			</div>';
				file_put_contents($hname, file_get_contents($hname) . $add);
				break;
				case "TBitBtn":
					if ($events[$formname][$object->name]["onclick"]){
						//if (!$isEvent){
							$code = 'if (isset($_GET["' . $object->name . '"' . "])){\n" . $events[$formname][$object->name]["onclick"] . "\n}\n";
							file_put_contents($dir . "/events.php", file_get_contents($dir . "/events.php") . $code);
						//}
					}
					$fsize = $object->fontSize + 5;
					$fstyle = $object->font->style;
					$add = '
			<style type="text/css">
			#' . $object->name . '
			{
			   border: 1px #A9A9A9 solid;
			   background-color: #F0F0F0;
			   color: #000000;
			   font-family: ' . $object->font->name . ';';
			   if ($fstyle[0] == fsBold){
						$add .= '
			   font-weight: bold;';
					}
					if ($fstyle[0] == fsItalic){
						$add .= '
			   font-style: italic;';
					}
					$add .= '
			   font-size: ' . $fsize . 'px;
			}
			</style>
			<input type="submit" id="' . $object->name . '" name="' . $object->name . '" value="' . $object->text . '" style="position:absolute;left:' . $object->x . 'px;top:' . $object->y . 'px;width:' . $object->w . 'px;height:' . $object->h . 'px;z-index:0;">';
					file_put_contents($hname, file_get_contents($hname) . $add);
				break;
				case "TLinkLabel":
					$fsize = $object->fontSize + 5;
					switch ($object->alignment){
						case taLeftJustify:
							$ta = "left";
						break;
						case taRightJustify:
							$ta = "right";
						break;
						case taCenter:
							$ta = "center";
						break;
					}
					$add = '
			<div id="' . $object->name . '" style="position:absolute;left:' . $object->x . 'px;top:' . $object->y . 'px;width:250px;height:16px;z-index:0;text-align:' . $ta . ';">
			<span style="color:#000000;font-family:' . $object->font->name . ';font-size:' . $fsize . 'px;"><a href="' . $object->link . '">' . $object->caption . '</a></span>
			</div>';
					file_put_contents($hname, file_get_contents($hname) . $add);
				break;
				case "TEdit":
					$fsize = $object->fontSize + 5;
					$fstyle = $object->font->style;
					$add = '
			<style type="text/css">
			#' . $object->name . '
			{
			   border: 1px #A9A9A9 ';
					if ($object->borderStyle == "bsSingle"){
						$add .= 'solid;';
					} else {
						$add .= 'none;';
					}
					$add .= '
			   background-color: ' . strtoupper("#" . dechex($object->font->color)) . ';
			   color: #000000;
			   font-family: ' . $object->font->name . ';';
					if ($fstyle[0] == fsBold){
						$add .= '
			   font-weight: bold;';
					}
					if ($fstyle[0] == fsItalic){
						$add .= '
			   font-style: italic;';
					}
					$add .= '
			   font-size: ' . $fsize . 'px;
			}
			</style>
			<input type="text" id="' . $object->name . '" name="' . $object->name . '" value="' . $object->text . '" style="position:absolute;left:' . $object->x . 'px;top:' . $object->y . 'px;width:' . $object->w . 'px;height:' . $object->h . 'px;z-index:0;">';
					file_put_contents($hname, file_get_contents($hname) . $add);
				break;
				case "TMemo":
					$fsize = $object->fontSize + 5;
					$fstyle = $object->font->style;
					$add = '
			<style type="text/css">
			#' . $object->name . '
			{
			   border: 1px #A9A9A9 ';
					if ($object->borderStyle == "bsSingle"){
						$add .= 'solid;';
					} else {
						$add .= 'none;';
					}
					$add .= '
			   background-color: ' . strtoupper("#" . dechex($object->font->color)) . ';
			   color: #000000;
			   font-family: ' . $object->font->name . ';';
					if ($fstyle[0] == fsBold){
						$add .= '
			   font-weight: bold;';
					}
					if ($fstyle[0] == fsItalic){
						$add .= '
			   font-style: italic;';
					}
					$add .= '
			   font-size: ' . $fsize . 'px;';
					switch ($object->alignment){
						case "taLeftJustify":
							$add .= '
			   text-align: left;';
						break;
						case "taRightJustify":
							$add .= '
			   text-align: right;';
						break;
						case "taCenter":
							$add .= '
			   text-align: center;';
						break;
					}
					$add .= '
			   resize: none;
			}
			</style>
			<textarea id="' . $object->name . '" name="' . $object->name . '" style="position:absolute;left:' . $object->x . 'px;top:' . $object->y . 'px;width:' . $object->w . 'px;height:' . $object->h . 'px;z-index:0;"';
					if ($object->readOnly){
						$add .= ' readonly';
					}
					$add .= '>'. $object->text . '</textarea>';
					file_put_contents($hname, file_get_contents($hname) . $add);
				break;
				case "TMImage":
					$object->saveToFile($dir . "images/" . $object->name . ".png");
					$add = '
			<style type="text/css">
			#' . $object->name . '
			{
			   border: 0px #000000 solid;
			   left: 0;
			   top: 0;
			   width: 100%;
			   height: 100%;
			}
			</style>
			<div id="' . $object->name . '" style="position:absolute;left:' . $object->x . 'px;top:' . $object->y . 'px;width:' . $object->w . 'px;height:' . $object->h . 'px;z-index:0;">
			<img src="images/' . $object->name . '.png" id="' . $object->name . '" alt=""></div>';
					file_put_contents($hname, file_get_contents($hname) . $add);
				break;
				case "TCheckBox":
					$checked = $object->checked;
					$textx = $object->x + 94;
					$texty = $object->y + 4;
					$add = '
			<input type="checkbox" id="' . $object->name . '" name="' . $object->name . '" value="on" style="position:absolute;left:' . $object->x . 'px;top:' . $object->y . 'px;width:' . $object->w . 'px;height:' . $object->h . 'px;z-index:0;">
			<div id="' . $object->name . 'Text" style="position:absolute;left:' . $textx . 'px;top:' . $texty . 'px;width:250px;height:16px;z-index:0;text-align:' . $ta . ';">
			<span style="color:#000000;font-family:' . $object->font->name . ';font-size:' . $fsize . 'px;">' . $object->text . '</span>
			</div>';
					file_put_contents($hname, file_get_contents($hname) . $add);
				break;
				case "TShape":
					$add = '
			<style type="text/css">
			#' . $object->name . ' {
				width: ' . $object->w . 'px;
				height: ' . $object->h . 'px;
				background: #' . strtoupper(dechex($object->brushColor)) . ';
				border: ' . $object->penWidth . 'px #' . strtoupper(dechex($object->penColor)) . ' solid;
			}
			</style>
			<div id="' . $object->name . '" style="position:absolute;left:100px;top:100px;"></div>';
				file_put_contents($hname, file_get_contents($hname) . $add);
				break;
				default:
					$notCompiled .= " " . $object->name . " (Класс " . get_class($object) . ")\n";
				break;
			}
		}


		file_put_contents($hname, file_get_contents($hname) . '
			</form>
			</body>
		</html>');

		file_put_contents($dir . "/events.php", file_get_contents($dir . "/events.php") . "\n?>");

		if ($notCompiled){
			pre ("Некоторые объекты не были скомпилированы:\n" . $notCompiled . "\nОни не поддерживаются данной версией компилятора в HTML.");
		}
	}
	
}

?>