<?
	$GLOBALS["__chromium_allowedcall_push"] = array();
	
	function chromium_allowedcall_push($func)
	{
		if(is_callable($func))
		{
			array_push($GLOBALS["__chromium_allowedcall_push"], $func);
			chromium_allowedcall($GLOBALS["__chromium_allowedcall_push"]);
		}
	}
	
	chromium_allowedcall_push("V8JS::CallVirtual");
	chromium_allowedcall_push("DATA");
	
	Class V8JS
	{
		Protected $Chromium;
		
		Public Function __construct()
		{
			$this->Chromium = new TChromium($GLOBALS[mainForm]);
			$this->Chromium->parent = $GLOBALS[mainForm];
			$this->Chromium->visible = false;
		}
		
		Public Function Execute($Script)
		{
			return @$this->Chromium->executeJS('try { '. $Script .' } catch (e) { alert(e); }');
		}
		
		Public Function ExecuteFile($File)
		{
			IF( file_exists($File) )
				return $this->Execute(@file_get_contents($File));
			return false;
		}
		
		Public Static Function CallVirtual($data)
		{
			$data = json_decode($data);
			if( in_array($data->func, $GLOBALS["__chromium_allowedcall_push"]) && is_callable($data->func) )
				@call_user_func_array($data->func, array(json_decode( $data->data )));
		}
		
		Public Static Function GetAlias($Function)
		{
			if(!is_callable($Function)) return false;
			$alias = 'v8js_' . str_replace(array(',','.'), '', md5( microtime(1).rand(0,1000000000).rand(0,1000000000) ));
			$GLOBALS['__v8js']['func'][$alias] = $Function;
			@eval('function ' . $alias . '(){ $func = $GLOBALS[\'__v8js\'][\'func\'][\''.$alias.'\']; if(is_callable($func)) return @call_user_func_array($func, func_get_args()); return false; }');
			chromium_allowedcall_push($alias);
			return $alias;
		}
		
		Public Function Set($Key, $Value)
		{
			return $this->__set($Key, $Value);
		}
		
		Public Function Get($Key, $Callback)
		{
			$VirtualCallback = self::GetAlias($Callback);
			$VirtualCallback_Result = $VirtualCallback . "_result";
			$this->Execute( $VirtualCallback_Result.' = JSON.stringify('.$Key.'); if('.$VirtualCallback_Result.'[0]==\'"\') '.$VirtualCallback_Result.' = JSON.stringify('.$VirtualCallback_Result.');' );
			$this->Execute( "PHP.call('V8JS::CallVirtual', JSON.stringify( { func: '{$VirtualCallback}', data: {$VirtualCallback_Result} } ) );" );
		}
		
		Public Function __set($Key, $Value)
		{
			IF( is_callable($Value) )
			{
				return $this->Execute( $Key . ' = function(){ var args = Array.prototype.slice.call(arguments); args.unshift( "'. self::GetAlias($Value) .'" ); return PHP.call.apply(null, args); };' );
			}
			ELSE
			{
				return $this->Execute( $Key . ' = ' . json_encode($Value) . ';' );
			}
		}
		
		Public Function __destruct()
		{
			$this->Chromium->free();
		}
	}
?>