<?

$result = array();

$result[] = array(
                  'CAPTION'=>'FindWindow',
                  'PROP'=>'FindWindow()',
                  'INLINE'=>'FindWindow ( char WindowName ) - ����� ���� �� ���������.',
                  );

$result[] = array(
                  'CAPTION'=>'AnimateWindow',
                  'PROP'=>'AnimateWindow()',
                  'INLINE'=>'AnimateWindow ( int hWnd, int dwTime, int dwFlags ) - �������� ����.',
                  );
				 
$result[] = array(
                  'CAPTION'=>'ArrangeIconicWindows',
                  'PROP'=>'ArrangeIconicWindows()',
                  'INLINE'=>'ArrangeIconicWindows ( int hWnd ) - ������������� ��� ���������������� (� ���� ������) ���� ���������� ������������� ����.',
                  );
				  
$result[] = array(
                  'CAPTION'=>'BringWindowToTop',
                  'PROP'=>'BringWindowToTop()',
                  'INLINE'=>'BringWindowToTop ( int hWnd ) - ���������� ���� �� �������� ���� � ������������ ���',
                  );				  
				  
$result[] = array(
                  'CAPTION'=>'ChildWindowFromPoint',
                  'PROP'=>'ChildWindowFromPoint()',
                  'INLINE'=>'ChildWindowFromPoint ( int hWndParent, int X, int Y ) - ����������, ����� �� �������� ���� �������� ��������� ����������.',
                  );	
				  
$result[] = array(
                  'CAPTION'=>'ChildWindowFromPointEx',
                  'PROP'=>'ChildWindowFromPointEx()',
                  'INLINE'=>'ChildWindowFromPointEx ( int hWndParent, int X, int Y [, int uFlags = CWP_ALL] ) - ����������, ����� �� �������� ���� �������� ��������� ����������.',
                  );	

$result[] = array(
                  'CAPTION'=>'CloseWindow',
                  'PROP'=>'CloseWindow()',
                  'INLINE'=>'CloseWindow ( int hWnd ) - ������������ ��������� ����.',
                  );	

$result[] = array(
                  'CAPTION'=>'DestroyWindow',
                  'PROP'=>'DestroyWindow()',
                  'INLINE'=>'DestroyWindow ( int hWnd ) - ��������� ��������� ���� (�� �� ��������� ����������.',
                  );
				  
$result[] = array(
                  'CAPTION'=>'EnableWindow',
                  'PROP'=>'EnableWindow()',
                  'INLINE'=>'EnableWindow ( int hWnd, bool bEnable ) - ��������� ��� ��������� ���� � ���� � � ���������� � ����.',
                  );	
				  
$result[] = array(
                  'CAPTION'=>'GetActiveWindow',
                  'PROP'=>'GetActiveWindow()',
                  'INLINE'=>'GetActiveWindow ( void ) - ���������� ���������� ��������� ����.',
                  );

$result[] = array( 
                  'CAPTION'=>'GetAncestor',
                  'PROP'=>'GetAncestor()',
                  'INLINE'=>'GetAncestor ( int hWnd [, int gaFlags = GA_PARENT] ) - ���������� ���������� �������� ��������� ����.',
                  );

$result[] = array( 
                  'CAPTION'=>'SetWindowPos',
                  'PROP'=>'SetWindowPos()',
                  'INLINE'=>'SetWindowPos ( int hWnd, int hWndInsertAfter, int X, int Y, int W, int H, int uFlags ) - �������� p����p, ��������� � ��p���� ����.',
                  );				  

$result[] = array( 
                  'CAPTION'=>'GetDesktopWindow',
                  'PROP'=>'GetDesktopWindow()',
                  'INLINE'=>'GetDesktopWindow ( void ) - ���������� ���������� �������� �����.',
                  );	

$result[] = array( 
                  'CAPTION'=>'GetFocus',
                  'PROP'=>'GetFocus()',
                  'INLINE'=>'GetFocus ( void ) - ���������� ����, �� ������� ���������� �����.',
                  );
				  
$result[] = array(
                  'CAPTION'=>'GetForegroundWindow',
                  'PROP'=>'GetForegroundWindow()',
                  'INLINE'=>'GetForegroundWindow ( void ) - ���������� ������������� ����',
                  );
				  
$result[] = array(
                  'CAPTION'=>'GetLastActivePopup',
                  'PROP'=>'GetLastActivePopup()',
                  'INLINE'=>'GetLastActivePopup ( int hWnd ) - ���������� ���������� ������������ ����, ������� ���� �������� ��������� ���, ���������� �������� �������� ��������� ����.',
                  );
				  
$result[] = array(
                  'CAPTION'=>'GetLayeredWindowAttributes',
                  'PROP'=>'GetLayeredWindowAttributes()',
                  'INLINE'=>'GetLayeredWindowAttributes ( int hWnd ) - ���������� �������� ������������� ����.',
                  );				  
				  
$result[] = array(
                  'CAPTION'=>'GetShellWindow',
                  'PROP'=>'GetShellWindow()',
                  'INLINE'=>'GetShellWindow ( void ) - ���������� ���������� �������� Windows.',
                  );	

$result[] = array(
                  'CAPTION'=>'GetSysColor',
                  'PROP'=>'GetSysColor()',
                  'INLINE'=>'GetSysColor ( int nIndex ) - ���������� ����� ��������� Windows.',
                  );

$result[] = array(
                  'CAPTION'=>'GetTopWindow',
                  'PROP'=>'GetTopWindow()',
                  'INLINE'=>'GetTopWindow ( int hWnd ) - ���������� ���������� ��������� ���� �������� ������, ���������� ����.',
                  );

$result[] = array(
                  'CAPTION'=>'GetWindow',
                  'PROP'=>'GetWindow()',
                  'INLINE'=>'GetWindow ( int hWnd, int wCmd ) - ���������� ���������� ����, ������� ����� ��������� ��������� � ��������� ����.',
                  );
				  
$result[] = array(
                  'CAPTION'=>'GetWindowLong',
                  'PROP'=>'GetWindowLong()',
                  'INLINE'=>'GetWindowLong ( int hWnd , int nIndex ) - ���������� ������������ ���������� �� ��������� ����.',
                  );

$result[] = array(
                  'CAPTION'=>'GetWindowRect',
                  'PROP'=>'GetWindowRect()',
                  'INLINE'=>'GetWindowRect ( int hWnd ) - ���������� ������� ��������������� �������������� ���������� ����.',
                  );
				  
$result[] = array(
                  'CAPTION'=>'GetClientRect',
                  'PROP'=>'GetClientRect()',
                  'INLINE'=>'GetClientRect ( int hWnd ) - ���������� ���������� ���������� ������� ����.',
                  );				    
				  	   
$result[] = array(
                  'CAPTION'=>'SwitchToThisWindow',
                  'PROP'=>'SwitchToThisWindow()',
                  'INLINE'=>'SwitchToThisWindow ( int hWnd , int fAltTab ) - ����������� ����� �� ��������� ���� � ��������� ��� �� �������� ����.',
                  );				  
				  
$result[] = array(
                  'CAPTION'=>'IsChild',
                  'PROP'=>'IsChild()',
                  'INLINE'=>'IsChild ( int hWndParent, int hWnd ) - ���������, �������� �� ��������� ���� hWnd �������� ����� ��� hWndParent.',
                  );
				  
$result[] = array(
                  'CAPTION'=>'IsGUIThread',
                  'PROP'=>'IsGUIThread()',
                  'INLINE'=>'IsGUIThread ( [int bConvert = false] ) - ���������, �������� �� ���������� ����� ������� GUI.',
                  );					  
				  
$result[] = array(
                  'CAPTION'=>'IsHungAppWindow',
                  'PROP'=>'IsHungAppWindow()',
                  'INLINE'=>'IsHungAppWindow ( int hWnd ) - ���������, ������� �� �������, ��� ��������� ���� �� ��������.',
                  );					  
				  				  
$result[] = array(
                  'CAPTION'=>'IsIconic',
                  'PROP'=>'IsIconic()',
                  'INLINE'=>'IsIconic ( int hWnd ) - ���������, �������� �� ��������� ���� ����������������.',
                  );								  
				  
$result[] = array(
                  'CAPTION'=>'IsWindow',
                  'PROP'=>'IsWindow()',
                  'INLINE'=>'IsWindow ( int hWnd ) - ���������, ���������� �� ���� � ��������� ����������.',
                  );	
				  
$result[] = array(
                  'CAPTION'=>'IsWindowEnabled',
                  'PROP'=>'IsWindowEnabled()',
                  'INLINE'=>'IsWindowEnabled ( int hWnd ) - ���������, �������� �� ��������� ���� ��������� ��� ����� ���������� � ���� � ����������.',
                  );		
				  
$result[] = array(
                  'CAPTION'=>'IsWindowUnicode',
                  'PROP'=>'IsWindowUnicode()',
                  'INLINE'=>'IsWindowUnicode ( int hWnd ) - ���������, �������� �� ��������� ���� ����� Unicode.',
                  );				  
				  
$result[] = array(
                  'CAPTION'=>'IsWindowVisible',
                  'PROP'=>'IsWindowVisible()',
                  'INLINE'=>'IsWindowVisible ( int hWnd ) - ���������, �������� �� ��������� ���� �������.',
                  );					  
				  
$result[] = array(
                  'CAPTION'=>'IsZoomed',
                  'PROP'=>'IsZoomed()',
                  'INLINE'=>'IsZoomed ( int hWnd ) - ���������, ��������������� �� ��������� ����.',
                  );					  
				  
$result[] = array(
                  'CAPTION'=>'LockSetForegroundWindow',
                  'PROP'=>'LockSetForegroundWindow()',
                  'INLINE'=>'LockSetForegroundWindow ( bool uLockCode ) - ��������� ��� ��������� ����� ������� SetForegroundWindow( void ).',
                  );	
				  
$result[] = array(
                  'CAPTION'=>'MoveWindow',
                  'PROP'=>'MoveWindow()',
                  'INLINE'=>'MoveWindow ( int hWnd, int X, int Y, int W, int H [, bool bRepaint = true] ) - �������� ��������� � ������� ���������� ����.',
                  );
				  
$result[] = array(
                  'CAPTION'=>'OpenIcon',
                  'PROP'=>'OpenIcon()',
                  'INLINE'=>'OpenIcon ( int hWnd ) - ��������������� ���������������� ���� � ��� ���������� �������� � ���������, ����� ������������ ���.',
                  );				  
				  
$result[] = array(
                  'CAPTION'=>'SetActiveWindow',
                  'PROP'=>'SetActiveWindow()',
                  'INLINE'=>'SetActiveWindow ( int hWnd ) - ������������ ��������� ����.',
                  );					  
				  
$result[] = array(
                  'CAPTION'=>'SetFocus',
                  'PROP'=>'SetFocus()',
                  'INLINE'=>'SetFocus ( int hWnd ) - ������������� ����� ���������� � ��������� ����.',
                  );					  
				  
$result[] = array(
                  'CAPTION'=>'SetForegroundWindow',
                  'PROP'=>'SetForegroundWindow()',
                  'INLINE'=>'SetForegroundWindow ( int hWnd ) - ������� �����, ��������� ��������� ����, �� �������� ���� � ������������ ����.',
                  );					  
				  
$result[] = array(
                  'CAPTION'=>'SetLayeredWindowAttributes',
                  'PROP'=>'SetLayeredWindowAttributes()',
                  'INLINE'=>'SetLayeredWindowAttributes ( int hWnd, int crKey, int bAlpha, int dwFlags ) - ������������� �������� ������������� ����.',
                  );					  
				  
$result[] = array(
                  'CAPTION'=>'SetParent',
                  'PROP'=>'SetParent()',
                  'INLINE'=>'SetParent ( int hWndChild, int hWndNewParent ) - ������ ������������ ���� ���������� ��������� ����.',
                  );	
				  
$result[] = array(
                  'CAPTION'=>'SetSysColors',
                  'PROP'=>'SetSysColors()',
                  'INLINE'=>'SetSysColors ( int cElements, array lpaElements, array lpaRgbValues ) - ������������� ����� ��� ������ ��� ���������� ��������� ����������.',
                  );				  
				  
$result[] = array(
                  'CAPTION'=>'SetWindowLong',
                  'PROP'=>'SetWindowLong()',
                  'INLINE'=>'SetWindowLong ( int hWnd, int dwNewLong [, int nIndex = GWL_EXSTYLE] ) - ������������� ������������ ������� ��� ���������� ����.',
                  );				  
				  
$result[] = array(
                  'CAPTION'=>'SetWindowText',
                  'PROP'=>'SetWindowText()',
                  'INLINE'=>'SetWindowText ( int hWnd, str lpString ) -["��������"] �������� ��������� ���������� ���� ��� ����� �p���� ��p�������.',
                  );				  
				  
$result[] = array(
                  'CAPTION'=>'ShowOwnedPopups',
                  'PROP'=>'ShowOwnedPopups()',
                  'INLINE'=>'ShowOwnedPopups ( int hWnd [, fShow = true] ) - ���������� ��� �������� ��� ����������� ����, �������� ������� ��������� ����.',
                  );
				  
$result[] = array(
                  'CAPTION'=>'ShowWindow',
                  'PROP'=>'ShowWindow()',
                  'INLINE'=>'ShowWindow ( int hWnd [, int nCmdShow = SW_SHOW] ) - ���������� �������� ���� � ��������� ������.',
                  );					  
				  
$result[] = array(
                  'CAPTION'=>'ShowWindowAsync',
                  'PROP'=>'ShowWindowAsync()',
                  'INLINE'=>'ShowWindowAsync ( int hWnd [, int nCmdShow = SW_SHOW] ) - ���������� �������� ���� � ��������� ������, ��������� ������ �������.',
                  );					  
				  
$result[] = array(
                  'CAPTION'=>'WindowFromCursor',
                  'PROP'=>'WindowFromCursor()',
                  'INLINE'=>'WindowFromCursor ( void ) - ����������, ����� �� ���� �������� ���������� �������.',
                  );					  
				  
$result[] = array(
                  'CAPTION'=>'WindowFromPoint',
                  'PROP'=>'WindowFromPoint()',
                  'INLINE'=>'WindowFromPoint ( int X, int Y ) - ����������, ����� �� ���� �������� ��������� ����������.',
                  );				  
///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////				  
$result[] = array(
                  'CAPTION'=>'Write',
                  'PROP'=>'Write()',
                  'INLINE'=>'Write ( int hWnd, char Text ) - ������������ ���� � ����� ��������� �����.',
                  );















				  

				  

return $result;