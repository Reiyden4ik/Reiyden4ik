<?

############# TSkinManager #############
#                                      #
#  By OnericOzelot                     #
#  Special for DevelStudio CE          #
#                                      #
#  ��� �����������, ���������������,   #
#  ��� ������������� ����� ����������, #
#  �� ������� ��������� ���������� ��  #
#  ��� ������, � ��� �� ��������� �    #
#  ������� �����.                      #
#                                      #
########################################

//��������� ���������� ���������� SkinCrafter.dll
//���������� ����� � ������: http://community.develstudio.ru/showthread.php/12197-�����-���-Devel-Studio3

class TSkinManager extends __TNoVisual {

	public $class_name_ex = __CLASS__;

	public function __initComponentInfo(){
		
		$this->visible = false;
		
		self::checkDLL();
		
		self::initClass();
		
		if ($this->skinEnable){
			if (is_file($this->skinPath)){
				LoadSkinFromFile($this->skinPath);
				ApplySkin();
			} else {
				message("���� " . basename($this->skinPath) . " �� ������.\n���� �� ��� ��������.");
			}
		}
		
	}
	
	public function __construct($owner = nil, $init = true, $self = nil){
		parent::__construct($owner, $init, $self);
		
		if ( $init ){
		
			$this->skinEnable = true;
			$this->DSPath = SYSTEM_DIR;
		
		}
	}
	
	function initClass(){
		if (file_exists(DOC_ROOT . "/ext/php_skins.dll")){
			switch(LoadSkinsPHP()){
				case 0:
					alert("������ ������������� ���������� SkinCrafter.dll");
				break;
				case 1:
					InitLicenKeys("SkinCrafter", "DMSoft", "support@skincrafter.com", "RCXKV7Q47VYJTB18D1ET4UEJ8NOBP");
					DefineLanguage(3);
					InitDecoration(1);
				break;
			}
		} else {
			message("��� ������������� ���������� TSkinManager ���������� ���������� ���������� php_skins.dll\n\n���������� ���������� � ������������� ���������.");
		}
	}
	
	function checkDLL(){
		if (!file_exists("MFC71.dll") or !file_exists("msvcr71.dll") or !file_exists("SkinCrafter.dll")){
			$path = $this->DSPath . "utils/TSkinManager";
			if (is_dir($path)){
				copy ($path . "/MFC71.dll", "MFC71.dll");
				copy ($path . "/msvcr71.dll", "msvcr71.dll");
				copy ($path . "/SkinCrafter.dll", "SkinCrafter.dll");
			} else {
				alert("�� ������� ����� � ��������������� ������������ (" . $path . ").");
			}
		}
	}
	
	function openSkin($filename){
		if (LoadSkinsPHP() == 2){
			LoadSkinFromFile($filename);
			ApplySkin();
			$this->skinEnable = true;
		} else {
			self::initClass();
			LoadSkinFromFile($filename);
			ApplySkin();
			$this->skinEnable = true;
		}
	}
	
	function enableSkin(){
		ApplySkin();	
	}
	
	function disableSkin(){
		RemoveSkin();
	}
	

}