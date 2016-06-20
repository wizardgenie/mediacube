import urllib , urllib2 , re , xbmcplugin , xbmcgui , xbmc , xbmcaddon
import os , sys , time , xbmcvfs , glob , shutil , datetime , zipfile , ntpath
import subprocess , threading
import yt , downloader , checkPath
import binascii
import hashlib
import speedtest
if 64 - 64: i11iIiiIii
try :
 from sqlite3 import dbapi2 as database
 if 65 - 65: O0 / iIii1I11I1II1 % OoooooooOO - i1IIi
except :
 from pysqlite2 import dbapi2 as database
 if 73 - 73: II111iiii
from addon . common . addon import Addon
from addon . common . net import Net
if 22 - 22: I1IiiI * Oo0Ooo / OoO0O00 . OoOoOO00 . o0oOOo0O0Ooo / I1ii11iIi11i
######################################################
I1IiI = 'plugin.program.mediacube'
o0OOO = 'MediaCube Wizard'
if 13 - 13: ooOo + Oo
o0O = xbmcaddon . Addon ( id = I1IiI )
zip = o0O . getSetting ( 'zip' )
IiiIII111iI = o0O . getSetting ( 'localcopy' )
IiII = o0O . getSetting ( 'private' )
iI1Ii11111iIi = o0O . getSetting ( 'reseller' )
i1i1II = o0O . getSetting ( 'openelec' )
O0oo0OO0 = o0O . getSetting ( 'favourites' )
I1i1iiI1 = o0O . getSetting ( 'sources' )
iiIIIII1i1iI = o0O . getSetting ( 'repositories' )
o0oO0 = o0O . getSetting ( 'mastercopy' )
oo00 = o0O . getSetting ( 'username' ) . replace ( ' ' , '%20' )
o00 = o0O . getSetting ( 'password' )
Oo0oO0ooo = o0O . getSetting ( 'versionoverride' )
o0oOoO00o = o0O . getSetting ( 'login' )
i1 = o0O . getSetting ( 'addonportal' )
oOOoo00O0O = o0O . getSetting ( 'maintenance' )
i1111 = o0O . getSetting ( 'hardwareportal' )
i11 = o0O . getSetting ( 'maintenance' )
I11 = o0O . getSetting ( 'latestnews' )
Oo0o0000o0o0 = o0O . getSetting ( 'tutorialportal' )
oOo0oooo00o = o0O . getSetting ( 'startupvideo' )
oO0o0o0ooO0oO = o0O . getSetting ( 'startupvideopath' )
oo0o0O00 = o0O . getSetting ( 'wizardurl1' )
oO = o0O . getSetting ( 'wizardname1' )
i1iiIIiiI111 = o0O . getSetting ( 'wizardurl2' )
oooOOOOO = o0O . getSetting ( 'wizardname2' )
i1iiIII111ii = o0O . getSetting ( 'wizardurl3' )
i1iIIi1 = o0O . getSetting ( 'wizardname3' )
ii11iIi1I = o0O . getSetting ( 'wizardurl4' )
iI111I11I1I1 = o0O . getSetting ( 'wizardname4' )
OOooO0OOoo = o0O . getSetting ( 'wizardurl5' )
iIii1 = o0O . getSetting ( 'wizardname5' )
oOOoO0 = xbmcgui . Dialog ( )
O0OoO000O0OO = xbmcgui . DialogProgress ( )
iiI1IiI = xbmc . translatePath ( 'special://home/' )
II = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
ooOoOoo0O = xbmc . translatePath ( os . path . join ( II , 'addon_data' ) )
OooO0 = xbmc . translatePath ( os . path . join ( II , 'Database' ) )
II11iiii1Ii = xbmc . translatePath ( os . path . join ( II , 'Thumbnails' ) )
OO0o = xbmc . translatePath ( os . path . join ( 'special://home' , 'addons' , '' ) )
Ooo = xbmc . translatePath ( os . path . join ( OO0o , I1IiI , 'default.py' ) )
O0o0Oo = xbmc . translatePath ( os . path . join ( OO0o , I1IiI , 'fanart.jpg' ) )
Oo00OOOOO = xbmc . translatePath ( os . path . join ( OO0o , I1IiI , 'resources' , 'addonxml' ) )
O0O = xbmc . translatePath ( os . path . join ( II , 'guisettings.xml' ) )
O00o0OO = xbmc . translatePath ( os . path . join ( II , 'guifix.xml' ) )
I11i1 = xbmc . translatePath ( os . path . join ( OO0o , I1IiI , 'icon.png' ) )
iIi1ii1I1 = xbmc . translatePath ( os . path . join ( II , 'favourites.xml' ) )
o0 = xbmc . translatePath ( os . path . join ( II , 'sources.xml' ) )
I11II1i = xbmc . translatePath ( os . path . join ( II , 'advancedsettings.xml' ) )
IIIII = xbmc . translatePath ( os . path . join ( II , 'profiles.xml' ) )
ooooooO0oo = xbmc . translatePath ( os . path . join ( II , 'RssFeeds.xml' ) )
IIiiiiiiIi1I1 = xbmc . translatePath ( os . path . join ( II , 'keymaps' , 'keyboard.xml' ) )
I1IIIii = xbmc . translatePath ( os . path . join ( zip ) )
oOoOooOo0o0 = xbmc . translatePath ( os . path . join ( I1IIIii , 'Community Builds' , '' ) )
OOOO = xbmc . translatePath ( os . path . join ( ooOoOoo0O , I1IiI , 'startup.xml' ) )
OOO00 = xbmc . translatePath ( os . path . join ( ooOoOoo0O , I1IiI , 'temp.xml' ) )
iiiiiIIii = xbmc . translatePath ( os . path . join ( ooOoOoo0O , I1IiI , 'id.xml' ) )
O000OO0 = xbmc . translatePath ( os . path . join ( OO0o , 'plugin.program.tbs' ) )
I11iii1Ii = xbmc . translatePath ( os . path . join ( OO0o , 'repository.totalinstaller' ) )
I1IIiiIiii = xbmc . translatePath ( os . path . join ( OO0o , 'repository.totalrevolution' ) )
O000oo0O = xbmc . translatePath ( os . path . join ( OO0o , 'plugin.program.totalrevolution' ) )
OOOOi11i1 = xbmc . translatePath ( os . path . join ( ooOoOoo0O , I1IiI , 'idtemp.xml' ) )
IIIii1II1II = xbmc . translatePath ( os . path . join ( ooOoOoo0O , I1IiI , 'temp' ) )
i1I1iI = xbmc . translatePath ( os . path . join ( OO0o , I1IiI , 'resources/' ) )
oo0OooOOo0 = xbmc . translatePath ( os . path . join ( OO0o , I1IiI , 'default.py' ) )
o0OO00oO = xbmc . getSkinDir ( )
I11i1I1I = xbmc . translatePath ( 'special://logpath/' )
oO0Oo = '/storage/backup'
oOOoo0Oo = '/storage/.restore/'
o00OO00OoO = Net ( )
OOOO0OOoO0O0 = xbmc . translatePath ( os . path . join ( ooOoOoo0O , I1IiI ) )
O0Oo000ooO00 = xbmc . translatePath ( os . path . join ( OOOO0OOoO0O0 , 'guinew.xml' ) )
oO0 = xbmc . translatePath ( os . path . join ( OOOO0OOoO0O0 , 'guitemp' , '' ) )
Ii1iIiII1ii1 = xbmc . translatePath ( os . path . join ( I1IIIii , 'Database' ) )
ooOooo000oOO = os . path . join ( OO0o , 'packages' )
Oo0oOOo = os . path . join ( II , 'addontemp' )
Oo0OoO00oOO0o = xbmc . translatePath ( os . path . join ( II , '.cbcfg' ) )
OOO00O = 'http://urlshortbot.com/noobs'
OOoOO0oo0ooO = [ 'firstrun' , 'plugin.program.mediacube' , 'plugin.program.totalinstaller' , 'script.module.addon.common' , 'addons' , 'addon_data' , 'userdata' , 'sources.xml' , 'favourites.xml' ]
O0o0O00Oo0o0 = 0.0
O00O0oOO00O00 = 0.0
i1Oo00 = '0'
i1i = [ '/storage/.kodi' , '/storage/.cache' , '/storage/.config' , '/storage/.ssh' ]
iiI111I1iIiI = '1889903'
IIIi1I1IIii1II = 'MediaCube'
O0ii1ii1ii = 'mediacube15'
oooooOoo0ooo = 'All the Addons you installed and settings you customize will be erased and you will have a fresh, up to date version of the latest Media Cube build. Would you like to continue?'
if 6 - 6: oOoO0o00OO0 - iI1iiIiiII . OOo00O0 / iIII % iIi1i1ii1
if 82 - 82: oOO - iIII % oOO % ooOo
def IIii ( type , name , url , mode , iconimage = '' , fanart = '' , video = '' , description = '' ) :
 if type != 'folder2' and type != 'addon' :
  if 85 - 85: I1ii11iIi11i % OOo00O0 % oOO
  if 82 - 82: i11iIiiIii - OOo00O0 * OoooooooOO / oOoO0o00OO0
  if 31 - 31: iIII . OoO0O00 - iIii1I11I1II1
  if 64 - 64: oOoO0o00OO0
  if 22 - 22: Oo0Ooo + iI1iiIiiII % I1ii11iIi11i
  if 9 - 9: OoooooooOO
  iconimage = I11i1
 if type == 'addon' :
  if 62 - 62: Oo / OoO0O00 + iI1iiIiiII / OoO0O00 . II111iiii
  if len ( iconimage ) > 0 :
   iconimage = iconimage
  else :
   iconimage = 'DefaultFolder.png'
   if 68 - 68: i11iIiiIii % I1ii11iIi11i + i11iIiiIii
   if 31 - 31: II111iiii . I1IiiI
   if 1 - 1: Oo0Ooo / o0oOOo0O0Ooo % OOo00O0 * iIII . i11iIiiIii
 if fanart == '' :
  fanart = O0o0Oo
  if 2 - 2: I1ii11iIi11i * oOoO0o00OO0 - iIii1I11I1II1 + I1IiiI . ooOo % OOo00O0
 ooOOOoOooOoO = sys . argv [ 0 ]
 ooOOOoOooOoO += "?url=" + urllib . quote_plus ( url )
 ooOOOoOooOoO += "&mode=" + str ( mode )
 ooOOOoOooOoO += "&name=" + urllib . quote_plus ( name )
 ooOOOoOooOoO += "&fanart=" + urllib . quote_plus ( fanart )
 ooOOOoOooOoO += "&video=" + urllib . quote_plus ( video )
 ooOOOoOooOoO += "&description=" + urllib . quote_plus ( description )
 if 91 - 91: OOo00O0 % i1IIi % iIii1I11I1II1
 IIi1I11I1II = True
 OooOoooOo = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 if 46 - 46: OOo00O0
 OooOoooOo . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 OooOoooOo . setProperty ( "Fanart_Image" , fanart )
 OooOoooOo . setProperty ( "Build.Video" , video )
 if 8 - 8: ooOo * OoOoOO00 - iI1iiIiiII - OoO0O00 * Oo % I1IiiI
 if ( type == 'folder' ) or ( type == 'folder2' ) or ( type == 'tutorial_folder' ) or ( type == 'news_folder' ) :
  IIi1I11I1II = ii ( handle = int ( sys . argv [ 1 ] ) , url = ooOOOoOooOoO , listitem = OooOoooOo , isFolder = True )
  if 90 - 90: o0oOOo0O0Ooo % i1IIi / OoO0O00
 else :
  IIi1I11I1II = ii ( handle = int ( sys . argv [ 1 ] ) , url = ooOOOoOooOoO , listitem = OooOoooOo , isFolder = False )
  if 44 - 44: Oo0Ooo . OoO0O00 / I1ii11iIi11i + iI1iiIiiII
 return IIi1I11I1II
 if 65 - 65: O0
 if 68 - 68: Oo % iIi1i1ii1
def ooO00OO0 ( name , url , mode , iconimage , fanart , video , description , skins , guisettingslink , artpack ) :
 ooOOOoOooOoO = sys . argv [ 0 ]
 ooOOOoOooOoO += "?url=" + urllib . quote_plus ( url )
 ooOOOoOooOoO += "&mode=" + str ( mode )
 ooOOOoOooOoO += "&name=" + urllib . quote_plus ( name )
 ooOOOoOooOoO += "&iconimage=" + urllib . quote_plus ( iconimage )
 ooOOOoOooOoO += "&fanart=" + urllib . quote_plus ( fanart )
 ooOOOoOooOoO += "&video=" + urllib . quote_plus ( video )
 ooOOOoOooOoO += "&description=" + urllib . quote_plus ( description )
 ooOOOoOooOoO += "&skins=" + urllib . quote_plus ( skins )
 ooOOOoOooOoO += "&guisettingslink=" + urllib . quote_plus ( guisettingslink )
 ooOOOoOooOoO += "&artpack=" + urllib . quote_plus ( artpack )
 if 31 - 31: OOo00O0 % OOo00O0 % oOoO0o00OO0
 IIi1I11I1II = True
 OooOoooOo = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 if 69 - 69: OoO0O00 - Oo0Ooo + i1IIi / iIi1i1ii1
 OooOoooOo . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 OooOoooOo . setProperty ( "Fanart_Image" , fanart )
 OooOoooOo . setProperty ( "Build.Video" , video )
 if 49 - 49: O0 . OOo00O0
 if ( mode == None ) or ( mode == 'restore_option' ) or ( mode == 'backup_option' ) or ( mode == 'cb_root_menu' ) or ( mode == 'genres' ) or ( mode == 'grab_builds' ) or ( mode == 'community_menu' ) or ( mode == 'instructions' ) or ( mode == 'countries' ) or ( mode == 'update_build' ) or ( url == None ) or ( len ( url ) < 1 ) :
  if 11 - 11: iIII * I1IiiI . iIii1I11I1II1 % OoooooooOO + OOo00O0
  IIi1I11I1II = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = ooOOOoOooOoO , listitem = OooOoooOo , isFolder = True )
  if 78 - 78: OoO0O00 . Oo + OoO0O00 / oOoO0o00OO0 / OoO0O00
 else :
  IIi1I11I1II = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = ooOOOoOooOoO , listitem = OooOoooOo , isFolder = False )
  if 54 - 54: OoOoOO00 % OOo00O0
 return IIi1I11I1II
 if 37 - 37: OoOoOO00 * Oo0Ooo / oOO - OOo00O0 % II111iiii . ooOo
 if 88 - 88: OOo00O0 . II111iiii * II111iiii % iIi1i1ii1
def ii ( handle , url , listitem , isFolder ) :
 xbmcplugin . addDirectoryItem ( handle , url , listitem , isFolder )
 if 15 - 15: i1IIi * I1IiiI + i11iIiiIii
 if 6 - 6: oOO / i11iIiiIii + OOo00O0 * ooOo
def o00o0 ( name , url , mode , iconimage , fanart , buildname , author , version , description , updated , skins , videoaddons , audioaddons , programaddons , pictureaddons , sources , adult ) :
 if 45 - 45: O0
 iconimage = I11i1
 if 26 - 26: oOoO0o00OO0 - iIii1I11I1II1 - I1IiiI / OoO0O00 . OoOoOO00 % iIii1I11I1II1
 ooOOOoOooOoO = sys . argv [ 0 ]
 ooOOOoOooOoO += "?url=" + urllib . quote_plus ( url )
 ooOOOoOooOoO += "&mode=" + str ( mode )
 ooOOOoOooOoO += "&name=" + urllib . quote_plus ( name )
 ooOOOoOooOoO += "&iconimage=" + urllib . quote_plus ( iconimage )
 ooOOOoOooOoO += "&fanart=" + urllib . quote_plus ( fanart )
 ooOOOoOooOoO += "&author=" + urllib . quote_plus ( author )
 ooOOOoOooOoO += "&description=" + urllib . quote_plus ( description )
 ooOOOoOooOoO += "&version=" + urllib . quote_plus ( version )
 ooOOOoOooOoO += "&buildname=" + urllib . quote_plus ( buildname )
 ooOOOoOooOoO += "&updated=" + urllib . quote_plus ( updated )
 ooOOOoOooOoO += "&skins=" + urllib . quote_plus ( skins )
 ooOOOoOooOoO += "&videoaddons=" + urllib . quote_plus ( videoaddons )
 ooOOOoOooOoO += "&audioaddons=" + urllib . quote_plus ( audioaddons )
 ooOOOoOooOoO += "&buildname=" + urllib . quote_plus ( buildname )
 ooOOOoOooOoO += "&programaddons=" + urllib . quote_plus ( programaddons )
 ooOOOoOooOoO += "&pictureaddons=" + urllib . quote_plus ( pictureaddons )
 ooOOOoOooOoO += "&sources=" + urllib . quote_plus ( sources )
 ooOOOoOooOoO += "&adult=" + urllib . quote_plus ( adult )
 if 91 - 91: o0oOOo0O0Ooo . iIii1I11I1II1 / ooOo + i1IIi
 IIi1I11I1II = True
 OooOoooOo = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 if 42 - 42: oOO . o0oOOo0O0Ooo . oOO - I1ii11iIi11i
 OooOoooOo . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 OooOoooOo . setProperty ( "Fanart_Image" , fanart )
 OooOoooOo . setProperty ( "Build.Video" , i1ii1I1I1 )
 if 74 - 74: o0oOOo0O0Ooo . OOo00O0
 IIi1I11I1II = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = ooOOOoOooOoO , listitem = OooOoooOo , isFolder = False )
 if 18 - 18: Oo + OOo00O0 - iI1iiIiiII . II111iiii + i11iIiiIii
 return IIi1I11I1II
 if 20 - 20: iIi1i1ii1
def Oo0oO00o ( title , name , url , mode , iconimage = '' , fanart = '' , video = '' , description = '' , zip_link = '' , repo_link = '' , repo_id = '' , addon_id = '' , provider_name = '' , forum = '' , data_path = '' ) :
 if len ( iconimage ) > 0 :
  if 13 - 13: oOoO0o00OO0 * Oo0Ooo * oOO
  iconimage = I11i1
 else :
  iconimage = 'DefaultFolder.png'
  if 50 - 50: o0oOOo0O0Ooo * oOoO0o00OO0 % O0
 if fanart == '' :
  fanart = O0o0Oo
  if 61 - 61: I1IiiI - Oo . ooOo / Oo + Oo0Ooo
 ooOOOoOooOoO = sys . argv [ 0 ]
 ooOOOoOooOoO += "?url=" + urllib . quote_plus ( url )
 ooOOOoOooOoO += "&zip_link=" + urllib . quote_plus ( zip_link )
 ooOOOoOooOoO += "&repo_link=" + urllib . quote_plus ( repo_link )
 ooOOOoOooOoO += "&data_path=" + urllib . quote_plus ( data_path )
 ooOOOoOooOoO += "&provider_name=" + str ( provider_name )
 ooOOOoOooOoO += "&forum=" + str ( forum )
 ooOOOoOooOoO += "&repo_id=" + str ( repo_id )
 ooOOOoOooOoO += "&addon_id=" + str ( addon_id )
 ooOOOoOooOoO += "&mode=" + str ( mode )
 ooOOOoOooOoO += "&name=" + urllib . quote_plus ( name )
 ooOOOoOooOoO += "&fanart=" + urllib . quote_plus ( fanart )
 ooOOOoOooOoO += "&video=" + urllib . quote_plus ( video )
 ooOOOoOooOoO += "&description=" + urllib . quote_plus ( description )
 if 5 - 5: oOO + oOO / O0 * Oo0Ooo - Oo % oOO
 IIi1I11I1II = True
 OooOoooOo = xbmcgui . ListItem ( title , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 if 15 - 15: i11iIiiIii % iI1iiIiiII . Oo0Ooo + I1ii11iIi11i
 OooOoooOo . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 OooOoooOo . setProperty ( "Fanart_Image" , fanart )
 OooOoooOo . setProperty ( "Build.Video" , video )
 if 61 - 61: Oo0Ooo * I1ii11iIi11i % Oo0Ooo - i1IIi - iIii1I11I1II1
 ii ( handle = int ( sys . argv [ 1 ] ) , url = ooOOOoOooOoO , listitem = OooOoooOo , isFolder = False )
 if 74 - 74: I1ii11iIi11i + II111iiii / OoO0O00
 if 100 - 100: OoOoOO00 * iIii1I11I1II1
def oOo00oOoO000 ( url ) :
 IIii ( 'folder' , '[COLOR=yellow][PLUGIN][/COLOR] Audio' , url + '&typex=audio' , 'grab_addons' , 'audio.png' , '' , '' , '' )
 IIii ( 'folder' , '[COLOR=yellow][PLUGIN][/COLOR] Image (Picture)' , url + '&typex=image' , 'grab_addons' , 'pictures.png' , '' , '' , '' )
 IIii ( 'folder' , '[COLOR=yellow][PLUGIN][/COLOR] Program' , url + '&typex=program' , 'grab_addons' , 'programs.png' , '' , '' , '' )
 IIii ( 'folder' , '[COLOR=yellow][PLUGIN][/COLOR] Video' , url + '&typex=video' , 'grab_addons' , 'video.png' , '' , '' , '' )
 IIii ( 'folder' , '[COLOR=lime][SCRAPER][/COLOR] Movies (Used for library scanning)' , url + '&typex=movie%20scraper' , 'grab_addons' , 'movies.png' , '' , '' , '' )
 IIii ( 'folder' , '[COLOR=lime][SCRAPER][/COLOR] TV Shows (Used for library scanning)' , url + '&typex=tv%20show%20scraper' , 'grab_addons' , 'tvshows.png' , '' , '' , '' )
 IIii ( 'folder' , '[COLOR=lime][SCRAPER][/COLOR] Music Artists (Used for library scanning)' , url + '&typex=artist%20scraper' , 'grab_addons' , 'artists.png' , '' , '' , '' )
 IIii ( 'folder' , '[COLOR=lime][SCRAPER][/COLOR] Music Videos (Used for library scanning)' , url + '&typex=music%20video%20scraper' , 'grab_addons' , 'musicvideos.png' , '' , '' , '' )
 IIii ( 'folder' , '[COLOR=orange][SERVICE][/COLOR] All Services' , url + '&typex=service' , 'grab_addons' , 'services.png' , '' , '' , '' )
 IIii ( 'folder' , '[COLOR=orange][SERVICE][/COLOR] Weather Service' , url + '&typex=weather' , 'grab_addons' , 'weather.png' , '' , '' , '' )
 IIii ( 'folder' , '[COLOR=dodgerblue][OTHER][/COLOR] Repositories' , url + '&typex=repository' , 'grab_addons' , 'repositories.png' , '' , '' , '' )
 IIii ( 'folder' , '[COLOR=dodgerblue][OTHER][/COLOR] Scripts (Program Add-ons)' , url + '&typex=executable' , 'grab_addons' , 'scripts.png' , '' , '' , '' )
 IIii ( 'folder' , '[COLOR=dodgerblue][OTHER][/COLOR] Screensavers' , url + '&typex=screensaver' , 'grab_addons' , 'screensaver.png' , '' , '' , '' )
 IIii ( 'folder' , '[COLOR=dodgerblue][OTHER][/COLOR] Script Modules' , url + '&typex=script%20module' , 'grab_addons' , 'scriptmodules.png' , '' , '' , '' )
 IIii ( 'folder' , '[COLOR=dodgerblue][OTHER][/COLOR] Skins' , url + '&typex=skin' , 'grab_addons' , 'skins.png' , '' , '' , '' )
 IIii ( 'folder' , '[COLOR=dodgerblue][OTHER][/COLOR] Subtitles' , url + '&typex=subtitles' , 'grab_addons' , 'subtitles.png' , '' , '' , '' )
 IIii ( 'folder' , '[COLOR=dodgerblue][OTHER][/COLOR] Web Interface' , url + '&typex=web%20interface' , 'grab_addons' , 'webinterface.png' , '' , '' , '' )
 if 93 - 93: o0oOOo0O0Ooo % i1IIi . iI1iiIiiII . i11iIiiIii
 if 56 - 56: I1ii11iIi11i % O0 - I1IiiI
def O00o0OO0 ( ) :
 IIi1I1iiiii ( )
 xbmc . executebuiltin ( 'ActivateWindow(10040,"addons://outdated/",return)' )
 if 71 - 71: iIII * II111iiii * ooOo
 if 56 - 56: I1IiiI
def O0oO ( url ) :
 IIii ( 'folder' , 'African' , url + '&genre=african' , 'grab_addons' , 'african.png' , '' , '' , '' )
 IIii ( 'folder' , 'Arabic' , url + '&genre=arabic' , 'grab_addons' , 'arabic.png' , '' , '' , '' )
 IIii ( 'folder' , 'Asian' , url + '&genre=asian' , 'grab_addons' , 'asian.png' , '' , '' , '' )
 IIii ( 'folder' , 'Australian' , url + '&genre=australian' , 'grab_addons' , 'australian.png' , '' , '' , '' )
 IIii ( 'folder' , 'Austrian' , url + '&genre=austrian' , 'grab_addons' , 'austrian.png' , '' , '' , '' )
 IIii ( 'folder' , 'Belgian' , url + '&genre=belgian' , 'grab_addons' , 'belgian.png' , '' , '' , '' )
 IIii ( 'folder' , 'Brazilian' , url + '&genre=brazilian' , 'grab_addons' , 'brazilian.png' , '' , '' , '' )
 IIii ( 'folder' , 'Canadian' , url + '&genre=canadian' , 'grab_addons' , 'canadian.png' , '' , '' , '' )
 IIii ( 'folder' , 'Chinese' , url + '&genre=chinese' , 'grab_addons' , 'chinese.png' , '' , '' , '' )
 IIii ( 'folder' , 'Colombian' , url + '&genre=columbian' , 'grab_addons' , 'columbian.png' , '' , '' , '' )
 IIii ( 'folder' , 'Croatian' , url + '&genre=croatian' , 'grab_addons' , 'croatian.png' , '' , '' , '' )
 IIii ( 'folder' , 'Czech' , url + '&genre=czech' , 'grab_addons' , 'czech.png' , '' , '' , '' )
 IIii ( 'folder' , 'Danish' , url + '&genre=danish' , 'grab_addons' , 'danish.png' , '' , '' , '' )
 IIii ( 'folder' , 'Dominican' , url + '&genre=dominican' , 'grab_addons' , 'dominican.png' , '' , '' , '' )
 IIii ( 'folder' , 'Dutch' , url + '&genre=dutch' , 'grab_addons' , 'dutch.png' , '' , '' , '' )
 IIii ( 'folder' , 'Egyptian' , url + '&genre=egyptian' , 'grab_addons' , 'egyptian.png' , '' , '' , '' )
 IIii ( 'folder' , 'Filipino' , url + '&genre=filipino' , 'grab_addons' , 'filipino.png' , '' , '' , '' )
 IIii ( 'folder' , 'Finnish' , url + '&genre=finnish' , 'grab_addons' , 'finnish.png' , '' , '' , '' )
 IIii ( 'folder' , 'French' , url + '&genre=french' , 'grab_addons' , 'french.png' , '' , '' , '' )
 IIii ( 'folder' , 'German' , url + '&genre=german' , 'grab_addons' , 'german.png' , '' , '' , '' )
 IIii ( 'folder' , 'Greek' , url + '&genre=greek' , 'grab_addons' , 'greek.png' , '' , '' , '' )
 IIii ( 'folder' , 'Hebrew' , url + '&genre=hebrew' , 'grab_addons' , 'hebrew.png' , '' , '' , '' )
 IIii ( 'folder' , 'Hungarian' , url + '&genre=hungarian' , 'grab_addons' , 'hungarian.png' , '' , '' , '' )
 IIii ( 'folder' , 'Icelandic' , url + '&genre=icelandic' , 'grab_addons' , 'icelandic.png' , '' , '' , '' )
 IIii ( 'folder' , 'Indian' , url + '&genre=indian' , 'grab_addons' , 'indian.png' , '' , '' , '' )
 IIii ( 'folder' , 'Irish' , url + '&genre=irish' , 'grab_addons' , 'irish.png' , '' , '' , '' )
 IIii ( 'folder' , 'Italian' , url + '&genre=italian' , 'grab_addons' , 'italian.png' , '' , '' , '' )
 IIii ( 'folder' , 'Japanese' , url + '&genre=japanese' , 'grab_addons' , 'japanese.png' , '' , '' , '' )
 IIii ( 'folder' , 'Korean' , url + '&genre=korean' , 'grab_addons' , 'korean.png' , '' , '' , '' )
 IIii ( 'folder' , 'Lebanese' , url + '&genre=lebanese' , 'grab_addons' , 'lebanese.png' , '' , '' , '' )
 IIii ( 'folder' , 'Mongolian' , url + '&genre=mongolian' , 'grab_addons' , 'mongolian.png' , '' , '' , '' )
 IIii ( 'folder' , 'Moroccan' , url + '&genre=moroccan' , 'grab_addons' , 'moroccan.png' , '' , '' , '' )
 IIii ( 'folder' , 'Nepali' , url + '&genre=nepali' , 'grab_addons' , 'nepali.png' , '' , '' , '' )
 IIii ( 'folder' , 'New Zealand' , url + '&genre=newzealand' , 'grab_addons' , 'newzealand.png' , '' , '' , '' )
 IIii ( 'folder' , 'Norwegian' , url + '&genre=norwegian' , 'grab_addons' , 'norwegian.png' , '' , '' , '' )
 IIii ( 'folder' , 'Pakistani' , url + '&genre=pakistani' , 'grab_addons' , 'pakistani.png' , '' , '' , '' )
 IIii ( 'folder' , 'Polish' , url + '&genre=polish' , 'grab_addons' , 'polish.png' , '' , '' , '' )
 IIii ( 'folder' , 'Portuguese' , url + '&genre=portuguese' , 'grab_addons' , 'portuguese.png' , '' , '' , '' )
 IIii ( 'folder' , 'Romanian' , url + '&genre=romanian' , 'grab_addons' , 'romanian.png' , '' , '' , '' )
 IIii ( 'folder' , 'Russian' , url + '&genre=russian' , 'grab_addons' , 'russian.png' , '' , '' , '' )
 IIii ( 'folder' , 'Singapore' , url + '&genre=singapore' , 'grab_addons' , 'singapore.png' , '' , '' , '' )
 IIii ( 'folder' , 'Spanish' , url + '&genre=spanish' , 'grab_addons' , 'spanish.png' , '' , '' , '' )
 IIii ( 'folder' , 'Swedish' , url + '&genre=swedish' , 'grab_addons' , 'swedish.png' , '' , '' , '' )
 IIii ( 'folder' , 'Swiss' , url + '&genre=swiss' , 'grab_addons' , 'swiss.png' , '' , '' , '' )
 IIii ( 'folder' , 'Syrian' , url + '&genre=syrian' , 'grab_addons' , 'syrian.png' , '' , '' , '' )
 IIii ( 'folder' , 'Tamil' , url + '&genre=tamil' , 'grab_addons' , 'tamil.png' , '' , '' , '' )
 IIii ( 'folder' , 'Thai' , url + '&genre=thai' , 'grab_addons' , 'thai.png' , '' , '' , '' )
 IIii ( 'folder' , 'Turkish' , url + '&genre=turkish' , 'grab_addons' , 'turkish.png' , '' , '' , '' )
 IIii ( 'folder' , 'UK' , url + '&genre=uk' , 'grab_addons' , 'uk.png' , '' , '' , '' )
 IIii ( 'folder' , 'USA' , url + '&genre=usa' , 'grab_addons' , 'usa.png' , '' , '' , '' )
 IIii ( 'folder' , 'Vietnamese' , url + '&genre=vietnamese' , 'grab_addons' , 'vietnamese.png' , '' , '' , '' )
 if 73 - 73: I1ii11iIi11i * i11iIiiIii % ooOo . I1ii11iIi11i
 if 66 - 66: ooOo + ooOo + oOO / OOo00O0 + Oo
def iI ( url ) :
 ii1111iII = 'http://noobsandnerds.com/TI/AddonPortal/addondetails.php?id=%s' % ( url )
 iiiiI = oooOo0OOOoo0 ( ii1111iII ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 if 51 - 51: Oo0Ooo / OoOoOO00 . Oo * o0oOOo0O0Ooo + OoO0O00 * iIII
 OOOoOo = re . compile ( 'addon_types="(.+?)"' ) . findall ( iiiiI )
 O00o0 = re . compile ( 'name="(.+?)"' ) . findall ( iiiiI )
 I11iII = re . compile ( 'UID="(.+?)"' ) . findall ( iiiiI )
 iIIII = re . compile ( 'id="(.+?)"' ) . findall ( iiiiI )
 I11iI1i1I11I11 = re . compile ( 'provider_name="(.+?)"' ) . findall ( iiiiI )
 o000O0O = re . compile ( 'version="(.+?)"' ) . findall ( iiiiI )
 I1i1i1iii = re . compile ( 'created="(.+?)"' ) . findall ( iiiiI )
 I1111i = re . compile ( 'addon_types="(.+?)"' ) . findall ( iiiiI )
 iIIii = re . compile ( 'updated="(.+?)"' ) . findall ( iiiiI )
 o00O0O = re . compile ( 'downloads="(.+?)"' ) . findall ( iiiiI )
 if 20 - 20: i1IIi - oOO
 i1iI = re . compile ( 'description="(.+?)"' ) . findall ( iiiiI )
 Oo0O0 = re . compile ( 'devbroke="(.+?)"' ) . findall ( iiiiI )
 Ooo0OOoOoO0 = re . compile ( 'broken="(.+?)"' ) . findall ( iiiiI )
 oOo0OOoO0 = re . compile ( 'deleted="(.+?)"' ) . findall ( iiiiI )
 IIo0Oo0oO0oOO00 = re . compile ( 'mainbranch_notes="(.+?)"' ) . findall ( iiiiI )
 if 92 - 92: OoooooooOO * iIi1i1ii1
 o0000oO = re . compile ( 'repo_url="(.+?)"' ) . findall ( iiiiI )
 I1II1 = re . compile ( 'data_url="(.+?)"' ) . findall ( iiiiI )
 oooO = re . compile ( 'zip_url="(.+?)"' ) . findall ( iiiiI )
 i1I1i111Ii = re . compile ( 'genres="(.+?)"' ) . findall ( iiiiI )
 ooo = re . compile ( 'forum="(.+?)"' ) . findall ( iiiiI )
 i1i1iI1iiiI = re . compile ( 'repo_id="(.+?)"' ) . findall ( iiiiI )
 Ooo0oOooo0 = re . compile ( 'license="(.+?)"' ) . findall ( iiiiI )
 oOOOoo00 = re . compile ( 'platform="(.+?)"' ) . findall ( iiiiI )
 iiIiIIIiiI = re . compile ( 'visible="(.+?)"' ) . findall ( iiiiI )
 iiI1IIIi = re . compile ( 'script="(.+?)"' ) . findall ( iiiiI )
 II11IiIi11 = re . compile ( 'program_plugin="(.+?)"' ) . findall ( iiiiI )
 IIOOO0O00O0OOOO = re . compile ( 'script_module="(.+?)"' ) . findall ( iiiiI )
 I1iiii1I = re . compile ( 'video_plugin="(.+?)"' ) . findall ( iiiiI )
 OOo0 = re . compile ( 'audio_plugin="(.+?)"' ) . findall ( iiiiI )
 oO00ooooO0o = re . compile ( 'image_plugin="(.+?)"' ) . findall ( iiiiI )
 oo0o = re . compile ( 'repository="(.+?)"' ) . findall ( iiiiI )
 o0oO0oooOoo = re . compile ( 'weather_service="(.+?)"' ) . findall ( iiiiI )
 I1III1111iIi = re . compile ( 'skin="(.+?)"' ) . findall ( iiiiI )
 I1i111I = re . compile ( 'service="(.+?)"' ) . findall ( iiiiI )
 OooOo0oo0O0o00O = re . compile ( 'warning="(.+?)"' ) . findall ( iiiiI )
 I1i11 = re . compile ( 'web_interface="(.+?)"' ) . findall ( iiiiI )
 IiIi1I1 = re . compile ( 'movie_scraper="(.+?)"' ) . findall ( iiiiI )
 IiIIi1 = re . compile ( 'tv_scraper="(.+?)"' ) . findall ( iiiiI )
 IIIIiii1IIii = re . compile ( 'artist_scraper="(.+?)"' ) . findall ( iiiiI )
 II1i11I = re . compile ( 'music_video_scraper="(.+?)"' ) . findall ( iiiiI )
 ii1I1IIii11 = re . compile ( 'subtitles="(.+?)"' ) . findall ( iiiiI )
 O0o0oO = re . compile ( 'requires="(.+?)"' ) . findall ( iiiiI )
 IIIIiIiIi1 = re . compile ( 'modules="(.+?)"' ) . findall ( iiiiI )
 I11iiiiI1i = re . compile ( 'icon="(.+?)"' ) . findall ( iiiiI )
 iI1i11 = re . compile ( 'video_preview="(.+?)"' ) . findall ( iiiiI )
 OoOOoooOO0O = re . compile ( 'video_guide="(.+?)"' ) . findall ( iiiiI )
 ooo00Ooo = re . compile ( 'video_guide1="(.+?)"' ) . findall ( iiiiI )
 Oo0o0O00 = re . compile ( 'video_guide2="(.+?)"' ) . findall ( iiiiI )
 ii1 = re . compile ( 'video_guide3="(.+?)"' ) . findall ( iiiiI )
 I1i11OO = re . compile ( 'video_guide4="(.+?)"' ) . findall ( iiiiI )
 o0O0oo0OO0O = re . compile ( 'video_guide5="(.+?)"' ) . findall ( iiiiI )
 OO0 = re . compile ( 'video_guide6="(.+?)"' ) . findall ( iiiiI )
 o0Oooo = re . compile ( 'video_guide7="(.+?)"' ) . findall ( iiiiI )
 iiI = re . compile ( 'video_guide8="(.+?)"' ) . findall ( iiiiI )
 oOIIiIi = re . compile ( 'video_guide9="(.+?)"' ) . findall ( iiiiI )
 OOoOooOoOOOoo = re . compile ( 'video_guide10="(.+?)"' ) . findall ( iiiiI )
 Iiii1iI1i = re . compile ( 'video_label1="(.+?)"' ) . findall ( iiiiI )
 I1ii1ii11i1I = re . compile ( 'video_label2="(.+?)"' ) . findall ( iiiiI )
 o0OoOO = re . compile ( 'video_label3="(.+?)"' ) . findall ( iiiiI )
 O0O0Oo00 = re . compile ( 'video_label4="(.+?)"' ) . findall ( iiiiI )
 oOoO00o = re . compile ( 'video_label5="(.+?)"' ) . findall ( iiiiI )
 oO00O0 = re . compile ( 'video_label6="(.+?)"' ) . findall ( iiiiI )
 IIi1IIIi = re . compile ( 'video_label7="(.+?)"' ) . findall ( iiiiI )
 O00Ooo = re . compile ( 'video_label8="(.+?)"' ) . findall ( iiiiI )
 OOOO0OOO = re . compile ( 'video_label9="(.+?)"' ) . findall ( iiiiI )
 i1i1ii = re . compile ( 'video_label10="(.+?)"' ) . findall ( iiiiI )
 if 46 - 46: OoOoOO00 + OoO0O00
 if 70 - 70: OOo00O0 / iIii1I11I1II1
 if 85 - 85: OoooooooOO % i1IIi * OoooooooOO / I1ii11iIi11i
 ooOOoO = OOOoOo [ 0 ] if ( len ( OOOoOo ) > 0 ) else ''
 I1i11i = O00o0 [ 0 ] if ( len ( O00o0 ) > 0 ) else ''
 IiIi = I11iII [ 0 ] if ( len ( I11iII ) > 0 ) else ''
 OOOOO0O00 = iIIII [ 0 ] if ( len ( iIIII ) > 0 ) else ''
 Iii = I11iI1i1I11I11 [ 0 ] if ( len ( I11iI1i1I11I11 ) > 0 ) else ''
 iIIiIiI1I1 = o000O0O [ 0 ] if ( len ( o000O0O ) > 0 ) else ''
 ooO = I1i1i1iii [ 0 ] if ( len ( I1i1i1iii ) > 0 ) else ''
 iiOO0O0Ooo = I1111i [ 0 ] if ( len ( I1111i ) > 0 ) else ''
 oOoO0 = iIIii [ 0 ] if ( len ( iIIii ) > 0 ) else ''
 Oo0 = o00O0O [ 0 ] if ( len ( o00O0O ) > 0 ) else ''
 if 83 - 83: i11iIiiIii % o0oOOo0O0Ooo % oOO
 Ii1II1I11i1 = '[CR][CR][COLOR=dodgerblue]Description: [/COLOR]' + i1iI [ 0 ] if ( len ( i1iI ) > 0 ) else ''
 oOoooooOoO = Oo0O0 [ 0 ] if ( len ( Oo0O0 ) > 0 ) else ''
 Ii111 = Ooo0OOoOoO0 [ 0 ] if ( len ( Ooo0OOoOoO0 ) > 0 ) else ''
 I111i1i1111 = '[CR]' + oOo0OOoO0 [ 0 ] if ( len ( oOo0OOoO0 ) > 0 ) else ''
 IIII1 = '[CR][CR][COLOR=dodgerblue]User Notes: [/COLOR]' + IIo0Oo0oO0oOO00 [ 0 ] if ( len ( IIo0Oo0oO0oOO00 ) > 0 ) else ''
 if 10 - 10: iIi1i1ii1 / oOO + i11iIiiIii / iI1iiIiiII
 OOOoOoO = o0000oO [ 0 ] if ( len ( o0000oO ) > 0 ) else ''
 iIIIII1ii1I = I1II1 [ 0 ] if ( len ( I1II1 ) > 0 ) else ''
 Ii1i1iI = oooO [ 0 ] if ( len ( oooO ) > 0 ) else ''
 IIiI1 = i1I1i111Ii [ 0 ] if ( len ( i1I1i111Ii ) > 0 ) else ''
 i1iI1 = '[CR][CR][COLOR=dodgerblue]Support Forum: [/COLOR]' + ooo [ 0 ] if ( len ( ooo ) > 0 ) else '[CR][CR][COLOR=dodgerblue]Support Forum: [/COLOR]No forum details given by developer'
 ii1I1IiiI1ii1i = ooo [ 0 ] if ( len ( ooo ) > 0 ) else 'None'
 O0o = i1i1iI1iiiI [ 0 ] if ( len ( i1i1iI1iiiI ) > 0 ) else ''
 license = Ooo0oOooo0 [ 0 ] if ( len ( Ooo0oOooo0 ) > 0 ) else ''
 oO0OoO00o = '[COLOR=orange]     Platform: [/COLOR]' + oOOOoo00 [ 0 ] if ( len ( oOOOoo00 ) > 0 ) else ''
 II1iiiiII = iiIiIIIiiI [ 0 ] if ( len ( iiIiIIIiiI ) > 0 ) else ''
 O0OoOO0oo0 = iiI1IIIi [ 0 ] if ( len ( iiI1IIIi ) > 0 ) else ''
 oOOO0o0OO0000ooo = II11IiIi11 [ 0 ] if ( len ( II11IiIi11 ) > 0 ) else ''
 iIIII1iIIii = IIOOO0O00O0OOOO [ 0 ] if ( len ( IIOOO0O00O0OOOO ) > 0 ) else ''
 oOOO00o000o = I1iiii1I [ 0 ] if ( len ( I1iiii1I ) > 0 ) else ''
 iIi11i1 = OOo0 [ 0 ] if ( len ( OOo0 ) > 0 ) else ''
 oO00oo0o00o0o = oO00ooooO0o [ 0 ] if ( len ( oO00ooooO0o ) > 0 ) else ''
 IiIIIIIi = oo0o [ 0 ] if ( len ( oo0o ) > 0 ) else ''
 IiIi1iIIi1 = I1i111I [ 0 ] if ( len ( I1i111I ) > 0 ) else ''
 o0OO00oO = I1III1111iIi [ 0 ] if ( len ( I1III1111iIi ) > 0 ) else ''
 O0OoO0ooOO0o = OooOo0oo0O0o00O [ 0 ] if ( len ( OooOo0oo0O0o00O ) > 0 ) else ''
 OoOo0oOooOoOO = I1i11 [ 0 ] if ( len ( I1i11 ) > 0 ) else ''
 oo00ooOoO00 = o0oO0oooOoo [ 0 ] if ( len ( o0oO0oooOoo ) > 0 ) else ''
 o00oOoOo0 = IiIi1I1 [ 0 ] if ( len ( IiIi1I1 ) > 0 ) else ''
 o0O0O0ooo0oOO = IiIIi1 [ 0 ] if ( len ( IiIIi1 ) > 0 ) else ''
 oo000 = IIIIiii1IIii [ 0 ] if ( len ( IIIIiii1IIii ) > 0 ) else ''
 iiOoO = II1i11I [ 0 ] if ( len ( II1i11I ) > 0 ) else ''
 Iiiiii111i1ii = ii1I1IIii11 [ 0 ] if ( len ( ii1I1IIii11 ) > 0 ) else ''
 i1i1iII1 = O0o0oO [ 0 ] if ( len ( O0o0oO ) > 0 ) else ''
 iii11i1IIII = IIIIiIiIi1 [ 0 ] if ( len ( IIIIiIiIi1 ) > 0 ) else ''
 Ii = I11iiiiI1i [ 0 ] if ( len ( I11iiiiI1i ) > 0 ) else ''
 o00iiI1Ii1 = iI1i11 [ 0 ] if ( len ( iI1i11 ) > 0 ) else 'None'
 ii1i = OoOOoooOO0O [ 0 ] if ( len ( OoOOoooOO0O ) > 0 ) else 'None'
 oOOoo = ooo00Ooo [ 0 ] if ( len ( ooo00Ooo ) > 0 ) else 'None'
 iII1111III1I = Oo0o0O00 [ 0 ] if ( len ( Oo0o0O00 ) > 0 ) else 'None'
 ii11i = ii1 [ 0 ] if ( len ( ii1 ) > 0 ) else 'None'
 O00oOo00o0o = I1i11OO [ 0 ] if ( len ( I1i11OO ) > 0 ) else 'None'
 O00oO0 = o0O0oo0OO0O [ 0 ] if ( len ( o0O0oo0OO0O ) > 0 ) else 'None'
 O0Oo00OoOo = OO0 [ 0 ] if ( len ( OO0 ) > 0 ) else 'None'
 ii1ii111 = o0Oooo [ 0 ] if ( len ( o0Oooo ) > 0 ) else 'None'
 i11111I1I = iiI [ 0 ] if ( len ( iiI ) > 0 ) else 'None'
 ii1Oo0000oOo = oOIIiIi [ 0 ] if ( len ( oOIIiIi ) > 0 ) else 'None'
 I11o0oO00oO0o0o0 = OOoOooOoOOOoo [ 0 ] if ( len ( OOoOooOoOOOoo ) > 0 ) else 'None'
 I1I = Iiii1iI1i [ 0 ] if ( len ( Iiii1iI1i ) > 0 ) else 'None'
 ooooo = I1ii1ii11i1I [ 0 ] if ( len ( I1ii1ii11i1I ) > 0 ) else 'None'
 i11IIIiI1I = o0OoOO [ 0 ] if ( len ( o0OoOO ) > 0 ) else 'None'
 o0iiiI1I1iIIIi1 = O0O0Oo00 [ 0 ] if ( len ( O0O0Oo00 ) > 0 ) else 'None'
 IiiI1iiiiI1iI = oOoO00o [ 0 ] if ( len ( oOoO00o ) > 0 ) else 'None'
 iIiiiii1i = oO00O0 [ 0 ] if ( len ( oO00O0 ) > 0 ) else 'None'
 iiIi1IIiI = IIi1IIIi [ 0 ] if ( len ( IIi1IIIi ) > 0 ) else 'None'
 i1oO0OO0 = O00Ooo [ 0 ] if ( len ( O00Ooo ) > 0 ) else 'None'
 o0O0Oo00 = OOOO0OOO [ 0 ] if ( len ( OOOO0OOO ) > 0 ) else 'None'
 O0Oo0o000oO = i1i1ii [ 0 ] if ( len ( i1i1ii ) > 0 ) else 'None'
 if 99 - 99: ooOo * II111iiii * iIi1i1ii1
 if I111i1i1111 != '' :
  oOooO0 = '[CR][CR][COLOR=dodgerblue]Status: [/COLOR][COLOR=red]This add-on is depreciated, it\'s no longer available.[/COLOR]'
  if 79 - 79: OoO0O00 - iIii1I11I1II1 + iI1iiIiiII - iIi1i1ii1
 elif Ii111 == '' and oOoooooOoO == '' and O0OoO0ooOO0o == '' :
  oOooO0 = '[CR][CR][COLOR=dodgerblue]Status: [/COLOR][COLOR=lime]No reported problems[/COLOR]'
  if 93 - 93: II111iiii . I1IiiI - Oo0Ooo + OoOoOO00
 elif Ii111 == '' and oOoooooOoO == '' and O0OoO0ooOO0o != '' and I111i1i1111 == '' :
  oOooO0 = '[CR][CR][COLOR=dodgerblue]Status: [/COLOR][COLOR=orange]Although there have been no reported problems there may be issues with this add-on, see below.[/COLOR]'
  if 61 - 61: II111iiii
 elif Ii111 == '' and oOoooooOoO != '' :
  oOooO0 = '[CR][CR][COLOR=dodgerblue]Status: [/COLOR]Marked as broken by the add-on developer.[CR][COLOR=dodgerblue]Developer Comments: [/COLOR]' + oOoooooOoO
  if 15 - 15: i11iIiiIii % I1IiiI * oOoO0o00OO0 / iIi1i1ii1
 elif Ii111 != '' and oOoooooOoO == '' :
  oOooO0 = '[CR][CR][COLOR=dodgerblue]Status: [/COLOR]Marked as broken by a member of the community at [COLOR=orange]www.noobs[/COLOR][COLOR=dodgerblue]and[/COLOR][COLOR=orange]nerds.com[/COLOR][CR][COLOR=dodgerblue]User Comments: [/COLOR]' + Ii111
  if 90 - 90: OOo00O0
 elif Ii111 != '' and oOoooooOoO != '' :
  oOooO0 = '[CR][CR][COLOR=dodgerblue]Status: [/COLOR]Marked as broken by both the add-on developer and a member of the community at [COLOR=orange]www.noobs[/COLOR][COLOR=dodgerblue]and[/COLOR][COLOR=orange]nerds.com[/COLOR][CR][COLOR=dodgerblue]Developer Comments: [/COLOR]' + oOoooooOoO + '[CR][COLOR=dodgerblue]User Comments: [/COLOR]' + Ii111
  if 31 - 31: Oo + O0
  if 87 - 87: oOO
 IIIii = str ( '[COLOR=orange]Name: [/COLOR]' + I1i11i + '[COLOR=orange]     Author(s): [/COLOR]' + Iii + '[COLOR=orange][CR][CR]Version: [/COLOR]' + iIIiIiI1I1 + '[COLOR=orange]     Created: [/COLOR]' + ooO + '[COLOR=orange]     Updated: [/COLOR]' + oOoO0 + '[COLOR=orange][CR][CR]Repository: [/COLOR]' + O0o + oO0OoO00o + '[COLOR=orange]     Add-on Type(s): [/COLOR]' + iiOO0O0Ooo + i1i1iII1 + oOooO0 + I111i1i1111 + O0OoO0ooOO0o + i1iI1 + Ii1II1I11i1 + IIII1 )
 if 83 - 83: iIII % o0oOOo0O0Ooo % I1IiiI . iIii1I11I1II1 - iIII
 if 88 - 88: OoooooooOO
 if os . path . exists ( os . path . join ( OO0o , OOOOO0O00 ) ) :
  if 'script.module' in OOOOO0O00 or 'repo' in OOOOO0O00 :
   IIii ( '' , '[COLOR=orange]Already installed[/COLOR]' , '' , '' , Ii , '' , '' , '' )
  else :
   IIii ( '' , '[COLOR=orange]Already installed -[/COLOR] Click here to run the add-on' , OOOOO0O00 , 'run_addon' , Ii , '' , '' , '' )
   if 84 - 84: OoOoOO00 / oOoO0o00OO0 * OOo00O0 / ooOo - i11iIiiIii . Oo0Ooo
   if 60 - 60: I1ii11iIi11i * I1IiiI
 if I1i11i == '' :
  IIii ( '' , '[COLOR=yellow]Sorry request failed due to high traffic on server, please try again[/COLOR]' , '' , '' , Ii , '' , '' , '' )
  if 17 - 17: Oo % Oo0Ooo / I1ii11iIi11i . iIII * Oo - II111iiii
  if 41 - 41: iI1iiIiiII
 elif I1i11i != '' :
  if 77 - 77: iIi1i1ii1
  if ( Ii111 == '' ) and ( oOoooooOoO == '' ) and ( I111i1i1111 == '' ) and ( O0OoO0ooOO0o == '' ) :
   IIii ( 'addon' , '[COLOR=yellow][FULL DETAILS][/COLOR] No problems reported' , IIIii , 'text_guide' , Ii , '' , '' , IIIii )
   if 65 - 65: II111iiii . I1IiiI % ooOo * OoO0O00
  if ( Ii111 != '' and I111i1i1111 == '' ) or ( oOoooooOoO != '' and I111i1i1111 == '' ) or ( O0OoO0ooOO0o != '' and I111i1i1111 == '' ) :
   IIii ( 'addon' , '[COLOR=yellow][FULL DETAILS][/COLOR][COLOR=orange] Possbile problems reported[/COLOR]' , IIIii , 'text_guide' , Ii , '' , '' , IIIii )
   if 38 - 38: OoOoOO00 / OOo00O0 % Oo0Ooo
  if I111i1i1111 != '' :
   IIii ( 'addon' , '[COLOR=yellow][FULL DETAILS][/COLOR][COLOR=red] Add-on now depreciated[/COLOR]' , IIIii , 'text_guide' , Ii , '' , '' , IIIii )
   if 11 - 11: OOo00O0 - ooOo + II111iiii - iIii1I11I1II1
   if 7 - 7: iIII - oOoO0o00OO0 / II111iiii * iI1iiIiiII . OOo00O0 * OOo00O0
  if I111i1i1111 == '' :
   if 61 - 61: oOoO0o00OO0 % oOO - OoO0O00 / Oo0Ooo
   if O0o != '' and 'superrepo' not in O0o :
    Oo0oO00o ( '[COLOR=lime][INSTALL - Recommended] [/COLOR]' + I1i11i , I1i11i , '' , 'addon_install_zero' , 'Install.png' , '' , '' , Ii1II1I11i1 , ooOOoO , OOOoOoO , O0o , OOOOO0O00 , Iii , ii1I1IiiI1ii1i , iIIIII1ii1I )
    Oo0oO00o ( '[COLOR=lime][INSTALL - Backup Option] [/COLOR]' + I1i11i , I1i11i , '' , 'addon_install' , 'Install.png' , '' , '' , Ii1II1I11i1 , Ii1i1iI , OOOoOoO , O0o , OOOOO0O00 , Iii , ii1I1IiiI1ii1i , iIIIII1ii1I )
    if 4 - 4: OoooooooOO - i1IIi % iI1iiIiiII - Oo * o0oOOo0O0Ooo
   if O0o == '' or 'superrepo' in O0o :
    Oo0oO00o ( '[COLOR=lime][INSTALL] [/COLOR]' + I1i11i + ' - THIS IS NOT IN A SELF UPDATING REPO' , I1i11i , '' , 'addon_install' , 'Install.png' , '' , '' , Ii1II1I11i1 , Ii1i1iI , OOOoOoO , O0o , OOOOO0O00 , Iii , ii1I1IiiI1ii1i , iIIIII1ii1I )
    if 85 - 85: OoooooooOO * iIii1I11I1II1 . OOo00O0 / OoooooooOO % I1IiiI % O0
    if 36 - 36: iI1iiIiiII / II111iiii / iIII / iIII + I1ii11iIi11i
  if o00iiI1Ii1 != 'None' :
   IIii ( '' , '[COLOR=dodgerblue][VIDEO][/COLOR]  Preview' , oOOoo , 'play_video' , 'Video_Guide.png' , '' , '' , '' )
   if 95 - 95: iIII
  if oOOoo != 'None' :
   IIii ( '' , '[COLOR=dodgerblue][VIDEO][/COLOR]  ' + I1I , oOOoo , 'play_video' , 'Video_Guide.png' , '' , '' , '' )
   if 51 - 51: II111iiii + iIII . i1IIi . I1ii11iIi11i + OoOoOO00 * I1IiiI
  if iII1111III1I != 'None' :
   IIii ( '' , '[COLOR=dodgerblue][VIDEO][/COLOR]  ' + ooooo , iII1111III1I , 'play_video' , 'Video_Guide.png' , '' , '' , '' )
   if 72 - 72: ooOo + ooOo / II111iiii . OoooooooOO % iI1iiIiiII
  if ii11i != 'None' :
   IIii ( '' , '[COLOR=dodgerblue][VIDEO][/COLOR]  ' + i11IIIiI1I , ii11i , 'play_video' , 'Video_Guide.png' , '' , '' , '' )
   if 49 - 49: ooOo . OoO0O00 - Oo0Ooo * OoooooooOO . Oo0Ooo
  if O00oOo00o0o != 'None' :
   IIii ( '' , '[COLOR=dodgerblue][VIDEO][/COLOR]  ' + o0iiiI1I1iIIIi1 , O00oOo00o0o , 'play_video' , 'Video_Guide.png' , '' , '' , '' )
   if 2 - 2: OoooooooOO % Oo
  if O00oO0 != 'None' :
   IIii ( '' , '[COLOR=dodgerblue][VIDEO][/COLOR]  ' + IiiI1iiiiI1iI , O00oO0 , 'play_video' , 'Video_Guide.png' , '' , '' , '' )
   if 63 - 63: I1IiiI % iIii1I11I1II1
  if O0Oo00OoOo != 'None' :
   IIii ( '' , '[COLOR=dodgerblue][VIDEO][/COLOR]  ' + iIiiiii1i , O0Oo00OoOo , 'play_video' , 'Video_Guide.png' , '' , '' , '' )
   if 39 - 39: OOo00O0 / II111iiii / I1ii11iIi11i % I1IiiI
  if ii1ii111 != 'None' :
   IIii ( '' , '[COLOR=dodgerblue][VIDEO][/COLOR]  ' + iiIi1IIiI , ii1ii111 , 'play_video' , 'Video_Guide.png' , '' , '' , '' )
   if 89 - 89: iIi1i1ii1 + OoooooooOO + iIi1i1ii1 * i1IIi + iIii1I11I1II1 % oOoO0o00OO0
  if i11111I1I != 'None' :
   IIii ( '' , '[COLOR=dodgerblue][VIDEO][/COLOR]  ' + i1oO0OO0 , i11111I1I , 'play_video' , 'Video_Guide.png' , '' , '' , '' )
   if 59 - 59: Oo + i11iIiiIii
  if ii1Oo0000oOo != 'None' :
   IIii ( '' , '[COLOR=dodgerblue][VIDEO][/COLOR]  ' + o0O0Oo00 , ii1Oo0000oOo , 'play_video' , 'Video_Guide.png' , '' , '' , '' )
   if 88 - 88: i11iIiiIii - oOO
  if I11o0oO00oO0o0o0 != 'None' :
   IIii ( '' , '[COLOR=dodgerblue][VIDEO][/COLOR]  ' + O0Oo0o000oO , I11o0oO00oO0o0o0 , 'play_video' , 'Video_Guide.png' , '' , '' , '' )
   if 67 - 67: Oo . Oo0Ooo + OoOoOO00 - OoooooooOO
   if 70 - 70: Oo / II111iiii - iIii1I11I1II1 - OOo00O0
def IiiiIi1i ( url ) :
 IIii ( 'folder' , 'Anime' , url + '&genre=anime' , 'grab_addons' , 'anime.png' , '' , '' , '' )
 IIii ( 'folder' , 'Audiobooks' , url + '&genre=audiobooks' , 'grab_addons' , 'audiobooks.png' , '' , '' , '' )
 IIii ( 'folder' , 'Comedy' , url + '&genre=comedy' , 'grab_addons' , 'comedy.png' , '' , '' , '' )
 IIii ( 'folder' , 'Comics' , url + '&genre=comics' , 'grab_addons' , 'comics.png' , '' , '' , '' )
 IIii ( 'folder' , 'Documentary' , url + '&genre=documentary' , 'grab_addons' , 'documentary.png' , '' , '' , '' )
 IIii ( 'folder' , 'Downloads' , url + '&genre=downloads' , 'grab_addons' , 'downloads.png' , '' , '' , '' )
 IIii ( 'folder' , 'Food' , url + '&genre=food' , 'grab_addons' , 'food.png' , '' , '' , '' )
 IIii ( 'folder' , 'Gaming' , url + '&genre=gaming' , 'grab_addons' , 'gaming.png' , '' , '' , '' )
 IIii ( 'folder' , 'Health' , url + '&genre=health' , 'grab_addons' , 'health.png' , '' , '' , '' )
 IIii ( 'folder' , 'How To...' , url + '&genre=howto' , 'grab_addons' , 'howto.png' , '' , '' , '' )
 IIii ( 'folder' , 'Kids' , url + '&genre=kids' , 'grab_addons' , 'kids.png' , '' , '' , '' )
 IIii ( 'folder' , 'Live TV' , url + '&genre=livetv' , 'grab_addons' , 'livetv.png' , '' , '' , '' )
 IIii ( 'folder' , 'Movies' , url + '&genre=movies' , 'grab_addons' , 'movies.png' , '' , '' , '' )
 IIii ( 'folder' , 'Music' , url + '&genre=music' , 'grab_addons' , 'music.png' , '' , '' , '' )
 IIii ( 'folder' , 'News' , url + '&genre=news' , 'grab_addons' , 'news.png' , '' , '' , '' )
 IIii ( 'folder' , 'Photos' , url + '&genre=photos' , 'grab_addons' , 'photos.png' , '' , '' , '' )
 IIii ( 'folder' , 'Podcasts' , url + '&genre=podcasts' , 'grab_addons' , 'podcasts.png' , '' , '' , '' )
 IIii ( 'folder' , 'Radio' , url + '&genre=radio' , 'grab_addons' , 'radio.png' , '' , '' , '' )
 IIii ( 'folder' , 'Religion' , url + '&genre=religion' , 'grab_addons' , 'religion.png' , '' , '' , '' )
 IIii ( 'folder' , 'Space' , url + '&genre=space' , 'grab_addons' , 'space.png' , '' , '' , '' )
 IIii ( 'folder' , 'Sports' , url + '&genre=sports' , 'grab_addons' , 'sports.png' , '' , '' , '' )
 IIii ( 'folder' , 'Technology' , url + '&genre=tech' , 'grab_addons' , 'tech.png' , '' , '' , '' )
 IIii ( 'folder' , 'Trailers' , url + '&genre=trailers' , 'grab_addons' , 'trailers.png' , '' , '' , '' )
 IIii ( 'folder' , 'TV Shows' , url + '&genre=tv' , 'grab_addons' , 'tv.png' , '' , '' , '' )
 IIii ( 'folder' , 'Misc.' , url + '&genre=other' , 'grab_addons' , 'other.png' , '' , '' , '' )
 if 4 - 4: iIi1i1ii1 / i11iIiiIii / Oo
 if o0O . getSetting ( 'adult' ) == 'true' :
  IIii ( 'folder' , 'XXX' , url + '&genre=adult' , 'grab_addons' , 'adult.png' , '' , '' , '' )
  if 91 - 91: iIii1I11I1II1 % o0oOOo0O0Ooo . iIii1I11I1II1 % i1IIi / II111iiii * OoOoOO00
  if 10 - 10: II111iiii . OOo00O0
def I1i ( name , zip_link , repo_link , repo_id , addon_id , provider_name , forum , data_path ) :
 forum = str ( forum )
 repo_id = str ( repo_id )
 OOOOooO0oO00O0o = 1
 ooOO00oOOo000 = 1
 IIi = 1
 i11II11II1 = xbmc . translatePath ( os . path . join ( OO0o , addon_id ) )
 if 10 - 10: I1IiiI / Oo0Ooo % I1ii11iIi11i * oOO
 if os . path . exists ( i11II11II1 ) :
  I11oo0ooOO = 1
  if 24 - 24: OoO0O00 % OoO0O00 * iIii1I11I1II1
 else :
  I11oo0ooOO = 0
  if 50 - 50: OoO0O00 . i11iIiiIii - ooOo . ooOo
 I11I = xbmc . translatePath ( os . path . join ( ooOooo000oOO , name + '.zip' ) )
 iIIII1i = xbmc . translatePath ( os . path . join ( OO0o , addon_id ) )
 if 76 - 76: OOo00O0 + oOO
 O0OoO000O0OO . create ( "Installing Addon" , "Please wait whilst your addon is installed" , '' , '' )
 if 30 - 30: i11iIiiIii % iIii1I11I1II1 . oOoO0o00OO0 % iIii1I11I1II1
 try :
  downloader . download ( repo_link , I11I , O0OoO000O0OO )
  oOO00oO00O0OO ( I11I , OO0o , O0OoO000O0OO )
  if 96 - 96: OoOoOO00
 except :
  if 54 - 54: iIi1i1ii1
  try :
   downloader . download ( zip_link , I11I , O0OoO000O0OO )
   oOO00oO00O0OO ( I11I , OO0o , O0OoO000O0OO )
   if 84 - 84: iIi1i1ii1 - I1ii11iIi11i / oOoO0o00OO0
  except :
   if 13 - 13: iIII - Oo0Ooo - oOO
   try :
    if not os . path . exists ( iIIII1i ) :
     os . makedirs ( iIIII1i )
     if 92 - 92: oOO / OoOoOO00 * OoO0O00 . oOoO0o00OO0 % II111iiii
    iiiiI = oooOo0OOOoo0 ( data_path ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
    O0OoOoO00O = re . compile ( 'href="(.+?)"' , re . DOTALL ) . findall ( iiiiI )
    if 96 - 96: I1IiiI % Oo0Ooo . I1ii11iIi11i + Oo
    for Ii11Iii1i1ii in O0OoOoO00O :
     Ii1i1i1111 = xbmc . translatePath ( os . path . join ( iIIII1i , Ii11Iii1i1ii ) )
     if 57 - 57: iI1iiIiiII % II111iiii
     if addon_id not in Ii11Iii1i1ii and '/' not in Ii11Iii1i1ii :
      if 67 - 67: oOO + I1IiiI * i11iIiiIii - ooOo / iIII % OOo00O0
      try :
       O0OoO000O0OO . update ( 0 , "Downloading [COLOR=yellow]" + Ii11Iii1i1ii + '[/COLOR]' , '' , 'Please wait...' )
       downloader . download ( data_path + Ii11Iii1i1ii , Ii1i1i1111 , O0OoO000O0OO )
       if 92 - 92: iI1iiIiiII - ooOo - oOO % OoooooooOO / Oo
      except :
       print "failed to install" + Ii11Iii1i1ii
       if 19 - 19: Oo0Ooo - OoO0O00
     if '/' in Ii11Iii1i1ii and '..' not in Ii11Iii1i1ii and 'http' not in Ii11Iii1i1ii :
      ooo0oooo0 = data_path + Ii11Iii1i1ii
      OOO0ooo ( Ii1i1i1111 , ooo0oooo0 )
      if 7 - 7: o0oOOo0O0Ooo + i1IIi . I1IiiI / Oo0Ooo
   except :
    oOOoO0 . ok ( "Error downloading add-on" , 'There was an error downloading [COLOR=yellow]' + name , '[/COLOR]Please consider updating the add-on portal with details or report the error on the forum at [COLOR=orange]www.noobs[/COLOR][COLOR=dodgerblue]and[/COLOR][COLOR=orange]nerds.com[/COLOR]' )
    OOOOooO0oO00O0o = 0
    if 22 - 22: oOO - oOO % Oo . iIi1i1ii1 + ooOo
 if OOOOooO0oO00O0o == 1 :
  time . sleep ( 1 )
  O0OoO000O0OO . update ( 0 , "[COLOR=yellow]" + name + '[/COLOR]  [COLOR=lime]Successfully Installed[/COLOR]' , '' , 'Now installing repository' )
  time . sleep ( 1 )
  Oo00OOo00O = xbmc . translatePath ( os . path . join ( OO0o , repo_id ) )
  if 81 - 81: iIII . o0oOOo0O0Ooo / iIi1i1ii1
  if ( repo_id != 'repository.xbmc.org' ) and not ( os . path . exists ( Oo00OOo00O ) ) and ( repo_id != '' ) and ( 'superrepo' not in repo_id ) :
   Iii111Ii ( repo_id )
   if 54 - 54: iI1iiIiiII * iIi1i1ii1 - OoooooooOO % I1IiiI + O0
  xbmc . sleep ( 2000 )
  if 6 - 6: I1ii11iIi11i - II111iiii / ooOo + i11iIiiIii + Oo
  if os . path . exists ( i11II11II1 ) and I11oo0ooOO == 0 :
   O0O0o0o0o = 'http://noobsandnerds.com/TI/AddonPortal/downloadcount.php?id=%s' % ( addon_id )
   oooOo0OOOoo0 ( O0O0o0o0o )
   if 9 - 9: Oo0Ooo + OoOoOO00 - iIii1I11I1II1 - iI1iiIiiII + o0oOOo0O0Ooo
  o000O0OOoo ( name , addon_id )
  xbmc . executebuiltin ( 'UpdateLocalAddons' )
  xbmc . sleep ( 1000 )
  xbmc . executebuiltin ( 'UpdateAddonRepos' )
  if 60 - 60: I1IiiI * iIi1i1ii1 % OoO0O00 + ooOo
  if ooOO00oOOo000 == 0 :
   oOOoO0 . ok ( name + " Install Complete" , 'The add-on has been successfully installed but' , 'there was an error installing the repository.' , 'This will mean the add-on fails to update' )
   if 52 - 52: i1IIi
  if IIi == 0 :
   oOOoO0 . ok ( name + " Install Complete" , 'The add-on has been successfully installed but' , 'there was an error installing modules.' , 'This could result in errors with the add-on.' )
   if 84 - 84: iI1iiIiiII / iIII
  if IIi != 0 and ooOO00oOOo000 != 0 and forum != 'None' :
   oOOoO0 . ok ( name + " Install Complete" , 'Please support the developer(s) [COLOR=dodgerblue]' + provider_name , '[/COLOR]Support for this add-on can be found at [COLOR=yellow]' + forum , '[/COLOR][CR]Visit [COLOR=orange]www.noobs[/COLOR][COLOR=dodgerblue]and[/COLOR][COLOR=orange]nerds.com[/COLOR] for all your Kodi needs.' )
   if 86 - 86: OoOoOO00 * II111iiii - O0 . OoOoOO00 % iIii1I11I1II1 / Oo
  if IIi != 0 and ooOO00oOOo000 != 0 and forum == 'None' :
   oOOoO0 . ok ( name + " Install Complete" , 'Please support the developer(s) [COLOR=dodgerblue]' + provider_name , '[/COLOR]No details of forum support have been given.' )
   if 11 - 11: I1IiiI * ooOo + I1ii11iIi11i / I1ii11iIi11i
 xbmc . executebuiltin ( 'Container.Refresh' )
 if 37 - 37: i11iIiiIii + i1IIi
 if 23 - 23: OOo00O0 + oOoO0o00OO0 . OoOoOO00 * I1IiiI + I1ii11iIi11i
def I1iIi1iiiIiI ( name , contenttypes , repo_link , repo_id , addon_id , provider_name , forum , data_path ) :
 i11II11II1 = xbmc . translatePath ( os . path . join ( OO0o , addon_id ) )
 forum = str ( forum )
 if 41 - 41: I1ii11iIi11i * oOO - iI1iiIiiII + Oo0Ooo
 if not os . path . exists ( i11II11II1 ) :
  IiIIIII11I = 1
  if 17 - 17: OoooooooOO + Oo * oOoO0o00OO0 * OoOoOO00
 else :
  IiIIIII11I = 0
  if 36 - 36: O0 + Oo0Ooo
 repo_id = str ( repo_id )
 Oo00OOo00O = xbmc . translatePath ( os . path . join ( OO0o , repo_id ) )
 if 5 - 5: Oo0Ooo * OoOoOO00
 if os . path . exists ( i11II11II1 ) :
  I11oo0ooOO = 1
  ii1I11iIiIII1 = oOOoO0 . yesno ( 'Add-on Already Installed' , 'This add-on has already been detected on your system. Would you like to remove the old version and re-install? There should be no need for this unless you\'ve manually opened up the add-on code and edited in a text editor.' )
  if 52 - 52: o0oOOo0O0Ooo * iIII + OoOoOO00
  if ii1I11iIiIII1 == 1 :
   IiiiIiiI ( i11II11II1 )
   IiIIIII11I = 1
 else :
  I11oo0ooOO = 0
  if 72 - 72: i1IIi
 if IiIIIII11I == 1 :
  if 82 - 82: OoOoOO00 + OoooooooOO / i11iIiiIii * I1ii11iIi11i . OoooooooOO
  if ( repo_id != 'repository.xbmc.org' ) and not ( os . path . exists ( Oo00OOo00O ) ) and ( repo_id != '' ) and ( 'superrepo' not in repo_id ) :
   Iii111Ii ( repo_id )
   if 63 - 63: I1ii11iIi11i
  if not os . path . exists ( i11II11II1 ) :
   os . makedirs ( i11II11II1 )
   if 6 - 6: oOO / I1ii11iIi11i
  oOooO00o0O = os . path . join ( OO0o , addon_id , 'addon.xml' )
  OOo0iiIii1IIi = os . path . join ( OO0o , addon_id , 'default.py' )
  if 10 - 10: i11iIiiIii - o0oOOo0O0Ooo % iIii1I11I1II1
  shutil . copyfile ( Oo00OOOOO , oOooO00o0O )
  if 49 - 49: ooOo
  OOOOoOo00OO = open ( os . path . join ( oOooO00o0O ) , mode = 'r' )
  OooOo0o0Oo = OOOOoOo00OO . read ( )
  OOOOoOo00OO . close ( )
  if 71 - 71: iIii1I11I1II1 - Oo . I1IiiI % OoooooooOO + Oo
  if 26 - 26: Oo0Ooo + Oo / OoO0O00 % OoOoOO00 % I1ii11iIi11i + II111iiii
  i11I1I1iiI = re . compile ( 'testid[\s\S]*?' ) . findall ( OooOo0o0Oo )
  iIIII = i11I1I1iiI [ 0 ] if ( len ( i11I1I1iiI ) > 0 ) else 'None'
  I1i1iii1Ii = re . compile ( 'testname[\s\S]*?' ) . findall ( OooOo0o0Oo )
  O00o0 = I1i1iii1Ii [ 0 ] if ( len ( I1i1iii1Ii ) > 0 ) else 'None'
  iIO0O00OOo = re . compile ( 'testprovider[\s\S]*?' ) . findall ( OooOo0o0Oo )
  OoOOo = iIO0O00OOo [ 0 ] if ( len ( iIO0O00OOo ) > 0 ) else 'None'
  iii1 = re . compile ( 'testprovides[\s\S]*?' ) . findall ( OooOo0o0Oo )
  oOO0oo = iii1 [ 0 ] if ( len ( iii1 ) > 0 ) else 'None'
  II1iIi1IiIii = OooOo0o0Oo . replace ( iIIII , addon_id ) . replace ( O00o0 , name ) . replace ( OoOOo , provider_name ) . replace ( oOO0oo , contenttypes )
  if 30 - 30: oOO % OOo00O0 * Oo - I1ii11iIi11i * iI1iiIiiII % oOO
  iiiiI11ii = open ( oOooO00o0O , mode = 'w+' )
  iiiiI11ii . write ( str ( II1iIi1IiIii ) )
  iiiiI11ii . close ( )
  if 96 - 96: OOo00O0 . O0 / OOo00O0 % O0
  o0o000 = open ( OOo0iiIii1IIi , mode = 'w' )
  o0o000 . write ( 'import xbmcplugin,xbmcgui,xbmc,xbmcaddon,os,sys\nAddonID="' + addon_id + '"\nAddonName="' + name + '"\ndialog=xbmcgui.Dialog()\nxbmc.executebuiltin("UpdateLocalAddons")\nxbmc.executebuiltin("UpdateAddonRepos")\nchoice=dialog.yesno(AddonName+" Add-on Requires Update","This add-on may still be in the process of the updating, would you like check the status of your add-on updates or try re-installing via the Total Installer backup method? We highly recommend checking for updates.",yeslabel="Install Option 2", nolabel="Check Updates")\nif choice==0: xbmc.executebuiltin(\'ActivateWindow(10040,"addons://outdated/",return)\')\nelse: xbmc.executebuiltin(\'ActivateWindow(10001,"plugin://plugin.program.mediacube/?mode=grab_addons&url=%26redirect%26addonid%3d\'+AddonID+\'")\')\nxbmcplugin.endOfDirectory(int(sys.argv[1]))' )
  o0o000 . close ( )
  if 50 - 50: iIII % i1IIi
  xbmc . sleep ( 1000 )
  if 21 - 21: OoooooooOO - iIii1I11I1II1
  if os . path . exists ( i11II11II1 ) and I11oo0ooOO == 0 :
   O0O0o0o0o = 'http://noobsandnerds.com/TI/AddonPortal/downloadcount.php?id=%s' % ( addon_id )
   oooOo0OOOoo0 ( O0O0o0o0o )
   if 93 - 93: ooOo - o0oOOo0O0Ooo % OoOoOO00 . OoOoOO00 - oOO
  xbmc . executebuiltin ( 'UpdateLocalAddons' )
  xbmc . executebuiltin ( 'UpdateAddonRepos' )
  oOOoO0 . ok ( name + " Install Complete" , '[COLOR=dodgerblue]' + name + '[/COLOR] has now been installed, please allow a few moments for Kodi to update the add-on and it\'s dependencies.' )
  if 90 - 90: oOO + II111iiii * I1ii11iIi11i / iI1iiIiiII . o0oOOo0O0Ooo + o0oOOo0O0Ooo
 xbmc . executebuiltin ( 'Container.Refresh' )
 if 40 - 40: oOO / OoOoOO00 % i11iIiiIii % I1ii11iIi11i / I1IiiI
 if 62 - 62: i1IIi - OoOoOO00
def oo0O0oo ( name , contenttypes , repo_link , repo_id , addon_id , provider_name , forum , data_path ) :
 Oo00OOo00O = xbmc . translatePath ( os . path . join ( OO0o , repo_id ) )
 i11II11II1 = xbmc . translatePath ( os . path . join ( OO0o , addon_id ) )
 if 14 - 14: O0 / i1IIi / Oo0Ooo + iIii1I11I1II1
 if os . path . exists ( i11II11II1 ) :
  if 96 - 96: OOo00O0
  ii1I11iIiIII1 = oOOoO0 . yesno ( 'Add-on Already Installed' , 'This add-on has already been detected on your system. Would you like to remove the old version and re-install? There should be no need for this unless you\'ve manually opened up the add-on code and edited in a text editor.' )
  if 18 - 18: OOo00O0 * oOoO0o00OO0 - iI1iiIiiII
  if ii1I11iIiIII1 == 1 :
   IiiiIiiI ( i11II11II1 )
   if 31 - 31: Oo0Ooo - O0 % OoOoOO00 % ooOo
 if os . path . exists ( Oo00OOo00O ) :
  if 45 - 45: I1ii11iIi11i + II111iiii * i11iIiiIii
  if os . path . exists ( i11II11II1 ) :
   I11oo0ooOO = 1
   if 13 - 13: OoooooooOO * ooOo - iI1iiIiiII / Oo + oOoO0o00OO0 + iIII
  else :
   I11oo0ooOO = 0
   if 39 - 39: iIii1I11I1II1 - OoooooooOO
  ii1I11iIiIII1 = oOOoO0 . yesno ( 'WARNING!' , '[COLOR=orange]This Add-on may be unlawful in your region.[/COLOR][CR]The repository required for installation of this add-on has been detected on your system. Would you like to continue to the Kodi addon browser to install?' )
  if 81 - 81: I1ii11iIi11i - O0 * OoooooooOO
  if ii1I11iIiIII1 == 1 :
   if 23 - 23: II111iiii / ooOo
   if 'video' in contenttypes :
    xbmc . executebuiltin ( 'ActivateWindow(10040,"addons://' + repo_id + '/xbmc.addon.video/?",return)' )
    if 28 - 28: Oo0Ooo * oOO - OoO0O00
   elif 'executable' in contenttypes :
    xbmc . executebuiltin ( 'ActivateWindow(10040,"addons://' + repo_id + '/xbmc.addon.executable/?",return)' )
    if 19 - 19: oOoO0o00OO0
   elif 'audio' in contenttypes :
    xbmc . executebuiltin ( 'ActivateWindow(10040,"addons://' + repo_id + '/xbmc.addon.audio/?",return)' )
    if 67 - 67: O0 % iIii1I11I1II1 / iIII . i11iIiiIii - iI1iiIiiII + O0
  xbmc . sleep ( 2000 )
  if 27 - 27: Oo
  if os . path . exists ( i11II11II1 ) and I11oo0ooOO == 0 :
   O0O0o0o0o = 'http://noobsandnerds.com/TI/AddonPortal/downloadcount.php?id=%s' % ( addon_id )
   oooOo0OOOoo0 ( O0O0o0o0o )
   if 89 - 89: II111iiii / ooOo
 else :
  oOOoO0 . ok ( 'WARNING!' , '[COLOR=orange]This add-on may possibly be unlawful in your region.[/COLOR][CR]If you\'ve investigated the legality of it and are happy to install then you must have the following repository installed: [COLOR=dodgerblue]' + repo_id + '[/COLOR]' )
  if 14 - 14: Oo . I1IiiI * oOO + II111iiii - oOO + Oo
 xbmc . executebuiltin ( 'Container.Refresh' )
 if 18 - 18: ooOo - o0oOOo0O0Ooo - I1IiiI - I1IiiI
 if 54 - 54: Oo0Ooo + I1IiiI / OOo00O0 . I1IiiI * OoOoOO00
def IIiIiiiIIIIi1 ( name , contenttypes , repo_link , repo_id , addon_id , provider_name , forum , data_path ) :
 oOOoO0 . ok ( 'Add-on Not Approved' , 'Sorry there are no repository details for this add-on and it\'s been marked as potentially giving access to unlawful content. The most likely cause for this is the add-on has only been released via social media groups.' )
 if 39 - 39: OoO0O00 / iI1iiIiiII / iIi1i1ii1
 if 81 - 81: oOoO0o00OO0 / OoO0O00 % OoooooooOO * ooOo / ooOo
def IiiI ( ) :
 IIii ( '' , o0OOO + ' Storage Folder Check' , 'url' , 'check_storage' , 'Check_Download.png' , '' , '' , '' )
 IIii ( 'folder' , 'Completely remove an add-on (inc. passwords)' , 'plugin' , 'addon_removal_menu' , 'Remove_Addon.png' , '' , '' , '' )
 IIii ( '' , 'Make Add-ons Gotham/Helix Compatible' , 'none' , 'gotham' , 'Gotham_Compatible.png' , '' , '' , '' )
 IIii ( '' , 'Make Skins Kodi (Helix) Compatible' , 'none' , 'helix' , 'Kodi_Compatible.png' , '' , '' , '' )
 IIii ( '' , 'Hide my add-on passwords' , 'none' , 'hide_passwords' , 'Hide_Passwords.png' , '' , '' , '' )
 IIii ( 'folder' , 'OnTapp.TV / OSS Integration' , 'none' , 'addonfix' , 'Addon_Fixes.png' , '' , '' , '' )
 IIii ( 'folder' , 'Test My Download Speed' , 'none' , 'speedtest_menu' , 'Speed_Test.png' , '' , '' , '' )
 IIii ( '' , 'Unhide my add-on passwords' , 'none' , 'unhide_passwords' , 'Unhide_Passwords.png' , '' , '' , '' )
 IIii ( '' , 'Update My Add-ons (Force Refresh)' , 'none' , 'update' , 'Update_Addons.png' , '' , '' , '' )
 IIii ( '' , 'Wipe All Add-on Settings (addon_data)' , 'url' , 'remove_addon_data' , 'Delete_Addon_Data.png' , '' , '' , '' )
 if 19 - 19: II111iiii
 if 72 - 72: OoooooooOO / I1IiiI + iI1iiIiiII / OoOoOO00 * iI1iiIiiII
def Ii1iIi111i1i1 ( sign ) :
 IIii ( '' , '[COLOR=orange]noobs[/COLOR][COLOR=dodgerblue]and[/COLOR][COLOR=orange]nerds[/COLOR] Keyword Install' , OOO00O , 'keywords' , 'Keywords.png' , '' , '' , '' )
 IIii ( 'folder' , '[COLOR=darkcyan][Manual Search][/COLOR] Search By Name' , 'pass=' + sign + '&name=' , 'search_addons' , 'Search_Addons.png' , '' , '' , '' )
 IIii ( 'folder' , '[COLOR=darkcyan][Manual Search][/COLOR] Search By Author' , 'pass=' + sign + '&author=' , 'search_addons' , 'Search_Addons.png' , '' , '' , '' )
 IIii ( 'folder' , '[COLOR=darkcyan][Manual Search][/COLOR] Search In Description' , 'pass=' + sign + '&desc=' , 'search_addons' , 'Search_Addons.png' , '' , '' , '' )
 IIii ( 'folder' , '[COLOR=darkcyan][Manual Search][/COLOR] Search By Add-on ID' , 'pass=' + sign + '&addonid=' , 'search_addons' , 'Search_Addons.png' , '' , '' , '' )
 IIii ( 'folder' , '[COLOR=dodgerblue][Filter Results][/COLOR] By Genres' , 'pass=' + sign , 'addon_genres' , 'Search_Genre.png' , '' , '' , '' )
 IIii ( 'folder' , '[COLOR=dodgerblue][Filter Results][/COLOR] By Countries' , 'pass=' + sign , 'addon_countries' , 'Search_Country.png' , '' , '' , '' )
 IIii ( 'folder' , '[COLOR=dodgerblue][Filter Results][/COLOR] By Kodi Categories' , 'pass=' + sign , 'addon_categories' , 'Search_Category.png' , '' , '' , '' )
 IIii ( '' , '[COLOR=orange][Kodi Add-on Browser][/COLOR] Install From Zip' , '' , 'install_from_zip' , 'Search_Addons.png' , '' , '' , '' )
 IIii ( '' , '[COLOR=orange][Kodi Add-on Browser][/COLOR] Browse My Repositories' , '' , 'browse_repos' , 'Search_Addons.png' , '' , '' , '' )
 IIii ( '' , '[COLOR=orange][Kodi Add-on Browser][/COLOR] Check For Add-on Updates' , '' , 'check_updates' , 'Search_Addons.png' , '' , '' , '' )
 if 45 - 45: OoOoOO00 . o0oOOo0O0Ooo % OoOoOO00 * I1IiiI % I1IiiI
 if 63 - 63: iIi1i1ii1
def oo00ooOoo ( ) :
 for file in glob . glob ( os . path . join ( OO0o , '*' ) ) :
  I1i11i = str ( file ) . replace ( OO0o , '[COLOR=red]REMOVE [/COLOR]' ) . replace ( 'plugin.' , '[COLOR=dodgerblue](PLUGIN) [/COLOR]' ) . replace ( 'audio.' , '' ) . replace ( 'video.' , '' ) . replace ( 'skin.' , '[COLOR=yellow](SKIN) [/COLOR]' ) . replace ( 'repository.' , '[COLOR=orange](REPOSITORY) [/COLOR]' ) . replace ( 'script.' , '[COLOR=cyan](SCRIPT) [/COLOR]' ) . replace ( 'metadata.' , '[COLOR=orange](METADATA) [/COLOR]' ) . replace ( 'service.' , '[COLOR=pink](SERVICE) [/COLOR]' ) . replace ( 'weather.' , '[COLOR=green](WEATHER) [/COLOR]' ) . replace ( 'module.' , '[COLOR=orange](MODULE) [/COLOR]' )
  iii1IIIiiiI = ( os . path . join ( file , 'icon.png' ) )
  OoO00oo00 = ( os . path . join ( file , 'fanart.jpg' ) )
  IIii ( '' , I1i11i , file , 'remove_addons' , iii1IIIiiiI , OoO00oo00 , '' , '' )
  if 76 - 76: OoooooooOO + Oo0Ooo % iIII . OoO0O00 + II111iiii
  if 70 - 70: I1IiiI / oOoO0o00OO0
def IIiiiiIiIIii ( ) :
 o0O . openSettings ( sys . argv [ 0 ] )
 xbmc . executebuiltin ( 'Container.Refresh' )
 if 86 - 86: oOoO0o00OO0 / o0oOOo0O0Ooo - o0oOOo0O0Ooo + I1ii11iIi11i + ooOo
 if 33 - 33: o0oOOo0O0Ooo . OOo00O0 . iIII . i1IIi
def i1II1iII ( sourcefile , destfile , message_header , message1 , message2 , message3 , exclude_dirs , exclude_files ) :
 II1i = zipfile . ZipFile ( destfile , 'w' , zipfile . ZIP_DEFLATED )
 o0OO00oo = len ( sourcefile )
 i1i1IiIiIi1Ii = [ ]
 oO0ooOO = [ ]
 if 16 - 16: Oo0Ooo + oOO / Oo0Ooo / OoO0O00 % ooOo % I1ii11iIi11i
 O0OoO000O0OO . create ( message_header , message1 , message2 , message3 )
 if 22 - 22: II111iiii * OoO0O00 * oOoO0o00OO0 + I1ii11iIi11i * o0oOOo0O0Ooo
 for oo0o0 , oO0ooOoO , ooO0000o00O in os . walk ( sourcefile ) :
  if 91 - 91: oOoO0o00OO0 / O0 - iI1iiIiiII . I1IiiI
  for file in ooO0000o00O :
   oO0ooOO . append ( file )
   if 82 - 82: iIII * Oo / ooOo
 IiiIiI = len ( oO0ooOO )
 if 23 - 23: oOoO0o00OO0
 for oo0o0 , oO0ooOoO , ooO0000o00O in os . walk ( sourcefile ) :
  if 40 - 40: o0oOOo0O0Ooo - II111iiii / Oo0Ooo
  oO0ooOoO [ : ] = [ iiIiI1ii for iiIiI1ii in oO0ooOoO if iiIiI1ii not in exclude_dirs ]
  ooO0000o00O [ : ] = [ ooO0oo0o0 for ooO0oo0o0 in ooO0000o00O if ooO0oo0o0 not in exclude_files and not 'crashlog' in ooO0oo0o0 and not 'stacktrace' in ooO0oo0o0 ]
  if 9 - 9: I1IiiI + I1ii11iIi11i / I1IiiI . ooOo * oOO
  for file in ooO0000o00O :
   if 45 - 45: i11iIiiIii
   try :
    i1i1IiIiIi1Ii . append ( file )
    o00oo0 = len ( i1i1IiIiIi1Ii ) / float ( IiiIiI ) * 100
    O0OoO000O0OO . update ( 0 , "Backing Up" , '[COLOR yellow]%s[/COLOR]' % iiIiI1ii , 'Please Wait' )
    Oo0oOooOoOo = os . path . join ( oo0o0 , file )
    if 49 - 49: Oo . I1ii11iIi11i . i11iIiiIii - II111iiii / iI1iiIiiII
   except :
    print "Unable to backup file: " + file
    if 62 - 62: Oo
   if not 'temp' in oO0ooOoO :
    if 1 - 1: iIII / iIII - i11iIiiIii
    if not I1IiI in oO0ooOoO :
     if 87 - 87: Oo0Ooo / O0 * iIII / o0oOOo0O0Ooo
     try :
      I1iiIII = '01/01/1980'
      iIi1I1 = time . strftime ( '%d/%m/%Y' , time . gmtime ( os . path . getmtime ( Oo0oOooOoOo ) ) )
      if 63 - 63: OOo00O0 * I1ii11iIi11i . OoooooooOO / Oo * Oo0Ooo . oOO
      if iIi1I1 > I1iiIII :
       II1i . write ( Oo0oOooOoOo , Oo0oOooOoOo [ o0OO00oo : ] )
       if 62 - 62: i1IIi / oOO . I1IiiI * o0oOOo0O0Ooo
     except :
      print "Unable to backup file: " + file
      if 21 - 21: o0oOOo0O0Ooo
 II1i . close ( )
 O0OoO000O0OO . close ( )
 if 81 - 81: oOoO0o00OO0 / iIii1I11I1II1 - oOO * iIi1i1ii1 . I1IiiI * I1ii11iIi11i
 if 95 - 95: I1IiiI
def O0OOO000o0o ( sourcefile , destfile ) :
 II1i = zipfile . ZipFile ( destfile , 'w' , zipfile . ZIP_DEFLATED )
 o0OO00oo = len ( sourcefile )
 i1i1IiIiIi1Ii = [ ]
 oO0ooOO = [ ]
 if 19 - 19: II111iiii - i1IIi - Oo / Oo + OoOoOO00
 O0OoO000O0OO . create ( "Backing Up Files" , "Archiving..." , '' , 'Please Wait' )
 if 51 - 51: Oo0Ooo % OoOoOO00 * OoooooooOO . i11iIiiIii
 for oo0o0 , oO0ooOoO , ooO0000o00O in os . walk ( sourcefile ) :
  if 77 - 77: II111iiii
  for file in ooO0000o00O :
   oO0ooOO . append ( file )
   if 42 - 42: iI1iiIiiII * iIi1i1ii1 . iIII * I1IiiI + OoOoOO00
 IiiIiI = len ( oO0ooOO )
 if 25 - 25: oOoO0o00OO0 . I1IiiI + ooOo
 for oo0o0 , oO0ooOoO , ooO0000o00O in os . walk ( sourcefile ) :
  if 75 - 75: iIII - o0oOOo0O0Ooo % OOo00O0 + i11iIiiIii
  for file in ooO0000o00O :
   i1i1IiIiIi1Ii . append ( file )
   o00oo0 = len ( i1i1IiIiIi1Ii ) / float ( IiiIiI ) * 100
   O0OoO000O0OO . update ( int ( o00oo0 ) , "Backing Up" , '[COLOR yellow]%s[/COLOR]' % file , 'Please Wait' )
   Oo0oOooOoOo = os . path . join ( oo0o0 , file )
   if 100 - 100: oOoO0o00OO0 + o0oOOo0O0Ooo - i11iIiiIii - II111iiii
   if not 'temp' in oO0ooOoO :
    if 40 - 40: OoOoOO00 % OoO0O00
    if not I1IiI in oO0ooOoO :
     if 62 - 62: o0oOOo0O0Ooo
     import time
     I1iiIII = '01/01/1980'
     iIi1I1 = time . strftime ( '%d/%m/%Y' , time . gmtime ( os . path . getmtime ( Oo0oOooOoOo ) ) )
     if 15 - 15: oOoO0o00OO0 + iI1iiIiiII . Oo * OoO0O00 . OoOoOO00
     if iIi1I1 > I1iiIII :
      II1i . write ( Oo0oOooOoOo , Oo0oOooOoOo [ o0OO00oo : ] )
 II1i . close ( )
 O0OoO000O0OO . close ( )
 if 18 - 18: i1IIi % II111iiii + iIi1i1ii1 % iI1iiIiiII
 if 72 - 72: iIii1I11I1II1
def iI1I1II1 ( ) :
 IIii ( '' , 'Create My Own [COLOR=orange]noobs[/COLOR][COLOR=dodgerblue]and[/COLOR][COLOR=orange]nerds[/COLOR] Community Build' , 'url' , 'community_backup' , 'Backup.png' , '' , '' , 'Back Up Your Full System' )
 if Oo0o0Oo0O ( ) :
  IIii ( '' , '[COLOR=dodgerblue]Create OpenELEC Backup[/COLOR] (full backup can only be used on OpenELEC)' , 'none' , 'openelec_backup' , 'Backup.png' , '' , '' , '' )
 IIii ( '' , '[COLOR=dodgerblue]Create My Own Universal Build[/COLOR] (For copying to other devices)' , 'none' , 'community_backup_2' , 'Backup.png' , '' , '' , '' )
 IIii ( '' , '[COLOR=dodgerblue]Create My Own Full Backup[/COLOR] (will only work on THIS device)' , 'local' , 'local_backup' , 'Backup.png' , '' , '' , 'Back Up Your Full System' )
 IIii ( '' , 'Backup Addons Only' , 'addons' , 'restore_zip' , 'Backup.png' , '' , '' , 'Back Up Your Addons' )
 IIii ( '' , 'Backup Addon Data Only' , 'addon_data' , 'restore_zip' , 'Backup.png' , '' , '' , 'Back Up Your Addon Userdata' )
 IIii ( '' , 'Backup Guisettings.xml' , O0O , 'restore_backup' , 'Backup.png' , '' , '' , 'Back Up Your guisettings.xml' )
 if 63 - 63: iIii1I11I1II1
 if os . path . exists ( iIi1ii1I1 ) :
  IIii ( '' , 'Backup Favourites.xml' , iIi1ii1I1 , 'restore_backup' , 'Backup.png' , '' , '' , 'Back Up Your favourites.xml' )
  if 21 - 21: OoOoOO00 / o0oOOo0O0Ooo * iIII . i1IIi
 if os . path . exists ( o0 ) :
  IIii ( '' , 'Backup Source.xml' , o0 , 'restore_backup' , 'Backup.png' , '' , '' , 'Back Up Your sources.xml' )
  if 59 - 59: O0 + i1IIi - o0oOOo0O0Ooo
 if os . path . exists ( I11II1i ) :
  IIii ( '' , 'Backup Advancedsettings.xml' , I11II1i , 'restore_backup' , 'Backup.png' , '' , '' , 'Back Up Your advancedsettings.xml' )
  if 62 - 62: i11iIiiIii % Oo . iIII . Oo
 if os . path . exists ( IIiiiiiiIi1I1 ) :
  IIii ( '' , 'Backup Advancedsettings.xml' , IIiiiiiiIi1I1 , 'restore_backup' , 'Backup.png' , '' , '' , 'Back Up Your keyboard.xml' )
  if 84 - 84: i11iIiiIii * OoO0O00
 if os . path . exists ( ooooooO0oo ) :
  IIii ( '' , 'Backup RssFeeds.xml' , ooooooO0oo , 'restore_backup' , 'Backup.png' , '' , '' , 'Back Up Your RssFeeds.xml' )
  if 18 - 18: Oo - iI1iiIiiII - OoOoOO00 / iIi1i1ii1 - O0
  if 30 - 30: O0 + I1ii11iIi11i + II111iiii
def III1I ( ) :
 IIii ( 'folder' , 'Backup My Content' , 'none' , 'backup_option' , 'Backup.png' , '' , '' , '' )
 IIii ( 'folder' , 'Restore My Content' , 'none' , 'restore_option' , 'Restore.png' , '' , '' , '' )
 if 11 - 11: oOO - Oo + oOO * ooOo / I1IiiI
 if 53 - 53: iIii1I11I1II1 + o0oOOo0O0Ooo - OoOoOO00 - ooOo / oOO % i11iIiiIii
def I11oOOooo ( ) :
 xbmc . executebuiltin ( 'ActivateWindow(10040,"addons://repos/",return)' )
 if 80 - 80: I1IiiI - i11iIiiIii
 if 69 - 69: ooOo % OoooooooOO . I1IiiI
def I1III1II1I11 ( localbuildcheck , localversioncheck , id , welcometext ) :
 IIi11 = o0O . getSetting ( 'testcheck' )
 if id != '0' :
  if id != 'Local' :
   ooo0O0OOO000o = iiI1iii ( localbuildcheck , localversioncheck , id )
   if 79 - 79: OoO0O00 * OoOoOO00 . OoooooooOO - oOoO0o00OO0 * o0oOOo0O0Ooo
   if ooo0O0OOO000o == True :
    if 78 - 78: iIII
    if not 'Partially installed' in localbuildcheck :
     IIii ( 'folder' , '[COLOR=dodgerblue]' + localbuildcheck + ':[/COLOR] [COLOR=lime]NEW VERSION AVAILABLE[/COLOR]' , id , 'showinfo' , 'TOTALXBMC.png' , '' , '' , '' )
     if 83 - 83: iIii1I11I1II1 % OoOoOO00 % o0oOOo0O0Ooo % iIi1i1ii1 . I1ii11iIi11i % O0
    if '(Partially installed)' in localbuildcheck :
     IIii ( 'folder' , '[COLOR=lime]Current Build Installed: [/COLOR][COLOR=dodgerblue]' + localbuildcheck + '[/COLOR]' , id , 'showinfo2' , 'TOTALXBMC.png' , '' , '' , '' )
     if 47 - 47: o0oOOo0O0Ooo
   else :
    if localbuildcheck == 'None' :
     IIii ( 'folder' , '[COLOR=lime]Current Build Installed: [/COLOR][COLOR=dodgerblue]None[/COLOR]' , '' , '' , 'TOTALXBMC.png' , '' , '' , '' )
     if 66 - 66: I1IiiI - iIII
    else :
     IIii ( 'folder' , '[COLOR=lime]Current Build Installed: [/COLOR][COLOR=dodgerblue]' + localbuildcheck + '[/COLOR]' , id , 'showinfo' , 'TOTALXBMC.png' , '' , '' , '' )
     if 33 - 33: I1IiiI / OoO0O00
  else :
   if 12 - 12: II111iiii
   if localbuildcheck == 'Incomplete' :
    IIii ( '' , '[COLOR=lime]Your last restore is not yet completed[/COLOR]' , 'url' , IiIii1ii ( ) , 'TOTALXBMC.png' , '' , '' , '' )
    if 8 - 8: OoO0O00 + OoOoOO00 . iIii1I11I1II1 % O0
   else :
    IIii ( '' , '[COLOR=lime]Current Build Installed: [/COLOR][COLOR=dodgerblue]Local Build (' + localbuildcheck + ')[/COLOR]' , 'TOTALXBMC.png' , '' , '' , '' , '' , '' )
  IIii ( '' , '[COLOR=gold]---------------------------------------[/COLOR]' , 'None' , '' , 'TOTALXBMC.png' , '' , '' , '' )
  if 43 - 43: I1ii11iIi11i - OOo00O0
 if Oo0o0Oo0O ( ) :
  IIii ( '' , '[COLOR=darkcyan]Wi-Fi Settings[/COLOR]' , '' , 'openelec_settings' , 'Wi-Fi.png' , '' , '' , '' )
  if 70 - 70: OOo00O0 / Oo % oOO - iI1iiIiiII
 IIii ( 'folder' , '[COLOR=dodgerblue]Load ' + IIIi1I1IIii1II + ' Builds[/COLOR]' , '&reseller=' + urllib . quote ( IIIi1I1IIii1II ) + '&token=' + O0ii1ii1ii + '&visibility=reseller_private' , 'grab_builds' , 'Community_Builds.png' , '' , '' , '' )
 if 47 - 47: OOo00O0
 if 92 - 92: Oo + OoOoOO00 % i1IIi
 if 23 - 23: iIi1i1ii1 - Oo + iI1iiIiiII - OoOoOO00 * OoOoOO00 . Oo0Ooo
 if 47 - 47: ooOo % iIii1I11I1II1
 if 11 - 11: I1IiiI % iI1iiIiiII - OoO0O00 - ooOo + o0oOOo0O0Ooo
 if 98 - 98: OOo00O0 + iI1iiIiiII - OoO0O00
 if 79 - 79: Oo / iIi1i1ii1 . OoOoOO00 - I1ii11iIi11i
 if 47 - 47: OoooooooOO % O0 * OOo00O0 . iI1iiIiiII
 if 38 - 38: O0 - iIII % iIi1i1ii1
 if 64 - 64: iIii1I11I1II1
 if 15 - 15: I1ii11iIi11i + Oo / I1ii11iIi11i / iIi1i1ii1
 if 31 - 31: oOO + O0 + oOO . iIii1I11I1II1 + Oo0Ooo / o0oOOo0O0Ooo
 if 6 - 6: Oo0Ooo % iIII * oOoO0o00OO0 / I1IiiI + Oo0Ooo
 if I11 == 'true' :
  if 39 - 39: OoOoOO00 - Oo0Ooo / OOo00O0 * OoooooooOO
  IIii ( '' , '[COLOR=orange]Latest ' + IIIi1I1IIii1II + ' news[/COLOR]' , IIIi1I1IIii1II , 'notify_msg' , 'LatestNews.png' , '' , '' , '' )
  if 100 - 100: O0 . oOoO0o00OO0 . OoO0O00 + O0 * ooOo
  if 42 - 42: ooOo % OoooooooOO + o0oOOo0O0Ooo
  if 56 - 56: OoooooooOO + I1ii11iIi11i - OOo00O0
  if 24 - 24: o0oOOo0O0Ooo + oOO + oOoO0o00OO0 - iIii1I11I1II1
 if i11 == 'true' :
  IIii ( 'folder' , 'Tools' , 'none' , 'tools' , 'Additional_Tools.png' , '' , '' , '' )
  if 49 - 49: oOoO0o00OO0 . oOO * OoOoOO00 % iIII . O0
  if 48 - 48: O0 * iI1iiIiiII - O0 / iI1iiIiiII + OoOoOO00
def oO00oo000O ( ) :
 ii11 = 'defaultskindependecycheck'
 if os . path . exists ( Oo0oOOo ) :
  shutil . rmtree ( Oo0oOOo )
  if 63 - 63: o0oOOo0O0Ooo . iIII
 if not os . path . exists ( Oo0oOOo ) :
  os . makedirs ( Oo0oOOo )
  if 28 - 28: II111iiii
  if 86 - 86: iIii1I11I1II1
  if 18 - 18: OoO0O00 . II111iiii % OoOoOO00 % iI1iiIiiII
 if o0OO00oO != 'skin.confluence' :
  oo0 = os . path . join ( OO0o , o0OO00oO , 'addon.xml' )
  i1iIIi1II1iiI = open ( oo0 , mode = 'r' )
  III1Ii1i1I1 = i1iIIi1II1iiI . read ( )
  i1iIIi1II1iiI . close ( )
  if 97 - 97: iIi1i1ii1 . oOO - iIi1i1ii1 + I1IiiI * II111iiii
  I111Ii = re . compile ( '<requires[\s\S]*?\/requires' ) . findall ( III1Ii1i1I1 )
  ii11 = I111Ii [ 0 ] if ( len ( I111Ii ) > 0 ) else 'None'
  if 34 - 34: o0oOOo0O0Ooo / OOo00O0 % O0 . OoO0O00 . i1IIi
 iiO0O0o0oO0O00 = oooOo0OOOoo0 ( 'http://noobsandnerds.com/TI/AddonPortal/approved.php' )
 if 70 - 70: iIi1i1ii1 + ooOo
 O0OoO000O0OO . create ( 'Backing Up Add-ons' , '' , 'Please Wait...' )
 if 93 - 93: iIi1i1ii1 + iI1iiIiiII
 for I1i11i in os . listdir ( OO0o ) :
  if 33 - 33: O0
  if 78 - 78: O0 / II111iiii * OoO0O00
  if not 'plugin.program.mediacube' in I1i11i and not 'packages' in I1i11i and os . path . isdir ( os . path . join ( OO0o , I1i11i ) ) :
   if 50 - 50: OoooooooOO - iIii1I11I1II1 + i1IIi % iIi1i1ii1 - iIii1I11I1II1 % O0
   if 58 - 58: iIII + iIii1I11I1II1
   if I1i11i in iiO0O0o0oO0O00 and not I1i11i in ii11 and not 'script.' in I1i11i and not 'repo.' in I1i11i and not 'repository.' in I1i11i and os . path . isdir ( os . path . join ( OO0o , I1i11i ) ) :
    if 65 - 65: II111iiii - iIi1i1ii1 % o0oOOo0O0Ooo - OoOoOO00 * OOo00O0 + iI1iiIiiII
    if 79 - 79: oOO . OoOoOO00 % iIi1i1ii1 - Oo0Ooo
    if not 'service.xbmc.versioncheck' in I1i11i and not 'packages' in I1i11i and os . path . isdir ( os . path . join ( OO0o , I1i11i ) ) :
     if 69 - 69: oOO - o0oOOo0O0Ooo . oOO
     try :
      O0OoO000O0OO . update ( 0 , "Backing Up" , '[COLOR yellow]%s[/COLOR]' % I1i11i , 'Please Wait...' )
      os . makedirs ( os . path . join ( Oo0oOOo , I1i11i ) )
      if 9 - 9: ooOo % i11iIiiIii / Oo0Ooo
      oOooO00o0O = os . path . join ( Oo0oOOo , I1i11i , 'addon.xml' )
      OOo0iiIii1IIi = os . path . join ( Oo0oOOo , I1i11i , 'default.py' )
      OOOOoOo00OO = open ( os . path . join ( OO0o , I1i11i , 'addon.xml' ) , mode = 'r' )
      OooOo0o0Oo = OOOOoOo00OO . read ( )
      OOOOoOo00OO . close ( )
      if 20 - 20: ooOo * O0 + oOoO0o00OO0 - OoooooooOO . oOoO0o00OO0
      I1i1iii1Ii = re . compile ( ' name="(.+?)"' ) . findall ( OooOo0o0Oo )
      iIO0O00OOo = re . compile ( 'provider-name="(.+?)"' ) . findall ( OooOo0o0Oo )
      oOII1ii1ii11I1 = re . compile ( '<addon[\s\S]*?">' ) . findall ( OooOo0o0Oo )
      o0ooOO0o = re . compile ( '<description[\s\S]*?<\/description>' ) . findall ( OooOo0o0Oo )
      O00o0 = I1i1iii1Ii [ 0 ] if ( len ( I1i1iii1Ii ) > 0 ) else 'None'
      I11iI1i1I11I11 = iIO0O00OOo [ 0 ] if ( len ( iIO0O00OOo ) > 0 ) else 'Anonymous'
      ooo0 = oOII1ii1ii11I1 [ 0 ] if ( len ( oOII1ii1ii11I1 ) > 0 ) else 'None'
      i1iI = o0ooOO0o [ 0 ] if ( len ( o0ooOO0o ) > 0 ) else 'None'
      if 46 - 46: OOo00O0 - iIii1I11I1II1
      I1I1 = '<addon id="' + I1i11i + '" name="' + O00o0 + '" version="0" provider-name="' + I11iI1i1I11I11 + '">'
      IIIii = '<description>If you\'re seeing this message it means the add-on is still updating, please wait for the update process to complete.</description>'
      if 99 - 99: oOO / iIii1I11I1II1 - iI1iiIiiII * I1ii11iIi11i % I1IiiI
      if ooo0 != 'None' :
       II1iIi1IiIii = OooOo0o0Oo . replace ( i1iI , IIIii ) . replace ( ooo0 , I1I1 )
       if 13 - 13: OoO0O00
      else :
       II1iIi1IiIii = OooOo0o0Oo . replace ( i1iI , IIIii )
       if 70 - 70: iIi1i1ii1 + O0 . ooOo * iI1iiIiiII
      iiiiI11ii = open ( oOooO00o0O , mode = 'w+' )
      iiiiI11ii . write ( str ( II1iIi1IiIii ) )
      iiiiI11ii . close ( )
      o0o000 = open ( OOo0iiIii1IIi , mode = 'w+' )
      o0o000 . write ( 'import xbmcplugin,xbmcgui,xbmc,xbmcaddon,os,sys\nAddonID="' + I1i11i + '"\nAddonName="' + O00o0 + '"\ndialog=xbmcgui.Dialog()\nxbmc.executebuiltin("UpdateLocalAddons")\nxbmc.executebuiltin("UpdateAddonRepos")\nchoice=dialog.yesno(AddonName+" Add-on Requires Update","This add-on may still be in the process of the updating so we recommend waiting a few minutes to see if it updates naturally. Alternatively you can try reinstalling, would you like to attempt a reinstall of this add-on?",yeslabel="Install Option 2", nolabel="Wait")\nif choice==1: xbmc.executebuiltin(\'ActivateWindow(10001,"plugin://plugin.program.mediacube/?mode=grab_addons&url=%26redirect%26addonid%3d\'+AddonID+\'")\')\nxbmcplugin.endOfDirectory(int(sys.argv[1]))' )
      o0o000 . close ( )
      if 2 - 2: OoooooooOO . Oo . iIII
     except :
      print "### Failed to backup: " + I1i11i
      if 42 - 42: Oo % ooOo / OoO0O00 - ooOo * i11iIiiIii
      if 19 - 19: ooOo * I1IiiI % i11iIiiIii
   else :
    shutil . copytree ( os . path . join ( OO0o , I1i11i ) , os . path . join ( Oo0oOOo , I1i11i ) )
    if 24 - 24: o0oOOo0O0Ooo
 O0OoO000O0OO . close ( )
 if 10 - 10: o0oOOo0O0Ooo % iI1iiIiiII / Oo
 i11Ii1iIiII = "Creating Backup"
 O0oOo00Ooo0o0 = "Archiving..."
 i1IiII1i1I = ""
 iI1ii1ii1I = "Please Wait"
 if 18 - 18: ooOo * ooOo % ooOo
 i1II1iII ( Oo0oOOo , Oo0OoO00oOO0o , i11Ii1iIiII , O0oOo00Ooo0o0 , i1IiII1i1I , iI1ii1ii1I , '' , '' )
 if 17 - 17: O0 * OoOoOO00 * I1ii11iIi11i * II111iiii * oOoO0o00OO0 % i1IIi
 try :
  shutil . rmtree ( Oo0oOOo )
  if 33 - 33: I1ii11iIi11i * I1ii11iIi11i . oOO . i11iIiiIii
 except :
  print "### COMMUNITY BUILDS: Failed to remove temp addons folder - manual delete required ###"
  if 48 - 48: o0oOOo0O0Ooo . iI1iiIiiII + OoOoOO00 % I1ii11iIi11i / i11iIiiIii
  if 74 - 74: II111iiii . O0 - I1IiiI + iIII % i11iIiiIii % OoOoOO00
def O0OOO0 ( url ) :
 O0OoO000O0OO . create ( 'Cleaning Temp Paths' , '' , 'Please wait...' )
 if os . path . exists ( Oo0oOOo ) :
  shutil . rmtree ( Oo0oOOo )
  if 8 - 8: i11iIiiIii / II111iiii + o0oOOo0O0Ooo * iI1iiIiiII % iIII . oOoO0o00OO0
 if not os . path . exists ( Oo0oOOo ) :
  os . makedirs ( Oo0oOOo )
  if 6 - 6: iIII % Oo0Ooo . Oo0Ooo - I1ii11iIi11i / oOoO0o00OO0 . i1IIi
 oOO00oO00O0OO ( Oo0OoO00oOO0o , Oo0oOOo )
 if 99 - 99: OoOoOO00 . iIi1i1ii1
 for I1i11i in os . listdir ( Oo0oOOo ) :
  if 59 - 59: oOoO0o00OO0 / Oo0Ooo / Oo / O0 / OoOoOO00 + o0oOOo0O0Ooo
  if not 'totalinstaller' in I1i11i and not 'plugin.program.mediacube' in I1i11i :
   if not os . path . exists ( os . path . join ( OO0o , I1i11i ) ) :
    os . rename ( os . path . join ( Oo0oOOo , I1i11i ) , os . path . join ( OO0o , I1i11i ) )
    O0OoO000O0OO . update ( 0 , "Installing: [COLOR=yellow]" + I1i11i + '[/COLOR]' , '' , 'Please wait...' )
    print "### Successfully installed: " + I1i11i
    if 13 - 13: o0oOOo0O0Ooo % ooOo / iIi1i1ii1 % iIi1i1ii1 % O0
   else :
    print "### " + I1i11i + " Already exists on system"
    if 90 - 90: iIII . oOO / iIii1I11I1II1
    if 28 - 28: iIII + ooOo - oOO / iIii1I11I1II1 - I1IiiI
def Ii1i1 ( welcometext ) :
 oOoO00 = xbmc . getInfoLabel ( "System.BuildVersion" )
 i1ii1iIIi11i111I = float ( oOoO00 [ : 2 ] )
 iIIiIiI1I1 = int ( i1ii1iIIi11i111I )
 if 16 - 16: I1IiiI . iIii1I11I1II1
 if iI1Ii11111iIi == 'true' :
  if 27 - 27: i11iIiiIii - I1IiiI
  if i1i1II == 'true' :
   iii1IIiI ( 'yes' )
   if 33 - 33: oOoO0o00OO0
  if i1i1II == 'false' :
   iii1IIiI ( 'no' )
   if 98 - 98: OoOoOO00 % II111iiii
 if IiII == 'true' :
  IIii ( 'folder' , '[COLOR=dodgerblue]Show My Private List[/COLOR]' , '&visibility=private' , 'grab_builds' , 'Private_builds.png' , '' , '' , '' )
  if 95 - 95: iIii1I11I1II1 - iIi1i1ii1 - Oo + iIi1i1ii1 % I1ii11iIi11i . I1IiiI
 if ( ( oo00 . replace ( '%20' , ' ' ) in welcometext ) and ( 'elc' in welcometext ) ) or ( iI1Ii11111iIi == 'true' ) :
  if 41 - 41: O0 + ooOo . i1IIi - II111iiii * o0oOOo0O0Ooo . OoO0O00
  if ( iIIiIiI1I1 < 14 ) or ( Oo0oO0ooo == 'true' ) :
   IIii ( 'folder' , '[COLOR=dodgerblue]Show All Gotham Compatible Builds[/COLOR]' , '&xbmc=gotham&visibility=public' , 'grab_builds' , 'TRCOMMUNITYGOTHAMBUILDS.png' , '' , '' , '' )
   if 68 - 68: o0oOOo0O0Ooo
  if ( iIIiIiI1I1 == 14 ) or ( Oo0oO0ooo == 'true' ) :
   IIii ( 'folder' , '[COLOR=dodgerblue]Show All Helix Compatible Builds[/COLOR]' , '&xbmc=helix&visibility=public' , 'grab_builds' , 'TRCOMMUNITYHELIXBUILDS.png' , '' , '' , '' )
   if 20 - 20: iIi1i1ii1 - iIi1i1ii1
  if ( iIIiIiI1I1 == 15 ) or ( Oo0oO0ooo == 'true' ) :
   IIii ( 'folder' , '[COLOR=dodgerblue]Show All Isengard Compatible Builds[/COLOR]' , '&xbmc=isengard&visibility=public' , 'grab_builds' , 'TRCOMMUNITYHELIXBUILDS.png' , '' , '' , '' )
   if 37 - 37: iIII
   if 37 - 37: Oo0Ooo / iIII * O0
   if 73 - 73: OOo00O0 * OOo00O0 / oOO
  if oo0o0O00 != '' :
   IIii ( 'folder' , '[COLOR=darkcyan]Show ' + oO + ' Builds[/COLOR]' , '&id=1' , 'grab_builds' , 'TRCOMMUNITYGOTHAMBUILDS.png' , '' , '' , '' )
  if i1iiIIiiI111 != '' :
   IIii ( 'folder' , '[COLOR=darkcyan]Show ' + oooOOOOO + ' Builds[/COLOR]' , '&id=2' , 'grab_builds' , 'TRCOMMUNITYGOTHAMBUILDS.png' , '' , '' , '' )
  if i1iiIII111ii != '' :
   IIii ( 'folder' , '[COLOR=darkcyan]Show ' + i1iIIi1 + ' Builds[/COLOR]' , '&id=3' , 'grab_builds' , 'TRCOMMUNITYGOTHAMBUILDS.png' , '' , '' , '' )
  if ii11iIi1I != '' :
   IIii ( 'folder' , '[COLOR=darkcyan]Show ' + iI111I11I1I1 + ' Builds[/COLOR]' , '&id=4' , 'grab_builds' , 'TRCOMMUNITYGOTHAMBUILDS.png' , '' , '' , '' )
  if OOooO0OOoo != '' :
   IIii ( 'folder' , '[COLOR=darkcyan]Show ' + iIii1 + ' Builds[/COLOR]' , '&id=5' , 'grab_builds' , 'TRCOMMUNITYGOTHAMBUILDS.png' , '' , '' , '' )
 IIii ( '' , 'Create My Own Community Build' , 'url' , 'community_backup' , 'Backup.png' , '' , '' , 'Back Up Your Full System' )
 if 43 - 43: I1ii11iIi11i . i1IIi . iIII + O0 * iI1iiIiiII * O0
 if 41 - 41: I1ii11iIi11i + iI1iiIiiII % OoooooooOO . I1ii11iIi11i + OOo00O0 . OOo00O0
def Iiii11I ( skin ) :
 OO0ooo0 = '<onleft>%s</onleft>'
 II1II1iI = '<onright>%s</onright>'
 OooooO = '<onup>%s</onup>'
 oO0O0 = '<ondown>%s</ondown>'
 iI111i11iI1 = '<control type="button" id="%s">'
 if 2 - 2: OoOoOO00 + iIi1i1ii1 + OoooooooOO . i1IIi
 if 19 - 19: OOo00O0 - o0oOOo0O0Ooo - iI1iiIiiII - OoOoOO00 . OOo00O0 . iIi1i1ii1
 i11I1I = [
 ( '65' , '140' ) ,
 ( '66' , '164' ) ,
 ( '67' , '162' ) ,
 ( '68' , '142' ) ,
 ( '69' , '122' ) ,
 ( '70' , '143' ) ,
 ( '71' , '144' ) ,
 ( '72' , '145' ) ,
 ( '73' , '127' ) ,
 ( '74' , '146' ) ,
 ( '75' , '147' ) ,
 ( '76' , '148' ) ,
 ( '77' , '166' ) ,
 ( '78' , '165' ) ,
 ( '79' , '128' ) ,
 ( '80' , '129' ) ,
 ( '81' , '120' ) ,
 ( '82' , '123' ) ,
 ( '83' , '141' ) ,
 ( '84' , '124' ) ,
 ( '85' , '126' ) ,
 ( '86' , '163' ) ,
 ( '87' , '121' ) ,
 ( '88' , '161' ) ,
 ( '89' , '125' ) ,
 ( '90' , '160' ) ]
 if 71 - 71: OOo00O0
 for Iiii1i11ii1Ii , i1Oo0oOo000OoO0 in i11I1I :
  IIii1I1i = open ( skin ) . read ( )
  IIII1iIIii = IIii1I1i . replace ( iI111i11iI1 % Iiii1i11ii1Ii , iI111i11iI1 % i1Oo0oOo000OoO0 ) . replace ( OO0ooo0 % Iiii1i11ii1Ii , OO0ooo0 % i1Oo0oOo000OoO0 ) . replace ( II1II1iI % Iiii1i11ii1Ii , II1II1iI % i1Oo0oOo000OoO0 ) . replace ( OooooO % Iiii1i11ii1Ii , OooooO % i1Oo0oOo000OoO0 ) . replace ( oO0O0 % Iiii1i11ii1Ii , oO0O0 % i1Oo0oOo000OoO0 )
  ooO0oo0o0 = open ( skin , mode = 'w' )
  ooO0oo0o0 . write ( IIII1iIIii )
  ooO0oo0o0 . close ( )
  if 12 - 12: iIii1I11I1II1 . iI1iiIiiII . I1ii11iIi11i % I1IiiI . II111iiii . ooOo
def IIi1ii1 ( u , skin ) :
 OO0ooo0 = '<onleft>%s</onleft>'
 II1II1iI = '<onright>%s</onright>'
 OooooO = '<onup>%s</onup>'
 oO0O0 = '<ondown>%s</ondown>'
 iI111i11iI1 = '<control type="button" id="%s">'
 if 48 - 48: oOO / iIii1I11I1II1 + Oo + iIii1I11I1II1 . OoO0O00
 if u < 49 :
  o0o0OO0o00o0O = u + 61
  if 28 - 28: OoO0O00 - ooOo + OoOoOO00 + iI1iiIiiII / iIii1I11I1II1
 else :
  o0o0OO0o00o0O = u + 51
  if 26 - 26: iIii1I11I1II1 - O0 . O0
 IIii1I1i = open ( skin ) . read ( )
 IIII1iIIii = IIii1I1i . replace ( OO0ooo0 % u , OO0ooo0 % o0o0OO0o00o0O ) . replace ( II1II1iI % u , II1II1iI % o0o0OO0o00o0O ) . replace ( OooooO % u , OooooO % o0o0OO0o00o0O ) . replace ( oO0O0 % u , oO0O0 % o0o0OO0o00o0O ) . replace ( iI111i11iI1 % u , iI111i11iI1 % o0o0OO0o00o0O )
 ooO0oo0o0 = open ( skin , mode = 'w' )
 ooO0oo0o0 . write ( IIII1iIIii )
 ooO0oo0o0 . close ( )
 if 68 - 68: Oo + ooOo . O0 . iI1iiIiiII % i1IIi % Oo
 if 50 - 50: iIII + o0oOOo0O0Ooo
def o0OoOOo ( ) :
 O0Oo0 = xbmc . translatePath ( os . path . join ( zip , 'testCBFolder' ) )
 if 49 - 49: Oo
 if not os . path . exists ( zip ) :
  oOOoO0 . ok ( 'Download/Storage Path Check' , 'The download location you have stored does not exist .\nPlease update the addon settings and try again.' )
  o0O . openSettings ( sys . argv [ 0 ] )
  if 67 - 67: OoOoOO00 - o0oOOo0O0Ooo * OoOoOO00 + ooOo * Oo0Ooo
  if 98 - 98: i11iIiiIii . OOo00O0
def iiI1iii ( localbuildcheck , localversioncheck , id ) :
 ii1111iII = 'http://noobsandnerds.com/TI/Community_Builds/buildupdate.php?id=%s' % ( id )
 iiiiI = oooOo0OOOoo0 ( ii1111iII ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 if 35 - 35: iIII . O0 + Oo0Ooo + Oo + i1IIi
 if id != 'None' :
  OooOooO0O0o0 = re . compile ( 'version="(.+?)"' ) . findall ( iiiiI )
  OOO0o0 = OooOooO0O0o0 [ 0 ] if ( len ( OooOooO0O0o0 ) > 0 ) else ''
  if 34 - 34: I1IiiI % Oo0Ooo - OoOoOO00 + OOo00O0
  if localversioncheck < OOO0o0 :
   return True
   if 79 - 79: II111iiii - oOO . i1IIi + O0 % O0 * I1IiiI
 else :
  return False
  if 7 - 7: i1IIi + Oo % OOo00O0 / o0oOOo0O0Ooo + i1IIi
  if 41 - 41: iI1iiIiiII + i11iIiiIii / iIII % I1ii11iIi11i
def IiIii1ii ( ) :
 II1II1IIII = open ( iiiiiIIii , mode = 'r' )
 OooOo0o0Oo = II1II1IIII . read ( )
 II1II1IIII . close ( )
 if 37 - 37: OoooooooOO
 oo0ooO0 = re . compile ( 'name="(.+?)"' ) . findall ( OooOo0o0Oo )
 oOooo0OOO = oo0ooO0 [ 0 ] if ( len ( oo0ooO0 ) > 0 ) else ''
 if 65 - 65: OoooooooOO
 if oOooo0OOO == "Incomplete" :
  ii1I11iIiIII1 = xbmcgui . Dialog ( ) . yesno ( "Finish Restore Process" , 'If you\'re certain the correct skin has now been set click OK' , 'to finish the install process, once complete XBMC/Kodi will' , ' then close. Do you want to finish the install process?' , yeslabel = 'Yes' , nolabel = 'No' )
  if 14 - 14: Oo % OoooooooOO
  if ii1I11iIiIII1 == 1 :
   Oo0oO00 ( )
   if 41 - 41: O0 - oOoO0o00OO0 * iIii1I11I1II1
  elif ii1I11iIiIII1 == 0 :
   return
   if 12 - 12: o0oOOo0O0Ooo * iIi1i1ii1 % II111iiii * i1IIi * iIii1I11I1II1
def oO0oOoo0O ( ) :
 O0Oo0 = xbmc . translatePath ( os . path . join ( zip , 'testCBFolder' ) )
 if 26 - 26: Oo0Ooo + I1IiiI * Oo + oOO
 try :
  os . makedirs ( O0Oo0 )
  os . removedirs ( O0Oo0 )
  oOOoO0 . ok ( '[COLOR=lime]SUCCESS[/COLOR]' , 'Great news, the path you chose is writeable.' , 'Some of these builds are rather big, we recommend a minimum of 1GB storage space.' )
  if 88 - 88: oOoO0o00OO0 + i11iIiiIii % ooOo * Oo * Oo * iI1iiIiiII
 except :
  oOOoO0 . ok ( '[COLOR=red]CANNOT WRITE TO PATH[/COLOR]' , 'Kodi cannot write to the path you\'ve chosen. Please click OK in the settings menu to save the path then try again. Some devices give false results, we recommend using a USB stick as the backup path.' )
  if 24 - 24: oOO / OOo00O0 + iIII . iIII
  if 39 - 39: oOO + O0 / i1IIi % iIII / ooOo * iIII
def o0OO00000 ( data ) :
 data = data . replace ( '</p><p>' , '[CR][CR]' ) . replace ( '&ndash;' , '-' ) . replace ( '&mdash;' , '-' ) . replace ( "\n" , " " ) . replace ( "\r" , " " ) . replace ( "&rsquo;" , "'" ) . replace ( "&rdquo;" , '"' ) . replace ( "</a>" , " " ) . replace ( "&hellip;" , '...' ) . replace ( "&lsquo;" , "'" ) . replace ( "&ldquo;" , '"' )
 data = " " . join ( data . split ( ) )
 OO00Oo = re . compile ( r'< script[^<>]*?>.*?< / script >' )
 data = OO00Oo . sub ( '' , data )
 OO00Oo = re . compile ( r'< style[^<>]*?>.*?< / style >' )
 data = OO00Oo . sub ( '' , data )
 OO00Oo = re . compile ( r'' )
 data = OO00Oo . sub ( '' , data )
 OO00Oo = re . compile ( r'<[^<]*?>' )
 data = OO00Oo . sub ( '' , data )
 data = data . replace ( '&nbsp;' , ' ' )
 return data
 if 6 - 6: iI1iiIiiII - OoO0O00 . I1IiiI - O0
 if 16 - 16: OOo00O0 * OOo00O0 % iI1iiIiiII % I1IiiI
def I111i ( ) :
 ii1I11iIiIII1 = xbmcgui . Dialog ( ) . yesno ( 'Clear All Known Cache?' , 'This will clear all known cache files and can help if you\'re encountering kick-outs during playback as well as other random issues. There is no harm in using this.' , nolabel = 'Cancel' , yeslabel = 'Delete' )
 if 42 - 42: iIi1i1ii1 * iIII
 if ii1I11iIiIII1 == 1 :
  III11i1iIIiiI ( )
  oO0O0o0o00 ( )
  if 29 - 29: iIII . oOO - II111iiii
  if 68 - 68: iIii1I11I1II1 + II111iiii / ooOo
def oOooo00000 ( url ) :
 IIii ( 'folder' , 'African' , str ( url ) + '&genre=african' , 'grab_builds' , 'african.png' , '' , '' , '' )
 IIii ( 'folder' , 'Arabic' , str ( url ) + '&genre=arabic' , 'grab_builds' , 'arabic.png' , '' , '' , '' )
 IIii ( 'folder' , 'Asian' , str ( url ) + '&genre=asian' , 'grab_builds' , 'asian.png' , '' , '' , '' )
 IIii ( 'folder' , 'Australian' , str ( url ) + '&genre=australian' , 'grab_builds' , 'australian.png' , '' , '' , '' )
 IIii ( 'folder' , 'Austrian' , str ( url ) + '&genre=austrian' , 'grab_builds' , 'austrian.png' , '' , '' , '' )
 IIii ( 'folder' , 'Belgian' , str ( url ) + '&genre=belgian' , 'grab_builds' , 'belgian.png' , '' , '' , '' )
 IIii ( 'folder' , 'Brazilian' , str ( url ) + '&genre=brazilian' , 'grab_builds' , 'brazilian.png' , '' , '' , '' )
 IIii ( 'folder' , 'Canadian' , str ( url ) + '&genre=canadian' , 'grab_builds' , 'canadian.png' , '' , '' , '' )
 IIii ( 'folder' , 'Columbian' , str ( url ) + '&genre=columbian' , 'grab_builds' , 'columbian.png' , '' , '' , '' )
 IIii ( 'folder' , 'Czech' , str ( url ) + '&genre=czech' , 'grab_builds' , 'czech.png' , '' , '' , '' )
 IIii ( 'folder' , 'Danish' , str ( url ) + '&genre=danish' , 'grab_builds' , 'danish.png' , '' , '' , '' )
 IIii ( 'folder' , 'Dominican' , str ( url ) + '&genre=dominican' , 'grab_builds' , 'dominican.png' , '' , '' , '' )
 IIii ( 'folder' , 'Dutch' , str ( url ) + '&genre=dutch' , 'grab_builds' , 'dutch.png' , '' , '' , '' )
 IIii ( 'folder' , 'Egyptian' , str ( url ) + '&genre=egyptian' , 'grab_builds' , 'egyptian.png' , '' , '' , '' )
 IIii ( 'folder' , 'Filipino' , str ( url ) + '&genre=filipino' , 'grab_builds' , 'filipino.png' , '' , '' , '' )
 IIii ( 'folder' , 'Finnish' , str ( url ) + '&genre=finnish' , 'grab_builds' , 'finnish.png' , '' , '' , '' )
 IIii ( 'folder' , 'French' , str ( url ) + '&genre=french' , 'grab_builds' , 'french.png' , '' , '' , '' )
 IIii ( 'folder' , 'German' , str ( url ) + '&genre=german' , 'grab_builds' , 'german.png' , '' , '' , '' )
 IIii ( 'folder' , 'Greek' , str ( url ) + '&genre=greek' , 'grab_builds' , 'greek.png' , '' , '' , '' )
 IIii ( 'folder' , 'Hebrew' , str ( url ) + '&genre=hebrew' , 'grab_builds' , 'hebrew.png' , '' , '' , '' )
 IIii ( 'folder' , 'Hungarian' , str ( url ) + '&genre=hungarian' , 'grab_builds' , 'hungarian.png' , '' , '' , '' )
 IIii ( 'folder' , 'Icelandic' , str ( url ) + '&genre=icelandic' , 'grab_builds' , 'icelandic.png' , '' , '' , '' )
 IIii ( 'folder' , 'Indian' , str ( url ) + '&genre=indian' , 'grab_builds' , 'indian.png' , '' , '' , '' )
 IIii ( 'folder' , 'Irish' , str ( url ) + '&genre=irish' , 'grab_builds' , 'irish.png' , '' , '' , '' )
 IIii ( 'folder' , 'Italian' , str ( url ) + '&genre=italian' , 'grab_builds' , 'italian.png' , '' , '' , '' )
 IIii ( 'folder' , 'Japanese' , str ( url ) + '&genre=japanese' , 'grab_builds' , 'japanese.png' , '' , '' , '' )
 IIii ( 'folder' , 'Korean' , str ( url ) + '&genre=korean' , 'grab_builds' , 'korean.png' , '' , '' , '' )
 IIii ( 'folder' , 'Lebanese' , str ( url ) + '&genre=lebanese' , 'grab_builds' , 'lebanese.png' , '' , '' , '' )
 IIii ( 'folder' , 'Mongolian' , str ( url ) + '&genre=mongolian' , 'grab_builds' , 'mongolian.png' , '' , '' , '' )
 IIii ( 'folder' , 'Nepali' , str ( url ) + '&genre=nepali' , 'grab_builds' , 'nepali.png' , '' , '' , '' )
 IIii ( 'folder' , 'New Zealand' , str ( url ) + '&genre=newzealand' , 'grab_builds' , 'newzealand.png' , '' , '' , '' )
 IIii ( 'folder' , 'Norwegian' , str ( url ) + '&genre=norwegian' , 'grab_builds' , 'norwegian.png' , '' , '' , '' )
 IIii ( 'folder' , 'Pakistani' , str ( url ) + '&genre=pakistani' , 'grab_builds' , 'pakistani.png' , '' , '' , '' )
 IIii ( 'folder' , 'Polish' , str ( url ) + '&genre=polish' , 'grab_builds' , 'polish.png' , '' , '' , '' )
 IIii ( 'folder' , 'Portuguese' , str ( url ) + '&genre=portuguese' , 'grab_builds' , 'portuguese.png' , '' , '' , '' )
 IIii ( 'folder' , 'Romanian' , str ( url ) + '&genre=romanian' , 'grab_builds' , 'romanian.png' , '' , '' , '' )
 IIii ( 'folder' , 'Russian' , str ( url ) + '&genre=russian' , 'grab_builds' , 'russian.png' , '' , '' , '' )
 IIii ( 'folder' , 'Singapore' , str ( url ) + '&genre=singapore' , 'grab_builds' , 'singapore.png' , '' , '' , '' )
 IIii ( 'folder' , 'Spanish' , str ( url ) + '&genre=spanish' , 'grab_builds' , 'spanish.png' , '' , '' , '' )
 IIii ( 'folder' , 'Swedish' , str ( url ) + '&genre=swedish' , 'grab_builds' , 'swedish.png' , '' , '' , '' )
 IIii ( 'folder' , 'Swiss' , str ( url ) + '&genre=swiss' , 'grab_builds' , 'swiss.png' , '' , '' , '' )
 IIii ( 'folder' , 'Syrian' , str ( url ) + '&genre=syrian' , 'grab_builds' , 'syrian.png' , '' , '' , '' )
 IIii ( 'folder' , 'Tamil' , str ( url ) + '&genre=tamil' , 'grab_builds' , 'tamil.png' , '' , '' , '' )
 IIii ( 'folder' , 'Thai' , str ( url ) + '&genre=thai' , 'grab_builds' , 'thai.png' , '' , '' , '' )
 IIii ( 'folder' , 'Turkish' , str ( url ) + '&genre=turkish' , 'grab_builds' , 'turkish.png' , '' , '' , '' )
 IIii ( 'folder' , 'UK' , str ( url ) + '&genre=uk' , 'grab_builds' , 'uk.png' , '' , '' , '' )
 IIii ( 'folder' , 'USA' , str ( url ) + '&genre=usa' , 'grab_builds' , 'usa.png' , '' , '' , '' )
 IIii ( 'folder' , 'Vietnamese' , str ( url ) + '&genre=vietnamese' , 'grab_builds' , 'vietnamese.png' , '' , '' , '' )
 if 26 - 26: O0
 if 34 - 34: oOO * iIi1i1ii1
def OooOoOO0OO ( ) :
 I1iiIiiii1111 = 1
 o0OoOOo ( )
 I1ii1i11i = xbmc . translatePath ( os . path . join ( I1IIIii , 'Community Builds' , 'My Builds' , '' ) )
 Oooooo0O00o = xbmc . translatePath ( os . path . join ( I1IIIii , 'Community Builds' , 'My Builds' , 'my_full_backup.zip' ) )
 II11ii1 = xbmc . translatePath ( os . path . join ( I1IIIii , 'Community Builds' , 'My Builds' , 'my_full_backup_GUI_Settings.zip' ) )
 if 19 - 19: II111iiii - iIII
 if not os . path . exists ( I1ii1i11i ) :
  os . makedirs ( I1ii1i11i )
  if 59 - 59: o0oOOo0O0Ooo * OoO0O00 - iI1iiIiiII . Oo
 o0OO00oo0O = Ii1I1i111 ( heading = "Enter a name for this backup" )
 if ( not o0OO00oo0O ) :
  return False , 0
  if 57 - 57: ooOo . I1IiiI
 iIIi11i1i1i1I = urllib . quote_plus ( o0OO00oo0O )
 i1i1iI1 = xbmc . translatePath ( os . path . join ( I1ii1i11i , iIIi11i1i1i1I + '.zip' ) )
 oOOO00OOOoOO = [ I1IiI ]
 III = [ "xbmc.log" , "xbmc.old.log" , "kodi.log" , "kodi.old.log" , '.DS_Store' , '.setup_complete' , 'XBMCHelper.conf' , 'Thumbs.db' , '.gitignore' ]
 o0Ooo00 = [ I1IiI , 'cache' , 'system' , 'Thumbnails' , "peripheral_data" , 'library' , 'keymaps' ]
 oo = [ "xbmc.log" , "xbmc.old.log" , "kodi.log" , "kodi.old.log" , "Textures13.db" , '.DS_Store' , '.setup_complete' , 'XBMCHelper.conf' , 'advancedsettings.xml' , 'Thumbs.db' , '.gitignore' ]
 i11Ii1iIiII = "Creating full backup of existing build"
 iiIIiii = "Creating Community Build"
 O0oOo00Ooo0o0 = "Archiving..."
 i1IiII1i1I = ""
 iI1ii1ii1I = "Please Wait"
 if 51 - 51: Oo
 if o0oO0 == 'true' :
  i1II1iII ( iiI1IiI , Oooooo0O00o , i11Ii1iIiII , O0oOo00Ooo0o0 , i1IiII1i1I , iI1ii1ii1I , oOOO00OOOoOO , III )
  if 18 - 18: O0 + iIII
 ii1I11iIiIII1 = xbmcgui . Dialog ( ) . yesno ( "Do you want to include your addon_data folder?" , 'This contains ALL addon settings including passwords but may also contain important information such as skin shortcuts. We recommend MANUALLY removing the addon_data folders that aren\'t required.' , yeslabel = 'Yes' , nolabel = 'No' )
 if 30 - 30: Oo + II111iiii - iIII * OoooooooOO
 if ii1I11iIiIII1 == 0 :
  o0Ooo00 = [ I1IiI , 'cache' , 'system' , 'peripheral_data' , 'library' , 'keymaps' , 'addon_data' , 'Thumbnails' ]
  if 19 - 19: iIII - o0oOOo0O0Ooo . iIii1I11I1II1 . OoOoOO00 / Oo
 elif ii1I11iIiIII1 == 1 :
  pass
  if 87 - 87: OoOoOO00 - oOO - Oo + Oo0Ooo % iIii1I11I1II1 / i11iIiiIii
 i1iIIII1iiIIi ( iiI1IiI )
 i1II1iII ( iiI1IiI , i1i1iI1 , iiIIiii , O0oOo00Ooo0o0 , i1IiII1i1I , iI1ii1ii1I , o0Ooo00 , oo )
 time . sleep ( 1 )
 if 17 - 17: oOoO0o00OO0
 oOoO0ooO0000 = xbmc . translatePath ( os . path . join ( I1ii1i11i , iIIi11i1i1i1I + '_guisettings.zip' ) )
 OOOOO = zipfile . ZipFile ( oOoO0ooO0000 , mode = 'w' )
 if 68 - 68: oOoO0o00OO0 + OoO0O00 - O0 / OoO0O00 * OoOoOO00
 try :
  OOOOO . write ( O0O , 'guisettings.xml' , zipfile . ZIP_DEFLATED )
 except : I1iiIiiii1111 = 0
 if 50 - 50: Oo + II111iiii . I1IiiI / i1IIi / I1IiiI * ooOo
 try :
  OOOOO . write ( xbmc . translatePath ( os . path . join ( iiI1IiI , 'userdata' , 'profiles.xml' ) ) , 'profiles.xml' , zipfile . ZIP_DEFLATED )
 except : pass
 if 85 - 85: II111iiii . oOO % Oo % oOoO0o00OO0
 OOOOO . close ( )
 if 80 - 80: ooOo * oOoO0o00OO0 / iIii1I11I1II1 % ooOo / iIii1I11I1II1
 if o0oO0 == 'true' :
  Iiii1 = zipfile . ZipFile ( II11ii1 , mode = 'w' )
  try :
   Iiii1 . write ( O0O , 'guisettings.xml' , zipfile . ZIP_DEFLATED )
  except : I1iiIiiii1111 = 0
  if 36 - 36: OOo00O0
  try :
   Iiii1 . write ( xbmc . translatePath ( os . path . join ( iiI1IiI , 'userdata' , 'profiles.xml' ) ) , 'profiles.xml' , zipfile . ZIP_DEFLATED )
  except : pass
  Iiii1 . close ( )
  if 90 - 90: O0
  if I1iiIiiii1111 == 0 :
   oOOoO0 . ok ( "FAILED!" , 'The guisettings.xml file could not be found on your system, please reboot and try again.' , '' , '' )
   if 44 - 44: i1IIi . I1IiiI / i11iIiiIii + iIII
  else :
   oOOoO0 . ok ( "SUCCESS!" , 'You Are Now Backed Up and can share this build with the community.' )
   if 27 - 27: Oo
   if o0oO0 == 'true' :
    oOOoO0 . ok ( "Build Locations" , 'Full Backup (only used to restore on this device): [COLOR=dodgerblue]' + Oooooo0O00o , '[/COLOR]Universal Backup: [COLOR=dodgerblue]' + i1i1iI1 + '[/COLOR]' )
    if 52 - 52: iIi1i1ii1 % OoOoOO00 + iIii1I11I1II1 * ooOo . iI1iiIiiII
   else :
    oOOoO0 . ok ( "Build Location" , 'Universal Backup:[CR][COLOR=dodgerblue]' + i1i1iI1 + '[/COLOR]' )
    if 95 - 95: iIii1I11I1II1 . iIII - OoooooooOO * OoO0O00 / o0oOOo0O0Ooo
    if 74 - 74: ooOo
def iII1i1IIiI1I ( ) :
 o0OoOOo ( )
 ii1I11iIiIII1 = oOOoO0 . yesno ( '[COLOR=gold]Create[/COLOR] [COLOR=orange]noobs[/COLOR][COLOR=dodgerblue]and[/COLOR][COLOR=orange]nerds[/COLOR] [COLOR=gold]Build[/COLOR]' , 'This backup will only work if you share your build on the [COLOR=orange]noobs[/COLOR][COLOR=dodgerblue]and[/COLOR][COLOR=orange]nerds[/COLOR] portal with the rest of the community. It will not work with any other installer/wizard, do you wish to continue?' )
 if 67 - 67: iI1iiIiiII
 if ii1I11iIiIII1 == 1 :
  I1iiIiiii1111 = 1
  I1ii1i11i = xbmc . translatePath ( os . path . join ( I1IIIii , 'Community Builds' , 'My Builds' , '' ) )
  Oooooo0O00o = xbmc . translatePath ( os . path . join ( I1IIIii , 'Community Builds' , 'My Builds' , 'my_full_backup.zip' ) )
  II11ii1 = xbmc . translatePath ( os . path . join ( I1IIIii , 'Community Builds' , 'My Builds' , 'my_full_backup_GUI_Settings.zip' ) )
  if 43 - 43: OoO0O00 % OoO0O00
  if not os . path . exists ( I1ii1i11i ) :
   os . makedirs ( I1ii1i11i )
   if 46 - 46: Oo0Ooo % iIii1I11I1II1 . OOo00O0 . O0 * oOO / OoooooooOO
  o0OO00oo0O = Ii1I1i111 ( heading = "Enter a name for this backup" )
  if 7 - 7: ooOo - O0 * oOoO0o00OO0 - o0oOOo0O0Ooo - II111iiii
  if ( not o0OO00oo0O ) :
   return False , 0
   if 41 - 41: I1IiiI - iIi1i1ii1 % II111iiii . iIi1i1ii1 - oOoO0o00OO0
  iIIi11i1i1i1I = urllib . quote_plus ( o0OO00oo0O )
  i1i1iI1 = xbmc . translatePath ( os . path . join ( I1ii1i11i , iIIi11i1i1i1I + '.zip' ) )
  if 45 - 45: iI1iiIiiII - Oo
  if 70 - 70: OoO0O00 % I1IiiI / I1IiiI . oOoO0o00OO0 % oOO . II111iiii
  oOOO00OOOoOO = [ I1IiI ]
  III = [ "xbmc.log" , "xbmc.old.log" , "kodi.log" , "kodi.old.log" , '.DS_Store' , '.setup_complete' , 'XBMCHelper.conf' , 'Thumbs.db' , '.gitignore' ]
  o0Ooo00 = [ I1IiI , 'cache' , 'system' , 'addons' , 'Thumbnails' , "peripheral_data" , 'library' , 'keymaps' , 'script.module.metahandler' , 'script.artistslideshow' , 'ArtistSlideshow' ]
  oo = [ "xbmc.log" , "xbmc.old.log" , "kodi.log" , "kodi.old.log" , "Textures13.db" , '.DS_Store' , '.setup_complete' , 'XBMCHelper.conf' , 'advancedsettings.xml' , 'Thumbs.db' , '.gitignore' ]
  i11Ii1iIiII = "Creating full backup of existing build"
  iiIIiii = "Creating Community Build"
  O0oOo00Ooo0o0 = "Archiving..."
  i1IiII1i1I = ""
  iI1ii1ii1I = "Please Wait"
  if 10 - 10: iI1iiIiiII - i11iIiiIii . I1ii11iIi11i % i1IIi
  if 78 - 78: iIii1I11I1II1 * Oo0Ooo . Oo0Ooo - Oo . iIii1I11I1II1
  if o0oO0 == 'true' :
   i1II1iII ( iiI1IiI , Oooooo0O00o , i11Ii1iIiII , O0oOo00Ooo0o0 , i1IiII1i1I , iI1ii1ii1I , oOOO00OOOoOO , III )
   if 30 - 30: oOO + oOO % iIII - o0oOOo0O0Ooo - I1ii11iIi11i
  ii1I11iIiIII1 = xbmcgui . Dialog ( ) . yesno ( "Do you want to include your addon_data folder?" , 'This contains ALL addon settings including passwords but may also contain important information such as skin shortcuts. We recommend MANUALLY removing the addon_data folders that aren\'t required.' , yeslabel = 'Yes' , nolabel = 'No' )
  if 36 - 36: oOoO0o00OO0 % Oo
  if 72 - 72: I1IiiI / OOo00O0 - O0 + oOoO0o00OO0
  if ii1I11iIiIII1 == 0 :
   o0Ooo00 = [ I1IiI , 'cache' , 'system' , 'addons' , 'peripheral_data' , 'library' , 'keymaps' , 'addon_data' , 'Thumbnails' ]
   if 83 - 83: O0
  elif ii1I11iIiIII1 == 1 :
   pass
   if 89 - 89: Oo0Ooo + I1ii11iIi11i - o0oOOo0O0Ooo
   if 40 - 40: OoO0O00 + OoO0O00
  oO00oo000O ( )
  i1iIIII1iiIIi ( iiI1IiI )
  i1II1iII ( iiI1IiI , i1i1iI1 , iiIIiii , O0oOo00Ooo0o0 , i1IiII1i1I , iI1ii1ii1I , o0Ooo00 , oo )
  if 94 - 94: OOo00O0 * iIii1I11I1II1 . oOoO0o00OO0
  if 13 - 13: iIii1I11I1II1 * OoOoOO00 / iIi1i1ii1 % oOO + ooOo
  try :
   os . remove ( Oo0OoO00oOO0o )
  except :
   pass
   if 41 - 41: I1ii11iIi11i
  try :
   os . remove ( Oo0oOOo )
  except :
   pass
   if 5 - 5: Oo0Ooo
  time . sleep ( 1 )
  if 100 - 100: iI1iiIiiII + iIii1I11I1II1
  if 59 - 59: iIII
  oOoO0ooO0000 = xbmc . translatePath ( os . path . join ( I1ii1i11i , iIIi11i1i1i1I + '_guisettings.zip' ) )
  OOOOO = zipfile . ZipFile ( oOoO0ooO0000 , mode = 'w' )
  if 89 - 89: OoOoOO00 % iIii1I11I1II1
  try :
   OOOOO . write ( O0O , 'guisettings.xml' , zipfile . ZIP_DEFLATED )
   if 35 - 35: I1ii11iIi11i + iIi1i1ii1 - OoOoOO00 % ooOo % o0oOOo0O0Ooo % OoOoOO00
  except :
   I1iiIiiii1111 = 0
   if 45 - 45: I1IiiI * Oo % OoO0O00
  try :
   OOOOO . write ( xbmc . translatePath ( os . path . join ( iiI1IiI , 'userdata' , 'profiles.xml' ) ) , 'profiles.xml' , zipfile . ZIP_DEFLATED )
   if 24 - 24: oOO - oOoO0o00OO0 * ooOo
  except :
   pass
   if 87 - 87: iI1iiIiiII - I1ii11iIi11i % I1ii11iIi11i . ooOo / I1ii11iIi11i
  OOOOO . close ( )
  if 6 - 6: OoOoOO00 / iIii1I11I1II1 * OoooooooOO * i11iIiiIii
  if 79 - 79: iIII % OoO0O00
  if o0oO0 == 'true' :
   Iiii1 = zipfile . ZipFile ( II11ii1 , mode = 'w' )
   if 81 - 81: i11iIiiIii + i11iIiiIii * OoO0O00 + iIII
   try :
    Iiii1 . write ( O0O , 'guisettings.xml' , zipfile . ZIP_DEFLATED )
    if 32 - 32: O0 . OoooooooOO
   except :
    I1iiIiiii1111 = 0
    if 15 - 15: I1IiiI . OoO0O00
   try :
    Iiii1 . write ( xbmc . translatePath ( os . path . join ( iiI1IiI , 'userdata' , 'profiles.xml' ) ) , 'profiles.xml' , zipfile . ZIP_DEFLATED )
    if 17 - 17: i11iIiiIii / Oo0Ooo . OoO0O00 / I1IiiI
   except :
    pass
    if 38 - 38: i1IIi . I1ii11iIi11i % iI1iiIiiII + iIii1I11I1II1 + O0
   Iiii1 . close ( )
   if 47 - 47: OoO0O00 + iIII / II111iiii
  if I1iiIiiii1111 == 0 :
   oOOoO0 . ok ( "FAILED!" , 'The guisettings.xml file could not be found on your system, please reboot and try again.' , '' , '' )
   if 97 - 97: I1ii11iIi11i / I1IiiI % O0 + i1IIi - oOO
  else :
   oOOoO0 . ok ( "SUCCESS!" , 'You Are Now Backed Up and can share this build with the community.' )
   if 38 - 38: o0oOOo0O0Ooo % iIi1i1ii1 + i11iIiiIii + OOo00O0 + oOO / i11iIiiIii
   if o0oO0 == 'true' :
    oOOoO0 . ok ( "Build Locations" , 'Full Backup (only used to restore on this device): [COLOR=dodgerblue]' + Oooooo0O00o , '[/COLOR]Universal Backup (this will ONLY work for sharing on the [COLOR=orange]noobs[/COLOR][COLOR=dodgerblue]and[/COLOR][COLOR=orange]nerds[/COLOR] portal):[CR][COLOR=dodgerblue]' + i1i1iI1 + '[/COLOR]' )
    if 94 - 94: OOo00O0 - Oo0Ooo + ooOo
   else :
    oOOoO0 . ok ( "Build Location" , 'Universal Backup (this will ONLY work for sharing on the [COLOR=orange]noobs[/COLOR][COLOR=dodgerblue]and[/COLOR][COLOR=orange]nerds[/COLOR] portal):[CR][COLOR=dodgerblue]' + i1i1iI1 + '[/COLOR]' )
    if 59 - 59: oOoO0o00OO0 . I1IiiI - iIii1I11I1II1 + iIii1I11I1II1
    if 56 - 56: ooOo + oOO
def Ii1Ii1 ( url , video ) :
 ii1111iII = 'http://noobsandnerds.com/TI/Community_Builds/community_builds_premium.php?id=%s' % ( url )
 iiiiI = oooOo0OOOoo0 ( ii1111iII ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 ii1IiI11I = re . compile ( 'path="(.+?)"' ) . findall ( iiiiI )
 OO0Ooo000O0 = re . compile ( 'myart="(.+?)"' ) . findall ( iiiiI )
 o00o = re . compile ( 'artpack="(.+?)"' ) . findall ( iiiiI )
 iI1i11 = re . compile ( 'videopreview="(.+?)"' ) . findall ( iiiiI )
 Iiii1Ii = re . compile ( 'videoguide1="(.+?)"' ) . findall ( iiiiI )
 ooOOo00oo0 = re . compile ( 'videoguide2="(.+?)"' ) . findall ( iiiiI )
 IIIII1Ii = re . compile ( 'videoguide3="(.+?)"' ) . findall ( iiiiI )
 iIiI1 = re . compile ( 'videoguide4="(.+?)"' ) . findall ( iiiiI )
 I1IiII1I1i1I1 = re . compile ( 'videoguide5="(.+?)"' ) . findall ( iiiiI )
 II11iiI = re . compile ( 'videolabel1="(.+?)"' ) . findall ( iiiiI )
 iiIi = re . compile ( 'videolabel2="(.+?)"' ) . findall ( iiiiI )
 OooooOo = re . compile ( 'videolabel3="(.+?)"' ) . findall ( iiiiI )
 IIIiiiIiI = re . compile ( 'videolabel4="(.+?)"' ) . findall ( iiiiI )
 OO0OOoooo0o = re . compile ( 'videolabel5="(.+?)"' ) . findall ( iiiiI )
 O00o0 = re . compile ( 'name="(.+?)"' ) . findall ( iiiiI )
 IiIi1Ii = re . compile ( 'author="(.+?)"' ) . findall ( iiiiI )
 o000O0O = re . compile ( 'version="(.+?)"' ) . findall ( iiiiI )
 o0ooOO0o = re . compile ( 'description="(.+?)"' ) . findall ( iiiiI )
 iiIIiI11II1 = re . compile ( 'DownloadURL="(.+?)"' ) . findall ( iiiiI )
 oooOo = re . compile ( 'UpdateURL="(.+?)"' ) . findall ( iiiiI )
 oOoO0Oo0 = re . compile ( 'UpdateDate="(.+?)"' ) . findall ( iiiiI )
 i11i11i = re . compile ( 'UpdateDesc="(.+?)"' ) . findall ( iiiiI )
 iIIii = re . compile ( 'updated="(.+?)"' ) . findall ( iiiiI )
 iiI1iI = re . compile ( 'defaultskin="(.+?)"' ) . findall ( iiiiI )
 Ooo00O0 = re . compile ( 'skins="(.+?)"' ) . findall ( iiiiI )
 OoO0OOoO0 = re . compile ( 'videoaddons="(.+?)"' ) . findall ( iiiiI )
 iiI11i = re . compile ( 'audioaddons="(.+?)"' ) . findall ( iiiiI )
 o0Oo = re . compile ( 'programaddons="(.+?)"' ) . findall ( iiiiI )
 iiI1i = re . compile ( 'pictureaddons="(.+?)"' ) . findall ( iiiiI )
 i11I = re . compile ( 'sources="(.+?)"' ) . findall ( iiiiI )
 o0oO0o0oo0O0 = re . compile ( 'adult="(.+?)"' ) . findall ( iiiiI )
 O0oo00oOOO0o = re . compile ( 'guisettings="(.+?)"' ) . findall ( iiiiI )
 II1iI111iiIIiI1I = re . compile ( 'thumb="(.+?)"' ) . findall ( iiiiI )
 ooO00Oo = re . compile ( 'fanart="(.+?)"' ) . findall ( iiiiI )
 if 41 - 41: i11iIiiIii - i1IIi / Oo0Ooo * iIII / iIi1i1ii1 - Oo0Ooo
 oOOoOOO0oOoo = OO0Ooo000O0 [ 0 ] if ( len ( OO0Ooo000O0 ) > 0 ) else ''
 o0O0ooooooo00 = o00o [ 0 ] if ( len ( o00o ) > 0 ) else ''
 O0Oo0 = ii1IiI11I [ 0 ] if ( len ( ii1IiI11I ) > 0 ) else ''
 I1i11i = O00o0 [ 0 ] if ( len ( O00o0 ) > 0 ) else ''
 I1111ii11IIII = IiIi1Ii [ 0 ] if ( len ( IiIi1Ii ) > 0 ) else ''
 iIIiIiI1I1 = o000O0O [ 0 ] if ( len ( o000O0O ) > 0 ) else ''
 IIIii = o0ooOO0o [ 0 ] if ( len ( o0ooOO0o ) > 0 ) else 'No information available'
 oOoO0 = iIIii [ 0 ] if ( len ( iIIii ) > 0 ) else ''
 IiIi1II111I = iiI1iI [ 0 ] if ( len ( iiI1iI ) > 0 ) else ''
 o00oIIi1i1 = Ooo00O0 [ 0 ] if ( len ( Ooo00O0 ) > 0 ) else ''
 o0O0Ooo = OoO0OOoO0 [ 0 ] if ( len ( OoO0OOoO0 ) > 0 ) else ''
 O0oO00oOOooO = iiI11i [ 0 ] if ( len ( iiI11i ) > 0 ) else ''
 IiI = o0Oo [ 0 ] if ( len ( o0Oo ) > 0 ) else ''
 Iii1iiI = iiI1i [ 0 ] if ( len ( iiI1i ) > 0 ) else ''
 ii1IiiII = i11I [ 0 ] if ( len ( i11I ) > 0 ) else ''
 IiiI1II1II1i = o0oO0o0oo0O0 [ 0 ] if ( len ( o0oO0o0oo0O0 ) > 0 ) else ''
 iIO0OO0o0O00oO = O0oo00oOOO0o [ 0 ] if ( len ( O0oo00oOOO0o ) > 0 ) else 'None'
 o00O = iiIIiI11II1 [ 0 ] if ( len ( iiIIiI11II1 ) > 0 ) else 'None'
 oO0o0oOo = oooOo [ 0 ] if ( len ( oooOo ) > 0 ) else 'None'
 OoO0O0oo0o = oOoO0Oo0 [ 0 ] if ( len ( oOoO0Oo0 ) > 0 ) else 'None'
 iIi11I11 = i11i11i [ 0 ] if ( len ( i11i11i ) > 0 ) else 'None'
 o00iiI1Ii1 = iI1i11 [ 0 ] if ( len ( iI1i11 ) > 0 ) else 'None'
 oOOoo = Iiii1Ii [ 0 ] if ( len ( Iiii1Ii ) > 0 ) else 'None'
 iII1111III1I = ooOOo00oo0 [ 0 ] if ( len ( ooOOo00oo0 ) > 0 ) else 'None'
 ii11i = IIIII1Ii [ 0 ] if ( len ( IIIII1Ii ) > 0 ) else 'None'
 O00oOo00o0o = iIiI1 [ 0 ] if ( len ( iIiI1 ) > 0 ) else 'None'
 O00oO0 = I1IiII1I1i1I1 [ 0 ] if ( len ( I1IiII1I1i1I1 ) > 0 ) else 'None'
 I1I = II11iiI [ 0 ] if ( len ( II11iiI ) > 0 ) else 'None'
 ooooo = iiIi [ 0 ] if ( len ( iiIi ) > 0 ) else 'None'
 i11IIIiI1I = OooooOo [ 0 ] if ( len ( OooooOo ) > 0 ) else 'None'
 o0iiiI1I1iIIIi1 = IIIiiiIiI [ 0 ] if ( len ( IIIiiiIiI ) > 0 ) else 'None'
 IiiI1iiiiI1iI = OO0OOoooo0o [ 0 ] if ( len ( OO0OOoooo0o ) > 0 ) else 'None'
 iii1IIIiiiI = II1iI111iiIIiI1I [ 0 ] if ( len ( II1iI111iiIIiI1I ) > 0 ) else 'None'
 OoO00oo00 = ooO00Oo [ 0 ] if ( len ( ooO00Oo ) > 0 ) else 'None'
 if 40 - 40: iIii1I11I1II1
 II1II1IIII = open ( OOO00 , mode = 'w+' )
 II1II1IIII . write ( 'id="' + str ( video ) + '"\nname="' + I1i11i + '"\nversion="' + iIIiIiI1I1 + '"' )
 II1II1IIII . close ( )
 if 92 - 92: OoOoOO00 % O0
 oo00ooooOOo00 = open ( iiiiiIIii , mode = 'r' )
 ii1iOO00Oooo000 = oo00ooooOOo00 . read ( )
 oo00ooooOOo00 . close ( )
 if 38 - 38: OoO0O00 . oOO
 i11I1I1iiI = re . compile ( 'id="(.+?)"' ) . findall ( ii1iOO00Oooo000 )
 ii111iiIii = i11I1I1iiI [ 0 ] if ( len ( i11I1I1iiI ) > 0 ) else 'None'
 oO0o = re . compile ( 'version="(.+?)"' ) . findall ( ii1iOO00Oooo000 )
 i1Oo00 = oO0o [ 0 ] if ( len ( oO0o ) > 0 ) else 'None'
 iIiI , iIIiiiI1iI1 , oO00000oO0o0O = url . partition ( '&' )
 IIii ( '' , '[COLOR=yellow]IMPORTANT:[/COLOR] Install Instructions' , '' , 'instructions_2' , 'noobsandnerds.png' , '' , '' , '' )
 o00o0 ( '[COLOR=yellow]Description:[/COLOR] This contains important info from the build author' , 'None' , 'description' , 'BUILDDETAILS.png' , OoO00oo00 , I1i11i , I1111ii11IIII , iIIiIiI1I1 , IIIii , oOoO0 , o00oIIi1i1 , o0O0Ooo , O0oO00oOOooO , IiI , Iii1iiI , ii1IiiII , IiiI1II1II1i )
 if 34 - 34: Oo0Ooo - i1IIi - oOO - i1IIi
 if ii111iiIii == iIiI and i1Oo00 != iIIiIiI1I1 :
  IIii ( '' , '[COLOR=orange]----------------- UPDATE AVAILABLE ------------------[/COLOR]' , 'None' , '' , 'noobsandnerds.png' , '' , '' , '' )
  ooO00OO0 ( '[COLOR=dodgerblue]1. Update:[/COLOR] Erase My current build and install new build' , o00O , 'restore_community' , iii1IIIiiiI , '' , 'update' , I1i11i , IiIi1II111I , iIO0OO0o0O00oO , o0O0ooooooo00 )
  ooO00OO0 ( '[COLOR=dodgerblue]2. Update:[/COLOR] Keep My Library & Profiles' , o00O , 'restore_community' , iii1IIIiiiI , '' , 'updatelibprofile' , I1i11i , IiIi1II111I , iIO0OO0o0O00oO , o0O0ooooooo00 )
  ooO00OO0 ( '[COLOR=dodgerblue]3. Update:[/COLOR] Keep My Library Only' , o00O , 'restore_community' , iii1IIIiiiI , '' , 'updatelibrary' , I1i11i , IiIi1II111I , iIO0OO0o0O00oO , o0O0ooooooo00 )
  ooO00OO0 ( '[COLOR=dodgerblue]4. Update:[/COLOR] Keep My Profiles Only' , o00O , 'restore_community' , iii1IIIiiiI , '' , 'updateprofiles' , I1i11i , IiIi1II111I , iIO0OO0o0O00oO , o0O0ooooooo00 )
  if 62 - 62: oOoO0o00OO0 / ooOo % Oo0Ooo . OoooooooOO / i11iIiiIii / iIi1i1ii1
 if o00iiI1Ii1 != 'None' or oOOoo != 'None' or iII1111III1I != 'None' or ii11i != 'None' or O00oOo00o0o != 'None' or O00oO0 != 'None' :
  IIii ( '' , '[COLOR=orange]------------------ VIDEO GUIDES -----------------[/COLOR]' , 'None' , '' , 'noobsandnerds.png' , '' , '' , '' )
  if 60 - 60: I1IiiI % ooOo / o0oOOo0O0Ooo % ooOo * i11iIiiIii / OOo00O0
 if o00iiI1Ii1 != 'None' :
  IIii ( '' , '[COLOR=orange]Video:[/COLOR][COLOR=white] Preview[/COLOR]' , o00iiI1Ii1 , 'play_video' , 'Video_Preview.png' , OoO00oo00 , '' , '' )
  if 34 - 34: iIi1i1ii1 - Oo
 if oOOoo != 'None' :
  IIii ( '' , '[COLOR=orange]Video:[/COLOR][COLOR=white] ' + I1I + '[/COLOR]' , oOOoo , 'play_video' , 'Video_Guide.png' , OoO00oo00 , '' , '' )
  if 25 - 25: ooOo % I1IiiI + i11iIiiIii + O0 * OoooooooOO
 if iII1111III1I != 'None' :
  IIii ( '' , '[COLOR=orange]Video:[/COLOR][COLOR=white] ' + ooooo + '[/COLOR]' , iII1111III1I , 'play_video' , 'Video_Guide.png' , OoO00oo00 , '' , '' )
  if 64 - 64: i1IIi
 if ii11i != 'None' :
  IIii ( '' , '[COLOR=orange]Video:[/COLOR][COLOR=white] ' + i11IIIiI1I + '[/COLOR]' , ii11i , 'play_video' , 'Video_Guide.png' , OoO00oo00 , '' , '' )
  if 10 - 10: iIi1i1ii1 % O0 / I1IiiI % oOoO0o00OO0
 if O00oOo00o0o != 'None' :
  IIii ( '' , '[COLOR=orange]Video:[/COLOR][COLOR=white] ' + o0iiiI1I1iIIIi1 + '[/COLOR]' , O00oOo00o0o , 'play_video' , 'Video_Guide.png' , OoO00oo00 , '' , '' )
  if 25 - 25: II111iiii / OoO0O00
 if O00oO0 != 'None' :
  IIii ( '' , '[COLOR=orange]Video:[/COLOR][COLOR=white] ' + IiiI1iiiiI1iI + '[/COLOR]' , O00oO0 , 'play_video' , 'Video_Guide.png' , OoO00oo00 , '' , '' )
  if 64 - 64: O0 % oOO
 if ii111iiIii != iIiI :
  IIii ( '' , '[COLOR=orange]------------------ INSTALL OPTIONS ------------------[/COLOR]' , 'None' , '' , 'noobsandnerds.png' , '' , '' , '' )
  if 40 - 40: o0oOOo0O0Ooo + oOoO0o00OO0
 if o00O == 'None' :
  ooO00OO0 ( '[COLOR=orange]Sorry this build is currently unavailable[/COLOR]' , '' , '' , '' , '' , '' , '' , '' , '' , '' )
  if 77 - 77: i11iIiiIii % iIII + iIi1i1ii1 % OoooooooOO - oOoO0o00OO0
 if ii111iiIii != iIiI :
  if 26 - 26: Oo0Ooo + O0 - iIii1I11I1II1
  if 47 - 47: OoooooooOO
  if 2 - 2: OoOoOO00 % iIi1i1ii1 * Oo0Ooo * OoOoOO00
  if 65 - 65: i11iIiiIii + Oo0Ooo * OoooooooOO - OoO0O00
  ooO00OO0 ( '[COLOR=dodgerblue]1. Install:[/COLOR] Erase My current build and install new build' , o00O , 'restore_community' , iii1IIIiiiI , OoO00oo00 , 'merge' , I1i11i , IiIi1II111I , iIO0OO0o0O00oO , o0O0ooooooo00 )
  ooO00OO0 ( '[COLOR=dodgerblue]2. Install:[/COLOR] Keep My Library & Profiles' , o00O , 'restore_community' , iii1IIIiiiI , OoO00oo00 , 'libprofile' , I1i11i , IiIi1II111I , iIO0OO0o0O00oO , o0O0ooooooo00 )
  ooO00OO0 ( '[COLOR=dodgerblue]3. Install:[/COLOR] Keep My Library Only' , o00O , 'restore_community' , iii1IIIiiiI , OoO00oo00 , 'library' , I1i11i , IiIi1II111I , iIO0OO0o0O00oO , o0O0ooooooo00 )
  ooO00OO0 ( '[COLOR=dodgerblue]4. Install:[/COLOR] Keep My Profiles Only' , o00O , 'restore_community' , iii1IIIiiiI , OoO00oo00 , 'profiles' , I1i11i , IiIi1II111I , iIO0OO0o0O00oO , o0O0ooooooo00 )
  if 26 - 26: o0oOOo0O0Ooo % Oo + Oo % oOoO0o00OO0 * i11iIiiIii / OOo00O0
 if iIO0OO0o0O00oO != 'None' :
  IIii ( '' , '[COLOR=orange]---------- (OPTIONAL) Guisettings Fix ----------[/COLOR]' , 'None' , '' , 'noobsandnerds.png' , '' , '' , '' )
  IIii ( '' , '[COLOR=orange]Install Step 2:[/COLOR] Apply guisettings.xml fix' , iIO0OO0o0O00oO , 'guisettingsfix' , 'Fix_My_Build.png' , OoO00oo00 , '' , '' )
  if 64 - 64: ooOo % OoOoOO00 / II111iiii % oOO - OOo00O0
  if 2 - 2: iIi1i1ii1 - I1ii11iIi11i + o0oOOo0O0Ooo * OoO0O00 / OOo00O0
  if 26 - 26: Oo * Oo0Ooo
  if 31 - 31: oOoO0o00OO0 * ooOo . iI1iiIiiII
  if 35 - 35: oOoO0o00OO0
  if 94 - 94: oOO / i11iIiiIii % O0
  if 70 - 70: oOoO0o00OO0 - Oo0Ooo / OoooooooOO % OoooooooOO
  if 95 - 95: OoooooooOO % OoooooooOO . iI1iiIiiII
  if 26 - 26: ooOo + iIII - II111iiii . II111iiii + I1ii11iIi11i + OoOoOO00
def o0IiIiI111IIII1 ( ) :
 print '############################################################       DELETING USERDATA             ###############################################################'
 OOOoOooO000oO = xbmc . translatePath ( os . path . join ( 'special://home/userdata/addon_data' , '' ) )
 if 87 - 87: OOo00O0 % Oo0Ooo
 for OOo000o , oO0ooOoO , ooO0000o00O in os . walk ( OOOoOooO000oO ) :
  iiIIIIiI111 = 0
  iiIIIIiI111 += len ( ooO0000o00O )
  if 86 - 86: II111iiii % iIii1I11I1II1 / I1ii11iIi11i - o0oOOo0O0Ooo * iI1iiIiiII . I1IiiI
  if iiIIIIiI111 >= 0 :
   if 68 - 68: OoooooooOO * iIii1I11I1II1 + i1IIi - i1IIi
   for ooO0oo0o0 in ooO0000o00O :
    os . unlink ( os . path . join ( OOo000o , ooO0oo0o0 ) )
    if 76 - 76: OoO0O00 . OoooooooOO % iIi1i1ii1 * iI1iiIiiII
   for iiIiI1ii in oO0ooOoO :
    shutil . rmtree ( os . path . join ( OOo000o , iiIiI1ii ) )
    if 23 - 23: iIII + iIii1I11I1II1
    if 14 - 14: O0 % iIII % iI1iiIiiII * ooOo
def o0OOO00ooo ( ) :
 for I1iI11IiiI11i in glob . glob ( os . path . join ( I11i1I1I , 'xbmc_crashlog*.*' ) ) :
  IIIiIIIi11I = I1iI11IiiI11i
  os . remove ( I1iI11IiiI11i )
  oOOoO0 = xbmcgui . Dialog ( )
  oOOoO0 . ok ( "Crash Logs Deleted" , "Your old crash logs have now been deleted." )
  if 46 - 46: Oo . oOoO0o00OO0 % I1IiiI - oOO
  if 13 - 13: OoOoOO00 % OoOoOO00 % Oo0Ooo % I1IiiI * i1IIi % oOoO0o00OO0
def O0i1I11I ( ) :
 print '############################################################       DELETING PACKAGES             ###############################################################'
 I1IIi1i1Ii1I1 = xbmc . translatePath ( os . path . join ( 'special://home/addons/packages' , '' ) )
 if 85 - 85: OoooooooOO + Oo . iIii1I11I1II1 / oOoO0o00OO0 / oOoO0o00OO0
 for OOo000o , oO0ooOoO , ooO0000o00O in os . walk ( I1IIi1i1Ii1I1 ) :
  iiIIIIiI111 = 0
  iiIIIIiI111 += len ( ooO0000o00O )
  if 1 - 1: Oo - iIii1I11I1II1 * OoO0O00 * iIi1i1ii1 * O0
  if iiIIIIiI111 > 0 :
   if 98 - 98: oOO . Oo
   for ooO0oo0o0 in ooO0000o00O :
    os . unlink ( os . path . join ( OOo000o , ooO0oo0o0 ) )
    if 60 - 60: OoO0O00 - i1IIi . Oo + Oo * Oo + iI1iiIiiII
   for iiIiI1ii in oO0ooOoO :
    shutil . rmtree ( os . path . join ( OOo000o , iiIiI1ii ) )
    if 66 - 66: Oo * Oo / iIii1I11I1II1 + OoOoOO00 . Oo
    if 51 - 51: I1ii11iIi11i
def o0oOOOOoo0 ( ) :
 print '############################################################       DELETING USERDATA             ###############################################################'
 OOOoOooO000oO = xbmc . translatePath ( os . path . join ( 'special://home/userdata/addon_data' , '' ) )
 if 80 - 80: i11iIiiIii % I1ii11iIi11i
 for OOo000o , oO0ooOoO , ooO0000o00O in os . walk ( OOOoOooO000oO ) :
  iiIIIIiI111 = 0
  iiIIIIiI111 += len ( ooO0000o00O )
  if 54 - 54: o0oOOo0O0Ooo + oOoO0o00OO0 - iIii1I11I1II1 % oOO % iIII
  if iiIIIIiI111 >= 0 :
   if 19 - 19: I1ii11iIi11i / iIii1I11I1II1 % i1IIi . OoooooooOO
   for ooO0oo0o0 in ooO0000o00O :
    os . unlink ( os . path . join ( OOo000o , ooO0oo0o0 ) )
    if 57 - 57: oOO . Oo0Ooo - OoO0O00 - i11iIiiIii * iIi1i1ii1 / o0oOOo0O0Ooo
   for iiIiI1ii in oO0ooOoO :
    shutil . rmtree ( os . path . join ( OOo000o , iiIiI1ii ) )
    if 79 - 79: I1ii11iIi11i + o0oOOo0O0Ooo % Oo0Ooo * o0oOOo0O0Ooo
    if 21 - 21: OOo00O0
def o000O0OOoo ( name , addon_id ) :
 IIi = 1
 OOOOooO0oO00O0o = 1
 i11Ii = xbmc . translatePath ( os . path . join ( OO0o , addon_id , 'addon.xml' ) )
 iiiI1IiiI = open ( i11Ii , mode = 'r' )
 O0OOO0o0O = iiiI1IiiI . read ( )
 iiiI1IiiI . close ( )
 IiIIi1iiI = re . compile ( 'import addon="(.+?)"' ) . findall ( O0OOO0o0O )
 if 97 - 97: iIi1i1ii1 . oOoO0o00OO0 / I1IiiI
 for i1i1iII1 in IiIIi1iiI :
  if 83 - 83: oOoO0o00OO0 - I1ii11iIi11i * ooOo
  if not 'xbmc.python' in i1i1iII1 :
   print 'Script Requires --- ' + i1i1iII1
   oOO00OO0OooOo = xbmc . translatePath ( os . path . join ( OO0o , i1i1iII1 ) )
   if 13 - 13: O0 % oOO % oOoO0o00OO0
   if not os . path . exists ( oOO00OO0OooOo ) :
    ii1111iII = 'http://noobsandnerds.com/TI/AddonPortal/dependencyinstall.php?id=%s' % ( i1i1iII1 )
    iiiiI = oooOo0OOOoo0 ( ii1111iII ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
    O00o0 = re . compile ( 'name="(.+?)"' ) . findall ( iiiiI )
    o000O0O = re . compile ( 'version="(.+?)"' ) . findall ( iiiiI )
    o0000oO = re . compile ( 'repo_url="(.+?)"' ) . findall ( iiiiI )
    I1II1 = re . compile ( 'data_url="(.+?)"' ) . findall ( iiiiI )
    oooO = re . compile ( 'zip_url="(.+?)"' ) . findall ( iiiiI )
    i1i1iI1iiiI = re . compile ( 'repo_id="(.+?)"' ) . findall ( iiiiI )
    Ii11IiI111 = O00o0 [ 0 ] if ( len ( O00o0 ) > 0 ) else ''
    iIIiIiI1I1 = o000O0O [ 0 ] if ( len ( o000O0O ) > 0 ) else ''
    IIiii11ii1II1 = o0000oO [ 0 ] if ( len ( o0000oO ) > 0 ) else ''
    o0OO000O = I1II1 [ 0 ] if ( len ( I1II1 ) > 0 ) else ''
    O000o0000O = oooO [ 0 ] if ( len ( oooO ) > 0 ) else ''
    O00Ooo0O0OOOo = i1i1iI1iiiI [ 0 ] if ( len ( i1i1iI1iiiI ) > 0 ) else ''
    o0oooo0O = xbmc . translatePath ( os . path . join ( ooOooo000oOO , Ii11IiI111 + '.zip' ) )
    if 22 - 22: ooOo * OOo00O0
    try :
     downloader . download ( IIiii11ii1II1 , o0oooo0O , O0OoO000O0OO )
     oOO00oO00O0OO ( o0oooo0O , OO0o , O0OoO000O0OO )
     if 4 - 4: OoOoOO00 - ooOo + I1IiiI
    except :
     if 36 - 36: iIII
     try :
      downloader . download ( O000o0000O , o0oooo0O , O0OoO000O0OO )
      oOO00oO00O0OO ( o0oooo0O , OO0o , O0OoO000O0OO )
      if 19 - 19: OoOoOO00 . o0oOOo0O0Ooo . OoooooooOO
     except :
      if 13 - 13: Oo . Oo0Ooo / II111iiii
      try :
       if 43 - 43: iIii1I11I1II1 % OoO0O00
       if not os . path . exists ( oOO00OO0OooOo ) :
        os . makedirs ( oOO00OO0OooOo )
        if 84 - 84: Oo0Ooo
       iiiiI = oooOo0OOOoo0 ( o0OO000O ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
       O0OoOoO00O = re . compile ( 'href="(.+?)"' , re . DOTALL ) . findall ( iiiiI )
       if 44 - 44: OoooooooOO * i11iIiiIii / Oo0Ooo
       for Ii11Iii1i1ii in O0OoOoO00O :
        Ii1i1i1111 = xbmc . translatePath ( os . path . join ( oOO00OO0OooOo , Ii11Iii1i1ii ) )
        if 75 - 75: OoooooooOO . Oo + OoO0O00 / iI1iiIiiII - I1IiiI % iI1iiIiiII
        if addon_id not in Ii11Iii1i1ii and '/' not in Ii11Iii1i1ii :
         if 89 - 89: OOo00O0 * iIii1I11I1II1 + i11iIiiIii . OoooooooOO
         try :
          O0OoO000O0OO . update ( 0 , "Downloading [COLOR=yellow]" + Ii11Iii1i1ii + '[/COLOR]' , '' , 'Please wait...' )
          downloader . download ( o0OO000O + Ii11Iii1i1ii , Ii1i1i1111 , O0OoO000O0OO )
          if 51 - 51: Oo / oOO + OoO0O00 % OoOoOO00 / iI1iiIiiII
         except :
          print "failed to install" + Ii11Iii1i1ii
          if 25 - 25: o0oOOo0O0Ooo
        if '/' in Ii11Iii1i1ii and '..' not in Ii11Iii1i1ii and 'http' not in Ii11Iii1i1ii :
         ooo0oooo0 = o0OO000O + Ii11Iii1i1ii
         OOO0ooo ( Ii1i1i1111 , ooo0oooo0 )
         if 25 - 25: oOO * OOo00O0 / oOoO0o00OO0 / oOoO0o00OO0 % o0oOOo0O0Ooo
      except :
       oOOoO0 . ok ( "Error downloading dependency" , 'There was an error downloading [COLOR=dodgerblue]' + Ii11IiI111 + '[/COLOR]. Please consider updating the add-on portal with details or report the error on the forum at [COLOR=orange]noobs[/COLOR][COLOR=dodgerblue]and[/COLOR][COLOR=orange]nerds[/COLOR]' )
       OOOOooO0oO00O0o = 0
       IIi = 0
       if 19 - 19: ooOo - iIii1I11I1II1 / oOO . OoO0O00 * O0 - O0
    if OOOOooO0oO00O0o == 1 :
     time . sleep ( 1 )
     O0OoO000O0OO . update ( 0 , "[COLOR=yellow]" + Ii11IiI111 + '[/COLOR]  [COLOR=lime]Successfully Installed[/COLOR]' , '' , 'Please wait...' )
     time . sleep ( 1 )
     O0O0o0o0o = 'http://noobsandnerds.com/TI/AddonPortal/downloadcount.php?id=%s' % ( i1i1iII1 )
     oooOo0OOOoo0 ( O0O0o0o0o )
 O0OoO000O0OO . close ( )
 time . sleep ( 1 )
 if 41 - 41: i1IIi - I1IiiI
 if 48 - 48: I1IiiI - II111iiii / OoO0O00 + I1IiiI
def i1iii1IiiiI1i1 ( name , url , buildname , author , version , description , updated , skins , videoaddons , audioaddons , programaddons , pictureaddons , sources , adult ) :
 IIIiI1i1 ( buildname + '     v.' + version , '[COLOR=yellow][B]Author:   [/B][/COLOR]' + author + '[COLOR=yellow][B]               Last Updated:   [/B][/COLOR]' + updated + '[COLOR=yellow][B]               Adult Content:   [/B][/COLOR]' + adult + '[CR][CR][COLOR=yellow][B]Description:[CR][/B][/COLOR]' + description +
 '[CR][CR][COLOR=blue][B]Skins:   [/B][/COLOR]' + skins + '[CR][CR][COLOR=blue][B]Video Addons:   [/B][/COLOR]' + videoaddons + '[CR][CR][COLOR=blue][B]Audio Addons:   [/B][/COLOR]' + audioaddons +
 '[CR][CR][COLOR=blue][B]Program Addons:   [/B][/COLOR]' + programaddons + '[CR][CR][COLOR=blue][B]Picture Addons:   [/B][/COLOR]' + pictureaddons + '[CR][CR][COLOR=blue][B]Sources:   [/B][/COLOR]' + sources +
 '[CR][CR][COLOR=orange]Disclaimer: [/COLOR]These are community builds and they may overwrite some of your existing settings, '
 'It\'s purely the responsibility of the user to choose whether or not they wish to install these builds, the individual who uploads the build should state what\'s included and then it\'s the users decision to decide whether or not that content is suitable for them.' )
 if 13 - 13: Oo * oOoO0o00OO0 / O0 * o0oOOo0O0Ooo
 if 35 - 35: i1IIi * i11iIiiIii % I1ii11iIi11i / iIII / iIII
def OO00oO0OoO0o ( path ) :
 O0OoO000O0OO . create ( "[COLOR=orange]noobs[/COLOR][COLOR=dodgerblue]and[/COLOR][COLOR=orange]nerds[/COLOR]" , "Wiping..." , '' , 'Please Wait' )
 shutil . rmtree ( path , ignore_errors = True )
 if 5 - 5: Oo % Oo0Ooo % iIII % oOO
 if 17 - 17: iI1iiIiiII + II111iiii + OoooooooOO / Oo / iIII
def oOO00oO00O0OO ( _in , _out , dp = None ) :
 if dp :
  return oOoo0Ooooo ( _in , _out , dp )
  if 15 - 15: II111iiii * ooOo % OOo00O0 / i11iIiiIii - ooOo + Oo0Ooo
 return I1IIii11 ( _in , _out )
 if 22 - 22: oOO / oOO - iI1iiIiiII % oOoO0o00OO0 . Oo + iIII
 if 64 - 64: i1IIi % I1ii11iIi11i / iI1iiIiiII % OoooooooOO
def I1IIii11 ( _in , _out ) :
 try :
  I1iii1 = zipfile . ZipFile ( _in , 'r' )
  I1iii1 . extractall ( _out )
  if 19 - 19: ooOo % OoooooooOO . OoooooooOO
 except Exception , IiIiI11IIi11Iii :
  print str ( IiIiI11IIi11Iii )
  return False
  if 9 - 9: ooOo
 return True
 if 2 - 2: iIii1I11I1II1 * I1IiiI % i1IIi % I1ii11iIi11i + OoooooooOO + I1IiiI
 if 16 - 16: Oo
def oOoo0Ooooo ( _in , _out , dp ) :
 I1iii1 = zipfile . ZipFile ( _in , 'r' )
 oooO0o0oOoO = float ( len ( I1iii1 . infolist ( ) ) )
 I11iii = 0
 if 11 - 11: ooOo + iIi1i1ii1 . iIII * OoooooooOO - I1ii11iIi11i - Oo
 try :
  if 16 - 16: OOo00O0 / iIii1I11I1II1 + Oo * OOo00O0 * oOoO0o00OO0
  for iiIiI11IiI1ii in I1iii1 . infolist ( ) :
   I11iii += 1
   ooO0O0 = I11iii / oooO0o0oOoO * 100
   dp . update ( int ( ooO0O0 ) )
   I1iii1 . extract ( iiIiI11IiI1ii , _out )
   if 34 - 34: i1IIi - OoOoOO00 + o0oOOo0O0Ooo - Oo0Ooo % I1ii11iIi11i
 except Exception , IiIiI11IIi11Iii :
  print str ( IiIiI11IIi11Iii )
  return False
  if 43 - 43: oOoO0o00OO0 % i1IIi % oOO . i11iIiiIii
 return True
 if 56 - 56: O0 * OOo00O0 + OOo00O0 * iIii1I11I1II1 / oOO * iIi1i1ii1
def Oo0oO00 ( ) :
 os . remove ( iiiiiIIii )
 os . rename ( OOOOi11i1 , iiiiiIIii )
 xbmc . executebuiltin ( 'UnloadSkin' )
 xbmc . executebuiltin ( "ReloadSkin" )
 oOOoO0 . ok ( "Local Restore Complete" , 'XBMC/Kodi will now close.' , '' , '' )
 xbmc . executebuiltin ( "Quit" )
 if 25 - 25: iIii1I11I1II1 . oOoO0o00OO0 * i11iIiiIii + Oo0Ooo * oOoO0o00OO0
 if 67 - 67: OOo00O0
def i1iIIII1iiIIi ( url ) :
 O0OoO000O0OO . create ( "Changing Physical Paths To Special" , "Renaming paths..." , '' , 'Please Wait' )
 if 88 - 88: Oo0Ooo
 for OOo000o , oO0ooOoO , ooO0000o00O in os . walk ( url ) :
  if 8 - 8: I1ii11iIi11i
  for file in ooO0000o00O :
   if 82 - 82: OoooooooOO
   if file . endswith ( ".xml" ) :
    O0OoO000O0OO . update ( 0 , "Fixing" , file , 'Please Wait' )
    IIii1I1i = open ( ( os . path . join ( OOo000o , file ) ) ) . read ( )
    OoOO00oo0o = IIii1I1i . replace ( iiI1IiI , 'special://home/' )
    ooO0oo0o0 = open ( ( os . path . join ( OOo000o , file ) ) , mode = 'w' )
    ooO0oo0o0 . write ( str ( OoOO00oo0o ) )
    ooO0oo0o0 . close ( )
    if 76 - 76: OOo00O0 . iIII % OOo00O0 - iIi1i1ii1
    if 51 - 51: OoooooooOO + o0oOOo0O0Ooo * iIii1I11I1II1 * ooOo / i1IIi
def I11IiI1i ( ) :
 OooO = 'http://noobsandnerds.com/TI/AddonPortal/Addon_Fix/addonfix.txt'
 iiiiI = oooOo0OOOoo0 ( OooO ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 O0OoOoO00O = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( iiiiI )
 if 85 - 85: II111iiii
 for I1i11i , o0oOOoo0O , iii1IIIiiiI , OoO00oo00 , IIIii in O0OoOoO00O :
  IIii ( '' , I1i11i , o0oOOoo0O , 'OSS' , iii1IIIiiiI , OoO00oo00 , '' , IIIii )
  if 57 - 57: I1IiiI . i11iIiiIii * II111iiii + OoooooooOO + iI1iiIiiII
  if 73 - 73: O0 % oOoO0o00OO0 + OOo00O0 . I1ii11iIi11i . I1ii11iIi11i + iIII
def i1i111I ( ) :
 oOOO00OOOoOO = [ ]
 III = [ "xbmc.log" , "xbmc.old.log" , "kodi.log" , "kodi.old.log" , '.DS_Store' , '.setup_complete' , 'XBMCHelper.conf' , '.gitignore' ]
 i11Ii1iIiII = "Creating full backup of existing build"
 iiIIiii = "Creating Community Build"
 O0oOo00Ooo0o0 = "Archiving..."
 i1IiII1i1I = ""
 iI1ii1ii1I = "Please Wait"
 if 77 - 77: oOO
 i1II1iII ( iiI1IiI , myfullbackup , i11Ii1iIiII , O0oOo00Ooo0o0 , i1IiII1i1I , iI1ii1ii1I , oOOO00OOOoOO , III )
 if 52 - 52: iIi1i1ii1 - iI1iiIiiII + Oo0Ooo + OoO0O00 * iIII
 if 78 - 78: ooOo / OoooooooOO . ooOo
def I1IOoo ( url ) :
 IIii ( 'folder' , 'Anime' , str ( url ) + '&genre=anime' , 'grab_builds' , 'anime.png' , '' , '' , '' )
 IIii ( 'folder' , 'Audiobooks' , str ( url ) + '&genre=audiobooks' , 'grab_builds' , 'audiobooks.png' , '' , '' , '' )
 IIii ( 'folder' , 'Comedy' , str ( url ) + '&genre=comedy' , 'grab_builds' , 'comedy.png' , '' , '' , '' )
 IIii ( 'folder' , 'Comics' , str ( url ) + '&genre=comics' , 'grab_builds' , 'comics.png' , '' , '' , '' )
 IIii ( 'folder' , 'Documentary' , str ( url ) + '&genre=documentary' , 'grab_builds' , 'documentary.png' , '' , '' , '' )
 IIii ( 'folder' , 'Downloads' , str ( url ) + '&genre=downloads' , 'grab_builds' , 'downloads.png' , '' , '' , '' )
 IIii ( 'folder' , 'Food' , str ( url ) + '&genre=food' , 'grab_builds' , 'food.png' , '' , '' , '' )
 IIii ( 'folder' , 'Gaming' , str ( url ) + '&genre=gaming' , 'grab_builds' , 'gaming.png' , '' , '' , '' )
 IIii ( 'folder' , 'Health' , str ( url ) + '&genre=health' , 'grab_builds' , 'health.png' , '' , '' , '' )
 IIii ( 'folder' , 'How To...' , str ( url ) + '&genre=howto' , 'grab_builds' , 'howto.png' , '' , '' , '' )
 IIii ( 'folder' , 'Kids' , str ( url ) + '&genre=kids' , 'grab_builds' , 'kids.png' , '' , '' , '' )
 IIii ( 'folder' , 'Live TV' , str ( url ) + '&genre=livetv' , 'grab_builds' , 'livetv.png' , '' , '' , '' )
 IIii ( 'folder' , 'Movies' , str ( url ) + '&genre=movies' , 'grab_builds' , 'movies.png' , '' , '' , '' )
 IIii ( 'folder' , 'Music' , str ( url ) + '&genre=music' , 'grab_builds' , 'music.png' , '' , '' , '' )
 IIii ( 'folder' , 'News' , str ( url ) + '&genre=news' , 'grab_builds' , 'news.png' , '' , '' , '' )
 IIii ( 'folder' , 'Photos' , str ( url ) + '&genre=photos' , 'grab_builds' , 'photos.png' , '' , '' , '' )
 IIii ( 'folder' , 'Podcasts' , str ( url ) + '&genre=podcasts' , 'grab_builds' , 'podcasts.png' , '' , '' , '' )
 IIii ( 'folder' , 'Radio' , str ( url ) + '&genre=radio' , 'grab_builds' , 'radio.png' , '' , '' , '' )
 IIii ( 'folder' , 'Religion' , str ( url ) + '&genre=religion' , 'grab_builds' , 'religion.png' , '' , '' , '' )
 IIii ( 'folder' , 'Space' , str ( url ) + '&genre=space' , 'grab_builds' , 'space.png' , '' , '' , '' )
 IIii ( 'folder' , 'Sports' , str ( url ) + '&genre=sports' , 'grab_builds' , 'sports.png' , '' , '' , '' )
 IIii ( 'folder' , 'Technology' , str ( url ) + '&genre=tech' , 'grab_builds' , 'tech.png' , '' , '' , '' )
 IIii ( 'folder' , 'Trailers' , str ( url ) + '&genre=trailers' , 'grab_builds' , 'trailers.png' , '' , '' , '' )
 IIii ( 'folder' , 'TV Shows' , str ( url ) + '&genre=tv' , 'grab_builds' , 'tv.png' , '' , '' , '' )
 IIii ( 'folder' , 'Misc.' , str ( url ) + '&genre=other' , 'grab_builds' , 'other.png' , '' , '' , '' )
 if 94 - 94: II111iiii
 if o0O . getSetting ( 'adult' ) == 'true' :
  IIii ( 'folder' , 'XXX' , str ( url ) + '&genre=adult' , 'grab_builds' , 'adult.png' , '' , '' , '' )
  if 37 - 37: OoooooooOO
def Ii1I1i111 ( default = "" , heading = "" , hidden = False ) :
 oo0OooO = xbmc . Keyboard ( default , heading , hidden )
 if 4 - 4: iIII + iIii1I11I1II1 * OOo00O0 + Oo0Ooo * o0oOOo0O0Ooo % II111iiii
 oo0OooO . doModal ( )
 if ( oo0OooO . isConfirmed ( ) ) :
  return unicode ( oo0OooO . getText ( ) , "utf-8" )
 return default
 if 88 - 88: ooOo - i1IIi % i11iIiiIii % II111iiii * OoooooooOO
 if 40 - 40: Oo0Ooo
def iI1Ii11 ( ) :
 Ooo0 = [ ]
 IiiiIIi = sys . argv [ 2 ]
 if len ( IiiiIIi ) >= 2 :
  I1IIIi = sys . argv [ 2 ]
  OoOooOo00O = I1IIIi . replace ( '?' , '' )
  if ( I1IIIi [ len ( I1IIIi ) - 1 ] == '/' ) :
   I1IIIi = I1IIIi [ 0 : len ( I1IIIi ) - 2 ]
  oo0O0oOOO0o = OoOooOo00O . split ( '&' )
  Ooo0 = { }
  for oOo0Oo0Oo0 in range ( len ( oo0O0oOOO0o ) ) :
   OooOo0o0OO = { }
   OooOo0o0OO = oo0O0oOOO0o [ oOo0Oo0Oo0 ] . split ( '=' )
   if ( len ( OooOo0o0OO ) ) == 2 :
    Ooo0 [ OooOo0o0OO [ 0 ] ] = OooOo0o0OO [ 1 ]
    if 1 - 1: iIii1I11I1II1 % oOO + O0
 return Ooo0
 if 22 - 22: o0oOOo0O0Ooo + Oo0Ooo . oOO + I1ii11iIi11i * OOo00O0 . i11iIiiIii
def O0OOOOOO0ooO ( ) :
 O0Oo0 = xbmc . translatePath ( os . path . join ( 'special://home' , 'addons' ) )
 O0OoO000O0OO = xbmcgui . DialogProgress ( )
 O0OoO000O0OO . create ( "Gotham Addon Fix" , "Please wait whilst your addons" , '' , 'are being made Gotham compatible.' )
 if 18 - 18: Oo0Ooo - Oo * II111iiii + ooOo
 for I1iI11IiiI11i in glob . glob ( os . path . join ( O0Oo0 , '*.*' ) ) :
  if 93 - 93: OOo00O0 * ooOo . OoO0O00 - iI1iiIiiII + O0 * OoO0O00
  for file in glob . glob ( os . path . join ( I1iI11IiiI11i , '*.*' ) ) :
   if 59 - 59: II111iiii
   if 'addon.xml' in file :
    O0OoO000O0OO . update ( 0 , "Fixing" , file , 'Please Wait' )
    IIii1I1i = open ( file ) . read ( )
    OoOO00oo0o = IIii1I1i . replace ( 'addon="xbmc.python" version="1.0"' , 'addon="xbmc.python" version="2.1.0"' ) . replace ( 'addon="xbmc.python" version="2.0"' , 'addon="xbmc.python" version="2.1.0"' )
    ooO0oo0o0 = open ( file , mode = 'w' )
    ooO0oo0o0 . write ( str ( OoOO00oo0o ) )
    ooO0oo0o0 . close ( )
    if 43 - 43: Oo0Ooo + OoooooooOO
 oOOoO0 = xbmcgui . Dialog ( )
 oOOoO0 . ok ( "Your addons have now been made compatible" , "If you still find you have addons that aren't working please run the addon so it throws up a script error, upload a log and post details on the relevant support forum." )
 if 47 - 47: oOO
 if 92 - 92: oOoO0o00OO0 % i11iIiiIii % Oo0Ooo
def ii11Ii1IiiI1 ( ) :
 oOOoO0 = xbmcgui . Dialog ( )
 O00o0o = xbmcgui . Dialog ( ) . yesno ( 'Convert Addons To Gotham' , 'This will edit your addon.xml files so they show as Gotham compatible. It\'s doubtful this will have any effect on whether or not they work but it will get rid of the annoying incompatible pop-up message. Do you wish to continue?' )
 if 65 - 65: I1ii11iIi11i % ooOo . OoooooooOO * o0oOOo0O0Ooo * OoO0O00
 if O00o0o == 1 :
  O0OOOOOO0ooO ( )
  if 10 - 10: ooOo - OOo00O0 % II111iiii - iIi1i1ii1 - i1IIi
  if 10 - 10: I1ii11iIi11i - oOoO0o00OO0 . iIi1i1ii1
def iiIIIi1iIi ( url ) :
 global iiI111I1iIiI
 if 79 - 79: Oo % iIi1i1ii1 / ooOo - iIii1I11I1II1 - OoOoOO00
 if o0O . getSetting ( 'adult' ) == 'true' :
  IiiI1II1II1i = 'yes'
  if 60 - 60: II111iiii
 else :
  IiiI1II1II1i = 'no'
  if 90 - 90: OoOoOO00
 IIii1i = 'http://noobsandnerds.com/TI/AddonPortal/sortby_new.php?sortx=name&user=%s&adult=%s&%s' % ( oo00 , IiiI1II1II1i , url )
 iiiiI = oooOo0OOOoo0 ( IIii1i ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 if 69 - 69: iIi1i1ii1 / OoooooooOO % i11iIiiIii
 O0OoOoO00O = re . compile ( 'name="(.+?)"  <br> downloads="(.+?)"  <br> icon="(.+?)"  <br> broken="(.+?)"  <br> UID="(.+?)"  <br>' , re . DOTALL ) . findall ( iiiiI )
 if O0OoOoO00O == [ ] :
  if 18 - 18: i11iIiiIii - oOO * ooOo + o0oOOo0O0Ooo
  O0OoOoO00O = re . compile ( 'name="(.+?)" <br> downloads="(.+?)" <br> icon="(.+?)" <br> broken="(.+?)" <br> UID="(.+?)" <br>' , re . DOTALL ) . findall ( iiiiI )
 print O0OoOoO00O
 if 16 - 16: OoooooooOO * i11iIiiIii . OoooooooOO - iIii1I11I1II1 * i1IIi
 if O0OoOoO00O != [ ] :
  i1iI1IIi1I ( IIii1i , 'addons' )
  if 52 - 52: OoooooooOO / iIII % II111iiii
  for I1i11i , Oo0 , Ii , Ii111 , Ii11I1I11II in O0OoOoO00O :
   if 43 - 43: ooOo + OoooooooOO . o0oOOo0O0Ooo . I1ii11iIi11i
   if Ii111 == '0' :
    IIii ( 'folder2' , I1i11i + '[COLOR=lime] [' + Oo0 + ' downloads][/COLOR]' , Ii11I1I11II , 'addon_final_menu' , Ii , '' , '' )
    if 30 - 30: oOO - i11iIiiIii + I1IiiI / Oo0Ooo % O0
   if Ii111 == '1' :
    IIii ( 'folder2' , '[COLOR=red]' + I1i11i + ' [REPORTED AS BROKEN][/COLOR]' , Ii11I1I11II , 'addon_final_menu' , Ii , '' , '' )
    if 66 - 66: iIii1I11I1II1 % i11iIiiIii / I1IiiI
 elif '&redirect' in url :
  ii1I11iIiIII1 = oOOoO0 . yesno ( 'No Content Found' , 'This add-on cannot be found on the Add-on Portal.' , '' , 'Would you like to remove this item from your setup?' )
  if 47 - 47: I1ii11iIi11i * ooOo + iIii1I11I1II1 - ooOo / iIII
  if ii1I11iIiIII1 == 1 : print "remove"
  if 86 - 86: iIII
 else :
  oOOoO0 . ok ( 'No Content Found' , 'Sorry no content can be found that matches' , 'your search criteria.' , '' )
  if 43 - 43: I1IiiI / OOo00O0 / oOO + iIii1I11I1II1 + OoooooooOO
  if 33 - 33: II111iiii - iIII - oOO
def oO00oOoo00o0 ( url ) :
 if zip == '' :
  oOOoO0 . ok ( 'Storage/Download Folder Not Set' , 'You have not set your backup storage folder.\nPlease update the addon settings and try again.' , '' , '' )
  o0O . openSettings ( sys . argv [ 0 ] )
  if 41 - 41: ooOo / Oo + OOo00O0 + oOO
 if o0O . getSetting ( 'adult' ) == 'true' :
  IiiI1II1II1i = ''
  if 13 - 13: i11iIiiIii - i11iIiiIii . iIii1I11I1II1
 else :
  IiiI1II1II1i = 'no'
  if 33 - 33: OoooooooOO + iIi1i1ii1 / iIi1i1ii1 + iIi1i1ii1 * iIII
 if not 'id=' in url :
  IIii1i = 'http://noobsandnerds.com/TI/Community_Builds/sortby.php?sortx=name&orderx=ASC&adult=%s&%s' % ( IiiI1II1II1i , url )
  iiiiI = oooOo0OOOoo0 ( IIii1i ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
  if 26 - 26: iIi1i1ii1 . I1IiiI . OOo00O0 - OoooooooOO / iIii1I11I1II1
  O0OoOoO00O = re . compile ( 'name="(.+?)"  <br> id="(.+?)"  <br> Thumbnail="(.+?)"  <br> Fanart="(.+?)"  <br> downloads="(.+?)"  <br> <br>' , re . DOTALL ) . findall ( iiiiI )
  if O0OoOoO00O == [ ] :
   if 47 - 47: iIII
   O0OoOoO00O = re . compile ( 'name="(.+?)" <br> id="(.+?)" <br> Thumbnail="(.+?)" <br> Fanart="(.+?)" <br> downloads="(.+?)" <br> <br>' , re . DOTALL ) . findall ( iiiiI )
  i1iI1IIi1I ( url , 'communitybuilds' )
  if 76 - 76: OoO0O00 * iIii1I11I1II1 + I1ii11iIi11i - oOO - oOoO0o00OO0 / i1IIi
  for I1i11i , id , iIOoo0ooo0oo , I11iIiI1 , Oo0 in O0OoOoO00O :
   ooO00OO0 ( I1i11i + '[COLOR=lime] (' + Oo0 + ' downloads)[/COLOR]' , id + url , 'community_menu' , iIOoo0ooo0oo , I11iIiI1 , id , '' , '' , '' , '' )
   if 22 - 22: iIII * iI1iiIiiII - OoooooooOO
 if 'id=1' in url : IIii1i = oo0o0O00
 if 'id=2' in url : IIii1i = i1iiIIiiI111
 if 'id=3' in url : IIii1i = i1iiIII111ii
 if 'id=4' in url : IIii1i = ii11iIi1I
 if 'id=5' in url : IIii1i = OOooO0OOoo
 if 28 - 28: I1IiiI
 iiiiI = oooOo0OOOoo0 ( IIii1i ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 O0OoOoO00O = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( iiiiI )
 if 87 - 87: iIII . i1IIi % OoooooooOO * i11iIiiIii
 for I1i11i , url , iii1IIIiiiI , OoO00oo00 , IIIii in O0OoOoO00O :
  if not 'viewport' in I1i11i :
   IIii ( 'addon' , I1i11i , url , 'restore_local_CB' , iii1IIIiiiI , OoO00oo00 , IIIii , '' )
   if 67 - 67: iIi1i1ii1 / OoO0O00 . OoooooooOO
   if 51 - 51: II111iiii . ooOo . OoO0O00 % II111iiii
def III1I1ii ( url ) :
 IIii1i = 'http://noobsandnerds.com/TI/HardwarePortal/sortby.php?sortx=Added&orderx=DESC&%s' % ( url )
 iiiiI = oooOo0OOOoo0 ( IIii1i ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 if 4 - 4: iIii1I11I1II1 . i1IIi
 O0OoOoO00O = re . compile ( 'name="(.+?)"  <br> id="(.+?)"  <br> thumb="(.+?)"  <br><br>' , re . DOTALL ) . findall ( iiiiI )
 if O0OoOoO00O == [ ] :
  if 63 - 63: iIii1I11I1II1 + iIII % i1IIi / I1IiiI % II111iiii
  O0OoOoO00O = re . compile ( 'name="(.+?)" <br> id="(.+?)" <br> thumb="(.+?)" <br><br>' , re . DOTALL ) . findall ( iiiiI )
 i1iI1IIi1I ( IIii1i , 'hardware' )
 if 60 - 60: o0oOOo0O0Ooo . OoOoOO00 % iIi1i1ii1 / I1IiiI / O0
 for I1i11i , id , IiIii11I in O0OoOoO00O :
  IIii ( 'folder2' , I1i11i , id , 'hardware_final_menu' , IiIii11I , '' , '' )
  if 97 - 97: i1IIi + OOo00O0 . oOO - OOo00O0
  if 53 - 53: O0 . I1IiiI
def o0oOOoO000 ( url ) :
 IIii1i = 'http://noobsandnerds.com/TI/LatestNews/sortby.php?sortx=item_date&orderx=DESC&%s' % ( url )
 iiiiI = oooOo0OOOoo0 ( IIii1i ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 if 86 - 86: iIii1I11I1II1 - oOoO0o00OO0 % oOO . Oo * OoOoOO00 . i1IIi
 O0OoOoO00O = re . compile ( 'name="(.+?)"  <br> date="(.+?)"  <br> source="(.+?)"  <br> id="(.+?)"  <br><br>' , re . DOTALL ) . findall ( iiiiI )
 if O0OoOoO00O == [ ] :
  if 75 - 75: oOoO0o00OO0 + oOO / oOO - Oo * OoO0O00 * oOO
  O0OoOoO00O = re . compile ( 'name="(.+?)" <br> date="(.+?)" <br> source="(.+?)" <br> id="(.+?)" <br><br>' , re . DOTALL ) . findall ( iiiiI )
 for I1i11i , o0OO0ooOOO , i1i1I1Ii1IIii , id in O0OoOoO00O :
  if 80 - 80: i11iIiiIii
  if "OpenELEC" in i1i1I1Ii1IIii :
   IIii ( '' , I1i11i + '  (' + o0OO0ooOOO + ')' , id , 'news_menu' , 'OpenELEC.png' , '' , '' )
   if 29 - 29: I1IiiI . Oo + II111iiii . Oo0Ooo
  if "Official" in i1i1I1Ii1IIii :
   IIii ( '' , I1i11i + '  (' + o0OO0ooOOO + ')' , id , 'news_menu' , 'XBMC.png' , '' , '' )
   if 29 - 29: iI1iiIiiII - O0 . oOO / I1ii11iIi11i / i1IIi . OoOoOO00
  if "Raspbmc" in i1i1I1Ii1IIii :
   IIii ( '' , I1i11i + '  (' + o0OO0ooOOO + ')' , id , 'news_menu' , 'Raspbmc.png' , '' , '' )
   if 36 - 36: OoO0O00 - O0 * I1IiiI / I1ii11iIi11i / Oo
  if "XBMC4Xbox" in i1i1I1Ii1IIii :
   IIii ( '' , I1i11i + '  (' + o0OO0ooOOO + ')' , id , 'news_menu' , 'XBMC4Xbox.png' , '' , '' )
   if 33 - 33: OoooooooOO % I1ii11iIi11i . O0 / I1ii11iIi11i
  if "noobsandnerds" in i1i1I1Ii1IIii :
   IIii ( '' , I1i11i + '  (' + o0OO0ooOOO + ')' , id , 'news_menu' , 'noobsandnerds.png' , '' , '' )
   if 63 - 63: iIII + iIii1I11I1II1 + I1IiiI + iIi1i1ii1
   if 72 - 72: OoO0O00 + i11iIiiIii + I1ii11iIi11i
def oOooOoOOo0O ( url ) :
 IIii1i = 'http://noobsandnerds.com/TI/TutorialPortal/sortby.php?sortx=Name&orderx=ASC&%s' % ( url )
 iiiiI = oooOo0OOOoo0 ( IIii1i ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 if 41 - 41: OOo00O0
 O0OoOoO00O = re . compile ( 'name="(.+?)"  <br> about="(.+?)"  <br> id="(.+?)"  <br><br>' , re . DOTALL ) . findall ( iiiiI )
 if O0OoOoO00O == [ ] :
  if 88 - 88: O0 . ooOo % I1IiiI
  O0OoOoO00O = re . compile ( 'name="(.+?)" <br> about="(.+?)" <br> id="(.+?)" <br><br>' , re . DOTALL ) . findall ( iiiiI )
 i1iI1IIi1I ( IIii1i , 'tutorials' )
 if 10 - 10: I1IiiI + O0
 for I1i11i , Oooo0Oo00o , id in O0OoOoO00O :
  IIii ( 'folder' , I1i11i , id , 'tutorial_final_menu' , 'Tutorials.png' , '' , Oooo0Oo00o )
  if 32 - 32: OoOoOO00 . iIii1I11I1II1 % ooOo . O0 . OoOoOO00 / OOo00O0
  if 45 - 45: iIii1I11I1II1
def I1I111IIIi1 ( url , local ) :
 o0OoOOo ( )
 ii1I11iIiIII1 = xbmcgui . Dialog ( ) . yesno ( I1i11i , 'This will over-write your existing guisettings.xml.' , 'Are you sure this is the build you have installed?' , '' , nolabel = 'No, Cancel' , yeslabel = 'Yes, Fix' )
 if 66 - 66: o0oOOo0O0Ooo % OoOoOO00
 if ii1I11iIiIII1 == 1 :
  II1I1iIIiIIii ( url , local )
  if 65 - 65: i11iIiiIii - oOO * oOoO0o00OO0 + oOO / iIII + o0oOOo0O0Ooo
  if 35 - 35: O0 + Oo0Ooo - I1IiiI % iI1iiIiiII % II111iiii
def II1I1iIIiIIii ( url , local ) :
 o0OOOO = False
 OOoo0OOOo0o = 0
 iI1111i1i11Ii = 1
 if 62 - 62: OOo00O0
 if os . path . exists ( O0Oo000ooO00 ) :
  os . remove ( O0Oo000ooO00 )
  if 8 - 8: OOo00O0 - I1IiiI * Oo0Ooo % I1ii11iIi11i * OoooooooOO
 if os . path . exists ( O00o0OO ) :
  os . remove ( O00o0OO )
  if 26 - 26: i1IIi / OOo00O0 . OOo00O0
 if os . path . exists ( IIIII ) :
  os . remove ( IIIII )
  if 20 - 20: Oo - OOo00O0 / Oo0Ooo * OoO0O00
 if not os . path . exists ( oO0 ) :
  os . makedirs ( oO0 )
  if 55 - 55: OoooooooOO
  if 73 - 73: OoOoOO00 - I1ii11iIi11i % Oo0Ooo + I1ii11iIi11i - O0 . OoO0O00
 try :
  shutil . copyfile ( O0O , O0Oo000ooO00 )
  if 38 - 38: O0
 except :
  print "No guisettings found, most likely due to a previously failed attempt at install"
  if 79 - 79: i1IIi . ooOo
 if local != 1 :
  i1i1i11iI11II = os . path . join ( I1IIIii , 'guifix.zip' )
  if 6 - 6: OoOoOO00 . II111iiii * I1IiiI . I1IiiI / iI1iiIiiII
 else :
  i1i1i11iI11II = xbmc . translatePath ( url )
  if 14 - 14: iIi1i1ii1 % iIII - O0 / iIi1i1ii1
  if 91 - 91: i11iIiiIii % iIi1i1ii1 * ooOo - I1ii11iIi11i . iIi1i1ii1
 iIo00oo = str ( os . path . getsize ( i1i1i11iI11II ) )
 O0OoO000O0OO . create ( "Installing Skin Fix" , "Checking " , '' , 'Please Wait' )
 O0OoO000O0OO . update ( 0 , "" , "Extracting Zip Please Wait" )
 oOO00oO00O0OO ( i1i1i11iI11II , oO0 , O0OoO000O0OO )
 if 78 - 78: iIII - oOoO0o00OO0 % O0 - Oo % OoO0O00
 if local != 'library' or local != 'updatelibrary' or local != 'fresh' :
  if 43 - 43: OoO0O00
  try :
   OoOooO = open ( oO0 + 'profiles.xml' , mode = 'r' )
   I1I1i11iiiiI = OoOooO . read ( )
   OoOooO . close ( )
   if 66 - 66: ooOo / OoOoOO00
   if os . path . exists ( oO0 + 'profiles.xml' ) :
    if 13 - 13: II111iiii
    if local == None :
     ii1I11iIiIII1 = xbmcgui . Dialog ( ) . yesno ( "PROFILES DETECTED" , 'This build has profiles included, would you like to overwrite your existing profiles or keep the ones you have?' , '' , '' , nolabel = 'Keep my profiles' , yeslabel = 'Use new profiles' )
     if 55 - 55: Oo0Ooo % i1IIi * oOoO0o00OO0
    if local != None :
     ii1I11iIiIII1 = 1
     if 95 - 95: Oo / II111iiii - o0oOOo0O0Ooo % iIi1i1ii1 . oOoO0o00OO0
    if ii1I11iIiIII1 == 1 :
     iiiiI11ii = open ( IIIII , mode = 'w' )
     time . sleep ( 1 )
     iiiiI11ii . write ( I1I1i11iiiiI )
     time . sleep ( 1 )
     iiiiI11ii . close ( )
     iI1111i1i11Ii = 0
     if 63 - 63: iIii1I11I1II1 / oOO
  except :
   print "no profiles.xml file"
   if 24 - 24: Oo0Ooo / iIii1I11I1II1 % Oo * OoOoOO00 - iIii1I11I1II1
   if 50 - 50: II111iiii
 os . rename ( oO0 + 'guisettings.xml' , O00o0OO )
 if 39 - 39: II111iiii . OoOoOO00 - Oo0Ooo * i1IIi . OoooooooOO
 if local != 'fresh' :
  iIIiI = oOOoO0 . yesno ( "Do You Want To Keep Your Kodi Settings?" , 'Would you like to keep your existing settings or would you rather erase them and install the ones associated with this latest build?' , nolabel = 'Keep my settings' , yeslabel = 'Replace my settings' )
  if 90 - 90: OOo00O0 * iI1iiIiiII - OOo00O0 + OoO0O00 + oOoO0o00OO0 % O0
 if local == 'fresh' :
  iIIiI = 1
  if 11 - 11: Oo % iIi1i1ii1 * OoOoOO00
 if iIIiI == 1 :
  if 58 - 58: OoooooooOO - oOoO0o00OO0 + iIii1I11I1II1 * i11iIiiIii
  if os . path . exists ( O0O ) :
   if 80 - 80: i1IIi . I1IiiI - ooOo + Oo + OOo00O0 % ooOo
   try :
    print "Attempting to remove guisettings"
    os . remove ( O0O )
    o0OOOO = True
    if 13 - 13: II111iiii / OoOoOO00 / OoOoOO00 + oOO
   except :
    print "Problem removing guisettings"
    o0OOOO = False
    if 49 - 49: O0 / II111iiii * I1IiiI - OoooooooOO . II111iiii % iIII
   try :
    print "Attempting to replace guisettings with new"
    os . rename ( O00o0OO , O0O )
    o0OOOO = True
    if 13 - 13: ooOo . iIii1I11I1II1 . Oo . iIII
   except :
    print "Failed to replace guisettings with new"
    o0OOOO = False
    if 58 - 58: oOoO0o00OO0
    if 7 - 7: II111iiii / iIII % oOoO0o00OO0 + I1IiiI - O0
 if iIIiI == 0 :
  II1II1IIII = open ( O0Oo000ooO00 , mode = 'r' )
  OooOo0o0Oo = II1II1IIII . read ( )
  II1II1IIII . close ( )
  if 45 - 45: I1IiiI / OOo00O0 + ooOo + iIII
  iIIII1Iii11 = re . compile ( '<skinsettings>[\s\S]*?<\/skinsettings>' ) . findall ( OooOo0o0Oo )
  II1IIIi1i1I = re . compile ( '<skin default[\s\S]*?<\/skin>' ) . findall ( OooOo0o0Oo )
  o0III11IiI = re . compile ( '<lookandfeel>[\s\S]*?<\/lookandfeel>' ) . findall ( OooOo0o0Oo )
  o0ooo = iIIII1Iii11 [ 0 ] if ( len ( iIIII1Iii11 ) > 0 ) else ''
  o0oo00O = II1IIIi1i1I [ 0 ] if ( len ( II1IIIi1i1I ) > 0 ) else ''
  IIIIII1iI1II = o0III11IiI [ 0 ] if ( len ( o0III11IiI ) > 0 ) else ''
  if 14 - 14: I1IiiI / O0
  if 43 - 43: ooOo - iIII % i11iIiiIii * II111iiii . iIi1i1ii1 - oOoO0o00OO0
  oo00ooooOOo00 = open ( O00o0OO , mode = 'r' )
  ii1iOO00Oooo000 = oo00ooooOOo00 . read ( )
  oo00ooooOOo00 . close ( )
  if 13 - 13: OoO0O00
  O00 = re . compile ( '<skinsettings>[\s\S]*?<\/skinsettings>' ) . findall ( ii1iOO00Oooo000 )
  oO0o00 = re . compile ( '<skin default[\s\S]*?<\/skin>' ) . findall ( ii1iOO00Oooo000 )
  Oo0OOOO0oOoo0 = re . compile ( '<lookandfeel>[\s\S]*?<\/lookandfeel>' ) . findall ( ii1iOO00Oooo000 )
  O0OIIII1i = O00 [ 0 ] if ( len ( O00 ) > 0 ) else ''
  i1I1Iiii = oO0o00 [ 0 ] if ( len ( oO0o00 ) > 0 ) else ''
  I1iIIIiiii = Oo0OOOO0oOoo0 [ 0 ] if ( len ( Oo0OOOO0oOoo0 ) > 0 ) else ''
  II1iIi1IiIii = OooOo0o0Oo . replace ( o0ooo , O0OIIII1i ) . replace ( IIIIII1iI1II , I1iIIIiiii ) . replace ( o0oo00O , i1I1Iiii )
  if 44 - 44: iIi1i1ii1 / iI1iiIiiII * Oo * i1IIi . iI1iiIiiII * i11iIiiIii
  iiiiI11ii = open ( O0Oo000ooO00 , mode = 'w+' )
  iiiiI11ii . write ( str ( II1iIi1IiIii ) )
  iiiiI11ii . close ( )
  if 91 - 91: iI1iiIiiII - OOo00O0 . i1IIi . I1ii11iIi11i * o0oOOo0O0Ooo % OOo00O0
  if 30 - 30: oOoO0o00OO0
  if os . path . exists ( O0O ) :
   if 85 - 85: II111iiii + oOO * oOoO0o00OO0
   try :
    os . remove ( O0O )
    o0OOOO = True
    if 12 - 12: iI1iiIiiII . I1IiiI % o0oOOo0O0Ooo
   except :
    o0OOOO = False
    if 28 - 28: iI1iiIiiII - I1IiiI % OoO0O00 * iIi1i1ii1
  try :
   os . rename ( O0Oo000ooO00 , O0O )
   os . remove ( O00o0OO )
   o0OOOO = True
   if 80 - 80: Oo * iIII
  except :
   o0OOOO = False
   if 4 - 4: iIii1I11I1II1 . iIi1i1ii1 + II111iiii % OoooooooOO
   if 82 - 82: OoooooooOO / oOO * oOoO0o00OO0 * O0 . I1ii11iIi11i
 if o0OOOO == True or local == None :
  if 21 - 21: II111iiii + Oo0Ooo
  try :
   II1II1IIII = open ( OOO00 , mode = 'r' )
   OooOo0o0Oo = II1II1IIII . read ( )
   II1II1IIII . close ( )
   if 59 - 59: Oo + I1IiiI / II111iiii / OoOoOO00
   oOoo00 = re . compile ( 'id="(.+?)"' ) . findall ( OooOo0o0Oo )
   IIiIi = re . compile ( 'name="(.+?)"' ) . findall ( OooOo0o0Oo )
   I1I1IIiiI1 = re . compile ( 'version="(.+?)"' ) . findall ( OooOo0o0Oo )
   oooOOO0o0O0 = oOoo00 [ 0 ] if ( len ( oOoo00 ) > 0 ) else ''
   iiiI1IiI = IIiIi [ 0 ] if ( len ( IIiIi ) > 0 ) else ''
   OOO0o0 = I1I1IIiiI1 [ 0 ] if ( len ( I1I1IIiiI1 ) > 0 ) else ''
   if 2 - 2: O0 % iIi1i1ii1 % I1ii11iIi11i % o0oOOo0O0Ooo - Oo0Ooo
   iiiiI11ii = open ( iiiiiIIii , mode = 'w+' )
   iiiiI11ii . write ( 'id="' + str ( oooOOO0o0O0 ) + '"\nname="' + iiiI1IiI + '"\nversion="' + OOO0o0 + '"\ngui="' + iIo00oo + '"' )
   iiiiI11ii . close ( )
   if 20 - 20: o0oOOo0O0Ooo
   II1II1IIII = open ( OOOO , mode = 'r' )
   OooOo0o0Oo = II1II1IIII . read ( )
   II1II1IIII . close ( )
   if 86 - 86: iIi1i1ii1 % I1IiiI
   Iii1iIIiii1ii = re . compile ( 'version="(.+?)"' ) . findall ( OooOo0o0Oo )
   i1Oo00 = Iii1iIIiii1ii [ 0 ] if ( len ( Iii1iIIiii1ii ) > 0 ) else ''
   II1iIi1IiIii = OooOo0o0Oo . replace ( i1Oo00 , OOO0o0 )
   if 13 - 13: iIii1I11I1II1 - II111iiii % O0 . iI1iiIiiII % OoO0O00
   iiiiI11ii = open ( OOOO , mode = 'w' )
   iiiiI11ii . write ( str ( II1iIi1IiIii ) )
   iiiiI11ii . close ( )
   os . remove ( OOO00 )
   if 2 - 2: OoooooooOO - iI1iiIiiII % ooOo / I1IiiI / o0oOOo0O0Ooo
  except :
   iiiiI11ii = open ( iiiiiIIii , mode = 'w+' )
   iiiiI11ii . write ( 'id="None"\nname="Unknown"\nversion="Unknown"\ngui="' + iIo00oo + '"' )
   iiiiI11ii . close ( )
   if 3 - 3: II111iiii / Oo
   if 48 - 48: oOO . I1ii11iIi11i
 if os . path . exists ( oO0 + 'profiles.xml' ) :
  os . remove ( oO0 + 'profiles.xml' )
  time . sleep ( 1 )
  if 49 - 49: i1IIi - OoOoOO00 . Oo0Ooo + iIii1I11I1II1 - oOO / Oo0Ooo
 if os . path . exists ( oO0 ) :
  os . removedirs ( oO0 )
  if 24 - 24: ooOo - OOo00O0 / oOO
 iIiiII1Ii1ii = xbmc . translatePath ( os . path . join ( ooOoOoo0O , I1IiI , 'notification.txt' ) )
 if 34 - 34: I1IiiI
 if os . path . exists ( iIiiII1Ii1ii ) :
  os . remove ( iIiiII1Ii1ii )
  if 57 - 57: Oo . iI1iiIiiII % o0oOOo0O0Ooo
 if o0OOOO == True :
  I1I11 ( )
  iI1i1iI1iI ( )
  if 18 - 18: oOoO0o00OO0 + Oo0Ooo - OoO0O00 / iIi1i1ii1 / Oo
  if 53 - 53: Oo + o0oOOo0O0Ooo . ooOo / oOoO0o00OO0
def o0000oOooo0oo ( url ) :
 ii1111iII = 'http://noobsandnerds.com/TI/HardwarePortal/hardwaredetails.php?id=%s' % ( url )
 iiiiI = oooOo0OOOoo0 ( ii1111iII ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 O00o0 = re . compile ( 'name="(.+?)"' ) . findall ( iiiiI )
 OoOoO = re . compile ( 'manufacturer="(.+?)"' ) . findall ( iiiiI )
 Iiii1Ii = re . compile ( 'video_guide1="(.+?)"' ) . findall ( iiiiI )
 ooOOo00oo0 = re . compile ( 'video_guide2="(.+?)"' ) . findall ( iiiiI )
 IIIII1Ii = re . compile ( 'video_guide3="(.+?)"' ) . findall ( iiiiI )
 iIiI1 = re . compile ( 'video_guide4="(.+?)"' ) . findall ( iiiiI )
 I1IiII1I1i1I1 = re . compile ( 'video_guide5="(.+?)"' ) . findall ( iiiiI )
 II11iiI = re . compile ( 'video_label1="(.+?)"' ) . findall ( iiiiI )
 iiIi = re . compile ( 'video_label2="(.+?)"' ) . findall ( iiiiI )
 OooooOo = re . compile ( 'video_label3="(.+?)"' ) . findall ( iiiiI )
 IIIiiiIiI = re . compile ( 'video_label4="(.+?)"' ) . findall ( iiiiI )
 OO0OOoooo0o = re . compile ( 'video_label5="(.+?)"' ) . findall ( iiiiI )
 o0o00OoOO = re . compile ( 'shops="(.+?)"' ) . findall ( iiiiI )
 o0ooOO0o = re . compile ( 'description="(.+?)"' ) . findall ( iiiiI )
 Iii1iii1I = re . compile ( 'screenshot1="(.+?)"' ) . findall ( iiiiI )
 oOo000Oo00o = re . compile ( 'screenshot2="(.+?)"' ) . findall ( iiiiI )
 o0o = re . compile ( 'screenshot3="(.+?)"' ) . findall ( iiiiI )
 oOOoOoOO = re . compile ( 'screenshot4="(.+?)"' ) . findall ( iiiiI )
 iII11 = re . compile ( 'screenshot5="(.+?)"' ) . findall ( iiiiI )
 O00OO00OOOoO = re . compile ( 'screenshot6="(.+?)"' ) . findall ( iiiiI )
 IiI11Ii1iI = re . compile ( 'screenshot7="(.+?)"' ) . findall ( iiiiI )
 ooOo0 = re . compile ( 'screenshot8="(.+?)"' ) . findall ( iiiiI )
 oOo0o = re . compile ( 'screenshot9="(.+?)"' ) . findall ( iiiiI )
 O000OOO000o = re . compile ( 'screenshot10="(.+?)"' ) . findall ( iiiiI )
 I11iiIiiI1iIi11 = re . compile ( 'screenshot11="(.+?)"' ) . findall ( iiiiI )
 II1I1I11i1I1 = re . compile ( 'screenshot12="(.+?)"' ) . findall ( iiiiI )
 iiIi1 = re . compile ( 'screenshot13="(.+?)"' ) . findall ( iiiiI )
 oOOO0 = re . compile ( 'screenshot14="(.+?)"' ) . findall ( iiiiI )
 oo0I11iIi1i1I1i1 = re . compile ( 'added="(.+?)"' ) . findall ( iiiiI )
 oOOOoo00 = re . compile ( 'platform="(.+?)"' ) . findall ( iiiiI )
 iiiiii1ii1 = re . compile ( 'chipset="(.+?)"' ) . findall ( iiiiI )
 iIIII1i1 = re . compile ( 'official_guide="(.+?)"' ) . findall ( iiiiI )
 I1I1oO00o0oOoo = re . compile ( 'official_preview="(.+?)"' ) . findall ( iiiiI )
 II1iI111iiIIiI1I = re . compile ( 'thumbnail="(.+?)"' ) . findall ( iiiiI )
 oOOI1 = re . compile ( 'stock_rom="(.+?)"' ) . findall ( iiiiI )
 OO = re . compile ( 'CPU="(.+?)"' ) . findall ( iiiiI )
 I1ii1 = re . compile ( 'GPU="(.+?)"' ) . findall ( iiiiI )
 II1iII1 = re . compile ( 'RAM="(.+?)"' ) . findall ( iiiiI )
 I11II11IiI11 = re . compile ( 'flash="(.+?)"' ) . findall ( iiiiI )
 O00o = re . compile ( 'wifi="(.+?)"' ) . findall ( iiiiI )
 Ii11Iiii1iiii = re . compile ( 'bluetooth="(.+?)"' ) . findall ( iiiiI )
 i1IIII1111 = re . compile ( 'LAN="(.+?)"' ) . findall ( iiiiI )
 Ooo0o0000OO = re . compile ( 'xbmc_version="(.+?)"' ) . findall ( iiiiI )
 iIiI1II1I1 = re . compile ( 'pros="(.+?)"' ) . findall ( iiiiI )
 OooiIiI1i1Ii = re . compile ( 'cons="(.+?)"' ) . findall ( iiiiI )
 Oo0o00o = re . compile ( 'library_scan="(.+?)"' ) . findall ( iiiiI )
 III1I1 = re . compile ( '4k="(.+?)"' ) . findall ( iiiiI )
 iI1IIIIII = re . compile ( '1080="(.+?)"' ) . findall ( iiiiI )
 OO0oO0Oo = re . compile ( '720="(.+?)"' ) . findall ( iiiiI )
 OoooOO0 = re . compile ( '3D="(.+?)"' ) . findall ( iiiiI )
 oo0OoO = re . compile ( 'DTS="(.+?)"' ) . findall ( iiiiI )
 iIIi1iii1 = re . compile ( 'BootTime="(.+?)"' ) . findall ( iiiiI )
 o00o0OOoOo0O0 = re . compile ( 'CopyFiles="(.+?)"' ) . findall ( iiiiI )
 I1 = re . compile ( 'CopyVideo="(.+?)"' ) . findall ( iiiiI )
 o0I1IiiiiI1i1I = re . compile ( 'EthernetTest="(.+?)"' ) . findall ( iiiiI )
 I11i1I1 = re . compile ( 'Slideshow="(.+?)"' ) . findall ( iiiiI )
 ooOooO = re . compile ( 'total_review="(.+?)"' ) . findall ( iiiiI )
 oooo = re . compile ( 'whufclee_review="(.+?)"' ) . findall ( iiiiI )
 IIIiI1iIIII = re . compile ( 'CB_Premium="(.+?)"' ) . findall ( iiiiI )
 if 75 - 75: Oo % II111iiii
 I1i11i = O00o0 [ 0 ] if ( len ( O00o0 ) > 0 ) else ''
 IIIIi1Iii1iIi = OoOoO [ 0 ] if ( len ( OoOoO ) > 0 ) else ''
 oOOoo = Iiii1Ii [ 0 ] if ( len ( Iiii1Ii ) > 0 ) else 'None'
 iII1111III1I = ooOOo00oo0 [ 0 ] if ( len ( ooOOo00oo0 ) > 0 ) else 'None'
 ii11i = IIIII1Ii [ 0 ] if ( len ( IIIII1Ii ) > 0 ) else 'None'
 O00oOo00o0o = iIiI1 [ 0 ] if ( len ( iIiI1 ) > 0 ) else 'None'
 O00oO0 = I1IiII1I1i1I1 [ 0 ] if ( len ( I1IiII1I1i1I1 ) > 0 ) else 'None'
 I1I = II11iiI [ 0 ] if ( len ( II11iiI ) > 0 ) else 'None'
 ooooo = iiIi [ 0 ] if ( len ( iiIi ) > 0 ) else 'None'
 i11IIIiI1I = OooooOo [ 0 ] if ( len ( OooooOo ) > 0 ) else 'None'
 o0iiiI1I1iIIIi1 = IIIiiiIiI [ 0 ] if ( len ( IIIiiiIiI ) > 0 ) else 'None'
 IiiI1iiiiI1iI = OO0OOoooo0o [ 0 ] if ( len ( OO0OOoooo0o ) > 0 ) else 'None'
 ii1IIi1iI1ii1 = o0o00OoOO [ 0 ] if ( len ( o0o00OoOO ) > 0 ) else ''
 IIIii = o0ooOO0o [ 0 ] if ( len ( o0ooOO0o ) > 0 ) else ''
 o00iIIiIi111iI = Iii1iii1I [ 0 ] if ( len ( Iii1iii1I ) > 0 ) else ''
 II1I1ii = oOo000Oo00o [ 0 ] if ( len ( oOo000Oo00o ) > 0 ) else ''
 oo0OO0O = o0o [ 0 ] if ( len ( o0o ) > 0 ) else ''
 OO0OooOOoO00OO00 = oOOoOoOO [ 0 ] if ( len ( oOOoOoOO ) > 0 ) else ''
 ii11ii1iIiI1 = iII11 [ 0 ] if ( len ( iII11 ) > 0 ) else ''
 OoOo0oO0 = O00OO00OOOoO [ 0 ] if ( len ( O00OO00OOOoO ) > 0 ) else ''
 i111iIi1i1 = IiI11Ii1iI [ 0 ] if ( len ( IiI11Ii1iI ) > 0 ) else ''
 OOo00O0O = ooOo0 [ 0 ] if ( len ( ooOo0 ) > 0 ) else ''
 oooOoO = oOo0o [ 0 ] if ( len ( oOo0o ) > 0 ) else ''
 IiiIi1IiiiI = O000OOO000o [ 0 ] if ( len ( O000OOO000o ) > 0 ) else ''
 OO0oooOO = I11iiIiiI1iIi11 [ 0 ] if ( len ( I11iiIiiI1iIi11 ) > 0 ) else ''
 IIIi1iiIIiiiI = II1I1I11i1I1 [ 0 ] if ( len ( II1I1I11i1I1 ) > 0 ) else ''
 I1IIiIi1iI = iiIi1 [ 0 ] if ( len ( iiIi1 ) > 0 ) else ''
 oOo0 = oOOO0 [ 0 ] if ( len ( oOOO0 ) > 0 ) else ''
 Iiii11 = oo0I11iIi1i1I1i1 [ 0 ] if ( len ( oo0I11iIi1i1I1i1 ) > 0 ) else ''
 oO0OoO00o = oOOOoo00 [ 0 ] if ( len ( oOOOoo00 ) > 0 ) else ''
 o00000O = iiiiii1ii1 [ 0 ] if ( len ( iiiiii1ii1 ) > 0 ) else ''
 iIiiiII11 = iIIII1i1 [ 0 ] if ( len ( iIIII1i1 ) > 0 ) else 'None'
 ooo00Oo0 = I1I1oO00o0oOoo [ 0 ] if ( len ( I1I1oO00o0oOoo ) > 0 ) else 'None'
 IiIii11I = II1iI111iiIIiI1I [ 0 ] if ( len ( II1iI111iiIIiI1I ) > 0 ) else ''
 iIii1i1Ii = oOOI1 [ 0 ] if ( len ( oOOI1 ) > 0 ) else ''
 III1iIii = OO [ 0 ] if ( len ( OO ) > 0 ) else ''
 iiIII1i1 = I1ii1 [ 0 ] if ( len ( I1ii1 ) > 0 ) else ''
 oOOo0OOoOO0 = II1iII1 [ 0 ] if ( len ( II1iII1 ) > 0 ) else ''
 IiIiIIi1IiiIi1III = I11II11IiI11 [ 0 ] if ( len ( I11II11IiI11 ) > 0 ) else ''
 IiIiIiiIIii = O00o [ 0 ] if ( len ( O00o ) > 0 ) else ''
 OOo00O00o0O0 = Ii11Iiii1iiii [ 0 ] if ( len ( Ii11Iiii1iiii ) > 0 ) else ''
 iI1III = i1IIII1111 [ 0 ] if ( len ( i1IIII1111 ) > 0 ) else ''
 oOoO00 = Ooo0o0000OO [ 0 ] if ( len ( Ooo0o0000OO ) > 0 ) else ''
 I1I111 = iIiI1II1I1 [ 0 ] if ( len ( iIiI1II1I1 ) > 0 ) else ''
 I1iI = OooiIiI1i1Ii [ 0 ] if ( len ( OooiIiI1i1Ii ) > 0 ) else ''
 IIiiI = Oo0o00o [ 0 ] if ( len ( Oo0o00o ) > 0 ) else ''
 ooO0 = III1I1 [ 0 ] if ( len ( III1I1 ) > 0 ) else ''
 IIOoOOoOo = iI1IIIIII [ 0 ] if ( len ( iI1IIIIII ) > 0 ) else ''
 Ii1 = OO0oO0Oo [ 0 ] if ( len ( OO0oO0Oo ) > 0 ) else ''
 Iiiiii = OoooOO0 [ 0 ] if ( len ( OoooOO0 ) > 0 ) else ''
 IiIii1i11i1 = oo0OoO [ 0 ] if ( len ( oo0OoO ) > 0 ) else ''
 ooOOo00o0ooO = iIIi1iii1 [ 0 ] if ( len ( iIIi1iii1 ) > 0 ) else ''
 iIOO = o00o0OOoOo0O0 [ 0 ] if ( len ( o00o0OOoOo0O0 ) > 0 ) else ''
 I1III1I11I1 = I1 [ 0 ] if ( len ( I1 ) > 0 ) else ''
 oO000OoO00OoO = o0I1IiiiiI1i1I [ 0 ] if ( len ( o0I1IiiiiI1i1I ) > 0 ) else ''
 I1IiIi1iiI = I11i1I1 [ 0 ] if ( len ( I11i1I1 ) > 0 ) else ''
 iiII1II11i = ooOooO [ 0 ] if ( len ( ooOooO ) > 0 ) else ''
 ooO0OoooooOo0oOo0 = oooo [ 0 ] if ( len ( oooo ) > 0 ) else 'None'
 II11II = IIIiI1iIIII [ 0 ] if ( len ( IIIiI1iIIII ) > 0 ) else ''
 i1ii11 = str ( '[COLOR=dodgerblue]Added: [/COLOR]' + Iiii11 + '[CR][COLOR=dodgerblue]Manufacturer: [/COLOR]' + IIIIi1Iii1iIi + '[CR][COLOR=dodgerblue]Supported Roms: [/COLOR]' + oO0OoO00o + '[CR][COLOR=dodgerblue]Chipset: [/COLOR]' + o00000O + '[CR][COLOR=dodgerblue]CPU: [/COLOR]' + III1iIii + '[CR][COLOR=dodgerblue]GPU: [/COLOR]' + iiIII1i1 + '[CR][COLOR=dodgerblue]RAM: [/COLOR]' + oOOo0OOoOO0 + '[CR][COLOR=dodgerblue]Flash: [/COLOR]' + IiIiIIi1IiiIi1III + '[CR][COLOR=dodgerblue]Wi-Fi: [/COLOR]' + IiIiIiiIIii + '[CR][COLOR=dodgerblue]Bluetooth: [/COLOR]' + OOo00O00o0O0 + '[CR][COLOR=dodgerblue]LAN: [/COLOR]' + iI1III + '[CR][CR][COLOR=yellow]About: [/COLOR]' + IIIii + '[CR][CR][COLOR=yellow]Summary:[/COLOR][CR][CR][COLOR=dodgerblue]Pros:[/COLOR]    ' + I1I111 + '[CR][CR][COLOR=dodgerblue]Cons:[/COLOR]  ' + I1iI + '[CR][CR][COLOR=yellow]Benchmark Results:[/COLOR][CR][CR][COLOR=dodgerblue]Boot Time:[/COLOR][CR]' + ooOOo00o0ooO + '[CR][CR][COLOR=dodgerblue]Time taken to scan 1,000 movies (local NFO files):[/COLOR][CR]' + IIiiI + '[CR][CR][COLOR=dodgerblue]Copy 4,000 files (660.8MB) locally:[/COLOR][CR]' + iIOO + '[CR][CR][COLOR=dodgerblue]Copy a MP4 file (339.4MB) locally:[/COLOR][CR]' + I1III1I11I1 + '[CR][CR][COLOR=dodgerblue]Ethernet Speed - Copy MP4 (339.4MB) from SMB share to device:[/COLOR][CR]' + oO000OoO00OoO + '[CR][CR][COLOR=dodgerblue]4k Playback:[/COLOR][CR]' + ooO0 + '[CR][CR][COLOR=dodgerblue]1080p Playback:[/COLOR][CR]' + IIOoOOoOo + '[CR][CR][COLOR=dodgerblue]720p Playback:[/COLOR][CR]' + Ii1 + '[CR][CR][COLOR=dodgerblue]Audio Playback:[/COLOR][CR]' + IiIii1i11i1 + '[CR][CR][COLOR=dodgerblue]Image Slideshow:[/COLOR][CR]' + I1IiIi1iiI )
 IIIo00O = str ( '[COLOR=dodgerblue]Added: [/COLOR]' + Iiii11 + '[CR][COLOR=dodgerblue]Manufacturer: [/COLOR]' + IIIIi1Iii1iIi + '[CR][COLOR=dodgerblue]Supported Roms: [/COLOR]' + oO0OoO00o + '[CR][COLOR=dodgerblue]Chipset: [/COLOR]' + o00000O + '[CR][COLOR=dodgerblue]CPU: [/COLOR]' + III1iIii + '[CR][COLOR=dodgerblue]GPU: [/COLOR]' + iiIII1i1 + '[CR][COLOR=dodgerblue]RAM: [/COLOR]' + oOOo0OOoOO0 + '[CR][COLOR=dodgerblue]Flash: [/COLOR]' + IiIiIIi1IiiIi1III + '[CR][COLOR=dodgerblue]Wi-Fi: [/COLOR]' + IiIiIiiIIii + '[CR][COLOR=dodgerblue]Bluetooth: [/COLOR]' + OOo00O00o0O0 + '[CR][COLOR=dodgerblue]LAN: [/COLOR]' + iI1III + '[CR][CR][COLOR=yellow]About: [/COLOR]' + IIIii + '[CR][CR][COLOR=yellow]Summary:[/COLOR][CR][CR][COLOR=dodgerblue]Pros:[/COLOR]    ' + I1I111 + '[CR][CR][COLOR=dodgerblue]Cons:[/COLOR]  ' + I1iI + '[CR][CR][COLOR=orange]4k Playback:[/COLOR]  ' + ooO0 + '[CR][CR][COLOR=orange]1080p Playback:[/COLOR]  ' + IIOoOOoOo + '[CR][CR][COLOR=orange]720p Playback:[/COLOR]  ' + Ii1 + '[CR][CR][COLOR=orange]DTS Compatibility:[/COLOR]  ' + IiIii1i11i1 + '[CR][CR][COLOR=orange]Time taken to scan 100 movies:[/COLOR]  ' + IIiiI )
 if 26 - 26: OoOoOO00
 if IIIii != '' and ii1IIi1iI1ii1 != '' :
  IIii ( '' , '[COLOR=yellow][Text Guide][/COLOR]  Official Description' , i1ii11 , 'text_guide' , 'Tutorials.png' , O0o0Oo , '' , '' )
 if IIIii != '' and ii1IIi1iI1ii1 == '' :
  IIii ( '' , '[COLOR=yellow][Text Guide][/COLOR]  Official Description' , IIIo00O , 'text_guide' , 'Tutorials.png' , O0o0Oo , '' , '' )
 if ooO0OoooooOo0oOo0 != 'None' :
  IIii ( '' , '[COLOR=lime][VIDEO][/COLOR]   Benchmark Review' , ooO0OoooooOo0oOo0 , 'play_video' , 'Video_Guide.png' , O0o0Oo , '' , '' )
 if ooo00Oo0 != 'None' :
  IIii ( '' , '[COLOR=lime][VIDEO][/COLOR]   Official Video Preview' , ooo00Oo0 , 'play_video' , 'Video_Guide.png' , O0o0Oo , '' , '' )
 if iIiiiII11 != 'None' :
  IIii ( '' , '[COLOR=lime][VIDEO][/COLOR]   Official Video Guide' , iIiiiII11 , 'play_video' , 'Video_Guide.png' , O0o0Oo , '' , '' )
 if oOOoo != 'None' :
  IIii ( '' , '[COLOR=lime][VIDEO][/COLOR]  ' + I1I , oOOoo , 'play_video' , 'Video_Guide.png' , O0o0Oo , '' , '' )
 if iII1111III1I != 'None' :
  IIii ( '' , '[COLOR=lime][VIDEO][/COLOR]  ' + ooooo , iII1111III1I , 'play_video' , 'Video_Guide.png' , O0o0Oo , '' , '' )
 if ii11i != 'None' :
  IIii ( '' , '[COLOR=lime][VIDEO][/COLOR]  ' + i11IIIiI1I , ii11i , 'play_video' , 'Video_Guide.png' , O0o0Oo , '' , '' )
 if O00oOo00o0o != 'None' :
  IIii ( '' , '[COLOR=lime][VIDEO][/COLOR]  ' + o0iiiI1I1iIIIi1 , O00oOo00o0o , 'play_video' , 'Video_Guide.png' , O0o0Oo , '' , '' )
 if O00oO0 != 'None' :
  IIii ( '' , '[COLOR=lime][VIDEO][/COLOR]  ' + IiiI1iiiiI1iI , O00oO0 , 'play_video' , 'Video_Guide.png' , O0o0Oo , '' , '' )
  if 1 - 1: iIII + iIi1i1ii1 + OoO0O00 * I1IiiI * oOO
  if 9 - 9: OoOoOO00 + II111iiii * I1IiiI - iIii1I11I1II1
def Ii1o0OOOoo0000 ( ) :
 IIii ( 'folder' , '[COLOR=yellow]Manual Search[/COLOR]' , 'hardware' , 'manual_search' , 'Manual_Search.png' , '' , '' , '' )
 IIii ( 'folder' , '[COLOR=lime]All Devices[/COLOR]' , '' , 'grab_hardware' , 'All.png' , '' , '' , '' )
 IIii ( 'folder' , '[COLOR=orange][Hardware][/COLOR] Game Consoles' , 'device=Console' , 'grab_hardware' , 'Consoles.png' , '' , '' , '' )
 IIii ( 'folder' , '[COLOR=orange][Hardware][/COLOR] HTPC' , 'device=HTPC' , 'grab_hardware' , 'HTPC.png' , '' , '' , '' )
 IIii ( 'folder' , '[COLOR=orange][Hardware][/COLOR] Phones' , 'device=Phone' , 'grab_hardware' , 'Phones.png' , '' , '' , '' )
 IIii ( 'folder' , '[COLOR=orange][Hardware][/COLOR] Set Top Boxes' , 'device=STB' , 'grab_hardware' , 'STB.png' , '' , '' , '' )
 IIii ( 'folder' , '[COLOR=orange][Hardware][/COLOR] Tablets' , 'device=Tablet' , 'grab_hardware' , 'Tablets.png' , '' , '' , '' )
 IIii ( 'folder' , '[COLOR=dodgerblue][Accessories][/COLOR] Remotes/Keyboards' , 'device=Remote' , 'grab_hardware' , 'Remotes.png' , '' , '' , '' )
 IIii ( 'folder' , '[COLOR=dodgerblue][Accessories][/COLOR] Gaming Controllers' , 'device=Controller' , 'grab_hardware' , 'Controllers.png' , '' , '' , '' )
 IIii ( 'folder' , '[COLOR=dodgerblue][Accessories][/COLOR] Dongles' , 'device=Dongle' , 'grab_hardware' , 'Dongles.png' , '' , '' , '' )
 if 19 - 19: OoooooooOO . I1IiiI + iIi1i1ii1 - I1IiiI / I1IiiI % iIII
 if 4 - 4: i11iIiiIii * I1ii11iIi11i + OoooooooOO - iIII . oOO . iIii1I11I1II1
def IIiIIiI1iIII ( url ) :
 IIii ( 'folder' , '[COLOR=yellow][CPU][/COLOR] Allwinner Devices' , str ( url ) + '&chip=Allwinner' , 'grab_hardware' , 'Allwinner.png' , '' , '' , '' )
 IIii ( 'folder' , '[COLOR=yellow][CPU][/COLOR] AMLogic Devices' , str ( url ) + '&chip=AMLogic' , 'grab_hardware' , 'AMLogic.png' , '' , '' , '' )
 IIii ( 'folder' , '[COLOR=yellow][CPU][/COLOR] Intel Devices' , str ( url ) + '&chip=Intel' , 'grab_hardware' , 'Intel.png' , '' , '' , '' )
 IIii ( 'folder' , '[COLOR=yellow][CPU][/COLOR] Rockchip Devices' , str ( url ) + '&chip=Rockchip' , 'grab_hardware' , 'Rockchip.png' , '' , '' , '' )
 IIii ( 'folder' , '[COLOR=lime][Platform][/COLOR] Android' , str ( url ) + '&platform=Android' , 'grab_hardware' , 'Android.png' , '' , '' , '' )
 IIii ( 'folder' , '[COLOR=lime][Platform][/COLOR] iOS' , str ( url ) + '&platform=iOS' , 'grab_hardware' , 'iOS.png' , '' , '' , '' )
 IIii ( 'folder' , '[COLOR=lime][Platform][/COLOR] Linux' , str ( url ) + '&platform=Linux' , 'grab_hardware' , 'Linux.png' , '' , '' , '' )
 IIii ( 'folder' , '[COLOR=lime][Platform][/COLOR] OpenELEC' , str ( url ) + '&platform=OpenELEC' , 'grab_hardware' , 'OpenELEC.png' , '' , '' , '' )
 IIii ( 'folder' , '[COLOR=lime][Platform][/COLOR] OSX' , str ( url ) + '&platform=OSX' , 'grab_hardware' , 'OSX.png' , '' , '' , '' )
 IIii ( 'folder' , '[COLOR=lime][Platform][/COLOR] Pure Linux' , str ( url ) + '&platform=Custom_Linux' , 'grab_hardware' , 'Custom_Linux.png' , '' , '' , '' )
 IIii ( 'folder' , '[COLOR=lime][Platform][/COLOR] Windows' , str ( url ) + '&platform=Windows' , 'grab_hardware' , 'Windows.png' , '' , '' , '' )
 IIii ( 'folder' , '[COLOR=orange][Flash Storage][/COLOR] 4GB' , str ( url ) + '&flash=4GB' , 'grab_hardware' , 'Flash.png' , '' , '' , '' )
 IIii ( 'folder' , '[COLOR=orange][Flash Storage][/COLOR] 8GB' , str ( url ) + '&flash=8GB' , 'grab_hardware' , 'Flash.png' , '' , '' , '' )
 IIii ( 'folder' , '[COLOR=orange][Flash Storage][/COLOR] 16GB' , str ( url ) + '&flash=16GB' , 'grab_hardware' , 'Flash.png' , '' , '' , '' )
 IIii ( 'folder' , '[COLOR=orange][Flash Storage][/COLOR] 32GB' , str ( url ) + '&flash=32GB' , 'grab_hardware' , 'Flash.png' , '' , '' , '' )
 IIii ( 'folder' , '[COLOR=orange][Flash Storage][/COLOR] 64GB' , str ( url ) + '&flash=64GB' , 'grab_hardware' , 'Flash.png' , '' , '' , '' )
 IIii ( 'folder' , '[COLOR=dodgerblue][RAM][/COLOR] 1GB' , str ( url ) + '&ram=1GB' , 'grab_hardware' , 'RAM.png' , '' , '' , '' )
 IIii ( 'folder' , '[COLOR=dodgerblue][RAM][/COLOR] 2GB' , str ( url ) + '&ram=2GB' , 'grab_hardware' , 'RAM.png' , '' , '' , '' )
 IIii ( 'folder' , '[COLOR=dodgerblue][RAM][/COLOR] 4GB' , str ( url ) + '&ram=4GB' , 'grab_hardware' , 'RAM.png' , '' , '' , '' )
 if 72 - 72: iIII % i1IIi / iIii1I11I1II1
 if 95 - 95: O0 . OoO0O00
 if 89 - 89: i1IIi
def I11II ( ) :
 o0OO00oO = xbmc . getSkinDir ( )
 O0Oo0 = xbmc . translatePath ( os . path . join ( OO0o , o0OO00oO ) )
 if 89 - 89: OoO0O00 . I1ii11iIi11i - i11iIiiIii * Oo0Ooo * i11iIiiIii
 for OOo000o , oO0ooOoO , ooO0000o00O in os . walk ( O0Oo0 ) :
  if 20 - 20: i11iIiiIii . iI1iiIiiII
  for ooO0oo0o0 in ooO0000o00O :
   if 17 - 17: OoOoOO00 - I1IiiI
   if 'DialogKeyboard.xml' in ooO0oo0o0 :
    o0OO00oO = os . path . join ( OOo000o , ooO0oo0o0 )
    IIii1I1i = open ( o0OO00oO ) . read ( )
    IIII1iIIii = IIii1I1i . replace ( '<control type="label" id="310"' , '<control type="edit" id="312"' )
    ooO0oo0o0 = open ( o0OO00oO , mode = 'w' )
    ooO0oo0o0 . write ( IIII1iIIii )
    ooO0oo0o0 . close ( )
    Iiii11I ( o0OO00oO )
    if 63 - 63: OoOoOO00 - ooOo / iIii1I11I1II1 - iI1iiIiiII / iIi1i1ii1
    for oOo0Oo0Oo0 in range ( 48 , 58 ) :
     IIi1ii1 ( oOo0Oo0Oo0 , o0OO00oO )
     if 34 - 34: OOo00O0 / o0oOOo0O0Ooo + Oo - o0oOOo0O0Ooo + Oo0Ooo . ooOo
 oOOoO0 = xbmcgui . Dialog ( )
 oOOoO0 . ok ( "Skin Changes Successful" , 'A BIG thank you to Mikey1234 for this fix. The code used for this function was ported from the Xunity Maintenance add-on' )
 xbmc . executebuiltin ( 'ReloadSkin()' )
 if 97 - 97: i1IIi
def ii1iI1i1 ( ) :
 oOOoO0 = xbmcgui . Dialog ( )
 O00o0o = xbmcgui . Dialog ( ) . yesno ( 'Convert This Skin To Kodi (Helix)?' , 'This will fix the problem with a blank on-screen keyboard showing in skins designed for Gotham (being run on Kodi). This will only affect the currently running skin.' , nolabel = 'No, Cancel' , yeslabel = 'Yes, Fix' )
 if 51 - 51: oOO * OOo00O0 / i1IIi
 if O00o0o == 1 :
  I11II ( )
  if 2 - 2: ooOo + iIII . OOo00O0 - i1IIi + iIi1i1ii1
  if 54 - 54: OoooooooOO . ooOo - OOo00O0
def oO0o00o000Oo0 ( ) :
 if oOOoO0 . yesno ( "Hide Passwords" , "This will hide all your passwords in your" , "add-on settings, are you sure you wish to continue?" ) :
  for OOo000o , oO0ooOoO , ooO0000o00O in os . walk ( OO0o ) :
   for ooO0oo0o0 in ooO0000o00O :
    if ooO0oo0o0 == 'settings.xml' :
     ii1I1iIi = open ( os . path . join ( OOo000o , ooO0oo0o0 ) ) . read ( )
     O0OoOoO00O = re . compile ( '<setting id=(.+?)>' ) . findall ( ii1I1iIi )
     for O0o0OOo0o0o in O0OoOoO00O :
      if 'pass' in O0o0OOo0o0o :
       if not 'option="hidden"' in O0o0OOo0o0o :
        try :
         o0oO00oooo = O0o0OOo0o0o . replace ( '/' , ' option="hidden"/' )
         ooO0oo0o0 = open ( os . path . join ( OOo000o , ooO0oo0o0 ) , mode = 'w' )
         ooO0oo0o0 . write ( str ( ii1I1iIi ) . replace ( O0o0OOo0o0o , o0oO00oooo ) )
         ooO0oo0o0 . close ( )
        except :
         pass
  oOOoO0 . ok ( "Passwords Hidden" , "Your passwords will now show as stars (hidden), if you want to undo this please use the option to unhide passwords." )
  if 63 - 63: II111iiii - oOoO0o00OO0 . OoOoOO00
  if 8 - 8: I1IiiI * oOO / iIII + OoOoOO00 . iIII - Oo
def Oo0O ( url ) :
 ii1111iII = 'http://noobsandnerds.com/TI/Community_Builds/guisettings.php?id=%s' % ( url )
 iiiiI = oooOo0OOOoo0 ( ii1111iII ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 O0oo00oOOO0o = re . compile ( 'guisettings="(.+?)"' ) . findall ( iiiiI )
 iIO0OO0o0O00oO = O0oo00oOOO0o [ 0 ] if ( len ( O0oo00oOOO0o ) > 0 ) else 'None'
 if 60 - 60: Oo * oOO * OoO0O00
 II1I1iIIiIIii ( iIO0OO0o0O00oO , O0ooO )
 if 42 - 42: O0 * OOo00O0 . OoOoOO00 / Oo - iI1iiIiiII . oOoO0o00OO0
 if 57 - 57: o0oOOo0O0Ooo + Oo0Ooo * I1ii11iIi11i - oOO % iIii1I11I1II1 - iI1iiIiiII
def III1I11II11I ( path ) :
 OOI11 = xbmc . translatePath ( os . path . join ( II , 'background_art' , '' ) )
 if 73 - 73: OOo00O0 / oOO + OoO0O00 / OoOoOO00 . II111iiii * iI1iiIiiII
 if os . path . exists ( OOI11 ) :
  OO00oO0OoO0o ( OOI11 )
  if 21 - 21: I1IiiI - I1IiiI + OOo00O0 % I1IiiI * ooOo
 time . sleep ( 1 )
 if 74 - 74: OOo00O0 / oOoO0o00OO0 . I1IiiI - OoooooooOO + II111iiii + oOoO0o00OO0
 if not os . path . exists ( OOI11 ) :
  os . makedirs ( OOI11 )
  if 36 - 36: iI1iiIiiII * I1IiiI * I1ii11iIi11i . oOoO0o00OO0 * I1ii11iIi11i
 try :
  O0OoO000O0OO . create ( "Installing Artwork" , "Downloading artwork pack" , '' , 'Please Wait' )
  o0O0ooooooo00 = os . path . join ( I1IIIii , IIIi1I1IIii1II + '_artpack.zip' )
  downloader . download ( path , o0O0ooooooo00 , O0OoO000O0OO )
  time . sleep ( 1 )
  O0OoO000O0OO . create ( "[COLOR=blue][B]T[/COLOR][COLOR=dodgerblue]R[/COLOR] [COLOR=white]Community Builds[/COLOR][/B]" , "Checking " , '' , 'Please Wait' )
  O0OoO000O0OO . update ( 0 , "" , "Extracting Zip Please Wait" )
  oOO00oO00O0OO ( o0O0ooooooo00 , OOI11 , O0OoO000O0OO )
  if 76 - 76: Oo + O0 / iIII - OoO0O00
 except :
  pass
  if 27 - 27: Oo0Ooo - iIii1I11I1II1 * OOo00O0 * II111iiii * I1ii11iIi11i
  if 9 - 9: i11iIiiIii + Oo - OoOoOO00 / oOO % i1IIi / ooOo
def iiI1 ( url ) :
 IIii ( '' , '[COLOR=orange]noobs[/COLOR][COLOR=dodgerblue]and[/COLOR][COLOR=orange]nerds[/COLOR] Keyword Install' , OOO00O , 'keywords' , 'Keywords.png' , '' , '' , '' )
 if i1 == 'true' :
  IIii ( 'folder' , 'Manage Add-ons' , iiI111I1iIiI , 'addonmenu' , 'Search_Addons.png' , '' , '' , '' )
  if 42 - 42: OoO0O00 - I1ii11iIi11i * iIII - oOO
 if oOOoo00O0O == 'true' :
  IIii ( 'folder' , 'Community Builds' , url , 'CB_Menu' , 'Community_Builds.png' , '' , '' , '' )
  if 75 - 75: OOo00O0 * Oo0Ooo / iIi1i1ii1 * Oo0Ooo / oOO
  if 14 - 14: i1IIi * iIii1I11I1II1 - iI1iiIiiII * OoOoOO00 - OOo00O0 / ooOo
def OO0OOoOOO ( ) :
 xbmc . executebuiltin ( 'ActivateWindow(10040,"addons://install/",return)' )
 if 96 - 96: I1ii11iIi11i - O0
 if 35 - 35: Oo . oOoO0o00OO0 . iIi1i1ii1 - oOoO0o00OO0 % oOoO0o00OO0 + iIi1i1ii1
def Iii111Ii ( repo_id ) :
 ooOO00oOOo000 = 1
 ii1111iII = 'http://noobsandnerds.com/TI/AddonPortal/dependencyinstall.php?id=%s' % ( repo_id )
 iiiiI = oooOo0OOOoo0 ( ii1111iII ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 O00o0 = re . compile ( 'name="(.+?)"' ) . findall ( iiiiI )
 o000O0O = re . compile ( 'version="(.+?)"' ) . findall ( iiiiI )
 o0000oO = re . compile ( 'repo_url="(.+?)"' ) . findall ( iiiiI )
 I1II1 = re . compile ( 'data_url="(.+?)"' ) . findall ( iiiiI )
 oooO = re . compile ( 'zip_url="(.+?)"' ) . findall ( iiiiI )
 i1i1iI1iiiI = re . compile ( 'repo_id="(.+?)"' ) . findall ( iiiiI )
 oO0oO00 = O00o0 [ 0 ] if ( len ( O00o0 ) > 0 ) else ''
 iIIiIiI1I1 = o000O0O [ 0 ] if ( len ( o000O0O ) > 0 ) else ''
 IIiii11ii1II1 = o0000oO [ 0 ] if ( len ( o0000oO ) > 0 ) else ''
 o0OO000O = I1II1 [ 0 ] if ( len ( I1II1 ) > 0 ) else ''
 O000o0000O = oooO [ 0 ] if ( len ( oooO ) > 0 ) else ''
 O00Ooo0O0OOOo = i1i1iI1iiiI [ 0 ] if ( len ( i1i1iI1iiiI ) > 0 ) else ''
 IiiI1Ii1II = xbmc . translatePath ( os . path . join ( ooOooo000oOO , O00Ooo0O0OOOo + '.zip' ) )
 OO0oIii1I1I = xbmc . translatePath ( os . path . join ( OO0o , O00Ooo0O0OOOo ) )
 if 41 - 41: I1IiiI . Oo0Ooo . iIII % OoooooooOO + OoO0O00
 O0OoO000O0OO . create ( 'Installing Repository' , 'Please wait...' , '' )
 if 23 - 23: I1IiiI - o0oOOo0O0Ooo % ooOo . O0 * OoooooooOO + oOO
 try :
  downloader . download ( IIiii11ii1II1 , IiiI1Ii1II , O0OoO000O0OO )
  oOO00oO00O0OO ( IiiI1Ii1II , OO0o , O0OoO000O0OO )
  xbmc . executebuiltin ( 'UpdateLocalAddons' )
  xbmc . executebuiltin ( 'UpdateAddonRepos' )
  if 53 - 53: Oo0Ooo
 except :
  if 3 - 3: iIII - OoooooooOO * OoooooooOO - I1IiiI / iIi1i1ii1 * I1ii11iIi11i
  try :
   downloader . download ( O000o0000O , IiiI1Ii1II , O0OoO000O0OO )
   oOO00oO00O0OO ( IiiI1Ii1II , OO0o , O0OoO000O0OO )
   xbmc . executebuiltin ( 'UpdateLocalAddons' )
   xbmc . executebuiltin ( 'UpdateAddonRepos' )
   if 58 - 58: iIII % iIii1I11I1II1 / i11iIiiIii % o0oOOo0O0Ooo . iIi1i1ii1 * OOo00O0
  except :
   if 32 - 32: OoooooooOO + o0oOOo0O0Ooo
   try :
    if 91 - 91: oOO - iIi1i1ii1 * iIi1i1ii1
    if not os . path . exists ( OO0oIii1I1I ) :
     os . makedirs ( OO0oIii1I1I )
     if 55 - 55: iIii1I11I1II1 + I1IiiI - Oo0Ooo
    iiiiI = oooOo0OOOoo0 ( o0OO000O ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
    O0OoOoO00O = re . compile ( 'href="(.+?)"' , re . DOTALL ) . findall ( iiiiI )
    if 24 - 24: OoO0O00 / iIi1i1ii1 + OOo00O0 * oOoO0o00OO0 * OOo00O0
    for Ii11Iii1i1ii in O0OoOoO00O :
     Ii1i1i1111 = xbmc . translatePath ( os . path . join ( OO0oIii1I1I , Ii11Iii1i1ii ) )
     if 10 - 10: I1IiiI - I1ii11iIi11i - Oo0Ooo - o0oOOo0O0Ooo
     if OOOOO0O00 not in Ii11Iii1i1ii and '/' not in Ii11Iii1i1ii :
      if 21 - 21: OoooooooOO + iIi1i1ii1
      try :
       O0OoO000O0OO . update ( 0 , "Downloading [COLOR=yellow]" + Ii11Iii1i1ii + '[/COLOR]' , '' , 'Please wait...' )
       downloader . download ( o0OO000O + Ii11Iii1i1ii , Ii1i1i1111 , O0OoO000O0OO )
       if 43 - 43: i11iIiiIii . I1ii11iIi11i . ooOo
      except : print "failed to install" + Ii11Iii1i1ii
      if 31 - 31: iI1iiIiiII % o0oOOo0O0Ooo % iIi1i1ii1 . I1ii11iIi11i / o0oOOo0O0Ooo * ooOo
     if '/' in Ii11Iii1i1ii and '..' not in Ii11Iii1i1ii and 'http' not in Ii11Iii1i1ii :
      ooo0oooo0 = o0OO000O + Ii11Iii1i1ii
      OOO0ooo ( Ii1i1i1111 , ooo0oooo0 )
      if 74 - 74: I1IiiI . oOO / OOo00O0 . iIII
   except :
    oOOoO0 . ok ( "Error downloading repository" , 'There was an error downloading[CR][COLOR=dodgerblue]' + oO0oO00 + '[/COLOR]. Please consider updating the add-on portal with details or report the error on the forum at [COLOR=orange]www.noobs[/COLOR][COLOR=dodgerblue]and[/COLOR][COLOR=orange]nerds.com[/COLOR]' )
    ooOO00oOOo000 = 0
    if 74 - 74: Oo0Ooo / iIi1i1ii1 % iIi1i1ii1 . iIII
    if 72 - 72: i1IIi
 if ooOO00oOOo000 == 1 :
  time . sleep ( 1 )
  O0OoO000O0OO . update ( 0 , "[COLOR=yellow]" + oO0oO00 + '[/COLOR]  [COLOR=lime]Successfully Installed[/COLOR]' , '' , 'Now installing dependencies' )
  time . sleep ( 1 )
  O0O0o0o0o = 'http://noobsandnerds.com/TI/AddonPortal/downloadcount.php?id=%s' % ( repo_id )
  oooOo0OOOoo0 ( O0O0o0o0o )
  if 21 - 21: iIi1i1ii1 . Oo / i11iIiiIii * i1IIi
  if 82 - 82: oOO * Oo0Ooo % i11iIiiIii * i1IIi . Oo
def o0Oo00o0 ( ) :
 IIii ( '' , '[COLOR=dodgerblue][TEXT GUIDE][/COLOR]  What is Community Builds?' , 'url' , 'instructions_3' , 'How_To.png' , '' , '' , '' )
 IIii ( '' , '[COLOR=dodgerblue][TEXT GUIDE][/COLOR]  Creating a Community Build' , 'url' , 'instructions_1' , 'How_To.png' , '' , '' , '' )
 IIii ( '' , '[COLOR=dodgerblue][TEXT GUIDE][/COLOR]  Installing a Community Build' , 'url' , 'instructions_2' , 'How_To.png' , '' , '' , '' )
 IIii ( '' , '[COLOR=lime][VIDEO GUIDE][/COLOR]  Add Your Own Guides @ [COLOR=orange]www.noobs[/COLOR][COLOR=dodgerblue]and[/COLOR][COLOR=orange]nerds.com[/COLOR]' , 'K0XIxEodUhc' , 'play_video' , 'How_To.png' , '' , '' , '' )
 IIii ( '' , '[COLOR=lime][VIDEO GUIDE][/COLOR]  Community Builds FULL GUIDE' , "ewuxVfKZ3Fs" , 'play_video' , 'howto.png' , '' , '' , '' )
 IIii ( '' , '[COLOR=lime][VIDEO GUIDE][/COLOR]  IMPORTANT initial settings' , "1vXniHsEMEg" , 'play_video' , 'howto.png' , '' , '' , '' )
 IIii ( '' , '[COLOR=lime][VIDEO GUIDE][/COLOR]  Install a Community Build' , "kLsVOapuM1A" , 'play_video' , 'howto.png' , '' , '' , '' )
 IIii ( '' , '[COLOR=lime][VIDEO GUIDE][/COLOR]  Fixing a half installed build (guisettings.xml fix)' , "X8QYLziFzQU" , 'play_video' , 'howto.png' , '' , '' , '' )
 IIii ( '' , '[COLOR=lime][VIDEO GUIDE][/COLOR]  [COLOR=yellow](OLD METHOD)[/COLOR]Create a Community Build (part 1)' , "3rMScZF2h_U" , 'play_video' , 'howto.png' , '' , '' , '' )
 IIii ( '' , '[COLOR=lime][VIDEO GUIDE][/COLOR]  [COLOR=yellow](OLD METHOD)[/COLOR]Create a Community Build (part 2)' , "C2IPhn0OSSw" , 'play_video' , 'howto.png' , '' , '' , '' )
 if 42 - 42: iIi1i1ii1 / OoOoOO00 % ooOo
 if 63 - 63: OoO0O00 % i1IIi - ooOo
def Iii1i11 ( ) :
 IIIiI1i1 ( 'Creating A Community Backup' ,
 '[COLOR=yellow]NEW METHOD[/COLOR][CR][COLOR=blue][B]Step 1:[/COLOR] Remove any sensitive data[/B][CR]Make sure you\'ve removed any sensitive data such as passwords and usernames in your addon_data folder.'
 '[CR][CR][COLOR=blue][B]Step 2:[/COLOR] Backup your system[/B][CR]Choose the backup option from the main menu, in there you\'ll find the option to create a Full Backup and this will create two zip files that you need to upload to a server.'
 '[CR][CR][COLOR=blue][B]Step 3:[/COLOR] Upload the zips[/B][CR]Upload the two zip files to a server that Kodi can access, it has to be a direct link and not somewhere that asks for captcha - Dropbox and archive.org are two good examples.'
 '[CR][CR][COLOR=blue][B]Step 4:[/COLOR] Submit build at [COLOR=orange]www.noobs[/COLOR][COLOR=dodgerblue]and[/COLOR][COLOR=orange]nerds.com[/COLOR][/B]'
 '[CR]Create a thread on the Community Builds section of the forum at [COLOR=orange]www.noobs[/COLOR][COLOR=dodgerblue]and[/COLOR][COLOR=orange]nerds.com[/COLOR].[CR]Full details can be found on there of the template you should use when posting, once you\'ve created your support thread (NOT BEFORE) you can request to become a member of the Community Builder group and you\'ll then have access to the web form for adding your builds to the portal.'
 '[CR][CR][COLOR=yellow]OLD METHOD[/COLOR][CR][COLOR=blue][B]Step 1: Backup your system[/B][/COLOR][CR]Choose the backup option from the main menu, you will be asked whether you would like to delete your addon_data folder. If you decide to choose this option [COLOR=yellow][B]make sure[/COLOR][/B] you already have a full backup of your system as it will completely wipe your addon settings (any stored settings such as passwords or any other changes you\'ve made to addons since they were first installed). If sharing a build with the community it\'s highly advised that you wipe your addon_data but if you\'ve made changes or installed extra data packages (e.g. skin artwork packs) then backup the whole build and then manually delete these on your PC and zip back up again (more on this later).'
 '[CR][CR][COLOR=blue][B]Step 2: Edit zip file on your PC[/B][/COLOR][CR]Copy your backup.zip file to your PC, extract it and delete all the addons and addon_data that isn\'t required.'
 '[CR][COLOR=blue]What to delete:[/COLOR][CR][COLOR=lime]/addons/packages[/COLOR] This folder contains zip files of EVERY addon you\'ve ever installed - it\'s not needed.'
 '[CR][COLOR=lime]/addons/<skin.xxx>[/COLOR] Delete any skins that aren\'t used, these can be very big files.'
 '[CR][COLOR=lime]/addons/<addon_id>[/COLOR] Delete any other addons that aren\'t used, it\'s easy to forget you\'ve got things installed that are no longer needed.'
 '[CR][COLOR=lime]/userdata/addon_data/<addon_id>[/COLOR] Delete any folders that don\'t contain important changes to addons. If you delete these the associated addons will just reset to their default values.'
 '[CR][COLOR=lime]/userdata/<all other folders>[/COLOR] Delete all other folders in here such as keymaps. If you\'ve setup profiles make sure you [COLOR=yellow][B]keep the profiles directory[/COLOR][/B].'
 '[CR][COLOR=lime]/userdata/Thumbnails/[/COLOR] Delete this folder, it contains all cached artwork. You can safely delete this but must also delete the file listed below.'
 '[CR][COLOR=lime]/userdata/Database/Textures13.db[/COLOR] Delete this and it will tell XBMC to regenerate your thumbnails - must do this if delting thumbnails folder.'
 '[CR][COLOR=lime]/xbmc.log (or Kodi.log)[/COLOR] Delete your log files, this includes any crashlog files you may have.'
 '[CR][CR][COLOR=blue][B]Step 3: Compress and upload[/B][/COLOR][CR]Use a program like 7zip to create a zip file of your remaining folders and upload to a file sharing site like dropbox.'
 '[CR][CR][COLOR=blue][B]Step 4: Submit build at [COLOR=orange]www.noobs[/COLOR][COLOR=dodgerblue]and[/COLOR][COLOR=orange]nerds.com[/COLOR][/B][/COLOR]'
 '[CR]Create a thread on the Community Builds section of the forum at [COLOR=orange]www.noobs[/COLOR][COLOR=dodgerblue]and[/COLOR][COLOR=orange]nerds.com[/COLOR][/B].[CR]Full details can be found on there of the template you should use when posting.' )
 if 40 - 40: I1ii11iIi11i / iIii1I11I1II1 . iIII % oOO
 if 56 - 56: oOO . iIii1I11I1II1 + i1IIi
def o0oOOoOo00o ( ) :
 IIIiI1i1 ( 'Installing a build' , '[COLOR=blue][B]Step 1 (Optional): Backup your system[/B][/COLOR][CR]When selecting an install option you\'ll be asked if you want to create a backup - we strongly recommend creating a backup of your system in case you don\'t like the build and want to revert back. Remember your backup may be quite large so if you\'re using a device with a very small amount of storage we recommend using a USB stick or SD card as the storage location otherwise you may run out of space and the install may fail.'
 '[CR][CR][COLOR=blue][B]Step 2: Choose an install method:[/B][/COLOR][CR][CR]-------------------------------------------------------[CR][CR][COLOR=lime]1. Fresh Install:[/COLOR] This will wipe all existing settings[CR]As the title suggests this will completely wipe all your current Kodi settings. Your settings will be replaced with the ones uploaded by the build author, some builders like to use this method (especially if they have the Live TV PVR setup) so always check the description to find out if they recommend using this method. This method is also great if you feel there\'s content installed on your Kodi install that may be causing issues, it will fully wipe your Kodi and install the build over the top.'
 '[CR][CR]-------------------------------------------------------[CR][CR][COLOR=lime]2. Install:[/COLOR] Keep my library & profiles[CR]This will install a build over the top of your existing setup so you won\'t lose anything already installed in Kodi. Your library and any profiles you may have setup will also remain unchanged.'
 '[CR][CR]-------------------------------------------------------[CR][CR][COLOR=lime]3. Install:[/COLOR] Keep my library only[CR]This will do exactly the same as number 2 (above) but it will delete any profiles you may have and replace them with the ones the build author has created.'
 '[CR][CR]-------------------------------------------------------[CR][CR][COLOR=lime]4. Install:[/COLOR] Keep my profiles only[CR]Again, the same as number 2 but your library will be replaced with the one created by the build author. If you\'ve spent a long time setting up your library and have it just how you want it then use this with caution and make sure you do a backup!'
 '[CR][CR]-------------------------------------------------------[CR][CR][COLOR=blue][B]Step 3: Replace or keep settings?[/COLOR][/B][CR]When completing the install process (only on options 2-4) you\'ll be asked if you want to keep your existing Kodi settings or replace with the ones in the build. If you choose to keep your settings then only the important skin related settings are copied over from the build. All your other Kodi settings such as screen calibration, region, audio output, resolution etc. will remain intact. Choosing to replace your settings could possibly cause a few issues, unless the build author has specifically recommended you replace the settings with theirs we would always recommend keeping your own.'
 '[CR][CR][COLOR=blue][B]Step 4: [/COLOR][COLOR=red]VERY IMPORTANT[/COLOR][/B][CR]For the install to complete properly Kodi MUST force close, this means forcing it to close via your operating system rather than elegantly via the Kodi menu. By default this add-on will attempt to make your operating system force close Kodi but there are systems that will not allow this (devices that do not allow Kodi to have root permissions).'
 ' Once the final step of the install process has been completed you\'ll see a dialog explaining Kodi is attempting a force close, please be patient and give it a minute. If after a minute Kodi hasn\'t closed or restarted you will need to manually force close. The recommended solution for force closing is to go into your operating system menu and make it force close the Kodi app but if you dont\'t know how to do that you can just pull the power from the unit.'
 ' Pulling the power is fairly safe these days, on most set top boxes it\'s the only way to switch them off - they rarely have a power switch. Even though it\'s considered fairly safe nowadays you do this at your own risk and we would always recommend force closing via the operating system menu.' )
 if 22 - 22: iIi1i1ii1 - I1IiiI
 if 96 - 96: i1IIi + Oo0Ooo - II111iiii . OoooooooOO . Oo / OoO0O00
def oOOo ( ) :
 IIIiI1i1 ( 'What is a community build' , 'Community Builds are pre-configured builds of XBMC/Kodi based on different users setups. Have you ever watched youtube videos or seen screenshots of Kodi in action and thought "wow I wish I could do that"? Well now you can have a brilliant setup at the click of a button, completely pre-configured by users on the [COLOR=orange]www.noobs[/COLOR][COLOR=dodgerblue]and[/COLOR][COLOR=orange]nerds.com[/COLOR][/B] forum. If you\'d like to get involved yourself and share your build with the community it\'s very simple to do, just go to the forum where you\'ll find full details or you can follow the guide in this addon.' )
 if 97 - 97: Oo
 if 41 - 41: OoooooooOO - Oo0Ooo * iIii1I11I1II1 . i1IIi
def I1iiIIiI11I ( url = 'http://www.iplocation.net/' , inc = 1 ) :
 O0OoOoO00O = re . compile ( "<td width='80'>(.+?)</td><td>(.+?)</td><td>(.+?)</td><td>.+?</td><td>(.+?)</td>" ) . findall ( o00OO00OoO . http_GET ( url ) . content )
 for I11II1I , oOoOo000 , iiI1IiI1I1I , IIIiI1i in O0OoOoO00O :
  if inc < 2 : oOOoO0 = xbmcgui . Dialog ( ) ; oOOoO0 . ok ( 'Check My IP' , "[B][COLOR gold]Your IP Address is: [/COLOR][/B] %s" % I11II1I , '[B][COLOR gold]Your IP is based in: [/COLOR][/B] %s' % iiI1IiI1I1I , '[B][COLOR gold]Your Service Provider is:[/COLOR][/B] %s' % IIIiI1i )
  inc = inc + 1
  if 22 - 22: iIII / Oo
  if 62 - 62: iI1iiIiiII - ooOo + iIii1I11I1II1 / Oo . OOo00O0 / iI1iiIiiII
def oOoO ( url ) :
 if not os . path . exists ( ooOooo000oOO ) :
  os . makedirs ( ooOooo000oOO )
  if 52 - 52: Oo + Oo0Ooo
 oOoO0oOO0o = ''
 iIIi11i1i1i1I = 'Enter Keyword'
 oO0000oo0o0o0 = i1I1 ( iIIi11i1i1i1I )
 oOoO0oOO0o = url + oO0000oo0o0o0
 i1i1i11iI11II = os . path . join ( ooOooo000oOO , oO0000oo0o0o0 + '.zip' )
 if 59 - 59: oOoO0o00OO0 + iIii1I11I1II1 / iIi1i1ii1 - OoO0O00 . o0oOOo0O0Ooo
 if oO0000oo0o0o0 != '' :
  oO0000Oo = oOOoO0 . yesno ( 'Backup existing setup' , 'Installing certain keywords can result in some existing settings or add-ons to be replaced. Would you like to create a backup before proceeding?' )
  if 45 - 45: Oo0Ooo . OoooooooOO + Oo . iIi1i1ii1 % I1ii11iIi11i
  if oO0000Oo == 1 :
   I1I111iiiIi11 ( )
   if 67 - 67: oOoO0o00OO0 / O0 * iI1iiIiiII - iIII . OoooooooOO + iIII
  try :
   print "Attempting download " + oOoO0oOO0o + " to " + i1i1i11iI11II
   O0OoO000O0OO . create ( "Web Installer" , "Downloading " , '' , 'Please Wait' )
   downloader . download ( oOoO0oOO0o , i1i1i11iI11II )
   print "### Keyword " + oO0000oo0o0o0 + " Successfully downloaded"
   O0OoO000O0OO . update ( 0 , "" , "Extracting Zip Please Wait" )
   if 20 - 20: iIi1i1ii1 - OoOoOO00
   if zipfile . is_zipfile ( i1i1i11iI11II ) :
    if 91 - 91: i1IIi
    try :
     oOO00oO00O0OO ( i1i1i11iI11II , iiI1IiI , O0OoO000O0OO )
     xbmc . executebuiltin ( 'UpdateLocalAddons' )
     xbmc . executebuiltin ( 'UpdateAddonRepos' )
     oOOoO0 . ok ( "[COLOR=orange]noobs[/COLOR][COLOR=dodgerblue]and[/COLOR][COLOR=orange]nerds[/COLOR]" , "" , "Content now installed" , "" )
     O0OoO000O0OO . close ( )
     if 31 - 31: i11iIiiIii + iI1iiIiiII % OoOoOO00
    except :
     oOOoO0 . ok ( "Error with zip" , 'There was an error trying to install this file. It may possibly be corrupt, either try again or contact the author of this keyword.' )
     print "### Unable to install keyword (passed zip check): " + oO0000oo0o0o0
   else :
    oOOoO0 . ok ( "Keyword Error" , 'The keyword you typed could not be installed. Please check the spelling and if you continue to receive this message it probably means that keyword is no longer available.' )
    if 9 - 9: oOO . oOoO0o00OO0 - Oo0Ooo . iIi1i1ii1
  except :
   oOOoO0 . ok ( "Keyword Error" , 'The keyword you typed could not be installed. Please check the spelling and if you continue to receive this message it probably means that keyword is no longer available.' )
   print "### Unable to install keyword (unknown error, most likely a typo in keyword entry): " + oO0000oo0o0o0
   if 39 - 39: Oo
 if os . path . exists ( i1i1i11iI11II ) :
  os . remove ( i1i1i11iI11II )
  if 70 - 70: iIII % OoO0O00 % I1IiiI
  if 95 - 95: OoOoOO00 - iIi1i1ii1 / O0 * I1IiiI - o0oOOo0O0Ooo
def iI1i1iI1iI ( ) :
 if 12 - 12: iIii1I11I1II1 % Oo0Ooo . OOo00O0 . iIII % i11iIiiIii
 if xbmc . getCondVisibility ( 'system.platform.windows' ) :
  print "############   try windows force close  #################"
  try :
   os . system ( '@ECHO off' )
   os . system ( 'TASKKILL /im Kodi.exe /f' )
  except : pass
  try :
   os . system ( '@ECHO off' )
   os . system ( 'tskill Kodi.exe' )
  except : pass
  try :
   os . system ( '@ECHO off' )
   os . system ( 'tskill XBMC.exe' )
  except : pass
  try :
   os . system ( '@ECHO off' )
   os . system ( 'TASKKILL /im XBMC.exe /f' )
  except : pass
 elif xbmc . getCondVisibility ( 'system.platform.osx' ) :
  print "############   try osx force close  #################"
  try : os . system ( 'killall -9 XBMC' )
  except : pass
  try : os . system ( 'killall -9 Kodi' )
  except : pass
 else :
  if 2 - 2: ooOo * ooOo . OoOoOO00 * iI1iiIiiII * iIii1I11I1II1
  print "############   try linux force close  #################"
  try : os . system ( 'killall XBMC' )
  except : pass
  try : os . system ( 'killall Kodi' )
  except : pass
  try : os . system ( 'killall -9 xbmc.bin' )
  except : pass
  try : os . system ( 'killall -9 kodi.bin' )
  except : pass
  if 13 - 13: oOoO0o00OO0 / O0 . i11iIiiIii * i1IIi % i11iIiiIii
  print "############   try atv force close  #################"
  try : os . system ( 'killall AppleTV' )
  except : pass
  print "############   try raspbmc force close  #################"
  try : os . system ( 'sudo initctl stop kodi' )
  except : pass
  try : os . system ( 'sudo initctl stop xbmc' )
  except : pass
  if 8 - 8: OoOoOO00 - OoooooooOO
  print "############   try android force close  #################"
  try : os . system ( 'adb shell am force-stop org.xbmc.kodi' )
  except : pass
  try : os . system ( 'adb shell am force-stop org.kodi' )
  except : pass
  try : os . system ( 'adb shell am force-stop org.xbmc.xbmc' )
  except : pass
  try : os . system ( 'adb shell am force-stop org.xbmc' )
  except : pass
  try : os . system ( 'adb shell kill org.xbmc.kodi' )
  except : pass
  try : os . system ( 'adb shell kill org.kodi' )
  except : pass
  try : os . system ( 'adb shell kill org.xbmc.xbmc' )
  except : pass
  try : os . system ( 'adb shell kill org.xbmc' )
  except : pass
  try : os . system ( 'Process.killProcess(android.os.Process.org.xbmc,kodi());' )
  except : pass
  try : os . system ( 'Process.killProcess(android.os.Process.org.kodi());' )
  except : pass
  try : os . system ( 'Process.killProcess(android.os.Process.org.xbmc.xbmc());' )
  except : pass
  try : os . system ( 'Process.killProcess(android.os.Process.org.xbmc());' )
  except : pass
  oOOoO0 . ok ( 'Force Close Required' , 'On the following screen, please click the big button at the top which says "KILL selected apps". If this is your first time running the wizard, a menu will pop-up first. Click "OK" then "Kill selected apps". After Kodi restarts, you will begin to see update notifications on your screen. Please allow all files to download and update before Cubing. ~5 mins.' )
  try : xbmc . executebuiltin ( 'StartAndroidActivity(com.rechild.advancedtaskkiller)' )
  except : pass
  if 99 - 99: II111iiii / iIII % OoooooooOO . i11iIiiIii
  if 18 - 18: o0oOOo0O0Ooo . oOO
def OoIII ( ) :
 xbmc . executebuiltin ( 'ReplaceWindow(settings)' )
 if 61 - 61: OoO0O00 / oOoO0o00OO0 % Oo - oOO
 if 26 - 26: O0 . oOoO0o00OO0 + OOo00O0 - iI1iiIiiII . oOoO0o00OO0
 if 2 - 2: I1ii11iIi11i . Oo0Ooo * Oo % II111iiii . OOo00O0
 if 46 - 46: OoOoOO00 + I1IiiI % OoooooooOO * i11iIiiIii - Oo0Ooo
def I1I111iiiIi11 ( ) :
 o0OoOOo ( )
 if 47 - 47: OOo00O0 * OoOoOO00 * iIII
 I1ii1i11i = xbmc . translatePath ( os . path . join ( I1IIIii , 'Community Builds' , 'My Builds' , '' ) )
 Oooooo0O00o = xbmc . translatePath ( os . path . join ( I1IIIii , 'Community Builds' , 'My Builds' , 'my_full_backup.zip' ) )
 II11ii1 = xbmc . translatePath ( os . path . join ( I1IIIii , 'Community Builds' , 'My Builds' , 'my_full_backup_GUI_Settings.zip' ) )
 if 46 - 46: iI1iiIiiII
 if not os . path . exists ( I1ii1i11i ) :
  os . makedirs ( I1ii1i11i )
  if 42 - 42: iIii1I11I1II1
 o0OO00oo0O = Ii1I1i111 ( heading = "Enter a name for this backup" )
 if 32 - 32: Oo0Ooo - iI1iiIiiII . OoooooooOO - OoooooooOO - Oo0Ooo . iIii1I11I1II1
 if ( not o0OO00oo0O ) :
  return False , 0
  if 34 - 34: Oo0Ooo
 iIIi11i1i1i1I = urllib . quote_plus ( o0OO00oo0O )
 i1i1iI1 = xbmc . translatePath ( os . path . join ( I1ii1i11i , iIIi11i1i1i1I + '.zip' ) )
 oOOO00OOOoOO = [ I1IiI ]
 III = [ "xbmc.log" , "xbmc.old.log" , "kodi.log" , "kodi.old.log" , '.DS_Store' , '.setup_complete' , 'XBMCHelper.conf' , 'Thumbs.db' , '.gitignore' ]
 i11Ii1iIiII = "Creating full backup of existing build"
 iiIIiii = "Creating Community Build"
 O0oOo00Ooo0o0 = "Archiving..."
 i1IiII1i1I = ""
 iI1ii1ii1I = "Please Wait"
 if 31 - 31: i1IIi - oOoO0o00OO0 + iIi1i1ii1 + oOO . oOO . O0
 i1II1iII ( iiI1IiI , Oooooo0O00o , i11Ii1iIiII , O0oOo00Ooo0o0 , i1IiII1i1I , iI1ii1ii1I , oOOO00OOOoOO , III )
 oOOoO0 . ok ( 'Full Backup Complete' , 'You can locate your backup at:[COLOR=dodgerblue]' , Oooooo0O00o + '[/COLOR]' )
 if 33 - 33: i1IIi / OOo00O0 * OoO0O00
 if 2 - 2: ooOo . Oo
def ii1O0oOOo ( ) :
 oOoO00 = xbmc . getInfoLabel ( "System.BuildVersion" )
 iIIiIiI1I1 = float ( oOoO00 [ : 4 ] )
 if 33 - 33: I1IiiI * iIi1i1ii1
 if iIIiIiI1I1 < 14 :
  OOooooO0 = os . path . join ( I11i1I1I , 'xbmc.log' )
  IIIiI1i1 ( 'XBMC Log' , OOooooO0 )
  if 23 - 23: OOo00O0 / OoOoOO00 + o0oOOo0O0Ooo . O0
 else :
  OOooooO0 = os . path . join ( I11i1I1I , 'kodi.log' )
  IIIiI1i1 ( 'Kodi Log' , OOooooO0 )
  if 76 - 76: OoOoOO00 . iIII - II111iiii * OoO0O00
  if 78 - 78: iIii1I11I1II1 / O0 * ooOo / OOo00O0 / OoOoOO00
def i1II1 ( ) :
 oOOoO0 . ok ( "Restore local guisettings fix" , "You should [COLOR=lime]ONLY[/COLOR] use this option if the guisettings fix is failing to download via the addon. Installing via this method means you do not receive notifications of updates" )
 Oo00o0o0O ( )
 if 82 - 82: II111iiii
 if 15 - 15: Oo
def o0oOOO0 ( mode ) :
 if not mode . endswith ( "premium" ) and not mode . endswith ( "public" ) and not mode . endswith ( "private" ) :
  o0OO00oo0O = Ii1I1i111 ( heading = "Search for content" )
  if 11 - 11: oOoO0o00OO0 / OoOoOO00
  if ( not o0OO00oo0O ) :
   return False , 0
   if 17 - 17: oOO
  iIIi11i1i1i1I = urllib . quote_plus ( o0OO00oo0O )
  if 13 - 13: Oo0Ooo - oOoO0o00OO0 / ooOo - Oo0Ooo - OOo00O0 / i11iIiiIii
  if mode == 'tutorials' :
   oOooOoOOo0O ( 'name=' + iIIi11i1i1i1I )
   if 29 - 29: iIII - oOoO0o00OO0 . O0 . O0
  if mode == 'hardware' :
   III1I1ii ( 'name=' + iIIi11i1i1i1I )
   if 16 - 16: i1IIi * oOO % OoO0O00 + iI1iiIiiII
  if mode == 'news' :
   o0oOOoO000 ( 'name=' + iIIi11i1i1i1I )
   if 50 - 50: ooOo - OoooooooOO + OOo00O0 % OoO0O00
 if mode . endswith ( "premium" ) or mode . endswith ( "public" ) or mode . endswith ( "private" ) :
  IIii ( 'folder' , 'Search By Name' , mode + '&name=' , 'search_builds' , 'Manual_Search.png' , '' , '' , '' )
  IIii ( 'folder' , 'Search By Uploader' , mode + '&author=' , 'search_builds' , 'Search_Genre.png' , '' , '' , '' )
  IIii ( 'folder' , 'Search By Audio Addons Installed' , mode + '&audio=' , 'search_builds' , 'Search_Addons.png' , '' , '' , '' )
  IIii ( 'folder' , 'Search By Picture Addons Installed' , mode + '&pics=' , 'search_builds' , 'Search_Addons.png' , '' , '' , '' )
  IIii ( 'folder' , 'Search By Program Addons Installed' , mode + '&progs=' , 'search_builds' , 'Search_Addons.png' , '' , '' , '' )
  IIii ( 'folder' , 'Search By Video Addons Installed' , mode + '&vids=' , 'search_builds' , 'Search_Addons.png' , '' , '' , '' )
  IIii ( 'folder' , 'Search By Skins Installed' , mode + '&skins=' , 'search_builds' , 'Search_Addons.png' , '' , '' , '' )
  if 12 - 12: i1IIi / I1ii11iIi11i - OOo00O0 . i11iIiiIii / i1IIi / OoooooooOO
  if 88 - 88: iI1iiIiiII / i11iIiiIii % OoOoOO00 % Oo
def OOI1 ( url ) :
 ii1111iII = 'http://noobsandnerds.com/TI/LatestNews/LatestNews.php?id=%s' % ( url )
 iiiiI = oooOo0OOOoo0 ( ii1111iII ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 O00o0 = re . compile ( 'name="(.+?)"' ) . findall ( iiiiI )
 IiIi1Ii = re . compile ( 'author="(.+?)"' ) . findall ( iiiiI )
 oooO00oOOooO = re . compile ( 'date="(.+?)"' ) . findall ( iiiiI )
 I1111i = re . compile ( 'content="(.+?)###END###"' ) . findall ( iiiiI )
 if 34 - 34: iIii1I11I1II1 / II111iiii
 I1i11i = O00o0 [ 0 ] if ( len ( O00o0 ) > 0 ) else ''
 I1111ii11IIII = IiIi1Ii [ 0 ] if ( len ( IiIi1Ii ) > 0 ) else ''
 o0OO0ooOOO = oooO00oOOooO [ 0 ] if ( len ( oooO00oOOooO ) > 0 ) else ''
 OooOo0o0Oo = I1111i [ 0 ] if ( len ( I1111i ) > 0 ) else ''
 IIIii111i = o0OO00000 ( OooOo0o0Oo )
 IIIii = str ( '[COLOR=orange]Source: [/COLOR]' + I1111ii11IIII + '     [COLOR=orange]Date: [/COLOR]' + o0OO0ooOOO + '[CR][CR][COLOR=lime]Details: [/COLOR][CR]' + IIIii111i )
 if 58 - 58: Oo % OOo00O0 * O0 + I1ii11iIi11i - iIII
 IIIiI1i1 ( I1i11i , IIIii )
 if 26 - 26: i1IIi / I1IiiI / oOoO0o00OO0 + oOoO0o00OO0
 if 46 - 46: iIi1i1ii1 % I1ii11iIi11i + iI1iiIiiII
def Ooii ( url ) :
 if iI1Ii11111iIi == 'true' :
  IIii ( '' , '[COLOR=orange]Latest ' + IIIi1I1IIii1II + ' news[/COLOR]' , IIIi1I1IIii1II , 'notify_msg' , 'LatestNews.png' , '' , '' , '' )
 IIii ( 'folder' , '[COLOR=yellow]Manual Search[/COLOR]' , 'news' , 'manual_search' , 'Manual_Search.png' , '' , '' , '' )
 if 28 - 28: OoO0O00
 IIii ( 'folder' , 'Official Kodi.tv News' , str ( url ) + '&author=Official%20Kodi' , 'grab_news' , 'XBMC.png' , '' , '' , '' )
 if 73 - 73: Oo0Ooo . oOO - Oo0Ooo % Oo / i11iIiiIii / iIii1I11I1II1
 if 15 - 15: oOO * iIii1I11I1II1 * ooOo
 if 96 - 96: iIi1i1ii1 * iIii1I11I1II1 / OoOoOO00 % Oo * II111iiii
 if 3 - 3: Oo . Oo0Ooo / i11iIiiIii + OoO0O00
 if 47 - 47: iIII . Oo
 if 96 - 96: oOoO0o00OO0 % II111iiii / oOO % Oo / oOO % i11iIiiIii
def O0000ooO ( title , message , times , icon ) :
 icon = i1I1iI + icon
 xbmc . executebuiltin ( "XBMC.Notification(" + title + "," + message + "," + times + "," + icon + ")" )
 if 83 - 83: iIi1i1ii1 + o0oOOo0O0Ooo % ooOo / OoO0O00
def o0o000O0ooo0O ( url ) :
 iIiiII1Ii1ii = xbmc . translatePath ( os . path . join ( ooOoOoo0O , I1IiI , 'notification.txt' ) )
 if 46 - 46: iIII % iIi1i1ii1 + iIii1I11I1II1 * I1IiiI
 if not os . path . exists ( iIiiII1Ii1ii ) :
  II1II1IIII = open ( iIiiII1Ii1ii , mode = 'w' )
  II1II1IIII . write ( '20150101000000' )
  II1II1IIII . close ( )
  if 64 - 64: I1ii11iIi11i * iI1iiIiiII * Oo0Ooo % iIII % oOO
 OoO0000O = open ( iIiiII1Ii1ii , 'r' ) . read ( )
 if 33 - 33: iIi1i1ii1 + OOo00O0 - Oo0Ooo / iI1iiIiiII + ooOo . OoOoOO00
 ii1111iII = 'http://noobsandnerds.com/TI/Community_Builds/notify?reseller=%s' % ( IIIi1I1IIii1II )
 iiiiI = oooOo0OOOoo0 ( ii1111iII ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 Oo0Oi1 = re . compile ( 'notify="(.+?)"' ) . findall ( iiiiI )
 oooO00oOOooO = re . compile ( 'date="(.+?)"' ) . findall ( iiiiI )
 iIi1iiii1ii = Oo0Oi1 [ 0 ] if ( len ( Oo0Oi1 ) > 0 ) else 'No news items available'
 oO0oOo = oooO00oOOooO [ 0 ] if ( len ( oooO00oOOooO ) > 0 ) else ''
 IIiIiii = oO0oOo . replace ( '-' , '' ) . replace ( ' ' , '' ) . replace ( ':' , '' )
 if 71 - 71: o0oOOo0O0Ooo + Oo . Oo0Ooo - OoOoOO00 * i11iIiiIii . OoOoOO00
 if int ( OoO0000O ) < int ( IIiIiii ) :
  II1II1IIII = open ( iIiiII1Ii1ii , mode = 'w' )
  II1II1IIII . write ( IIiIiii )
  II1II1IIII . close ( )
  oOOoO0 . ok ( 'Latest ' + IIIi1I1IIii1II + ' News' , iIi1iiii1ii )
  if 91 - 91: O0 - oOoO0o00OO0 % iIi1i1ii1
 else :
  oOOoO0 . ok ( 'Latest ' + IIIi1I1IIii1II + ' News' , iIi1iiii1ii )
  if 46 - 46: oOO / I1IiiI . iIII % OoO0O00 / i11iIiiIii
  if 13 - 13: iIi1i1ii1 % o0oOOo0O0Ooo + Oo + iIi1i1ii1 + i11iIiiIii - I1ii11iIi11i
def ooooooo0oOo0 ( ) :
 xbmc . executebuiltin ( 'ActivateWindow(filemanager,return)' )
 return
 if 81 - 81: i11iIiiIii % I1IiiI / OOo00O0 % OoO0O00 / iIi1i1ii1 % iIii1I11I1II1
 if 14 - 14: I1ii11iIi11i * Oo0Ooo + i11iIiiIii % Oo - ooOo
def iIIiio000oo ( ) :
 xbmc . executebuiltin ( 'ActivateWindow(systeminfo)' )
 if 58 - 58: oOO + II111iiii + iI1iiIiiII . OoooooooOO
 if 42 - 42: iIii1I11I1II1 / oOoO0o00OO0 . O0 . iI1iiIiiII
def oooOo0OOOoo0 ( url ) :
 Ii1i111iI = urllib2 . Request ( url )
 Ii1i111iI . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows; U; Windows NT 10.0; WOW64; Windows NT 5.1; en-GB; rv:1.9.0.3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36 Gecko/2008092417 Firefox/3.0.3' )
 if 48 - 48: Oo0Ooo
 OooO0oO0Oo0 = urllib2 . urlopen ( Ii1i111iI )
 iiiiI = OooO0oO0Oo0 . read ( )
 OooO0oO0Oo0 . close ( )
 return iiiiI . replace ( '\r' , '' ) . replace ( '\n' , '' ) . replace ( '\t' , '' )
 if 84 - 84: II111iiii / OoO0O00 . iIII
 if 79 - 79: Oo
def o00oO00O0 ( ) :
 import tarfile
 if 16 - 16: iI1iiIiiII / i11iIiiIii + O0 . iIII
 if not os . path . exists ( oO0Oo ) :
  os . makedirs ( oO0Oo )
  if 15 - 15: Oo0Ooo + OOo00O0 + I1IiiI * o0oOOo0O0Ooo
 O0OoO000O0OO . create ( "Creating Backup" , "Adding files... " , '' , 'Please Wait' )
 iII1111IIIIiI = tarfile . open ( os . path . join ( oO0Oo , IiiiiIi11 ( ) + '.tar' ) , 'w' )
 if 57 - 57: OOo00O0 / OoO0O00 - II111iiii
 for I1i1i1IIi1I in i1i :
  O0OoO000O0OO . update ( 0 , "Backing Up" , '[COLOR blue]%s[/COLOR]' % I1i1i1IIi1I , 'Please Wait' )
  iII1111IIIIiI . add ( I1i1i1IIi1I )
  if 18 - 18: ooOo * iI1iiIiiII / OoooooooOO % OoOoOO00 - i1IIi
 iII1111IIIIiI . close ( )
 O0OoO000O0OO . close ( )
 if 49 - 49: o0oOOo0O0Ooo - iIii1I11I1II1
 if 61 - 61: OOo00O0 * oOO
def Oo0o0Oo0O ( ) :
 oOoO00 = xbmc . getInfoLabel ( "System.BuildVersion" )
 iIIiIiI1I1 = float ( oOoO00 [ : 4 ] )
 if iIIiIiI1I1 < 14 :
  i1I1IiIiiI1II = os . path . join ( I11i1I1I , 'xbmc.log' )
 else :
  i1I1IiIiiI1II = os . path . join ( I11i1I1I , 'kodi.log' )
  if 39 - 39: OoooooooOO
 try :
  II1II1IIII = open ( i1I1IiIiiI1II , mode = 'r' )
  OooOo0o0Oo = II1II1IIII . read ( )
  II1II1IIII . close ( )
 except :
  try :
   II1II1IIII = open ( os . path . join ( iiI1IiI , 'temp' , 'kodi.log' ) , mode = 'r' )
   OooOo0o0Oo = II1II1IIII . read ( )
   II1II1IIII . close ( )
  except :
   try :
    II1II1IIII = open ( os . path . join ( iiI1IiI , 'temp' , 'xbmc.log' ) , mode = 'r' )
    OooOo0o0Oo = II1II1IIII . read ( )
    II1II1IIII . close ( )
   except : pass
   if 37 - 37: OOo00O0 . o0oOOo0O0Ooo / iI1iiIiiII / Oo * i1IIi
 if 'OpenELEC' in OooOo0o0Oo :
  return True
  if 90 - 90: I1IiiI . II111iiii - i1IIi + ooOo
  if 58 - 58: OOo00O0 - OoooooooOO
def o00oO00 ( ) :
 xbmc . executebuiltin ( 'RunAddon(service.openelec.settings)' )
 if 27 - 27: OOo00O0 . OoOoOO00 / OoooooooOO
 if 18 - 18: i1IIi . I1IiiI
def Oooo0O ( name , url , iconimage , description ) :
 oOOo0O0Oo = xbmc . translatePath ( os . path . join ( 'special://home/userdata/addon_data/script.tvguidedixie/' , '' ) )
 III1I1I1iiIi = os . path . join ( oOOo0O0Oo , 'local.ini' )
 ii1I11iIiIII1 = oOOoO0 . yesno ( 'OffsideStreams / OnTapp.TV Integration ' , str ( description ) , nolabel = 'Cancel' , yeslabel = 'Accept' )
 if 30 - 30: OoOoOO00 - i11iIiiIii
 if ii1I11iIiIII1 == 0 :
  return
  if 94 - 94: OoOoOO00 % OOo00O0
 elif ii1I11iIiIII1 == 1 :
  O0Oo0 = III1I1I1iiIi
  if 39 - 39: OoOoOO00 + iIi1i1ii1 % O0
  if not os . path . exists ( oOOo0O0Oo ) :
   oOOoO0 . ok ( '[COLOR=red]OnTapp Not Installed[/COLOR]' , 'The On-Tapp.TV addon has not been found on this system, please install then run this again.' )
   if 26 - 26: oOO + OoOoOO00
  else :
   download ( url , O0Oo0 )
   oOOoO0 . ok ( 'OSS Integration complete' , 'The OffsideStreams local.ini file has now been copied to your OnTapp.TV directory' )
   if 17 - 17: I1ii11iIi11i - OOo00O0 % Oo0Ooo * O0 % O0 * Oo
   if 6 - 6: iIi1i1ii1
def ii1iiIiiiI11 ( url ) :
 IIii ( 'folder' , '[COLOR=yellow]1. Install:[/COLOR]  Installation tutorials (e.g. flashing a new OS)' , str ( url ) + '&thirdparty=InstallTools' , 'grab_tutorials' , 'Install.png' , '' , '' , '' )
 IIii ( 'folder' , '[COLOR=dodgerblue]Add-on Tools:[/COLOR]  Add-on maintenance and coding tutorials' , str ( url ) + '&thirdparty=AddonTools' , 'grab_tutorials' , 'ADDONTOOLS.png' , '' , '' , '' )
 IIii ( 'folder' , '[COLOR=dodgerblue]Audio Tools:[/COLOR]  Audio related tutorials' , str ( url ) + '&thirdparty=AudioTools' , 'grab_tutorials' , 'AUDIOTOOLS.png' , '' , '' , '' )
 IIii ( 'folder' , '[COLOR=dodgerblue]Gaming Tools:[/COLOR]  Integrate a gaming section into your setup' , str ( url ) + '&thirdparty=GamingTools' , 'grab_tutorials' , 'gaming_portal.png' , '' , '' , '' )
 IIii ( 'folder' , '[COLOR=dodgerblue]Image Tools:[/COLOR]  Tutorials to assist with your pictures/photos' , str ( url ) + '&thirdparty=ImageTools' , 'grab_tutorials' , 'IMAGETOOLS.png' , '' , '' , '' )
 IIii ( 'folder' , '[COLOR=dodgerblue]Library Tools:[/COLOR]  Music and Video Library Tutorials' , str ( url ) + '&thirdparty=LibraryTools' , 'grab_tutorials' , 'LIBRARYTOOLS.png' , '' , '' , '' )
 IIii ( 'folder' , '[COLOR=dodgerblue]Skinning Tools:[/COLOR]  All your skinning advice' , str ( url ) + '&thirdparty=SkinningTools' , 'grab_tutorials' , 'SKINNINGTOOLS.png' , '' , '' , '' )
 IIii ( 'folder' , '[COLOR=dodgerblue]Video Tools:[/COLOR]  All video related tools' , str ( url ) + '&thirdparty=VideoTools' , 'grab_tutorials' , 'VIDEOTOOLS.png' , '' , '' , '' )
 if 95 - 95: iIi1i1ii1 - iIII
def I1ii ( ) :
 oO0ooo00OoOooooo = 'http://noobsandnerds.com/TI/Addon_Packs/addonpacks.txt'
 iiiiI = oooOo0OOOoo0 ( oO0ooo00OoOooooo ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 O0OoOoO00O = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( iiiiI )
 if 87 - 87: II111iiii - OoooooooOO / i1IIi . iI1iiIiiII - Oo0Ooo . i11iIiiIii
 for I1i11i , o0oOOoo0O , iii1IIIiiiI , OoO00oo00 , IIIii in O0OoOoO00O :
  IIii ( 'folder2' , I1i11i , o0oOOoo0O , 'popularwizard' , iii1IIIiiiI , OoO00oo00 , '' , IIIii )
  if 47 - 47: Oo0Ooo % OoO0O00 - oOO - Oo0Ooo * ooOo
def OOOOO0oOOoO ( name , url , iconimage , description ) :
 IIIiI1i1 ( name , description )
 ii1I11iIiIII1 = oOOoO0 . yesno ( name , 'This will install the ' + name , '' , 'Are you sure you want to continue?' , nolabel = 'Cancel' , yeslabel = 'Accept' )
 if 42 - 42: I1IiiI + i11iIiiIii / OoO0O00
 if ii1I11iIiIII1 == 0 :
  return
  if 64 - 64: iIII
 elif ii1I11iIiIII1 == 1 :
  import downloader
  O0Oo0 = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
  OooooOOOO = xbmc . translatePath ( os . path . join ( 'special://' , 'home' ) )
  O0OoO000O0OO = xbmcgui . DialogProgress ( )
  O0OoO000O0OO . create ( "Addon Packs" , "Downloading " + name + " addon pack." , '' , 'Please Wait' )
  i1i1i11iI11II = os . path . join ( O0Oo0 , name + '.zip' )
  if 89 - 89: O0 + iIII * iIi1i1ii1
  try :
   os . remove ( i1i1i11iI11II )
   if 30 - 30: OoOoOO00
  except :
   pass
   downloader . download ( url , i1i1i11iI11II , O0OoO000O0OO )
   time . sleep ( 3 )
   O0OoO000O0OO . update ( 0 , "" , "Extracting Zip Please Wait" )
   xbmc . executebuiltin ( "XBMC.Extract(%s,%s)" % ( i1i1i11iI11II , OooooOOOO ) )
   oOOoO0 . ok ( "Total Installer" , "All Done. Your addons will now go through the update process, it may take a minute or two until the addons are working." )
   time . sleep ( 1 )
   xbmc . executebuiltin ( 'UpdateLocalAddons' )
   xbmc . executebuiltin ( 'UpdateAddonRepos' )
   if 39 - 39: I1ii11iIi11i + o0oOOo0O0Ooo + iIi1i1ii1 + iIII
   if 48 - 48: iIi1i1ii1 / oOO . iIii1I11I1II1
   if 72 - 72: i1IIi . o0oOOo0O0Ooo
   if 3 - 3: OoOoOO00 % II111iiii - O0
   if 52 - 52: OoO0O00
   if 49 - 49: iI1iiIiiII . I1ii11iIi11i % oOO . Oo0Ooo * Oo
   if 44 - 44: iIii1I11I1II1 / O0 * Oo0Ooo + I1IiiI . oOO
   if 20 - 20: OOo00O0 + o0oOOo0O0Ooo . iIi1i1ii1 / i11iIiiIii
   if 7 - 7: OoOoOO00 / OoOoOO00 . iIi1i1ii1 * O0 + iIII + ooOo
   if 98 - 98: II111iiii * iIII - I1IiiI % o0oOOo0O0Ooo - OOo00O0 % I1ii11iIi11i
   if 69 - 69: i1IIi % OoO0O00 % iIi1i1ii1 / oOO / oOO
   if 6 - 6: II111iiii % I1ii11iIi11i % i1IIi * oOO
   if 47 - 47: O0
   if 55 - 55: OoO0O00 % O0 / OoooooooOO
   if 49 - 49: I1IiiI . OoO0O00 * OoooooooOO % i11iIiiIii + iIii1I11I1II1 * i1IIi
   if 88 - 88: I1ii11iIi11i * OOo00O0 + II111iiii
   if 62 - 62: OoooooooOO
   if 33 - 33: O0 . i11iIiiIii % o0oOOo0O0Ooo
   if 50 - 50: oOO
   if 81 - 81: i11iIiiIii * iIii1I11I1II1 / Oo0Ooo * Oo
   if 83 - 83: i11iIiiIii - I1IiiI * i11iIiiIii
   if 59 - 59: OOo00O0 - OoooooooOO / oOO + I1ii11iIi11i . o0oOOo0O0Ooo - OOo00O0
   if 29 - 29: ooOo
   if 26 - 26: O0 % Oo - iIII . Oo
   if 70 - 70: o0oOOo0O0Ooo + oOoO0o00OO0 / OOo00O0 + oOO / I1IiiI
   if 33 - 33: OoooooooOO . O0
   if 59 - 59: iIii1I11I1II1
   if 45 - 45: O0
   if 78 - 78: oOoO0o00OO0 - iIii1I11I1II1 + iIi1i1ii1 - I1ii11iIi11i - iIi1i1ii1
   if 21 - 21: OoooooooOO . O0 / i11iIiiIii
   if 86 - 86: OoOoOO00 / Oo
   if 40 - 40: iIii1I11I1II1 / oOO / I1IiiI + I1ii11iIi11i * Oo
   if 1 - 1: OoO0O00 * oOO + iIII . ooOo / oOO
   if 91 - 91: iI1iiIiiII + oOoO0o00OO0 - Oo0Ooo % OoOoOO00 . OOo00O0
   if 51 - 51: Oo / oOoO0o00OO0
   if 51 - 51: oOO * ooOo - iIi1i1ii1 + OOo00O0
   if 46 - 46: o0oOOo0O0Ooo - i11iIiiIii % OoO0O00 / iI1iiIiiII - OoOoOO00
   if 88 - 88: ooOo * I1IiiI / OoO0O00 - Oo / i1IIi . iIi1i1ii1
   if 26 - 26: i11iIiiIii - oOO
   if 45 - 45: oOO + II111iiii % OOo00O0
   if 55 - 55: oOO - ooOo % I1IiiI
   if 61 - 61: oOO
   if 22 - 22: iIii1I11I1II1 / oOO / I1IiiI - o0oOOo0O0Ooo
   if 21 - 21: ooOo . i11iIiiIii * oOoO0o00OO0 . Oo / Oo
def OOO0ooo ( recursive_location , remote_path ) :
 if not os . path . exists ( recursive_location ) :
  os . makedirs ( recursive_location )
  if 42 - 42: OoooooooOO / iIi1i1ii1 . o0oOOo0O0Ooo / O0 - iIII * iIII
 iiiiI = oooOo0OOOoo0 ( remote_path ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 O0OoOoO00O = re . compile ( 'href="(.+?)"' , re . DOTALL ) . findall ( iiiiI )
 if 1 - 1: iI1iiIiiII % iIi1i1ii1
 for Ii11Iii1i1ii in O0OoOoO00O :
  Ii1i1i1111 = xbmc . translatePath ( os . path . join ( recursive_location , Ii11Iii1i1ii ) )
  if 97 - 97: OoOoOO00
  if '/' not in Ii11Iii1i1ii :
   if 13 - 13: OoOoOO00 % Oo . O0 / Oo0Ooo % Oo0Ooo
   try :
    O0OoO000O0OO . update ( 0 , "Downloading [COLOR=yellow]" + Ii11Iii1i1ii + '[/COLOR]' , '' , 'Please wait...' )
    downloader . download ( remote_path + Ii11Iii1i1ii , Ii1i1i1111 , O0OoO000O0OO )
    if 19 - 19: iIi1i1ii1 % oOO - oOO % I1IiiI . Oo - OoooooooOO
   except :
    print "failed to install" + Ii11Iii1i1ii
    if 100 - 100: I1IiiI + iI1iiIiiII + o0oOOo0O0Ooo . i1IIi % OoooooooOO
  if '/' in Ii11Iii1i1ii and '..' not in Ii11Iii1i1ii and 'http' not in Ii11Iii1i1ii :
   Oo0oO0O0OO = remote_path + Ii11Iii1i1ii
   OOO0ooo ( Ii1i1i1111 , Oo0oO0O0OO )
   if 20 - 20: OoOoOO00
  else :
   pass
   if 1 - 1: iIi1i1ii1 * OoO0O00 - OOo00O0
   if 97 - 97: OOo00O0 . I1ii11iIi11i - iIii1I11I1II1 . oOO + I1IiiI % ooOo
def Ii1i1iiiIiIIiIiiii ( ) :
 oOOoO0 . ok ( "Register to unlock features" , "To get the most out of this addon please register at the [COLOR=orange]noobs[/COLOR][COLOR=dodgerblue]and[/COLOR][COLOR=orange]nerds[/COLOR] forum for free." , 'www.noobsandnerds.com' )
 if 99 - 99: iIII % iIi1i1ii1
 if 61 - 61: O0 + I1IiiI / OoooooooOO * OOo00O0 / II111iiii / OOo00O0
def O0OO0oOo00o0 ( ) :
 ii1I11iIiIII1 = xbmcgui . Dialog ( ) . yesno ( 'Delete Addon_Data Folder?' , 'This will free up space by deleting your addon_data folder. This contains all addon related settings including username and password info.' , nolabel = 'Cancel' , yeslabel = 'Delete' )
 if 43 - 43: O0 / iIi1i1ii1 . iIii1I11I1II1 - OoOoOO00
 if ii1I11iIiIII1 == 1 :
  o0oOOOOoo0 ( )
  oOOoO0 . ok ( "Addon_Data Removed" , '' , 'Your addon_data folder has now been removed.' , '' )
  if 47 - 47: II111iiii - I1ii11iIi11i - iI1iiIiiII
def IiiiIiiI ( url ) :
 iI1Iii1i1 = str ( url ) . replace ( OO0o , ooOoOoo0O )
 if 87 - 87: i11iIiiIii * II111iiii - iI1iiIiiII % OoooooooOO
 if oOOoO0 . yesno ( "Remove" , '' , "Do you want to Remove" ) :
  if 55 - 55: i1IIi
  for OOo000o , oO0ooOoO , ooO0000o00O in os . walk ( url ) :
   if 67 - 67: I1IiiI - OoO0O00
   for ooO0oo0o0 in ooO0000o00O :
    os . unlink ( os . path . join ( OOo000o , ooO0oo0o0 ) )
    if 60 - 60: i1IIi / iIii1I11I1II1 * ooOo + oOO + OoooooooOO + II111iiii
   for iiIiI1ii in oO0ooOoO :
    shutil . rmtree ( os . path . join ( OOo000o , iiIiI1ii ) )
  os . rmdir ( url )
  if 13 - 13: iIii1I11I1II1 - Oo
  try :
   if 14 - 14: oOO
   for OOo000o , oO0ooOoO , ooO0000o00O in os . walk ( iI1Iii1i1 ) :
    if 75 - 75: iIii1I11I1II1 % oOO / Oo - OOo00O0 % i11iIiiIii
    for ooO0oo0o0 in ooO0000o00O :
     os . unlink ( os . path . join ( OOo000o , ooO0oo0o0 ) )
     if 11 - 11: oOoO0o00OO0 . iI1iiIiiII
    for iiIiI1ii in oO0ooOoO :
     shutil . rmtree ( os . path . join ( OOo000o , iiIiI1ii ) )
     if 87 - 87: Oo + Oo
   os . rmdir ( iI1Iii1i1 )
   if 45 - 45: i1IIi - Oo0Ooo
  except :
   pass
   if 87 - 87: OoOoOO00 - OoO0O00 * OoO0O00 / iI1iiIiiII . oOoO0o00OO0 * o0oOOo0O0Ooo
  iii1I = os . path . join ( II , 'Database' , 'Addons16.db' )
  if 77 - 77: OoOoOO00
  try :
   os . remove ( iii1I )
   if 31 - 31: iIII / OOo00O0
  except :
   pass
   if 97 - 97: OoO0O00 + iIii1I11I1II1
  xbmc . executebuiltin ( 'UpdateLocalAddons' )
  xbmc . sleep ( 1000 )
  xbmc . executebuiltin ( 'UpdateAddonRepos' )
  oOOoO0 . ok ( 'Add-on removed' , 'You may have to restart Kodi to repopulate' , 'your add-on database. Until you restart you\'ll' , 'find your add-on is still showing even though it\'s deleted' )
  xbmc . executebuiltin ( 'Container.Refresh' )
  if 79 - 79: oOO + ooOo - II111iiii . Oo0Ooo
  if 26 - 26: iIII
def oo0o0o ( ) :
 o0OoOOo ( )
 I1I11I1i1i1II = xbmcgui . Dialog ( ) . browse ( 1 , 'Select the backup file you want to DELETE' , 'files' , '.zip' , False , False , I1IIIii )
 if 1 - 1: I1IiiI . iI1iiIiiII
 if I1I11I1i1i1II != I1IIIii :
  II11IIII1 = ntpath . basename ( I1I11I1i1i1II )
  ii1I11iIiIII1 = xbmcgui . Dialog ( ) . yesno ( 'Delete Backup File' , 'This will completely remove ' + II11IIII1 , 'Are you sure you want to delete?' , '' , nolabel = 'No, Cancel' , yeslabel = 'Yes, Delete' )
  if 33 - 33: iI1iiIiiII + OoOoOO00 - I1ii11iIi11i + iIii1I11I1II1 % i1IIi * iIII
  if ii1I11iIiIII1 == 1 :
   os . remove ( I1I11I1i1i1II )
   if 21 - 21: O0 * oOO % OoO0O00
   if 14 - 14: O0 / iIi1i1ii1 / oOO + iIII - iIII
def IiiI11iIi ( ) :
 ii1I11iIiIII1 = xbmcgui . Dialog ( ) . yesno ( 'Remove All Crash Logs?' , 'There is absolutely no harm in doing this, these are log files generated when Kodi crashes and are only used for debugging purposes.' , nolabel = 'Cancel' , yeslabel = 'Delete' )
 if 17 - 17: iIi1i1ii1 % oOO + iIII % o0oOOo0O0Ooo . i1IIi
 if ii1I11iIiIII1 == 1 :
  o0OOO00ooo ( )
  oOOoO0 . ok ( "Crash Logs Removed" , '' , 'Your crash log files have now been removed.' , '' )
  if 58 - 58: Oo
  if 94 - 94: OoooooooOO - oOO % Oo - OOo00O0 / i1IIi
def iiiiIIi11I1 ( ) :
 ii1I11iIiIII1 = xbmcgui . Dialog ( ) . yesno ( 'Delete Packages Folder?' , 'This will free up space by deleting the zip install files of your addons. The only downside is you\'ll no longer be able to rollback to older versions.' , nolabel = 'Cancel' , yeslabel = 'Delete' )
 if 77 - 77: Oo + OoooooooOO * OoooooooOO + OoooooooOO . OoO0O00 * O0
 if ii1I11iIiIII1 == 1 :
  O0i1I11I ( )
  oOOoO0 . ok ( "Packages Removed" , '' , 'Your zip install files have now been removed.' , '' )
  if 16 - 16: OoO0O00
  if 44 - 44: oOoO0o00OO0 . iIII % iIi1i1ii1 - oOO - I1ii11iIi11i
def oO0O0o0o00 ( ) :
 ii1I11iIiIII1 = xbmcgui . Dialog ( ) . yesno ( 'Clear Cached Images?' , 'This will clear your textures13.db file and remove your Thumbnails folder. These will automatically be repopulated after a restart.' , nolabel = 'Cancel' , yeslabel = 'Delete' )
 if 34 - 34: I1ii11iIi11i % i1IIi - OoO0O00
 if ii1I11iIiIII1 == 1 :
  I1I11 ( )
  OO00oO0OoO0o ( II11iiii1Ii )
  if 18 - 18: I1IiiI + iIi1i1ii1 - OOo00O0 % II111iiii / OoOoOO00 % O0
  ii1I11iIiIII1 = xbmcgui . Dialog ( ) . yesno ( 'Quit Kodi Now?' , 'Cache has been successfully deleted.' , 'You must now restart Kodi, would you like to quit now?' , '' , nolabel = 'I\'ll restart later' , yeslabel = 'Yes, quit' )
  if 59 - 59: O0 . o0oOOo0O0Ooo % I1ii11iIi11i * ooOo + oOoO0o00OO0
  if ii1I11iIiIII1 == 1 :
   try :
    xbmc . executebuiltin ( "RestartApp" )
    if 82 - 82: OoooooooOO
   except :
    iI1i1iI1iI ( )
    if 88 - 88: O0 / o0oOOo0O0Ooo * o0oOOo0O0Ooo . o0oOOo0O0Ooo . O0
    if 27 - 27: i11iIiiIii % OOo00O0 + iI1iiIiiII . Oo
def I1I11 ( ) :
 iIIi1I1 = xbmc . translatePath ( 'special://home/userdata/Database/Textures13.db' )
 try :
  ooI1 = database . connect ( iIIi1I1 )
  i1Iii1i1II1 = ooI1 . cursor ( )
  i1Iii1i1II1 . execute ( "DROP TABLE IF EXISTS path" )
  i1Iii1i1II1 . execute ( "VACUUM" )
  ooI1 . commit ( )
  i1Iii1i1II1 . execute ( "DROP TABLE IF EXISTS sizes" )
  i1Iii1i1II1 . execute ( "VACUUM" )
  ooI1 . commit ( )
  i1Iii1i1II1 . execute ( "DROP TABLE IF EXISTS texture" )
  i1Iii1i1II1 . execute ( "VACUUM" )
  ooI1 . commit ( )
  i1Iii1i1II1 . execute ( """CREATE TABLE path (id integer, url text, type text, texture text, primary key(id))""" )
  ooI1 . commit ( )
  i1Iii1i1II1 . execute ( """CREATE TABLE sizes (idtexture integer,size integer, width integer, height integer, usecount integer, lastusetime text)""" )
  ooI1 . commit ( )
  i1Iii1i1II1 . execute ( """CREATE TABLE texture (id integer, url text, cachedurl text, imagehash text, lasthashcheck text, PRIMARY KEY(id))""" )
  ooI1 . commit ( )
 except :
  pass
  if 75 - 75: oOO % Oo / o0oOOo0O0Ooo % II111iiii
  if 30 - 30: o0oOOo0O0Ooo
def iii1IIiI ( url ) :
 ii1111iII = 'http://noobsandnerds.com/TI/Community_Builds/reseller_2?reseller=%s&token=%s&openelec=%s' % ( IIIi1I1IIii1II , O0ii1ii1ii , url )
 print ii1111iII
 iiiiI = oooOo0OOOoo0 ( ii1111iII ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 ii1IiI11I = re . compile ( 'path="(.+?)"' ) . findall ( iiiiI )
 IiI1i1iI = re . compile ( 'reseller="(.+?)"' ) . findall ( iiiiI )
 iIIi = re . compile ( 'premium="(.+?)"' ) . findall ( iiiiI )
 iIIIII = re . compile ( 'openelec="(.+?)"' ) . findall ( iiiiI )
 iiiII = IiI1i1iI [ 0 ] if ( len ( IiI1i1iI ) > 0 ) else 'None'
 Oo0OooII1iII11 = iIIi [ 0 ] if ( len ( iIIi ) > 0 ) else 'None'
 iiiI1 = iIIIII [ 0 ] if ( len ( iIIIII ) > 0 ) else 'None'
 exec iiiI1
 exec iiiII
 exec Oo0OooII1iII11
 if 13 - 13: i11iIiiIii - II111iiii - OoooooooOO * iIi1i1ii1
 if 50 - 50: Oo0Ooo - o0oOOo0O0Ooo % II111iiii . O0 . ooOo % II111iiii
def I1IiiI1I1I ( name , url , description ) :
 if 'Backup' in name :
  o0OoOOo ( )
  ii11i1II111 = open ( url ) . read ( )
  i1I1IiiIIiiI1I11 = os . path . join ( I1IIIii , description . split ( 'Your ' ) [ 1 ] )
  ooO0oo0o0 = open ( i1I1IiiIIiiI1I11 , mode = 'w' )
  ooO0oo0o0 . write ( ii11i1II111 )
  ooO0oo0o0 . close ( )
  if 74 - 74: o0oOOo0O0Ooo - oOO / I1IiiI
 else :
  if 'guisettings.xml' in description :
   IIii1I1i = open ( os . path . join ( I1IIIii , description . split ( 'Your ' ) [ 1 ] ) ) . read ( )
   oo0o0o0o0o0 = '<setting type="(.+?)" name="%s.(.+?)">(.+?)</setting>' % o0OO00oO
   O0OoOoO00O = re . compile ( oo0o0o0o0o0 ) . findall ( IIii1I1i )
   if 36 - 36: I1IiiI / Oo0Ooo % iIii1I11I1II1 / O0 . I1ii11iIi11i
   for type , OOOoOOooOoo , O00OO0oOOO in O0OoOoO00O :
    O00OO0oOOO = O00OO0oOOO . replace ( '&quot;' , '' ) . replace ( '&amp;' , '&' )
    xbmc . executebuiltin ( "Skin.Set%s(%s,%s)" % ( type . title ( ) , OOOoOOooOoo , O00OO0oOOO ) )
    if 41 - 41: iIII * OoooooooOO . oOO % i11iIiiIii
  else :
   i1I1IiiIIiiI1I11 = os . path . join ( url )
   ii11i1II111 = open ( os . path . join ( I1IIIii , description . split ( 'Your ' ) [ 1 ] ) ) . read ( )
   ooO0oo0o0 = open ( i1I1IiiIIiiI1I11 , mode = 'w' )
   ooO0oo0o0 . write ( ii11i1II111 )
   ooO0oo0o0 . close ( )
   if 11 - 11: iIii1I11I1II1 . iIi1i1ii1 - Oo0Ooo / oOoO0o00OO0 + II111iiii
 oOOoO0 . ok ( "[COLOR=blue][B]T[/COLOR][COLOR=dodgerblue]R[/COLOR] [COLOR=white]Community Builds[/COLOR][/B]" , "" , 'All Done !' , '' )
 if 29 - 29: oOoO0o00OO0 . i11iIiiIii + i1IIi - iI1iiIiiII + O0 . I1IiiI
 if 8 - 8: o0oOOo0O0Ooo
def ooOO0O0O ( name , url , video , description , skins , guisettingslink , artpack ) :
 O0OoO000O0OO . create ( "Backing Up Important Data" , 'Please wait...' , '' , '' )
 if 18 - 18: ooOo * O0 - I1IiiI + O0 + iIi1i1ii1
 if 70 - 70: o0oOOo0O0Ooo / oOoO0o00OO0 + ooOo % I1IiiI % Oo0Ooo + OoO0O00
 ooo0ooo0Oo = open ( iiiiiIIii , mode = 'r' )
 I1ii1iii = ooo0ooo0Oo . read ( )
 ooo0ooo0Oo . close ( )
 if 90 - 90: o0oOOo0O0Ooo % I1ii11iIi11i / OoOoOO00
 o0O00o0o = re . compile ( 'gui="(.+?)"' ) . findall ( I1ii1iii )
 I11Ii111IIi = o0O00o0o [ 0 ] if ( len ( o0O00o0o ) > 0 ) else '0'
 if 65 - 65: iIii1I11I1II1 . Oo + OOo00O0 . o0oOOo0O0Ooo
 if 100 - 100: II111iiii . iIi1i1ii1 - OoOoOO00 % II111iiii
 if O0oo0OO0 == 'true' :
  try :
   oO0OO00O0 = open ( iIi1ii1I1 , mode = 'r' )
   O000oOo0OO = oO0OO00O0 . read ( )
   oO0OO00O0 . close ( )
   if 57 - 57: I1ii11iIi11i
  except :
   print "### No favourites file to copy"
   if 30 - 30: I1ii11iIi11i * iIII % iIII * OOo00O0 . OOo00O0
 if I1i1iiI1 == 'true' :
  try :
   III1iIiIiII = open ( o0 , mode = 'r' )
   IiiI1iIiI = III1iIiIiII . read ( )
   III1iIiIiII . close ( )
   if 91 - 91: o0oOOo0O0Ooo * I1ii11iIi11i - OOo00O0 . II111iiii
  except :
   print "### No sources file to copy"
   if 1 - 1: Oo + iIi1i1ii1 * I1ii11iIi11i
   if 44 - 44: OOo00O0
 oOoOoOOOO0o = xbmc . getSkinDir ( )
 print "Current Skin: " + oOoOoOOOO0o
 if video == 'fresh' and oOoOoOOOO0o != "skin.confluence" :
  oOOoO0 . ok ( 'Default Confluence Skin Required' , '' , 'Please switch to the default Confluence skin.' , '' )
  xbmc . executebuiltin ( 'ActivateWindow(appearancesettings,return)' )
  return
  if 57 - 57: OOo00O0 . iI1iiIiiII * I1IiiI % iIi1i1ii1 + iIii1I11I1II1
 OoO00o = 1
 o0OoOOo ( )
 if 90 - 90: OoooooooOO % i11iIiiIii % o0oOOo0O0Ooo % iIi1i1ii1 - oOO + iIii1I11I1II1
 if 98 - 98: O0 / ooOo / OOo00O0
 if os . path . exists ( O0Oo000ooO00 ) :
  if 83 - 83: iIi1i1ii1
  if os . path . exists ( O0O ) :
   os . remove ( O0Oo000ooO00 )
   if 38 - 38: ooOo
  else :
   os . rename ( O0Oo000ooO00 , O0O )
   if 9 - 9: oOoO0o00OO0 . OoO0O00 . ooOo / OoooooooOO
 if os . path . exists ( O00o0OO ) :
  os . remove ( O00o0OO )
  if 59 - 59: iIii1I11I1II1 + i1IIi % II111iiii
  if 2 - 2: II111iiii + oOoO0o00OO0 . OoO0O00
 if not os . path . exists ( OOO00 ) :
  II1II1IIII = open ( OOO00 , mode = 'w+' )
  II1II1IIII . close ( )
  if 14 - 14: Oo * I1IiiI - I1ii11iIi11i
 O0OoO000O0OO . close ( )
 O0OoO000O0OO . create ( "Downloading Skin Fix" , "Downloading guisettings.xml" , '' , 'Please Wait' )
 i1i1i11iI11II = os . path . join ( I1IIIii , 'guifix.zip' )
 if 10 - 10: OOo00O0 % iIi1i1ii1 * I1ii11iIi11i * O0 * i11iIiiIii % iIi1i1ii1
 if 68 - 68: OoooooooOO * OoOoOO00
 downloader . download ( guisettingslink , i1i1i11iI11II , O0OoO000O0OO )
 O0OoO000O0OO . close ( )
 if 9 - 9: iIi1i1ii1
 if 36 - 36: iIi1i1ii1 / OoOoOO00 + OoOoOO00 * oOO / Oo * O0
 if zipfile . is_zipfile ( i1i1i11iI11II ) :
  iIo00oo = str ( os . path . getsize ( i1i1i11iI11II ) )
  if 17 - 17: OoO0O00 / oOO % I1IiiI
 else :
  iIo00oo = I11Ii111IIi
  if 47 - 47: Oo0Ooo * OoO0O00 / o0oOOo0O0Ooo * I1IiiI
  if 60 - 60: I1ii11iIi11i / iIII . i11iIiiIii / OoO0O00 % II111iiii
 II1II1IIII = open ( OOO00 , mode = 'r' )
 OooOo0o0Oo = II1II1IIII . read ( )
 II1II1IIII . close ( )
 if 6 - 6: OOo00O0 % o0oOOo0O0Ooo + iIi1i1ii1
 oOoo00 = re . compile ( 'id="(.+?)"' ) . findall ( OooOo0o0Oo )
 IIiIi = re . compile ( 'name="(.+?)"' ) . findall ( OooOo0o0Oo )
 I1I1IIiiI1 = re . compile ( 'version="(.+?)"' ) . findall ( OooOo0o0Oo )
 if 91 - 91: o0oOOo0O0Ooo + O0 * ooOo * iIII * I1ii11iIi11i
 oooOOO0o0O0 = oOoo00 [ 0 ] if ( len ( oOoo00 ) > 0 ) else ''
 iiiI1IiI = IIiIi [ 0 ] if ( len ( IIiIi ) > 0 ) else ''
 OOO0o0 = I1I1IIiiI1 [ 0 ] if ( len ( I1I1IIiiI1 ) > 0 ) else ''
 if 83 - 83: OoooooooOO
 if os . path . exists ( oO0 ) :
  os . removedirs ( oO0 )
  if 52 - 52: o0oOOo0O0Ooo / OoOoOO00 % ooOo % OoO0O00 / iIII % o0oOOo0O0Ooo
  if 88 - 88: Oo / i11iIiiIii / iI1iiIiiII / i11iIiiIii * I1ii11iIi11i % oOoO0o00OO0
 if I11Ii111IIi != iIo00oo :
  try :
   os . rename ( O0O , O0Oo000ooO00 )
   if 43 - 43: OoOoOO00 * OoO0O00 % i1IIi * iI1iiIiiII + iIii1I11I1II1
  except :
   oOOoO0 . ok ( "NO GUISETTINGS!" , 'No guisettings.xml file has been found.' , 'Please exit Kodi and try again' , '' )
   return
   if 80 - 80: o0oOOo0O0Ooo . OOo00O0 . OoooooooOO
   if 63 - 63: oOO . Oo
 if video != 'fresh' :
  ii1I11iIiIII1 = xbmcgui . Dialog ( ) . yesno ( name , oooooOoo0ooo )
  if 66 - 66: I1IiiI
 if ii1I11iIiIII1 == 0 :
  return
  if 99 - 99: OoO0O00 % O0 . iIi1i1ii1 - I1ii11iIi11i . Oo0Ooo / OoOoOO00
  if 60 - 60: I1ii11iIi11i
  if 78 - 78: ooOo + II111iiii
  if 55 - 55: OoooooooOO
  if 90 - 90: I1IiiI
  if 4 - 4: Oo % oOO - Oo - o0oOOo0O0Ooo
  if 30 - 30: iIII
  if 34 - 34: ooOo - II111iiii - o0oOOo0O0Ooo + OOo00O0 + iIi1i1ii1
  if 70 - 70: OoooooooOO + OoO0O00 * Oo0Ooo
  if 20 - 20: i11iIiiIii - II111iiii - oOO % ooOo . oOO
  if 50 - 50: iIii1I11I1II1 + iIi1i1ii1 - oOoO0o00OO0 - OoooooooOO
  if 84 - 84: OoOoOO00 - oOoO0o00OO0
  if 80 - 80: i11iIiiIii % Oo - Oo0Ooo % Oo
  if 89 - 89: iI1iiIiiII * oOoO0o00OO0 + OoOoOO00 / i11iIiiIii
  if 68 - 68: OoooooooOO * oOoO0o00OO0
  if 86 - 86: o0oOOo0O0Ooo / OoOoOO00
  if 40 - 40: OOo00O0
  if 62 - 62: oOO / Oo
  if 74 - 74: OOo00O0 % iIi1i1ii1 / iIi1i1ii1 - iIii1I11I1II1 - II111iiii + Oo
  if 92 - 92: oOoO0o00OO0 % iIi1i1ii1
  if 18 - 18: oOO + iIi1i1ii1 / Oo / ooOo + iIii1I11I1II1 % iIII
 if video == 'fresh' :
  oOoOO00Ooo ( 'CB' )
  if 49 - 49: i1IIi % ooOo / Oo . I1ii11iIi11i - iIi1i1ii1
 iiiiI11ii = open ( iiiiiIIii , mode = 'w+' )
 if 12 - 12: i11iIiiIii + oOoO0o00OO0 - I1ii11iIi11i
 if I11Ii111IIi != iIo00oo :
  iiiiI11ii . write ( 'id="' + str ( oooOOO0o0O0 ) + '"\nname="' + iiiI1IiI + ' [COLOR=yellow](Partially installed)[/COLOR]"\nversion="' + OOO0o0 + '"\ngui="' + iIo00oo + '"' )
  if 27 - 27: OOo00O0
 else :
  iiiiI11ii . write ( 'id="' + str ( oooOOO0o0O0 ) + '"\nname="' + iiiI1IiI + '"\nversion="' + OOO0o0 + '"\ngui="' + iIo00oo + '"' )
 iiiiI11ii . close ( )
 if 22 - 22: OoOoOO00 / I1IiiI
 if 33 - 33: oOoO0o00OO0
 if video == 'libprofile' or video == 'library' or video == 'updatelibprofile' or video == 'updatelibrary' :
  try :
   shutil . copytree ( OooO0 , Ii1iIiII1ii1 , symlinks = False , ignore = shutil . ignore_patterns ( "Textures13.db" , "Addons16.db" , "Addons15.db" , "saltscache.db-wal" , "saltscache.db-shm" , "saltscache.db" , "onechannelcache.db" ) )
   if 37 - 37: OoOoOO00 % o0oOOo0O0Ooo * OoO0O00 / i11iIiiIii * II111iiii * OOo00O0
  except :
   OoO00o = xbmcgui . Dialog ( ) . yesno ( name , 'There was an error trying to backup some databases. Continuing may wipe your existing library. Do you wish to continue?' , nolabel = 'No, cancel' , yeslabel = 'Yes, overwrite' )
   if 70 - 70: oOO . i11iIiiIii % OoOoOO00 + ooOo
   if OoO00o == 0 :
    return
    if 95 - 95: I1ii11iIi11i
  i1i1iI1 = xbmc . translatePath ( os . path . join ( I1IIIii , 'Database.zip' ) )
  O0OOO000o0o ( Ii1iIiII1ii1 , i1i1iI1 )
  if 48 - 48: oOoO0o00OO0
 if OoO00o == 0 :
  return
  if 14 - 14: iIii1I11I1II1 / o0oOOo0O0Ooo * iIII
 time . sleep ( 1 )
 if 35 - 35: iIii1I11I1II1
 if 34 - 34: OoO0O00 % I1IiiI . o0oOOo0O0Ooo % OoO0O00 % OoO0O00
 iII11II = xbmc . translatePath ( os . path . join ( iiI1IiI , '..' , 'koditemp.zip' ) )
 time . sleep ( 2 )
 O0OoO000O0OO . create ( "Community Builds" , "Downloading " + description + " build." , '' , 'Please Wait' )
 i1i1i11iI11II = os . path . join ( oOoOooOo0o0 , description + '.zip' )
 if 59 - 59: I1IiiI % ooOo % iIii1I11I1II1 / iIi1i1ii1 * OOo00O0 * OoO0O00
 if not os . path . exists ( oOoOooOo0o0 ) :
  os . makedirs ( oOoOooOo0o0 )
  if 34 - 34: iIII
 downloader . download ( url , i1i1i11iI11II , O0OoO000O0OO )
 if 89 - 89: OOo00O0
 if 38 - 38: i1IIi - oOO
 if 14 - 14: OOo00O0 * iIII % i11iIiiIii . i11iIiiIii + ooOo / I1ii11iIi11i
 if 19 - 19: I1IiiI
 if 86 - 86: I1ii11iIi11i + OoOoOO00 * iIII + oOO
 if 23 - 23: OoO0O00 - ooOo * iIii1I11I1II1
 if 1 - 1: oOoO0o00OO0 - Oo0Ooo / i1IIi
 if 96 - 96: OoooooooOO % OOo00O0 - OoooooooOO % O0
 try :
  iiiiIiiiii1I = open ( IIIII , mode = 'r' )
  iIiI11I = iiiiIiiiii1I . read ( )
  iiiiIiiiii1I . close ( )
  if 33 - 33: ooOo + Oo0Ooo + iIi1i1ii1 * ooOo / o0oOOo0O0Ooo
 except :
  print "### No profiles detected, most likely a fresh wipe performed"
  if 78 - 78: iIII + oOoO0o00OO0 - o0oOOo0O0Ooo + OoO0O00 / iIii1I11I1II1
 O0OoO000O0OO . close ( )
 O0OoO000O0OO . create ( "Community Builds" , "Checking " , '' , 'Please Wait' )
 if 47 - 47: Oo
 if 20 - 20: iIi1i1ii1 % oOO - iIi1i1ii1 * OoooooooOO / I1ii11iIi11i
 if zipfile . is_zipfile ( i1i1i11iI11II ) :
  O0OoO000O0OO . update ( 0 , "" , "Extracting Zip Please Wait" )
  oOO00oO00O0OO ( i1i1i11iI11II , iiI1IiI , O0OoO000O0OO )
  time . sleep ( 1 )
  if 57 - 57: iIII % oOoO0o00OO0 * Oo % I1ii11iIi11i
 else :
  oOOoO0 . ok ( 'Not a valid zip file' , 'This file is not a valid zip file, please let the build author know on their support thread so they can amend the download path. It\'s most likely just a simple typo on their behalf.' )
  return
  if 65 - 65: i1IIi - OoooooooOO
  if 66 - 66: I1ii11iIi11i / i1IIi * I1IiiI - OoOoOO00 + ooOo
  if 74 - 74: OOo00O0 / iIi1i1ii1 / II111iiii - OOo00O0 / ooOo % oOoO0o00OO0
 O0OoO000O0OO . create ( "Restoring Dependencies" , "Checking " , '' , 'Please Wait' )
 O0OoO000O0OO . update ( 0 , "" , "Extracting Zip Please Wait" )
 if 19 - 19: iIII % OoooooooOO + OoooooooOO
 if O0oo0OO0 == 'true' :
  try :
   print "### Attempting to add back favourites ###"
   iiiiI11ii = open ( iIi1ii1I1 , mode = 'w+' )
   iiiiI11ii . write ( O000oOo0OO )
   iiiiI11ii . close ( )
   O0OoO000O0OO . update ( 0 , "" , "Copying Favourites" )
  except : print "### Failed to copy back favourites"
  if 7 - 7: i1IIi
 if I1i1iiI1 == 'true' :
  try :
   print "### Attempting to add back sources ###"
   iiiiI11ii = open ( o0 , mode = 'w+' )
   iiiiI11ii . write ( IiiI1iIiI )
   iiiiI11ii . close ( )
   O0OoO000O0OO . update ( 0 , "" , "Copying Sources" )
   if 91 - 91: OoOoOO00 - OoOoOO00 . iIII
  except :
   print "### Failed to copy back favourites"
   if 33 - 33: iIi1i1ii1 - iIii1I11I1II1 / iI1iiIiiII % O0
 time . sleep ( 1 )
 if os . path . exists ( Ii1iIiII1ii1 ) :
  shutil . rmtree ( Ii1iIiII1ii1 )
  if 80 - 80: iIII % OoooooooOO - iIII
  if 27 - 27: iIi1i1ii1 - o0oOOo0O0Ooo * I1ii11iIi11i - I1IiiI
  if 22 - 22: Oo0Ooo % OoooooooOO - Oo0Ooo - OOo00O0 . iI1iiIiiII
  if 100 - 100: II111iiii / iIi1i1ii1 / OOo00O0 - I1ii11iIi11i * iIii1I11I1II1
  if 7 - 7: i1IIi . iIII % i11iIiiIii * I1ii11iIi11i . oOoO0o00OO0 % I1ii11iIi11i
  if 35 - 35: I1IiiI
  if 48 - 48: OoooooooOO % OoooooooOO - OoO0O00 . OoOoOO00
  if 22 - 22: oOO . i11iIiiIii . OoooooooOO . i1IIi
  if 12 - 12: OoOoOO00 % Oo + ooOo . O0 % iIii1I11I1II1
  if 41 - 41: OoooooooOO
  if 13 - 13: oOoO0o00OO0 + iIi1i1ii1 - iIi1i1ii1 % ooOo / oOoO0o00OO0
 O0O0o0o0o = 'http://noobsandnerds.com/TI/Community_Builds/downloadcount.php?id=%s' % ( oooOOO0o0O0 )
 if not 'update' in video :
  oooOo0OOOoo0 ( O0O0o0o0o )
  if 4 - 4: I1IiiI + Oo - iIII + OOo00O0
  if 78 - 78: iI1iiIiiII
 if os . path . exists ( OOOO ) :
  II1II1IIII = open ( OOOO , mode = 'r' )
  OooOo0o0Oo = II1II1IIII . read ( )
  II1II1IIII . close ( )
  Iii1iIIiii1ii = re . compile ( 'version="[\s\S]*?"' ) . findall ( OooOo0o0Oo )
  i1Oo00 = Iii1iIIiii1ii [ 0 ] if ( len ( Iii1iIIiii1ii ) > 0 ) else ''
  II1iIi1IiIii = OooOo0o0Oo . replace ( i1Oo00 , 'version="' + OOO0o0 + '"' )
  iiiiI11ii = open ( OOOO , mode = 'w' )
  iiiiI11ii . write ( str ( II1iIi1IiIii ) )
  iiiiI11ii . close ( )
  if 29 - 29: II111iiii
 else :
  iiiiI11ii = open ( OOOO , mode = 'w+' )
  iiiiI11ii . write ( 'date="01011001"\nversion="' + OOO0o0 + '"' )
  iiiiI11ii . close ( )
  if 79 - 79: iIii1I11I1II1 - i11iIiiIii + oOO - II111iiii . iIii1I11I1II1
  if 84 - 84: Oo0Ooo % oOoO0o00OO0 * O0 * oOoO0o00OO0
 if IiiIII111iI == 'false' :
  os . remove ( i1i1i11iI11II )
  if 66 - 66: Oo / iIii1I11I1II1 - OoOoOO00 % O0 . oOO
  if 12 - 12: Oo0Ooo + I1IiiI
  if 37 - 37: i1IIi * i11iIiiIii
  if 95 - 95: i11iIiiIii % iIi1i1ii1 * Oo0Ooo + i1IIi . O0 + I1ii11iIi11i
  if 7 - 7: OoO0O00 * i11iIiiIii * iIii1I11I1II1 / Oo / iIi1i1ii1
  if 35 - 35: OOo00O0 * Oo
  if 65 - 65: II111iiii % i1IIi
 if 'prof' in video :
  try :
   III1II1iiI11 = open ( IIIII , mode = 'w+' )
   III1II1iiI11 . write ( iIiI11I )
   III1II1iiI11 . close ( )
  except : print "### Failed to write existing profile info back into profiles.xml"
  if 38 - 38: i1IIi / iIii1I11I1II1 + OOo00O0
  if 26 - 26: I1ii11iIi11i . iI1iiIiiII % o0oOOo0O0Ooo
 if video == 'library' or video == 'libprofile' or video == 'updatelibprofile' or video == 'updatelibrary' :
  oOO00oO00O0OO ( i1i1iI1 , OooO0 , O0OoO000O0OO )
  if 4 - 4: iIi1i1ii1
  if 80 - 80: Oo0Ooo . O0 % o0oOOo0O0Ooo . o0oOOo0O0Ooo
  if OoO00o != 1 :
   shutil . rmtree ( Ii1iIiII1ii1 )
 O0OoO000O0OO . close ( )
 if 52 - 52: OoO0O00 % i11iIiiIii . oOO % OoOoOO00 % OoooooooOO
 if 5 - 5: OoOoOO00 / O0 / i11iIiiIii
 if os . path . exists ( Oo0OoO00oOO0o ) :
  O0OOO0 ( description )
  if 88 - 88: II111iiii - OOo00O0 / OoooooooOO
  try :
   os . remove ( Oo0OoO00oOO0o )
   if 71 - 71: I1ii11iIi11i
  except :
   print "##' Failed to remove: " + Oo0OoO00oOO0o
   if 19 - 19: Oo0Ooo - OoO0O00 + i11iIiiIii / iIii1I11I1II1
  try :
   shutil . rmtree ( Oo0oOOo )
   if 1 - 1: iIII % i1IIi
  except :
   print "##' Failed to remove: " + Oo0oOOo
   if 41 - 41: OoO0O00 * OoO0O00 / OOo00O0 + I1ii11iIi11i . o0oOOo0O0Ooo
 else : print "### Community Builds - using an old build"
 if 84 - 84: i11iIiiIii + OoO0O00 * I1IiiI + I1ii11iIi11i / iI1iiIiiII
 if 80 - 80: I1ii11iIi11i
 if I11Ii111IIi != iIo00oo :
  print "### GUI SIZE DIFFERENT ATTEMPTING MERGE ###"
  ooOOO = os . path . join ( iiI1IiI , 'newbuild' )
  if 95 - 95: oOoO0o00OO0
  if not os . path . exists ( ooOOO ) :
   os . makedirs ( ooOOO )
   if 76 - 76: II111iiii - i1IIi . O0 * i11iIiiIii % o0oOOo0O0Ooo - OOo00O0
  os . makedirs ( oO0 )
  time . sleep ( 1 )
  II1I1iIIiIIii ( guisettingslink , video )
  time . sleep ( 1 )
  xbmc . executebuiltin ( 'UnloadSkin()' )
  time . sleep ( 1 )
  xbmc . executebuiltin ( 'ReloadSkin()' )
  time . sleep ( 1 )
  oOOoO0 . ok ( "Force Close Required" , "If you\'re seeing this message it means the force close was unsuccessful. Please close XBMC/Kodi via your operating system or pull the power." )
  if 30 - 30: iIi1i1ii1 % ooOo + ooOo * OoooooooOO - I1ii11iIi11i
 if I11Ii111IIi == iIo00oo :
  oOOoO0 . ok ( 'Successfully Updated' , 'Congratulations the following build:[COLOR=dodgerblue]' , description , '[/COLOR]has been successfully updated!' )
  if 69 - 69: I1ii11iIi11i + OoO0O00 / O0 + II111iiii / i11iIiiIii
  if 48 - 48: OoooooooOO / I1IiiI
def I1II11Ii11iI1 ( url ) :
 oO0Oooo = 0
 OoO00o = 0
 print "Restore Location: " + url
 if 16 - 16: OOo00O0 . O0 - iIi1i1ii1 * iIi1i1ii1
 o0OoOOo ( )
 if 80 - 80: iI1iiIiiII % I1ii11iIi11i
 if url == 'local' :
  I1I11I1i1i1II = xbmcgui . Dialog ( ) . browse ( 1 , 'Select the backup file you want to restore' , 'files' , '.zip' , False , False , I1IIIii )
  if I1I11I1i1i1II == '' :
   oO0Oooo = 1
   if 60 - 60: OoO0O00 % iIii1I11I1II1 . oOO * o0oOOo0O0Ooo % oOO - iIi1i1ii1
 if oO0Oooo == 1 :
  print "### No file selected, quitting restore process ###"
  return
  if 51 - 51: oOO * iIII * iIii1I11I1II1 / OoOoOO00 % iIII
 if url != 'local' :
  O0OoO000O0OO . create ( "Community Builds" , "Downloading build." , '' , 'Please Wait' )
  I1I11I1i1i1II = os . path . join ( oOoOooOo0o0 , IiiiiIi11 ( ) + '.zip' )
  if 36 - 36: I1ii11iIi11i * o0oOOo0O0Ooo + i11iIiiIii + OoooooooOO
  if not os . path . exists ( oOoOooOo0o0 ) :
   os . makedirs ( oOoOooOo0o0 )
   if 82 - 82: OoOoOO00 . OoOoOO00
  downloader . download ( url , I1I11I1i1i1II , O0OoO000O0OO )
  if 10 - 10: Oo0Ooo * I1ii11iIi11i . ooOo . OoooooooOO . Oo * I1ii11iIi11i
 if os . path . exists ( O0Oo000ooO00 ) :
  if os . path . exists ( O0O ) :
   os . remove ( O0Oo000ooO00 )
  else :
   os . rename ( O0Oo000ooO00 , O0O )
   if 80 - 80: iIi1i1ii1 + oOoO0o00OO0 . iIi1i1ii1 + Oo
 if os . path . exists ( O00o0OO ) :
  os . remove ( O00o0OO )
  if 85 - 85: i11iIiiIii . oOoO0o00OO0 + iI1iiIiiII / iI1iiIiiII
  if 43 - 43: iIII . OoooooooOO - II111iiii
 if not os . path . exists ( OOO00 ) :
  II1II1IIII = open ( OOO00 , mode = 'w+' )
  if 90 - 90: I1IiiI - iIii1I11I1II1 + I1ii11iIi11i * Oo * ooOo
 if os . path . exists ( oO0 ) :
  os . removedirs ( oO0 )
  if 19 - 19: iIi1i1ii1 * II111iiii % Oo0Ooo - i1IIi
  if 27 - 27: OoOoOO00 . O0 / I1ii11iIi11i . iIii1I11I1II1
 try :
  os . rename ( O0O , O0Oo000ooO00 )
  if 15 - 15: iI1iiIiiII + OoO0O00 % iIii1I11I1II1 - I1ii11iIi11i - i1IIi % o0oOOo0O0Ooo
 except :
  oOOoO0 . ok ( "NO GUISETTINGS!" , 'No guisettings.xml file has been found.' , 'Please exit XBMC and try again' , '' )
  return
  if 54 - 54: iIII - II111iiii . oOO + iI1iiIiiII
 ii1I11iIiIII1 = xbmcgui . Dialog ( ) . yesno ( I1i11i , oooooOoo0ooo , nolabel = 'Backup' , yeslabel = 'Install' )
 if ii1I11iIiIII1 == 0 :
  IIiii1I = xbmc . translatePath ( os . path . join ( I1IIIii , 'Community Builds' , 'My Builds' ) )
  if 76 - 76: iI1iiIiiII + OOo00O0 - iIII * iIii1I11I1II1 % i1IIi
  if not os . path . exists ( IIiii1I ) :
   os . makedirs ( IIiii1I )
   if 72 - 72: oOO + II111iiii . O0 - OOo00O0 / OoooooooOO . iIi1i1ii1
  o0OO00oo0O = Ii1I1i111 ( heading = "Enter a name for this backup" )
  if ( not o0OO00oo0O ) :
   return False , 0
   if 28 - 28: iIii1I11I1II1 . O0
  iIIi11i1i1i1I = urllib . quote_plus ( o0OO00oo0O )
  i1i1iI1 = xbmc . translatePath ( os . path . join ( IIiii1I , iIIi11i1i1i1I + '.zip' ) )
  oOOO00OOOoOO = [ I1IiI ]
  III = [ "xbmc.log" , "xbmc.old.log" , "kodi.log" , "kodi.old.log" , '.DS_Store' , '.setup_complete' , 'XBMCHelper.conf' , '.gitignore' ]
  i11Ii1iIiII = "Creating full backup of existing build"
  O0oOo00Ooo0o0 = "Archiving..."
  i1IiII1i1I = ""
  iI1ii1ii1I = "Please Wait"
  if 32 - 32: OoooooooOO
  i1II1iII ( iiI1IiI , i1i1iI1 , i11Ii1iIiII , O0oOo00Ooo0o0 , i1IiII1i1I , iI1ii1ii1I , oOOO00OOOoOO , III )
 iIi1I111 = xbmcgui . Dialog ( ) . yesno ( I1i11i , 'Would you like to keep your existing database files or overwrite? Overwriting will wipe any existing music or video library you may have scanned in.' , nolabel = 'Overwrite' , yeslabel = 'Keep Existing' )
 if iIi1I111 == 1 :
  if os . path . exists ( Ii1iIiII1ii1 ) :
   shutil . rmtree ( Ii1iIiII1ii1 )
   if 13 - 13: iI1iiIiiII - ooOo
  try :
   shutil . copytree ( OooO0 , Ii1iIiII1ii1 , symlinks = False , ignore = shutil . ignore_patterns ( "Textures13.db" , "Addons16.db" , "Addons15.db" , "saltscache.db-wal" , "saltscache.db-shm" , "saltscache.db" , "onechannelcache.db" ) )
   if 55 - 55: iIII % I1ii11iIi11i + O0 . o0oOOo0O0Ooo / iI1iiIiiII * OOo00O0
  except :
   OoO00o = xbmcgui . Dialog ( ) . yesno ( I1i11i , 'There was an error trying to backup some databases. Continuing may wipe your existing library. Do you wish to continue?' , nolabel = 'No, cancel' , yeslabel = 'Yes, overwrite' )
   if OoO00o == 1 : pass
   if OoO00o == 0 : oO0Oooo = 1 ; return
   if 63 - 63: iIi1i1ii1 - ooOo - OOo00O0 - oOO / ooOo + OoO0O00
  i1i1iI1 = xbmc . translatePath ( os . path . join ( I1IIIii , 'Database.zip' ) )
  O0OOO000o0o ( Ii1iIiII1ii1 , i1i1iI1 )
  if 94 - 94: iIII / I1IiiI . II111iiii
 if oO0Oooo == 1 :
  print "### Chose to exit restore function ###"
  return
  if 32 - 32: ooOo . Oo % Oo . OoOoOO00
 else :
  time . sleep ( 1 )
  OoOooO = open ( Ooo , mode = 'r' )
  I1I1i11iiiiI = OoOooO . read ( )
  OoOooO . close ( )
  if 37 - 37: Oo + O0 + Oo . OOo00O0 . o0oOOo0O0Ooo
  if 78 - 78: I1IiiI / oOoO0o00OO0 + o0oOOo0O0Ooo . Oo0Ooo / O0
  print "### Checking zip file structure ###"
  iIiiIIiiI = zipfile . ZipFile ( I1I11I1i1i1II )
  if 'xbmc.log' in iIiiIIiiI . namelist ( ) or 'kodi.log' in iIiiIIiiI . namelist ( ) or '.git' in iIiiIIiiI . namelist ( ) or '.svn' in iIiiIIiiI . namelist ( ) :
   print "### Whoever created this build has used completely the wrong backup method, lets try and fix it! ###"
   oOOoO0 . ok ( 'Fixing Bad Zip' , 'Whoever created this build has used the wrong backup method, please wait while we fix it - this could take some time! Click OK to proceed' )
   I1iii1 = zipfile . ZipFile ( I1I11I1i1i1II , 'r' )
   I1IIIi1ii1i = os . path . join ( oOoOooOo0o0 , 'fixed.zip' )
   iI1I1iii11i = zipfile . ZipFile ( I1IIIi1ii1i , 'w' )
   if 14 - 14: iI1iiIiiII + iI1iiIiiII * OoooooooOO * oOoO0o00OO0 + Oo0Ooo . I1IiiI
   O0OoO000O0OO . create ( "Fixing Build" , "Checking " , '' , 'Please Wait' )
   if 61 - 61: Oo . Oo
   for iiIiI11IiI1ii in I1iii1 . infolist ( ) :
    buffer = I1iii1 . read ( iiIiI11IiI1ii . filename )
    ii11III1IIii1i = str ( iiIiI11IiI1ii . filename )
    if 38 - 38: oOO - o0oOOo0O0Ooo - O0 + oOO % OoOoOO00 . o0oOOo0O0Ooo
    if ( iiIiI11IiI1ii . filename [ - 4 : ] != '.log' ) and not '.git' in ii11III1IIii1i and not '.svn' in ii11III1IIii1i :
     iI1I1iii11i . writestr ( iiIiI11IiI1ii , buffer )
     O0OoO000O0OO . update ( 0 , "Fixing..." , '[COLOR yellow]%s[/COLOR]' % iiIiI11IiI1ii . filename , 'Please Wait' )
     if 40 - 40: iIii1I11I1II1 * OoooooooOO * iIi1i1ii1 - iI1iiIiiII + i11iIiiIii
   O0OoO000O0OO . close ( )
   iI1I1iii11i . close ( )
   I1iii1 . close ( )
   I1I11I1i1i1II = I1IIIi1ii1i
   if 81 - 81: OoO0O00 * OoooooooOO / OOo00O0
  O0OoO000O0OO . create ( "Restoring Backup Build" , "Checking " , '' , 'Please Wait' )
  O0OoO000O0OO . update ( 0 , "" , "Extracting Zip Please Wait" )
  if 8 - 8: O0 * i1IIi - OoOoOO00 % I1IiiI / I1ii11iIi11i
  try :
   oOO00oO00O0OO ( I1I11I1i1i1II , iiI1IiI , O0OoO000O0OO )
  except :
   oOOoO0 . ok ( 'ERROR IN BUILD ZIP' , 'Please contact the build author, there are errors in this zip file that has caused the install process to fail. Most likely cause is it contains files with special characters in the name.' )
   return
   if 39 - 39: I1ii11iIi11i . ooOo * II111iiii + I1IiiI - iIii1I11I1II1
  time . sleep ( 1 )
  if 56 - 56: iIII - iI1iiIiiII + i11iIiiIii * OoO0O00 % I1IiiI
  if iIi1I111 == 1 :
   oOO00oO00O0OO ( i1i1iI1 , OooO0 , O0OoO000O0OO )
   if 37 - 37: iIii1I11I1II1 + iIII / iIi1i1ii1 . OoooooooOO
   if OoO00o != 1 :
    shutil . rmtree ( Ii1iIiII1ii1 )
    if 72 - 72: ooOo % oOO % Oo
  OO0oO0OoOooO0O = open ( Ooo , mode = 'w+' )
  OO0oO0OoOooO0O . write ( I1I1i11iiiiI )
  OO0oO0OoOooO0O . close ( )
  try :
   os . rename ( O0O , O00o0OO )
   if 7 - 7: Oo0Ooo - i11iIiiIii / ooOo / ooOo . i1IIi % oOoO0o00OO0
  except :
   print "NO GUISETTINGS DOWNLOADED"
   if 51 - 51: ooOo
  time . sleep ( 1 )
  II1II1IIII = open ( O0Oo000ooO00 , mode = 'r' )
  OooOo0o0Oo = II1II1IIII . read ( )
  II1II1IIII . close ( )
  iIIII1Iii11 = re . compile ( '<skinsettings>[\s\S]*?<\/skinsettings>' ) . findall ( OooOo0o0Oo )
  o0ooo = iIIII1Iii11 [ 0 ] if ( len ( iIIII1Iii11 ) > 0 ) else ''
  II1IIIi1i1I = re . compile ( '<skin default[\s\S]*?<\/skin>' ) . findall ( OooOo0o0Oo )
  o0oo00O = II1IIIi1i1I [ 0 ] if ( len ( II1IIIi1i1I ) > 0 ) else ''
  o0III11IiI = re . compile ( '<lookandfeel>[\s\S]*?<\/lookandfeel>' ) . findall ( OooOo0o0Oo )
  IIIIII1iI1II = o0III11IiI [ 0 ] if ( len ( o0III11IiI ) > 0 ) else ''
  if 23 - 23: i11iIiiIii * iIII * oOoO0o00OO0 % oOoO0o00OO0 - OoOoOO00 + II111iiii
  try :
   oo00ooooOOo00 = open ( O00o0OO , mode = 'r' )
   ii1iOO00Oooo000 = oo00ooooOOo00 . read ( )
   oo00ooooOOo00 . close ( )
   O00 = re . compile ( '<skinsettings>[\s\S]*?<\/skinsettings>' ) . findall ( ii1iOO00Oooo000 )
   O0OIIII1i = O00 [ 0 ] if ( len ( O00 ) > 0 ) else ''
   oO0o00 = re . compile ( '<skin default[\s\S]*?<\/skin>' ) . findall ( ii1iOO00Oooo000 )
   i1I1Iiii = oO0o00 [ 0 ] if ( len ( oO0o00 ) > 0 ) else ''
   Oo0OOOO0oOoo0 = re . compile ( '<lookandfeel>[\s\S]*?<\/lookandfeel>' ) . findall ( ii1iOO00Oooo000 )
   I1iIIIiiii = Oo0OOOO0oOoo0 [ 0 ] if ( len ( Oo0OOOO0oOoo0 ) > 0 ) else ''
   II1iIi1IiIii = OooOo0o0Oo . replace ( o0ooo , O0OIIII1i ) . replace ( IIIIII1iI1II , I1iIIIiiii ) . replace ( o0oo00O , i1I1Iiii )
   iiiiI11ii = open ( O0Oo000ooO00 , mode = 'w+' )
   iiiiI11ii . write ( str ( II1iIi1IiIii ) )
   iiiiI11ii . close ( )
   if 91 - 91: OoooooooOO + iIi1i1ii1 / II111iiii * OOo00O0 + o0oOOo0O0Ooo / Oo0Ooo
  except :
   print "NO GUISETTINGS DOWNLOADED"
   if 7 - 7: oOoO0o00OO0 / i11iIiiIii - iI1iiIiiII % OOo00O0
  if os . path . exists ( O0O ) :
   os . remove ( O0O )
   if 67 - 67: iIii1I11I1II1 - OoOoOO00
  os . rename ( O0Oo000ooO00 , O0O )
  try :
   os . remove ( O00o0OO )
   if 51 - 51: oOoO0o00OO0 * I1ii11iIi11i % I1ii11iIi11i + o0oOOo0O0Ooo
  except :
   pass
   if 16 - 16: O0 % I1IiiI * iIii1I11I1II1 - II111iiii + iIii1I11I1II1 + Oo0Ooo
  os . makedirs ( oO0 )
  time . sleep ( 1 )
  iI1i1iI1iI ( )
  if 4 - 4: oOoO0o00OO0
  if 60 - 60: II111iiii + iIi1i1ii1 / ooOo % OoooooooOO - i1IIi
  if 57 - 57: oOO
  if 99 - 99: Oo0Ooo + iIi1i1ii1 % oOO - o0oOOo0O0Ooo
  if 52 - 52: I1ii11iIi11i
  if 93 - 93: OOo00O0 . i11iIiiIii
  if 24 - 24: Oo . OoO0O00 + iIi1i1ii1 . ooOo - I1ii11iIi11i % OOo00O0
  if 49 - 49: O0 . Oo0Ooo / iI1iiIiiII
  if 29 - 29: I1ii11iIi11i / ooOo * O0 - i11iIiiIii - OoO0O00 + iI1iiIiiII
  if 86 - 86: I1IiiI / I1ii11iIi11i * iI1iiIiiII % i11iIiiIii
  if 20 - 20: OOo00O0 . OoooooooOO + OOo00O0 + oOO * I1ii11iIi11i
  if 44 - 44: i11iIiiIii
  if 69 - 69: Oo * O0 + i11iIiiIii
  if 65 - 65: O0 / OOo00O0 . i1IIi * OOo00O0 / iIii1I11I1II1 - ooOo
  if 93 - 93: OoOoOO00 % i11iIiiIii - iI1iiIiiII % OoO0O00
  if 55 - 55: o0oOOo0O0Ooo . I1ii11iIi11i
  if 63 - 63: ooOo
  if 79 - 79: I1ii11iIi11i - ooOo - o0oOOo0O0Ooo . Oo
  if 65 - 65: i11iIiiIii . OoO0O00 % OOo00O0 + iIII - i11iIiiIii
def Oo00o0o0O ( ) :
 o0OoOOo ( )
 oo00O0OO0oo0O = xbmcgui . Dialog ( ) . browse ( 1 , 'Select the guisettings zip file you want to restore' , 'files' , '.zip' , False , False , I1IIIii )
 if 1 - 1: Oo0Ooo * O0 . I1IiiI + oOO / OoOoOO00 + oOoO0o00OO0
 if oo00O0OO0oo0O == '' :
  return
  if 68 - 68: II111iiii
 else :
  O0ooO = 1
  I1I111IIIi1 ( oo00O0OO0oo0O , O0ooO )
  if 61 - 61: Oo . I1ii11iIi11i * ooOo / iIi1i1ii1 - OoO0O00
  if 18 - 18: iIi1i1ii1
def I111i1i ( url , name ) :
 ii1I11iIiIII1 = xbmcgui . Dialog ( ) . yesno ( 'Full Wipe And New Install' , 'This is a great option for first time install or if you\'re encountering any issues with your device. This will wipe all your Kodi settings, do you wish to continue?' , nolabel = 'Cancel' , yeslabel = 'Accept' )
 if ii1I11iIiIII1 == 0 :
  return
  if 14 - 14: II111iiii + OOo00O0 + iI1iiIiiII / OOo00O0 . iIii1I11I1II1
 elif ii1I11iIiIII1 == 1 :
  o0o0oO00O0O = '/storage/.restore/'
  O0Oo0 = os . path . join ( o0o0oO00O0O , '20141128094249.tar' )
  if not os . path . exists ( o0o0oO00O0O ) :
   try :
    os . makedirs ( o0o0oO00O0O )
   except :
    pass
  downloader . download ( url , O0Oo0 )
  time . sleep ( 2 )
  if 22 - 22: OOo00O0
  O0O0o0o0o = 'http://noobsandnerds.com/TI/Community_Builds/downloadcount.php?id=%s' % ( name )
  try :
   oooOo0OOOoo0 ( O0O0o0o0o )
  except :
   pass
   if 48 - 48: I1ii11iIi11i . I1IiiI
  oOOoO0 . ok ( "Download Complete - Press OK To Reboot" , 'Once you press OK your device will attempt to reboot, if it hasn\'t rebooted within 30 seconds please pull the power to manually shutdown. When booting you may see lines of text, don\'t worry this is normal update behaviour!' )
  xbmc . executebuiltin ( 'Reboot' )
  if 73 - 73: O0 . iIi1i1ii1 - OoooooooOO % oOoO0o00OO0 % i1IIi
  if 14 - 14: iIi1i1ii1 + iI1iiIiiII * Oo0Ooo
def iI11iI ( ) :
 oO0Oooo = 0
 ii1I11iIiIII1 = xbmcgui . Dialog ( ) . yesno ( 'Full Wipe And New Install' , 'This is a great option if you\'re encountering any issues with your device. This will wipe all your Kodi settings and restore with whatever is in the backup, do you wish to continue?' , nolabel = 'Cancel' , yeslabel = 'Accept' )
 if ii1I11iIiIII1 == 0 :
  return
  if 98 - 98: iIII * OOo00O0 . OoooooooOO . O0
 elif ii1I11iIiIII1 == 1 :
  I1I11I1i1i1II = xbmcgui . Dialog ( ) . browse ( 1 , 'Select the backup file you want to restore' , 'files' , '.tar' , False , False , oO0Oo )
  if I1I11I1i1i1II == '' :
   oO0Oooo = 1
   if 89 - 89: OOo00O0 / O0 % OoooooooOO - O0 . OoO0O00
  if oO0Oooo == 1 :
   print "### No file selected, quitting restore process ###"
   return
  O0Oo0 = os . path . join ( oOOoo0Oo , '20141128094249.tar' )
  if not os . path . exists ( oOOoo0Oo ) :
   try :
    os . makedirs ( oOOoo0Oo )
   except :
    pass
  O0OoO000O0OO . create ( 'Copying File To Restore Folder' , '' , 'Please wait...' )
  shutil . copyfile ( I1I11I1i1i1II , O0Oo0 )
  xbmc . executebuiltin ( 'Reboot' )
  if 32 - 32: oOO
  if 26 - 26: O0 * iI1iiIiiII - I1IiiI - OOo00O0 / iIii1I11I1II1
def oO0Ooo00O ( ) :
 IiIii1ii ( )
 if Oo0o0Oo0O ( ) :
  IIii ( '' , '[COLOR=dodgerblue]Restore a locally stored OpenELEC Backup[/COLOR]' , '' , 'restore_local_OE' , 'Restore.png' , '' , '' , 'Restore A Full OE System Backup' )
  if 74 - 74: o0oOOo0O0Ooo % OoOoOO00 . OOo00O0 % iIi1i1ii1 . O0 % II111iiii
 IIii ( '' , '[COLOR=dodgerblue]Restore A Locally stored build[/COLOR]' , 'local' , 'restore_local_CB' , 'Restore.png' , '' , '' , 'Restore A Full System Backup' )
 IIii ( '' , '[COLOR=dodgerblue]Restore Local guisettings file[/COLOR]' , 'url' , 'LocalGUIDialog' , 'Restore.png' , '' , '' , 'Back Up Your Full System' )
 if 5 - 5: ooOo - OoooooooOO / OoOoOO00
 if os . path . exists ( os . path . join ( I1IIIii , 'addons.zip' ) ) :
  IIii ( '' , 'Restore Your Addons' , 'addons' , 'restore_zip' , 'Restore.png' , '' , '' , 'Restore Your Addons' )
  if 30 - 30: oOoO0o00OO0 % o0oOOo0O0Ooo + i1IIi * OoooooooOO * OoO0O00 - II111iiii
 if os . path . exists ( os . path . join ( I1IIIii , 'addon_data.zip' ) ) :
  IIii ( '' , 'Restore Your Addon UserData' , 'addon_data' , 'restore_zip' , 'Restore.png' , '' , '' , 'Restore Your Addon UserData' )
  if 55 - 55: OoO0O00
 if os . path . exists ( os . path . join ( I1IIIii , 'guisettings.xml' ) ) :
  IIii ( '' , 'Restore Guisettings.xml' , O0O , 'resore_backup' , 'Restore.png' , '' , '' , 'Restore Your guisettings.xml' )
  if 20 - 20: oOO * iIi1i1ii1 * o0oOOo0O0Ooo - oOO
 if os . path . exists ( os . path . join ( I1IIIii , 'favourites.xml' ) ) :
  IIii ( '' , 'Restore Favourites.xml' , iIi1ii1I1 , 'resore_backup' , 'Restore.png' , '' , '' , 'Restore Your favourites.xml' )
  if 32 - 32: iI1iiIiiII * ooOo
 if os . path . exists ( os . path . join ( I1IIIii , 'sources.xml' ) ) :
  IIii ( '' , 'Restore Source.xml' , o0 , 'resore_backup' , 'Restore.png' , '' , '' , 'Restore Your sources.xml' )
  if 85 - 85: i11iIiiIii . OoO0O00 + OoO0O00
 if os . path . exists ( os . path . join ( I1IIIii , 'advancedsettings.xml' ) ) :
  IIii ( '' , 'Restore Advancedsettings.xml' , I11II1i , 'resore_backup' , 'Restore.png' , '' , '' , 'Restore Your advancedsettings.xml' )
  if 28 - 28: Oo0Ooo
 if os . path . exists ( os . path . join ( I1IIIii , 'keyboard.xml' ) ) :
  IIii ( '' , 'Restore Advancedsettings.xml' , IIiiiiiiIi1I1 , 'resore_backup' , 'Restore.png' , '' , '' , 'Restore Your keyboard.xml' )
  if 62 - 62: Oo0Ooo + OoooooooOO / OOo00O0
 if os . path . exists ( os . path . join ( I1IIIii , 'RssFeeds.xml' ) ) :
  IIii ( '' , 'Restore RssFeeds.xml' , ooooooO0oo , 'resore_backup' , 'Restore.png' , '' , '' , 'Restore Your RssFeeds.xml' )
  if 60 - 60: iI1iiIiiII / OoOoOO00 . oOoO0o00OO0 % Oo
  if 61 - 61: O0 . iI1iiIiiII . O0 * i11iIiiIii * II111iiii / iIi1i1ii1
def ooo0Oo000o ( url ) :
 o0OoOOo ( )
 if 'addons' in url :
  iiiI1iiI11iii = xbmc . translatePath ( os . path . join ( I1IIIii , 'addons.zip' ) )
  o0O0oOOoo0O0 = OO0o
  if 71 - 71: I1ii11iIi11i + oOoO0o00OO0 * Oo0Ooo - i1IIi . O0 % i11iIiiIii
 else :
  iiiI1iiI11iii = xbmc . translatePath ( os . path . join ( I1IIIii , 'addon_data.zip' ) )
  o0O0oOOoo0O0 = ooOoOoo0O
  if 40 - 40: oOO - i11iIiiIii % I1ii11iIi11i % I1IiiI . iIII * OoO0O00
 if 'Backup' in I1i11i :
  O0i1I11I ( )
  O0OoO000O0OO . create ( "Creating Backup" , "Backing Up" , '' , 'Please Wait' )
  II1i = zipfile . ZipFile ( iiiI1iiI11iii , 'w' , zipfile . ZIP_DEFLATED )
  o0OO00oo = len ( o0O0oOOoo0O0 )
  i1i1IiIiIi1Ii = [ ]
  oO0ooOO = [ ]
  for oo0o0 , oO0ooOoO , ooO0000o00O in os . walk ( o0O0oOOoo0O0 ) :
   for file in ooO0000o00O :
    oO0ooOO . append ( file )
  IiiIiI = len ( oO0ooOO )
  for oo0o0 , oO0ooOoO , ooO0000o00O in os . walk ( o0O0oOOoo0O0 ) :
   for file in ooO0000o00O :
    i1i1IiIiIi1Ii . append ( file )
    o00oo0 = len ( i1i1IiIiIi1Ii ) / float ( IiiIiI ) * 100
    O0OoO000O0OO . update ( int ( o00oo0 ) , "Backing Up" , '[COLOR yellow]%s[/COLOR]' % file , 'Please Wait' )
    Oo0oOooOoOo = os . path . join ( oo0o0 , file )
    if not 'temp' in oO0ooOoO :
     if not I1IiI in oO0ooOoO :
      import time
      I1iiIII = '01/01/1980'
      iIi1I1 = time . strftime ( '%d/%m/%Y' , time . gmtime ( os . path . getmtime ( Oo0oOooOoOo ) ) )
      if iIi1I1 > I1iiIII :
       II1i . write ( Oo0oOooOoOo , Oo0oOooOoOo [ o0OO00oo : ] )
  II1i . close ( )
  O0OoO000O0OO . close ( )
  oOOoO0 . ok ( "Backup Complete" , "You Are Now Backed Up" , '' , '' )
  if 51 - 51: O0 % ooOo - oOO * I1IiiI * ooOo
 else :
  O0OoO000O0OO . create ( "Extracting Zip" , "Checking " , '' , 'Please Wait' )
  O0OoO000O0OO . update ( 0 , "" , "Extracting Zip Please Wait" )
  oOO00oO00O0OO ( iiiI1iiI11iii , o0O0oOOoo0O0 , O0OoO000O0OO )
  time . sleep ( 1 )
  xbmc . executebuiltin ( 'UpdateLocalAddons ' )
  xbmc . executebuiltin ( "UpdateAddonRepos" )
  if 90 - 90: iI1iiIiiII + Oo0Ooo / iIii1I11I1II1 - O0 + oOO . I1ii11iIi11i
  if 'Backup' in I1i11i :
   oOOoO0 . ok ( "Install Complete" , 'Kodi will now close. Just re-open Kodi and wait for all the updates to complete.' )
   iI1i1iI1iI ( )
   if 58 - 58: OoO0O00 + OOo00O0 * o0oOOo0O0Ooo . oOoO0o00OO0
  else :
   oOOoO0 . ok ( "SUCCESS!" , "You Are Now Restored" , '' , '' )
   if 48 - 48: Oo
   if 25 - 25: Oo / oOO % Oo
def o0OooOO0 ( url ) :
 xbmc . executebuiltin ( 'RunAddon(' + url + ')' )
 if 16 - 16: ooOo / OOo00O0
 if 8 - 8: II111iiii + iIII
def i1I1 ( title ) :
 iiii11i1 = ''
 oo0OooO = xbmc . Keyboard ( iiii11i1 , title )
 oo0OooO . doModal ( )
 if oo0OooO . isConfirmed ( ) :
  iiii11i1 = oo0OooO . getText ( ) . replace ( ' ' , '%20' )
  if iiii11i1 == None :
   return False
 return iiii11i1
 if 31 - 31: oOoO0o00OO0 . i11iIiiIii . OoO0O00 * Oo0Ooo % iI1iiIiiII . o0oOOo0O0Ooo
 if 92 - 92: OoooooooOO / O0 * i1IIi + iIii1I11I1II1
def o00O00O0O0 ( url ) :
 o0OO00oo0O = Ii1I1i111 ( heading = "Search for add-ons" )
 if 87 - 87: I1ii11iIi11i
 if ( not o0OO00oo0O ) : return False , 0
 if 60 - 60: i11iIiiIii / i1IIi * Oo
 if 89 - 89: iIii1I11I1II1 * o0oOOo0O0Ooo + OoOoOO00 . i11iIiiIii + I1ii11iIi11i
 iIIi11i1i1i1I = urllib . quote_plus ( o0OO00oo0O )
 url += iIIi11i1i1i1I
 iiIIIi1iIi ( url )
 if 1 - 1: I1IiiI . oOoO0o00OO0 . I1ii11iIi11i
 if 19 - 19: O0 * oOoO0o00OO0 % OoooooooOO
def II111II1IiI ( url ) :
 o0OO00oo0O = Ii1I1i111 ( heading = "Search for content" )
 if 56 - 56: I1ii11iIi11i
 if 32 - 32: OoOoOO00 % O0 % i11iIiiIii - oOO . I1IiiI
 if ( not o0OO00oo0O ) : return False , 0
 if 24 - 24: ooOo % o0oOOo0O0Ooo / iIi1i1ii1 + o0oOOo0O0Ooo
 if 59 - 59: II111iiii % I1IiiI * O0 . OoooooooOO - OoooooooOO % O0
 iIIi11i1i1i1I = urllib . quote_plus ( o0OO00oo0O )
 url += iIIi11i1i1i1I
 oO00oOoo00o0 ( url )
 if 56 - 56: ooOo - i1IIi * OoooooooOO - II111iiii
 if 28 - 28: i1IIi / oOoO0o00OO0 . o0oOOo0O0Ooo
def iIIiiiIiiii11 ( url ) :
 ii1111iII = 'http://noobsandnerds.com/TI/Community_Builds/community_builds.php?id=%s' % ( url )
 iiiiI = oooOo0OOOoo0 ( ii1111iII ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 O00o0 = re . compile ( 'name="(.+?)"' ) . findall ( iiiiI )
 IiIi1Ii = re . compile ( 'author="(.+?)"' ) . findall ( iiiiI )
 o000O0O = re . compile ( 'version="(.+?)"' ) . findall ( iiiiI )
 I1i11i = O00o0 [ 0 ] if ( len ( O00o0 ) > 0 ) else ''
 I1111ii11IIII = IiIi1Ii [ 0 ] if ( len ( IiIi1Ii ) > 0 ) else ''
 iIIiIiI1I1 = o000O0O [ 0 ] if ( len ( o000O0O ) > 0 ) else ''
 oOOoO0 . ok ( I1i11i , 'Author: [COLOR=dodgerblue]' + I1111ii11IIII + '[/COLOR]      Latest Version: [COLOR=dodgerblue]' + iIIiIiI1I1 + '[/COLOR]' , '' , 'Click OK to view the build page.' )
 try :
  Ii1Ii1 ( url + '&visibility=homepage' , url )
 except :
  return
  print "### Could not find build No. " + url
  oOOoO0 . ok ( 'Build Not Found' , 'Sorry we couldn\'t find the build, it may be it\'s marked as private. Please try manually searching via the Community Builds section' )
  if 22 - 22: oOoO0o00OO0
  if 50 - 50: iIII . oOoO0o00OO0 / iI1iiIiiII . O0 . i11iIiiIii + II111iiii
def II1i1II1iIi ( url ) :
 oOOoO0 . ok ( "This build is not complete" , 'The guisettings.xml file was not copied over during the last install process. Click OK to go to the build page and complete Install Step 2 (guisettings fix).' )
 if 8 - 8: OoooooooOO
 try :
  Ii1Ii1 ( url + '&visibility=homepage' , url )
  if 60 - 60: Oo * OoOoOO00 % Oo0Ooo
 except :
  return
  print "### Could not find build No. " + url
  oOOoO0 . ok ( 'Build Not Found' , 'Sorry we couldn\'t find the build, it may be it\'s marked as private. Please try manually searching via the Community Builds section' )
  if 61 - 61: oOoO0o00OO0 . iIii1I11I1II1 - II111iiii % oOoO0o00OO0 * O0 % Oo0Ooo
  if 17 - 17: i1IIi % OoOoOO00 . Oo0Ooo - I1ii11iIi11i
def I1I11I11iIII ( ) :
 ii1111iII = 'http://noobsandnerds.com/TI/login/login_details.php?user=%s&pass=%s' % ( oo00 , o00 )
 iiiiI = oooOo0OOOoo0 ( ii1111iII ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 iiIII11IiiI = re . compile ( 'posts="(.+?)"' ) . findall ( iiiiI )
 IIiii1 = re . compile ( 'messages="(.+?)"' ) . findall ( iiiiI )
 iiIII1ii1 = re . compile ( 'unread="(.+?)"' ) . findall ( iiiiI )
 OOO00O00ooo0o = re . compile ( 'email="(.+?)"' ) . findall ( iiiiI )
 OoOoo = IIiii1 [ 0 ] if ( len ( IIiii1 ) > 0 ) else ''
 O0oOoOooo00oo = iiIII1ii1 [ 0 ] if ( len ( iiIII1ii1 ) > 0 ) else ''
 OOO0OO00 = OOO00O00ooo0o [ 0 ] if ( len ( OOO00O00ooo0o ) > 0 ) else ''
 oOO00 = iiIII11IiiI [ 0 ] if ( len ( iiIII11IiiI ) > 0 ) else ''
 oOOoO0 . ok ( '[COLOR=orange]noobs[/COLOR][COLOR=dodgerblue]and[/COLOR][COLOR=orange]nerds[/COLOR]' , 'Username:  ' + oo00 , 'Email: ' + OOO0OO00 , 'Unread Messages: ' + O0oOoOooo00oo + '/' + OoOoo + '[CR]Posts: ' + oOO00 )
 if 27 - 27: ooOo * Oo0Ooo * Oo0Ooo / iIII + Oo0Ooo
 if 94 - 94: oOO - i1IIi . O0 / I1IiiI
def i1iI1IIi1I ( url , type ) :
 if type == 'communitybuilds' :
  II111iiI1Ii1 = 'grab_builds'
  if url . endswith ( "visibility=premium" ) :
   IIii ( 'folder' , '[COLOR=yellow]Manual Search[/COLOR]' , '&reseller=' + urllib . quote ( IIIi1I1IIii1II ) + '&token=' + O0ii1ii1ii + '&visibility=premium' , 'manual_search' , 'Manual_Search.png' , '' , '' , '' )
  if url . endswith ( "visibility=reseller_private" ) :
   IIii ( 'folder' , '[COLOR=yellow]Manual Search[/COLOR]' , '&reseller=' + urllib . quote ( IIIi1I1IIii1II ) + '&token=' + O0ii1ii1ii + '&visibility=reseller_private' , 'manual_search' , 'Manual_Search.png' , '' , '' , '' )
  if url . endswith ( "visibility=public" ) :
   IIii ( 'folder' , '[COLOR=yellow]Manual Search[/COLOR]' , '&visibility=public' , 'manual_search' , 'Manual_Search.png' , '' , '' , '' )
  if url . endswith ( "visibility=private" ) :
   IIii ( 'folder' , '[COLOR=yellow]Manual Search[/COLOR]' , '&visibility=private' , 'manual_search' , 'Manual_Search.png' , '' , '' , '' )
 if type == 'tutorials' :
  II111iiI1Ii1 = 'grab_tutorials'
 if type == 'hardware' :
  II111iiI1Ii1 = 'grab_hardware'
 if type == 'addons' :
  II111iiI1Ii1 = 'grab_addons'
  IIii ( 'folder' , '[COLOR=dodgerblue]Sort by Most Popular[/COLOR]' , str ( url ) + '&sortx=downloads&orderx=DESC' , II111iiI1Ii1 , 'Popular.png' , '' , '' , '' )
 if type == 'hardware' :
  IIii ( 'folder' , '[COLOR=lime]Filter Results[/COLOR]' , url , 'hardware_filter_menu' , 'Filter.png' , '' , '' , '' )
 if type != 'addons' :
  IIii ( 'folder' , '[COLOR=dodgerblue]Sort by Most Popular[/COLOR]' , str ( url ) + '&sortx=downloadcount&orderx=DESC' , II111iiI1Ii1 , 'Popular.png' , '' , '' , '' )
 if type == 'tutorials' or type == 'hardware' :
  IIii ( 'folder' , '[COLOR=dodgerblue]Sort by Newest[/COLOR]' , str ( url ) + '&sortx=Added&orderx=DESC' , II111iiI1Ii1 , 'Latest.png' , '' , '' , '' )
 else :
  IIii ( 'folder' , '[COLOR=dodgerblue]Sort by Newest[/COLOR]' , str ( url ) + '&sortx=created&orderx=DESC' , II111iiI1Ii1 , 'Latest.png' , '' , '' , '' )
  IIii ( 'folder' , '[COLOR=dodgerblue]Sort by Recently Updated[/COLOR]' , str ( url ) + '&sortx=updated&orderx=DESC' , II111iiI1Ii1 , 'Recently_Updated.png' , '' , '' , '' )
 IIii ( 'folder' , '[COLOR=dodgerblue]Sort by A-Z[/COLOR]' , str ( url ) + '&sortx=name&orderx=ASC' , II111iiI1Ii1 , 'AtoZ.png' , '' , '' , '' )
 IIii ( 'folder' , '[COLOR=dodgerblue]Sort by Z-A[/COLOR]' , str ( url ) + '&sortx=name&orderx=DESC' , II111iiI1Ii1 , 'ZtoA.png' , '' , '' , '' )
 if type == 'public_CB' :
  IIii ( 'folder' , '[COLOR=dodgerblue]Sort by Genre[/COLOR]' , url , 'genres' , 'Search_Genre.png' , '' , '' , '' )
  IIii ( 'folder' , '[COLOR=dodgerblue]Sort by Country/Language[/COLOR]' , url , 'countries' , 'Search_Country.png' , '' , '' , '' )
  if 58 - 58: OoooooooOO * i1IIi * OoOoOO00
  if 99 - 99: Oo0Ooo
def OO0o0 ( ) :
 IIIiI1i1 ( 'Speed Test Instructions' , '[COLOR=blue][B]What file should I use: [/B][/COLOR][CR]This function will download a file and will work out your speed based on how long it took to download. You will then be notified of '
 'what quality streams you can expect to stream without buffering. You can choose to download a 10MB, 16MB, 32MB, 64MB or 128MB file to use with the test. Using the larger files will give you a better '
 'indication of how reliable your speeds are but obviously if you have a limited amount of bandwidth allowance you may want to opt for a smaller file.'
 '[CR][CR][COLOR=blue][B]How accurate is this speed test:[/B][/COLOR][CR]Not very accurate at all! As this test is based on downloading a file from a server it\'s reliant on the server not having a go-slow day '
 'but the servers used should be pretty reliable. The 10MB file is hosted on a different server to the others so if you\'re not getting the results expected please try another file. If you have a fast fiber '
 'connection the chances are your speed will show as considerably slower than your real download speed due to the server not being able to send the file as fast as your download speed allows. Essentially the '
 'test results will be limited by the speed of the server but you will at least be able to see if it\'s your connection that\'s causing buffering or if it\'s the host you\'re trying to stream from'
 '[CR][CR][COLOR=blue][B]What is the differnce between Live Streams and Online Video:[/COLOR][/B][CR]When you run the test you\'ll see results based on your speeds and these let you know the quality you should expect to '
 'be able stream with your connection. Live Streams as the title suggests are like traditional TV channels, they are being streamed live so for example if you wanted to watch CNN this would fall into this category. '
 'Online Videos relates to movies, tv shows, youtube clips etc. Basically anything that isn\'t live - if you\'re new to the world of streaming then think of it as On Demand content, this is content that\'s been recorded and stored on the web.'
 '[CR][CR][COLOR=blue][B]Why am I still getting buffering:[/COLOR][/B][CR]The results you get from this test are strictly based on your download speed, there are many other factors that can cause buffering and contrary to popular belief '
 'having a massively fast internet connection will not make any difference to your buffering issues if the server you\'re trying to get the content from is unable to send it fast enough. This can often happen and is usually '
 'down to heavy traffic (too many users accessing the same server). A 10 Mb/s connection should be plenty fast enough for almost all content as it\'s very rare a server can send it any quicker than that.'
 '[CR][CR][COLOR=blue][B]What\'s the difference between MB/s and Mb/s:[/COLOR][/B][CR]A lot of people think the speed they see advertised by their ISP is Megabytes (MB/S) per second - this is not true. Speeds are usually shown as Mb/s '
 'which is Megabit per second - there are 8 of these to a megabyte so if you want to work out how many megabytes per second you\'re getting you need to divide the speed by 8. It may sound sneaky but really it\'s just the unit that has always been used.'
 '[CR][CR]A direct link to the buffering thread explaining what you can do to improve your viewing experience can be found at [COLOR=yellow]http://bit.ly/bufferingfix[/COLOR]'
 '[CR][CR]Thank you, [COLOR=orange]noobs[/COLOR][COLOR=dodgerblue]and[/COLOR][COLOR=orange]nerds[/COLOR] Team.' )
 if 96 - 96: i1IIi - iIi1i1ii1 * I1IiiI % I1IiiI
def III11i ( ) :
 IIii ( '' , '[COLOR=blue]Instructions - Read me first[/COLOR]' , 'none' , 'speed_instructions' , 'howto.png' , '' , '' , '' )
 IIii ( '' , 'Download 16MB file   - [COLOR=lime]Server 1[/COLOR]' , 'https://totalrevolution.googlecode.com/svn/trunk/download%20files/16MB.txt' , 'runtest' , 'Download16.png' , '' , '' , '' )
 IIii ( '' , 'Download 32MB file   - [COLOR=lime]Server 1[/COLOR]' , 'https://totalrevolution.googlecode.com/svn/trunk/download%20files/32MB.txt' , 'runtest' , 'Download32.png' , '' , '' , '' )
 IIii ( '' , 'Download 64MB file   - [COLOR=lime]Server 1[/COLOR]' , 'https://totalrevolution.googlecode.com/svn/trunk/download%20files/64MB.txt' , 'runtest' , 'Download64.png' , '' , '' , '' )
 IIii ( '' , 'Download 128MB file - [COLOR=lime]Server 1[/COLOR]' , 'https://totalrevolution.googlecode.com/svn/trunk/download%20files/128MB.txt' , 'runtest' , 'Download128.png' , '' , '' , '' )
 IIii ( '' , 'Download 10MB file   - [COLOR=yellow]Server 2[/COLOR]' , 'http://www.wswd.net/testdownloadfiles/10MB.zip' , 'runtest' , 'Download10.png' , '' , '' , '' )
 if 54 - 54: iIi1i1ii1 . iIi1i1ii1 % iIii1I11I1II1 . o0oOOo0O0Ooo + O0
 if 94 - 94: Oo0Ooo . oOO
def IIIiI1i1 ( heading , anounce ) :
 class I11i1I1iiI1iI111 ( ) :
  WINDOW = 10147
  CONTROL_LABEL = 1
  CONTROL_TEXTBOX = 5
  def __init__ ( self , * args , ** kwargs ) :
   xbmc . executebuiltin ( "ActivateWindow(%d)" % ( self . WINDOW , ) )
   self . win = xbmcgui . Window ( self . WINDOW )
   xbmc . sleep ( 500 )
   self . setControls ( )
  def setControls ( self ) :
   self . win . getControl ( self . CONTROL_LABEL ) . setLabel ( heading )
   try : ooO0oo0o0 = open ( anounce ) ; iIIiiIi = ooO0oo0o0 . read ( )
   except : iIIiiIi = anounce
   self . win . getControl ( self . CONTROL_TEXTBOX ) . setText ( str ( iIIiiIi ) )
   return
 I11i1I1iiI1iI111 ( )
 while xbmc . getCondVisibility ( 'Window.IsVisible(textviewer)' ) :
  xbmc . sleep ( 500 )
  if 92 - 92: iI1iiIiiII . OOo00O0 % iIi1i1ii1 % O0
  if 93 - 93: Oo - i11iIiiIii . OoooooooOO
def oooOoo ( name , url ) :
 IIIiI1i1 ( name , url )
 if 97 - 97: iIi1i1ii1 . o0oOOo0O0Ooo % O0 - iIi1i1ii1 * OoooooooOO
 if 20 - 20: OoooooooOO + OoooooooOO % ooOo % OoooooooOO
def IiiiiIi11 ( ) :
 OO00O0OoooO = time . time ( )
 ooOOoOO000 = time . localtime ( OO00O0OoooO )
 return time . strftime ( '%Y%m%d%H%M%S' , ooOOoOO000 )
 if 79 - 79: OoO0O00 / o0oOOo0O0Ooo
 if 98 - 98: i11iIiiIii . i11iIiiIii * OoooooooOO
def OOo ( ) :
 IIii ( '' , '[COLOR=orange]noobs[/COLOR][COLOR=dodgerblue]and[/COLOR][COLOR=orange]nerds[/COLOR] Keyword Install' , OOO00O , 'keywords' , 'Keywords.png' , '' , '' , '' )
 if Oo0o0Oo0O ( ) :
  IIii ( '' , '[COLOR=darkcyan]Wi-Fi Settings[/COLOR]' , '' , 'openelec_settings' , 'Wi-Fi.png' , '' , '' , '' )
  if 86 - 86: OoOoOO00 . O0 . ooOo
  if 96 - 96: oOO / ooOo % O0 / Oo * OoO0O00 * oOoO0o00OO0
  if 27 - 27: OoOoOO00 % iI1iiIiiII / i1IIi . i1IIi * OoooooooOO % oOO
 IIii ( 'folder' , '[COLOR=dodgerblue]Add-on Maintenance/Fixes[/COLOR]' , 'none' , 'addonfixes' , 'Addon_Fixes.png' , '' , '' , '' )
 IIii ( 'folder' , '[COLOR=dodgerblue]Backup/Restore My Content[/COLOR]' , 'none' , 'backup_restore' , 'Backup.png' , '' , '' , '' )
 IIii ( 'folder' , '[COLOR=dodgerblue]Clean/Wipe Options[/COLOR]' , 'none' , 'wipetools' , 'Addon_Fixes.png' , '' , '' , '' )
 IIii ( '' , 'Check My IP Address' , 'none' , 'ipcheck' , 'Check_IP.png' , '' , '' , '' )
 IIii ( '' , 'Check XBMC/Kodi Version' , 'none' , 'xbmcversion' , 'Version_Check.png' , '' , '' , '' )
 IIii ( '' , 'Convert Physical Paths To Special' , iiI1IiI , 'fix_special' , 'Special_Paths.png' , '' , '' , '' )
 IIii ( '' , 'Force Close Kodi' , 'url' , 'kill_xbmc' , 'Kill_XBMC.png' , '' , '' , '' )
 IIii ( 'folder' , 'Test My Download Speed' , 'none' , 'speedtest_menu' , 'Speed_Test.png' , '' , '' , '' )
 IIii ( '' , 'Upload Log' , 'none' , 'uploadlog' , 'Log_File.png' , '' , '' , '' )
 IIii ( '' , 'View My Log' , 'none' , 'log' , 'View_Log.png' , '' , '' , '' )
 if 92 - 92: iI1iiIiiII - oOO / oOO + iIII
 if 57 - 57: Oo - OoooooooOO * OoO0O00 * OOo00O0 + ooOo
def o0o00O0oO ( url ) :
 IIii ( 'folder' , '[COLOR=yellow]1. Add-on Maintenance[/COLOR]' , str ( url ) + '&type=Maintenance' , 'grab_tutorials' , 'Maintenance.png' , '' , '' , '' )
 IIii ( 'folder' , 'Audio Add-ons' , str ( url ) + '&type=Audio' , 'grab_tutorials' , 'Audio.png' , '' , '' , '' )
 IIii ( 'folder' , 'Picture Add-ons' , str ( url ) + '&type=Pictures' , 'grab_tutorials' , 'Pictures.png' , '' , '' , '' )
 IIii ( 'folder' , 'Program Add-ons' , str ( url ) + '&type=Programs' , 'grab_tutorials' , 'Programs.png' , '' , '' , '' )
 IIii ( 'folder' , 'Video Add-ons' , str ( url ) + '&type=Video' , 'grab_tutorials' , 'Video.png' , '' , '' , '' )
 if 54 - 54: OoOoOO00 % iIii1I11I1II1
 if 24 - 24: iIII / iI1iiIiiII * Oo
def iiIIi1Ii1 ( url ) :
 O0O0o0o0o = 'http://noobsandnerds.com/TI/TutorialPortal/downloadcount.php?id=%s' % ( url )
 oooOo0OOOoo0 ( O0O0o0o0o )
 ii1111iII = 'http://noobsandnerds.com/TI/TutorialPortal/tutorialdetails.php?id=%s' % ( url )
 iiiiI = oooOo0OOOoo0 ( ii1111iII ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 O00o0 = re . compile ( 'name="(.+?)"' ) . findall ( iiiiI )
 IiIi1Ii = re . compile ( 'author="(.+?)"' ) . findall ( iiiiI )
 Iiii1Ii = re . compile ( 'video_guide1="(.+?)"' ) . findall ( iiiiI )
 ooOOo00oo0 = re . compile ( 'video_guide2="(.+?)"' ) . findall ( iiiiI )
 IIIII1Ii = re . compile ( 'video_guide3="(.+?)"' ) . findall ( iiiiI )
 iIiI1 = re . compile ( 'video_guide4="(.+?)"' ) . findall ( iiiiI )
 I1IiII1I1i1I1 = re . compile ( 'video_guide5="(.+?)"' ) . findall ( iiiiI )
 II11iiI = re . compile ( 'video_label1="(.+?)"' ) . findall ( iiiiI )
 iiIi = re . compile ( 'video_label2="(.+?)"' ) . findall ( iiiiI )
 OooooOo = re . compile ( 'video_label3="(.+?)"' ) . findall ( iiiiI )
 IIIiiiIiI = re . compile ( 'video_label4="(.+?)"' ) . findall ( iiiiI )
 OO0OOoooo0o = re . compile ( 'video_label5="(.+?)"' ) . findall ( iiiiI )
 i1oO00O = re . compile ( 'about="(.+?)"' ) . findall ( iiiiI )
 iiI1IIi1i1 = re . compile ( 'step1="(.+?)"' ) . findall ( iiiiI )
 oOOoO = re . compile ( 'step2="(.+?)"' ) . findall ( iiiiI )
 iIiiI = re . compile ( 'step3="(.+?)"' ) . findall ( iiiiI )
 ooo0O0O0OO = re . compile ( 'step4="(.+?)"' ) . findall ( iiiiI )
 oOooOOoO = re . compile ( 'step5="(.+?)"' ) . findall ( iiiiI )
 o0o000OOO = re . compile ( 'step6="(.+?)"' ) . findall ( iiiiI )
 I1111iii1ii11 = re . compile ( 'step7="(.+?)"' ) . findall ( iiiiI )
 Oooo = re . compile ( 'step8="(.+?)"' ) . findall ( iiiiI )
 III1II1I1iI = re . compile ( 'step9="(.+?)"' ) . findall ( iiiiI )
 oOOOO = re . compile ( 'step10="(.+?)"' ) . findall ( iiiiI )
 Oo0OO0o0oOO0 = re . compile ( 'step11="(.+?)"' ) . findall ( iiiiI )
 i1II1IiIIi = re . compile ( 'step12="(.+?)"' ) . findall ( iiiiI )
 o0O0 = re . compile ( 'step13="(.+?)"' ) . findall ( iiiiI )
 iiIi1I1IIIII1IIi = re . compile ( 'step14="(.+?)"' ) . findall ( iiiiI )
 i11iii1II1I1 = re . compile ( 'step15="(.+?)"' ) . findall ( iiiiI )
 Iii1iii1I = re . compile ( 'screenshot1="(.+?)"' ) . findall ( iiiiI )
 oOo000Oo00o = re . compile ( 'screenshot2="(.+?)"' ) . findall ( iiiiI )
 o0o = re . compile ( 'screenshot3="(.+?)"' ) . findall ( iiiiI )
 oOOoOoOO = re . compile ( 'screenshot4="(.+?)"' ) . findall ( iiiiI )
 iII11 = re . compile ( 'screenshot5="(.+?)"' ) . findall ( iiiiI )
 O00OO00OOOoO = re . compile ( 'screenshot6="(.+?)"' ) . findall ( iiiiI )
 IiI11Ii1iI = re . compile ( 'screenshot7="(.+?)"' ) . findall ( iiiiI )
 ooOo0 = re . compile ( 'screenshot8="(.+?)"' ) . findall ( iiiiI )
 oOo0o = re . compile ( 'screenshot9="(.+?)"' ) . findall ( iiiiI )
 O000OOO000o = re . compile ( 'screenshot10="(.+?)"' ) . findall ( iiiiI )
 I11iiIiiI1iIi11 = re . compile ( 'screenshot11="(.+?)"' ) . findall ( iiiiI )
 II1I1I11i1I1 = re . compile ( 'screenshot12="(.+?)"' ) . findall ( iiiiI )
 iiIi1 = re . compile ( 'screenshot13="(.+?)"' ) . findall ( iiiiI )
 oOOO0 = re . compile ( 'screenshot14="(.+?)"' ) . findall ( iiiiI )
 IiIi11iI1IIi = re . compile ( 'screenshot15="(.+?)"' ) . findall ( iiiiI )
 if 5 - 5: ooOo + OoOoOO00
 I1i11i = O00o0 [ 0 ] if ( len ( O00o0 ) > 0 ) else ''
 I1111ii11IIII = IiIi1Ii [ 0 ] if ( len ( IiIi1Ii ) > 0 ) else ''
 oOOoo = Iiii1Ii [ 0 ] if ( len ( Iiii1Ii ) > 0 ) else 'None'
 iII1111III1I = ooOOo00oo0 [ 0 ] if ( len ( ooOOo00oo0 ) > 0 ) else 'None'
 ii11i = IIIII1Ii [ 0 ] if ( len ( IIIII1Ii ) > 0 ) else 'None'
 O00oOo00o0o = iIiI1 [ 0 ] if ( len ( iIiI1 ) > 0 ) else 'None'
 O00oO0 = I1IiII1I1i1I1 [ 0 ] if ( len ( I1IiII1I1i1I1 ) > 0 ) else 'None'
 I1I = II11iiI [ 0 ] if ( len ( II11iiI ) > 0 ) else 'None'
 ooooo = iiIi [ 0 ] if ( len ( iiIi ) > 0 ) else 'None'
 i11IIIiI1I = OooooOo [ 0 ] if ( len ( OooooOo ) > 0 ) else 'None'
 o0iiiI1I1iIIIi1 = IIIiiiIiI [ 0 ] if ( len ( IIIiiiIiI ) > 0 ) else 'None'
 IiiI1iiiiI1iI = OO0OOoooo0o [ 0 ] if ( len ( OO0OOoooo0o ) > 0 ) else 'None'
 Oooo0Oo00o = i1oO00O [ 0 ] if ( len ( i1oO00O ) > 0 ) else ''
 OO0O0oooo0 = '[CR][CR][COLOR=dodgerblue]Step 1:[/COLOR][CR]' + iiI1IIi1i1 [ 0 ] if ( len ( iiI1IIi1i1 ) > 0 ) else ''
 ooOoo0OoO0 = '[CR][CR][COLOR=dodgerblue]Step 2:[/COLOR][CR]' + oOOoO [ 0 ] if ( len ( oOOoO ) > 0 ) else ''
 i1iiiiIi1 = '[CR][CR][COLOR=dodgerblue]Step 3:[/COLOR][CR]' + iIiiI [ 0 ] if ( len ( iIiiI ) > 0 ) else ''
 I1i1Iii1 = '[CR][CR][COLOR=dodgerblue]Step 4:[/COLOR][CR]' + ooo0O0O0OO [ 0 ] if ( len ( ooo0O0O0OO ) > 0 ) else ''
 IIIiII11II11 = '[CR][CR][COLOR=dodgerblue]Step 5:[/COLOR][CR]' + oOooOOoO [ 0 ] if ( len ( oOooOOoO ) > 0 ) else ''
 OOooo = '[CR][CR][COLOR=dodgerblue]Step 6:[/COLOR][CR]' + o0o000OOO [ 0 ] if ( len ( o0o000OOO ) > 0 ) else ''
 iII1 = '[CR][CR][COLOR=dodgerblue]Step 7:[/COLOR][CR]' + I1111iii1ii11 [ 0 ] if ( len ( I1111iii1ii11 ) > 0 ) else ''
 ii1i1iIiIIi = '[CR][CR][COLOR=dodgerblue]Step 8:[/COLOR][CR]' + Oooo [ 0 ] if ( len ( Oooo ) > 0 ) else ''
 iI11I11i = '[CR][CR][COLOR=dodgerblue]Step 9:[/COLOR][CR]' + III1II1I1iI [ 0 ] if ( len ( III1II1I1iI ) > 0 ) else ''
 O00Oo00o0 = '[CR][CR][COLOR=dodgerblue]Step 10:[/COLOR][CR]' + oOOOO [ 0 ] if ( len ( oOOOO ) > 0 ) else ''
 I1ii1i1 = '[CR][CR][COLOR=dodgerblue]Step 11:[/COLOR][CR]' + Oo0OO0o0oOO0 [ 0 ] if ( len ( Oo0OO0o0oOO0 ) > 0 ) else ''
 i11i1IiIi11 = '[CR][CR][COLOR=dodgerblue]Step 12:[/COLOR][CR]' + i1II1IiIIi [ 0 ] if ( len ( i1II1IiIIi ) > 0 ) else ''
 Oo0OiI1 = '[CR][CR][COLOR=dodgerblue]Step 13:[/COLOR][CR]' + o0O0 [ 0 ] if ( len ( o0O0 ) > 0 ) else ''
 IiiIIII1i1iII1 = '[CR][CR][COLOR=dodgerblue]Step 14:[/COLOR][CR]' + iiIi1I1IIIII1IIi [ 0 ] if ( len ( iiIi1I1IIIII1IIi ) > 0 ) else ''
 IiiiiI11iii11iI = '[CR][CR][COLOR=dodgerblue]Step 15:[/COLOR][CR]' + i11iii1II1I1 [ 0 ] if ( len ( i11iii1II1I1 ) > 0 ) else ''
 o00iIIiIi111iI = Iii1iii1I [ 0 ] if ( len ( Iii1iii1I ) > 0 ) else ''
 II1I1ii = oOo000Oo00o [ 0 ] if ( len ( oOo000Oo00o ) > 0 ) else ''
 oo0OO0O = o0o [ 0 ] if ( len ( o0o ) > 0 ) else ''
 OO0OooOOoO00OO00 = oOOoOoOO [ 0 ] if ( len ( oOOoOoOO ) > 0 ) else ''
 ii11ii1iIiI1 = iII11 [ 0 ] if ( len ( iII11 ) > 0 ) else ''
 OoOo0oO0 = O00OO00OOOoO [ 0 ] if ( len ( O00OO00OOOoO ) > 0 ) else ''
 i111iIi1i1 = IiI11Ii1iI [ 0 ] if ( len ( IiI11Ii1iI ) > 0 ) else ''
 OOo00O0O = ooOo0 [ 0 ] if ( len ( ooOo0 ) > 0 ) else ''
 oooOoO = oOo0o [ 0 ] if ( len ( oOo0o ) > 0 ) else ''
 IiiIi1IiiiI = O000OOO000o [ 0 ] if ( len ( O000OOO000o ) > 0 ) else ''
 OO0oooOO = I11iiIiiI1iIi11 [ 0 ] if ( len ( I11iiIiiI1iIi11 ) > 0 ) else ''
 IIIi1iiIIiiiI = II1I1I11i1I1 [ 0 ] if ( len ( II1I1I11i1I1 ) > 0 ) else ''
 I1IIiIi1iI = iiIi1 [ 0 ] if ( len ( iiIi1 ) > 0 ) else ''
 oOo0 = oOOO0 [ 0 ] if ( len ( oOOO0 ) > 0 ) else ''
 I111iIii1i1 = IiIi11iI1IIi [ 0 ] if ( len ( IiIi11iI1IIi ) > 0 ) else ''
 IIIii = str ( '[COLOR=orange]Author: [/COLOR]' + I1111ii11IIII + '[CR][CR][COLOR=lime]About: [/COLOR]' + Oooo0Oo00o + OO0O0oooo0 + ooOoo0OoO0 + i1iiiiIi1 + I1i1Iii1 + IIIiII11II11 + OOooo + iII1 + ii1i1iIiIIi + iI11I11i + O00Oo00o0 + I1ii1i1 + i11i1IiIi11 + Oo0OiI1 + IiiIIII1i1iII1 + IiiiiI11iii11iI )
 if 6 - 6: iIi1i1ii1 % iIII / iI1iiIiiII + iIi1i1ii1 . ooOo
 if OO0O0oooo0 != '' :
  IIii ( '' , '[COLOR=yellow][Text Guide][/COLOR]  ' + I1i11i , IIIii , 'text_guide' , 'How_To.png' , O0o0Oo , Oooo0Oo00o , '' )
 if oOOoo != 'None' :
  IIii ( '' , '[COLOR=lime][VIDEO][/COLOR]  ' + I1I , oOOoo , 'play_video' , 'Video_Guide.png' , O0o0Oo , '' , '' )
 if iII1111III1I != 'None' :
  IIii ( '' , '[COLOR=lime][VIDEO][/COLOR]  ' + ooooo , iII1111III1I , 'play_video' , 'Video_Guide.png' , O0o0Oo , '' , '' )
 if ii11i != 'None' :
  IIii ( '' , '[COLOR=lime][VIDEO][/COLOR]  ' + i11IIIiI1I , ii11i , 'play_video' , 'Video_Guide.png' , O0o0Oo , '' , '' )
 if O00oOo00o0o != 'None' :
  IIii ( '' , '[COLOR=lime][VIDEO][/COLOR]  ' + o0iiiI1I1iIIIi1 , O00oOo00o0o , 'play_video' , 'Video_Guide.png' , O0o0Oo , '' , '' )
 if O00oO0 != 'None' :
  IIii ( '' , '[COLOR=lime][VIDEO][/COLOR]  ' + IiiI1iiiiI1iI , O00oO0 , 'play_video' , 'Video_Guide.png' , O0o0Oo , '' , '' )
  if 70 - 70: iIii1I11I1II1 / iI1iiIiiII
  if 61 - 61: O0 * o0oOOo0O0Ooo + iIi1i1ii1 - Oo . I1IiiI - iIII
def i1I1I1iiI ( ) :
 if o0O . getSetting ( 'tutorial_manual_search' ) == 'true' :
  IIii ( 'folder' , '[COLOR=yellow]Manual Search[/COLOR]' , 'tutorials' , 'manual_search' , 'Manual_Search.png' , '' , '' , '' )
 if o0O . getSetting ( 'tutorial_all' ) == 'true' :
  IIii ( 'folder' , '[COLOR=lime]All Guides[/COLOR] Everything in one place' , '' , 'grab_tutorials' , 'All.png' , '' , '' , '' )
 if o0O . getSetting ( 'tutorial_kodi' ) == 'true' :
  IIii ( 'folder' , '[COLOR=lime]XBMC / Kodi[/COLOR] Specific' , '' , 'xbmc_menu' , 'XBMC.png' , '' , '' , '' )
 if o0O . getSetting ( 'tutorial_xbmc4xbox' ) == 'true' :
  IIii ( 'folder' , '[COLOR=lime]XBMC4Xbox[/COLOR] Specific' , '&platform=XBMC4Xbox' , 'xbmc_menu' , 'XBMC4Xbox.png' , '' , '' , '' )
 if o0O . getSetting ( 'tutorial_android' ) == 'true' :
  IIii ( 'folder' , '[COLOR=orange][Platform][/COLOR] Android' , '&platform=Android' , 'platform_menu' , 'Android.png' , '' , '' , '' )
 if o0O . getSetting ( 'tutorial_atv' ) == 'true' :
  IIii ( 'folder' , '[COLOR=orange][Platform][/COLOR] Apple TV' , '&platform=ATV' , 'platform_menu' , 'ATV.png' , '' , '' , '' )
 if o0O . getSetting ( 'tutorial_ios' ) == 'true' :
  IIii ( 'folder' , '[COLOR=orange][Platform][/COLOR] ATV2 & iOS' , '&platform=iOS' , 'platform_menu' , 'iOS.png' , '' , '' , '' )
 if o0O . getSetting ( 'tutorial_linux' ) == 'true' :
  IIii ( 'folder' , '[COLOR=orange][Platform][/COLOR] Linux' , '&platform=Linux' , 'platform_menu' , 'Linux.png' , '' , '' , '' )
 if o0O . getSetting ( 'tutorial_pure_linux' ) == 'true' :
  IIii ( 'folder' , '[COLOR=orange][Platform][/COLOR] Pure Linux' , '&platform=Custom_Linux' , 'platform_menu' , 'Custom_Linux.png' , '' , '' , '' )
 if o0O . getSetting ( 'tutorial_openelec' ) == 'true' :
  IIii ( 'folder' , '[COLOR=orange][Platform][/COLOR] OpenELEC' , '&platform=OpenELEC' , 'platform_menu' , 'OpenELEC.png' , '' , '' , '' )
 if o0O . getSetting ( 'tutorial_osmc' ) == 'true' :
  IIii ( 'folder' , '[COLOR=orange][Platform][/COLOR] OSMC' , '&platform=OSMC' , 'platform_menu' , 'OSMC.png' , '' , '' , '' )
 if o0O . getSetting ( 'tutorial_osx' ) == 'true' :
  IIii ( 'folder' , '[COLOR=orange][Platform][/COLOR] OSX' , '&platform=OSX' , 'platform_menu' , 'OSX.png' , '' , '' , '' )
 if o0O . getSetting ( 'tutorial_raspbmc' ) == 'true' :
  IIii ( 'folder' , '[COLOR=orange][Platform][/COLOR] Raspbmc' , '&platform=Raspbmc' , 'platform_menu' , 'Raspbmc.png' , '' , '' , '' )
 if o0O . getSetting ( 'tutorial_windows' ) == 'true' :
  IIii ( 'folder' , '[COLOR=orange][Platform][/COLOR] Windows' , '&platform=Windows' , 'platform_menu' , 'Windows.png' , '' , '' , '' )
 if o0O . getSetting ( 'tutorial_allwinner' ) == 'true' :
  IIii ( 'folder' , '[COLOR=dodgerblue][Hardware][/COLOR] Allwinner Devices' , '&hardware=Allwinner' , 'platform_menu' , 'Allwinner.png' , '' , '' , '' )
 if o0O . getSetting ( 'tutorial_aftv' ) == 'true' :
  IIii ( 'folder' , '[COLOR=dodgerblue][Hardware][/COLOR] Amazon Fire TV' , '&hardware=AFTV' , 'platform_menu' , 'AFTV.png' , '' , '' , '' )
 if o0O . getSetting ( 'tutorial_amlogic' ) == 'true' :
  IIii ( 'folder' , '[COLOR=dodgerblue][Hardware][/COLOR] AMLogic Devices' , '&hardware=AMLogic' , 'platform_menu' , 'AMLogic.png' , '' , '' , '' )
 if o0O . getSetting ( 'tutorial_boxee' ) == 'true' :
  IIii ( 'folder' , '[COLOR=dodgerblue][Hardware][/COLOR] Boxee' , '&hardware=Boxee' , 'platform_menu' , 'Boxee.png' , '' , '' , '' )
 if o0O . getSetting ( 'tutorial_intel' ) == 'true' :
  IIii ( 'folder' , '[COLOR=dodgerblue][Hardware][/COLOR] Intel Devices' , '&hardware=Intel' , 'platform_menu' , 'Intel.png' , '' , '' , '' )
 if o0O . getSetting ( 'tutorial_rpi' ) == 'true' :
  IIii ( 'folder' , '[COLOR=dodgerblue][Hardware][/COLOR] Raspberry Pi' , '&hardware=RaspberryPi' , 'platform_menu' , 'RaspberryPi.png' , '' , '' , '' )
 if o0O . getSetting ( 'tutorial_rockchip' ) == 'true' :
  IIii ( 'folder' , '[COLOR=dodgerblue][Hardware][/COLOR] Rockchip Devices' , '&hardware=Rockchip' , 'platform_menu' , 'Rockchip.png' , '' , '' , '' )
 if o0O . getSetting ( 'tutorial_xbox' ) == 'true' :
  IIii ( 'folder' , '[COLOR=dodgerblue][Hardware][/COLOR] Xbox' , '&hardware=Xbox' , 'platform_menu' , 'Xbox_Original.png' , '' , '' , '' )
  if 74 - 74: ooOo + iI1iiIiiII + OoooooooOO . O0 . o0oOOo0O0Ooo . oOO
  if 5 - 5: I1ii11iIi11i * oOoO0o00OO0 % iIi1i1ii1 . O0 * iIII
def o00OOOOoOO ( ) :
 oOOoO0 = xbmcgui . Dialog ( )
 if oOOoO0 . yesno ( "Make Add-on Passwords Visible?" , "This will make all your add-on passwords visible in the add-on settings. Are you sure you wish to continue?" ) :
  for OOo000o , oO0ooOoO , ooO0000o00O in os . walk ( OO0o ) :
   for ooO0oo0o0 in ooO0000o00O :
    if ooO0oo0o0 == 'settings.xml' :
     ii1I1iIi = open ( os . path . join ( OOo000o , ooO0oo0o0 ) ) . read ( )
     O0OoOoO00O = re . compile ( '<setting id=(.+?)>' ) . findall ( ii1I1iIi )
     for O0o0OOo0o0o in O0OoOoO00O :
      if 'pass' in O0o0OOo0o0o :
       if 'option="hidden"' in O0o0OOo0o0o :
        try :
         o0oO00oooo = O0o0OOo0o0o . replace ( ' option="hidden"' , '' )
         ooO0oo0o0 = open ( os . path . join ( OOo000o , ooO0oo0o0 ) , mode = 'w' )
         ooO0oo0o0 . write ( str ( ii1I1iIi ) . replace ( O0o0OOo0o0o , o0oO00oooo ) )
         ooO0oo0o0 . close ( )
        except :
         pass
  oOOoO0 . ok ( "Passwords Are now visible" , "Your passwords will now be visible in your add-on settings. If you want to undo this please use the option to hide passwords." )
  if 74 - 74: iIii1I11I1II1 . iIi1i1ii1 / oOoO0o00OO0 * I1ii11iIi11i / i11iIiiIii / iIII
  if 15 - 15: OoooooooOO
def O0O00 ( ) :
 if o0O . getSetting ( 'email' ) == '' :
  oOOoO0 = xbmcgui . Dialog ( )
  oOOoO0 . ok ( "No Email Address Set" , "A new window will Now open for you to enter your Email address. The logfile will be sent here" )
  o0O . openSettings ( )
 xbmc . executebuiltin ( 'XBMC.RunScript(special://home/addons/' + I1IiI + '/uploadLog.py)' )
 if 75 - 75: o0oOOo0O0Ooo
 if 20 - 20: OoO0O00 / i11iIiiIii * o0oOOo0O0Ooo - I1ii11iIi11i - II111iiii / i11iIiiIii
def IIIII1i1I ( localbuildcheck , localversioncheck , localidcheck ) :
 if o0oOoO00o == 'true' :
  ii1111iII = 'http://noobsandnerds.com/TI/login/login_details.php?user=%s&pass=%s' % ( oo00 , o00 )
 else : ii1111iII = 'http://noobsandnerds.com/TI/login/login_details.php?user=%s&pass=%s' % ( '' , '' )
 iiiiI = oooOo0OOOoo0 ( ii1111iII ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 OOo0Oo = re . compile ( 'login_msg="(.+?)"' ) . findall ( iiiiI )
 iI1iIiI1Ii1iI = OOo0Oo [ 0 ] if ( len ( OOo0Oo ) > 0 ) else ''
 if 58 - 58: II111iiii . iIi1i1ii1 . iI1iiIiiII * OoooooooOO / iI1iiIiiII / oOoO0o00OO0
 if 41 - 41: oOoO0o00OO0 + OoO0O00 . OOo00O0
 if not 'REGISTER FOR FREE' in iI1iIiI1Ii1iI :
  iiiiI11ii = open ( IIIii1II1II , mode = 'w+' )
  iiiiI11ii . write ( 'd="' + IiiiiIi11 ( ) + '"\nlogin_msg="' + iI1iIiI1Ii1iI + '"' )
  iiiiI11ii . close ( )
  if 73 - 73: i11iIiiIii * I1IiiI + o0oOOo0O0Ooo / ooOo
 I1III1II1I11 ( localbuildcheck , localversioncheck , localidcheck , iI1iIiI1Ii1iI )
 if 56 - 56: i1IIi
 if 11 - 11: i11iIiiIii % o0oOOo0O0Ooo / oOoO0o00OO0 * OoooooooOO
def IIi1I1iiiii ( ) :
 xbmc . executebuiltin ( 'UpdateLocalAddons' )
 xbmc . executebuiltin ( 'UpdateAddonRepos' )
 xbmcgui . Dialog ( ) . ok ( 'Force Refresh Started Successfully' , 'Depending on the speed of your device it could take a few minutes for the update to take effect.' )
 return
 if 82 - 82: iIII
 if 10 - 10: Oo0Ooo % Oo / oOoO0o00OO0 * iIII - o0oOOo0O0Ooo
def Oo0oo ( ) :
 ooo0o = 1
 try :
  oooOo0OOOoo0 ( 'http://google.com' )
 except :
  try :
   oooOo0OOOoo0 ( 'http://google.com' )
  except :
   try :
    oooOo0OOOoo0 ( 'http://google.com' )
   except :
    try :
     oooOo0OOOoo0 ( 'http://google.cn' )
    except :
     try :
      oooOo0OOOoo0 ( 'http://google.cn' )
     except :
      oOOoO0 . ok ( "NO INTERNET CONNECTION" , 'It looks like this device isn\'t connected to the internet. Only some of the maintenance options will work until you fix the connectivity problem.' )
      I1III1II1I11 ( '' , '' , '' , '[COLOR=orange]NO INTERNET CONNECTION[/COLOR]' )
      ooo0o = 0
 if ooo0o == 1 :
  o0OOO0O00Oo00 ( )
  if 78 - 78: OoO0O00
  if 13 - 13: ooOo / oOoO0o00OO0
def o0OOO0O00Oo00 ( ) :
 oOooo0OOO = 'None'
 ii111iiIii = '0'
 if 44 - 44: O0
 if 19 - 19: II111iiii . ooOo
 II1II1IIII = open ( OOOO , mode = 'r' )
 OooOo0o0Oo = II1II1IIII . read ( )
 II1II1IIII . close ( )
 if 54 - 54: oOoO0o00OO0 . iIi1i1ii1 * iIII - O0 * iIII
 II1i1i = re . compile ( 'date="(.+?)"' ) . findall ( OooOo0o0Oo )
 IIio0 = II1i1i [ 0 ] if ( len ( II1i1i ) > 0 ) else ''
 Iii1iIIiii1ii = re . compile ( 'version="(.+?)"' ) . findall ( OooOo0o0Oo )
 i1Oo00 = Iii1iIIiii1ii [ 0 ] if ( len ( Iii1iIIiii1ii ) > 0 ) else ''
 if 17 - 17: i11iIiiIii
 oo00ooooOOo00 = open ( iiiiiIIii , mode = 'r' )
 ii1iOO00Oooo000 = oo00ooooOOo00 . read ( )
 oo00ooooOOo00 . close ( )
 if 94 - 94: OoooooooOO - iIII + ooOo . OoooooooOO / i1IIi
 i11I1I1iiI = re . compile ( 'id="(.+?)"' ) . findall ( ii1iOO00Oooo000 )
 oo0ooO0 = re . compile ( 'name="(.+?)"' ) . findall ( ii1iOO00Oooo000 )
 ii111iiIii = i11I1I1iiI [ 0 ] if ( len ( i11I1I1iiI ) > 0 ) else 'None'
 oOooo0OOO = oo0ooO0 [ 0 ] if ( len ( oo0ooO0 ) > 0 ) else ''
 if 53 - 53: iIi1i1ii1 % I1ii11iIi11i
 if 17 - 17: OoooooooOO % iI1iiIiiII % O0
 if oOo0oooo00o == 'true' :
  try :
   iiiiI = oooOo0OOOoo0 ( oO0o0o0ooO0oO ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
   I1111iI = re . compile ( 'date="(.+?)"' ) . findall ( iiiiI )
   O000o0O0 = re . compile ( 'video="https://www.youtube.com/watch\?v=(.+?)"' ) . findall ( iiiiI )
   oO0oOo = I1111iI [ 0 ] if ( len ( I1111iI ) > 0 ) else ''
   O0000oOoO0o0 = O000o0O0 [ 0 ] if ( len ( O000o0O0 ) > 0 ) else ''
   if 19 - 19: i1IIi % ooOo / o0oOOo0O0Ooo . o0oOOo0O0Ooo
   if 98 - 98: oOoO0o00OO0 / O0 % OoOoOO00
   if int ( IIio0 ) < int ( oO0oOo ) :
    II1iIi1IiIii = OooOo0o0Oo . replace ( IIio0 , oO0oOo )
    iiiiI11ii = open ( OOOO , mode = 'w' )
    iiiiI11ii . write ( str ( II1iIi1IiIii ) )
    iiiiI11ii . close ( )
    if 71 - 71: i11iIiiIii * OoOoOO00 * Oo + ooOo + Oo0Ooo
   yt . PlayVideo ( O0000oOoO0o0 , forcePlayer = True )
   xbmc . sleep ( 500 )
   while xbmc . Player ( ) . isPlaying ( ) :
    xbmc . sleep ( 500 )
  except : pass
 if not os . path . exists ( IIIii1II1II ) :
  print "### First login check ###"
  IIIII1i1I ( oOooo0OOO , i1Oo00 , ii111iiIii )
  if 59 - 59: iIII
  if 54 - 54: Oo
 else :
  IIIIIIi1I = open ( IIIii1II1II , mode = 'r' )
  OoOo000o = IIIIIIi1I . read ( )
  IIIIIIi1I . close ( )
  if 40 - 40: Oo0Ooo * OoooooooOO + iIII
  ooOO0 = re . compile ( 'd="(.+?)"' ) . findall ( OoOo000o )
  i1IiIii1i = re . compile ( 'login_msg="(.+?)"' ) . findall ( OoOo000o )
  ooo0O0OOO000o = ooOO0 [ 0 ] if ( len ( ooOO0 ) > 0 ) else '0'
  iI1iIiI1Ii1iI = i1IiIii1i [ 0 ] if ( len ( i1IiIii1i ) > 0 ) else ''
  if 27 - 27: OoO0O00 % oOO - O0
  if int ( ooo0O0OOO000o ) + 2000000 > int ( IiiiiIi11 ( ) ) :
   print "### Login successful ###"
   I1III1II1I11 ( oOooo0OOO , i1Oo00 , ii111iiIii , iI1iIiI1Ii1iI )
  else :
   print "### Checking login ###"
   IIIII1i1I ( oOooo0OOO , i1Oo00 , ii111iiIii )
   if 44 - 44: I1ii11iIi11i + I1ii11iIi11i - Oo / II111iiii
   if 36 - 36: OoO0O00 - o0oOOo0O0Ooo . OOo00O0 % OOo00O0
def III11i1iIIiiI ( ) :
 iI1II = os . path . join ( xbmc . translatePath ( 'special://home' ) , 'cache' )
 if os . path . exists ( iI1II ) == True :
  for OOo000o , oO0ooOoO , ooO0000o00O in os . walk ( iI1II ) :
   iiIIIIiI111 = 0
   iiIIIIiI111 += len ( ooO0000o00O )
   if iiIIIIiI111 > 0 :
    for ooO0oo0o0 in ooO0000o00O :
     try :
      os . unlink ( os . path . join ( OOo000o , ooO0oo0o0 ) )
     except :
      pass
    for iiIiI1ii in oO0ooOoO :
     try :
      shutil . rmtree ( os . path . join ( OOo000o , iiIiI1ii ) )
     except :
      pass
 OO0o0oO0 = os . path . join ( xbmc . translatePath ( 'special://home' ) , 'temp' )
 if os . path . exists ( OO0o0oO0 ) == True :
  for OOo000o , oO0ooOoO , ooO0000o00O in os . walk ( OO0o0oO0 ) :
   iiIIIIiI111 = 0
   iiIIIIiI111 += len ( ooO0000o00O )
   if iiIIIIiI111 > 0 :
    for ooO0oo0o0 in ooO0000o00O :
     try :
      os . unlink ( os . path . join ( OOo000o , ooO0oo0o0 ) )
     except :
      pass
    for iiIiI1ii in oO0ooOoO :
     try :
      shutil . rmtree ( os . path . join ( OOo000o , iiIiI1ii ) )
     except :
      pass
 if xbmc . getCondVisibility ( 'system.platform.ATV2' ) :
  o00oiiIi1i = os . path . join ( '/private/var/mobile/Library/Caches/AppleTV/Video/' , 'Other' )
  for OOo000o , oO0ooOoO , ooO0000o00O in os . walk ( o00oiiIi1i ) :
   iiIIIIiI111 = 0
   iiIIIIiI111 += len ( ooO0000o00O )
   if iiIIIIiI111 > 0 :
    for ooO0oo0o0 in ooO0000o00O :
     os . unlink ( os . path . join ( OOo000o , ooO0oo0o0 ) )
    for iiIiI1ii in oO0ooOoO :
     shutil . rmtree ( os . path . join ( OOo000o , iiIiI1ii ) )
  o0o0OoOo = os . path . join ( '/private/var/mobile/Library/Caches/AppleTV/Video/' , 'LocalAndRental' )
  for OOo000o , oO0ooOoO , ooO0000o00O in os . walk ( o0o0OoOo ) :
   iiIIIIiI111 = 0
   iiIIIIiI111 += len ( ooO0000o00O )
   if iiIIIIiI111 > 0 :
    for ooO0oo0o0 in ooO0000o00O :
     os . unlink ( os . path . join ( OOo000o , ooO0oo0o0 ) )
    for iiIiI1ii in oO0ooOoO :
     shutil . rmtree ( os . path . join ( OOo000o , iiIiI1ii ) )
     if 49 - 49: i1IIi - OoOoOO00 - oOoO0o00OO0 * I1IiiI . oOO
 i11ii111II1II = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/script.module.simple.downloader' ) , '' )
 if os . path . exists ( i11ii111II1II ) == True :
  for OOo000o , oO0ooOoO , ooO0000o00O in os . walk ( i11ii111II1II ) :
   iiIIIIiI111 = 0
   iiIIIIiI111 += len ( ooO0000o00O )
   if iiIIIIiI111 > 0 :
    for ooO0oo0o0 in ooO0000o00O :
     os . unlink ( os . path . join ( OOo000o , ooO0oo0o0 ) )
    for iiIiI1ii in oO0ooOoO :
     shutil . rmtree ( os . path . join ( OOo000o , iiIiI1ii ) )
     if 2 - 2: II111iiii + iI1iiIiiII - OoO0O00 / OOo00O0 - OoO0O00 * I1ii11iIi11i
 oooOOOoo0O = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/script.image.music.slideshow/cache' ) , '' )
 if os . path . exists ( oooOOOoo0O ) == True :
  for OOo000o , oO0ooOoO , ooO0000o00O in os . walk ( oooOOOoo0O ) :
   iiIIIIiI111 = 0
   iiIIIIiI111 += len ( ooO0000o00O )
   if iiIIIIiI111 > 0 :
    for ooO0oo0o0 in ooO0000o00O :
     os . unlink ( os . path . join ( OOo000o , ooO0oo0o0 ) )
    for iiIiI1ii in oO0ooOoO :
     shutil . rmtree ( os . path . join ( OOo000o , iiIiI1ii ) )
     if 89 - 89: i1IIi
 ooOoOO0O00Ooo = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.iplayer/iplayer_http_cache' ) , '' )
 if os . path . exists ( ooOoOO0O00Ooo ) == True :
  for OOo000o , oO0ooOoO , ooO0000o00O in os . walk ( ooOoOO0O00Ooo ) :
   iiIIIIiI111 = 0
   iiIIIIiI111 += len ( ooO0000o00O )
   if iiIIIIiI111 > 0 :
    for ooO0oo0o0 in ooO0000o00O :
     os . unlink ( os . path . join ( OOo000o , ooO0oo0o0 ) )
    for iiIiI1ii in oO0ooOoO :
     shutil . rmtree ( os . path . join ( OOo000o , iiIiI1ii ) )
     if 15 - 15: iIi1i1ii1 . OoO0O00 - I1IiiI + OoooooooOO + iIi1i1ii1
 IiIII = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.itv/Images' ) , '' )
 if os . path . exists ( IiIII ) == True :
  for OOo000o , oO0ooOoO , ooO0000o00O in os . walk ( IiIII ) :
   iiIIIIiI111 = 0
   iiIIIIiI111 += len ( ooO0000o00O )
   if iiIIIIiI111 > 0 :
    for ooO0oo0o0 in ooO0000o00O :
     os . unlink ( os . path . join ( OOo000o , ooO0oo0o0 ) )
    for iiIiI1ii in oO0ooOoO :
     shutil . rmtree ( os . path . join ( OOo000o , iiIiI1ii ) )
     if 3 - 3: Oo0Ooo + Oo - I1IiiI
 Oo0ooIi1ii11i1II11 = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/script.navi-x/cache' ) , '' )
 if os . path . exists ( Oo0ooIi1ii11i1II11 ) == True :
  for OOo000o , oO0ooOoO , ooO0000o00O in os . walk ( Oo0ooIi1ii11i1II11 ) :
   iiIIIIiI111 = 0
   iiIIIIiI111 += len ( ooO0000o00O )
   if iiIIIIiI111 > 0 :
    for ooO0oo0o0 in ooO0000o00O :
     os . unlink ( os . path . join ( OOo000o , ooO0oo0o0 ) )
    for iiIiI1ii in oO0ooOoO :
     shutil . rmtree ( os . path . join ( OOo000o , iiIiI1ii ) )
     if 7 - 7: iIi1i1ii1 + ooOo - OoooooooOO + o0oOOo0O0Ooo % o0oOOo0O0Ooo
 i1IiI = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.phstreams/Cache' ) , '' )
 if os . path . exists ( i1IiI ) == True :
  for OOo000o , oO0ooOoO , ooO0000o00O in os . walk ( i1IiI ) :
   iiIIIIiI111 = 0
   iiIIIIiI111 += len ( ooO0000o00O )
   if iiIIIIiI111 > 0 :
    for ooO0oo0o0 in ooO0000o00O :
     os . unlink ( os . path . join ( OOo000o , ooO0oo0o0 ) )
    for iiIiI1ii in oO0ooOoO :
     shutil . rmtree ( os . path . join ( OOo000o , iiIiI1ii ) )
     if 31 - 31: oOoO0o00OO0 + OoO0O00 / I1IiiI * O0 + O0
 iiiiIiI1IIiI = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.audio.ramfm/cache' ) , '' )
 if os . path . exists ( iiiiIiI1IIiI ) == True :
  for OOo000o , oO0ooOoO , ooO0000o00O in os . walk ( iiiiIiI1IIiI ) :
   iiIIIIiI111 = 0
   iiIIIIiI111 += len ( ooO0000o00O )
   if iiIIIIiI111 > 0 :
    for ooO0oo0o0 in ooO0000o00O :
     os . unlink ( os . path . join ( OOo000o , ooO0oo0o0 ) )
    for iiIiI1ii in oO0ooOoO :
     shutil . rmtree ( os . path . join ( OOo000o , iiIiI1ii ) )
     if 53 - 53: iIii1I11I1II1 % OoOoOO00 % I1IiiI + I1ii11iIi11i % OoooooooOO
 IIII = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.whatthefurk/cache' ) , '' )
 if os . path . exists ( IIII ) == True :
  for OOo000o , oO0ooOoO , ooO0000o00O in os . walk ( IIII ) :
   iiIIIIiI111 = 0
   iiIIIIiI111 += len ( ooO0000o00O )
   if iiIIIIiI111 > 0 :
    for ooO0oo0o0 in ooO0000o00O :
     os . unlink ( os . path . join ( OOo000o , ooO0oo0o0 ) )
    for iiIiI1ii in oO0ooOoO :
     shutil . rmtree ( os . path . join ( OOo000o , iiIiI1ii ) )
     if 23 - 23: i1IIi
 try :
  IiI11IiIIi = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.genesis' ) , 'cache.db' )
  ooI1 = database . connect ( IiI11IiIIi )
  i1Iii1i1II1 = ooI1 . cursor ( )
  i1Iii1i1II1 . execute ( "DROP TABLE IF EXISTS rel_list" )
  i1Iii1i1II1 . execute ( "VACUUM" )
  ooI1 . commit ( )
  i1Iii1i1II1 . execute ( "DROP TABLE IF EXISTS rel_lib" )
  i1Iii1i1II1 . execute ( "VACUUM" )
  ooI1 . commit ( )
 except :
  pass
  if 92 - 92: iI1iiIiiII
  if 48 - 48: OOo00O0 . I1IiiI + O0
def oOoOO00Ooo ( mode ) :
 if zip == '' :
  oOOoO0 . ok ( 'Please set your backup location before proceeding' , 'You have not set your backup storage folder.\nPlease update the addon settings and try again.' )
  o0O . openSettings ( sys . argv [ 0 ] )
  iiI11 = o0O . getSetting ( 'zip' )
  if iiI11 == '' :
   oOoOO00Ooo ( mode )
 IIiii1I = xbmc . translatePath ( os . path . join ( I1IIIii , 'Community Builds' , 'My Builds' ) )
 if not os . path . exists ( IIiii1I ) :
  os . makedirs ( IIiii1I )
 ii1I11iIiIII1 = xbmcgui . Dialog ( ) . yesno ( "ABSOLUTELY CERTAIN?!!!" , 'Are you absolutely certain you want to wipe?' , '' , 'All addons and settings will be completely wiped!' , yeslabel = 'Yes' , nolabel = 'No' )
 if 49 - 49: iIii1I11I1II1 - iIii1I11I1II1 - OoOoOO00 + iIII / OoOoOO00
 if ii1I11iIiIII1 == 1 :
  if o0OO00oO != "skin.confluence" :
   oOOoO0 . ok ( 'Default Confluence Skin Required' , 'Please switch to the default Confluence skin before performing a wipe.' )
   xbmc . executebuiltin ( "ActivateWindow(appearancesettings,return)" )
   return
  else :
   if 74 - 74: OoooooooOO + I1ii11iIi11i % O0
   ii1I11iIiIII1 = xbmcgui . Dialog ( ) . yesno ( "VERY IMPORTANT" , 'This will completely wipe your install.' , 'Would you like to create a backup before proceeding?' , '' , yeslabel = 'No' , nolabel = 'Yes' )
   if ii1I11iIiIII1 == 0 :
    if not os . path . exists ( IIiii1I ) :
     os . makedirs ( IIiii1I )
    o0OO00oo0O = Ii1I1i111 ( heading = "Enter a name for this backup" )
    if ( not o0OO00oo0O ) : return False , 0
    iIIi11i1i1i1I = urllib . quote_plus ( o0OO00oo0O )
    i1i1iI1 = xbmc . translatePath ( os . path . join ( IIiii1I , iIIi11i1i1i1I + '.zip' ) )
    oOOO00OOOoOO = [ 'plugin.program.totalinstaller' , 'plugin.program.mediacube' ]
    III = [ "xbmc.log" , "xbmc.old.log" , "kodi.log" , "kodi.old.log" , '.DS_Store' , '.setup_complete' , 'XBMCHelper.conf' , '.gitignore' ]
    i11Ii1iIiII = "Creating full backup of existing build"
    O0oOo00Ooo0o0 = "Archiving..."
    i1IiII1i1I = ""
    iI1ii1ii1I = "Please Wait"
    i1II1iII ( iiI1IiI , i1i1iI1 , i11Ii1iIiII , O0oOo00Ooo0o0 , i1IiII1i1I , iI1ii1ii1I , oOOO00OOOoOO , III )
    if 32 - 32: I1ii11iIi11i + I1ii11iIi11i
    if 89 - 89: oOO + ooOo + iI1iiIiiII - Oo
   O0OoO000O0OO . create ( "Wiping Existing Content" , '' , 'Please wait...' , '' )
   for OOo000o , oO0ooOoO , ooO0000o00O in os . walk ( iiI1IiI , topdown = True ) :
    oO0ooOoO [ : ] = [ iiIiI1ii for iiIiI1ii in oO0ooOoO if iiIiI1ii not in OOoOO0oo0ooO ]
    for I1i11i in ooO0000o00O :
     try :
      O0OoO000O0OO . update ( 0 , "Removing [COLOR=yellow]" + I1i11i + '[/COLOR]' , '' , 'Please wait...' )
      os . unlink ( os . path . join ( OOo000o , I1i11i ) )
      os . remove ( os . path . join ( OOo000o , I1i11i ) )
      os . rmdir ( os . path . join ( OOo000o , I1i11i ) )
     except : print "Failed to remove file: " + I1i11i
     if 12 - 12: OoOoOO00 - o0oOOo0O0Ooo - iIi1i1ii1 / oOoO0o00OO0
   III1iii1 = [ I1i11i for I1i11i in os . listdir ( II ) if os . path . isdir ( os . path . join ( II , I1i11i ) ) ]
   try :
    for I1i11i in III1iii1 :
     try :
      if I1i11i not in OOoOO0oo0ooO :
       O0OoO000O0OO . update ( 0 , "Cleaning Directory: [COLOR=yellow]" + I1i11i + ' [/COLOR]' , '' , 'Please wait...' )
       shutil . rmtree ( os . path . join ( II , I1i11i ) )
     except : print "Failed to remove: " + I1i11i
   except : pass
   if 78 - 78: iIi1i1ii1 % Oo
   for OOo000o , oO0ooOoO , ooO0000o00O in os . walk ( II , topdown = True ) :
    oO0ooOoO [ : ] = [ iiIiI1ii for iiIiI1ii in oO0ooOoO if iiIiI1ii not in OOoOO0oo0ooO ]
    for I1i11i in ooO0000o00O :
     try :
      O0OoO000O0OO . update ( 0 , "Removing [COLOR=yellow]" + I1i11i + '[/COLOR]' , '' , 'Please wait...' )
      os . unlink ( os . path . join ( OOo000o , I1i11i ) )
      os . remove ( os . path . join ( OOo000o , I1i11i ) )
     except : print "Failed to remove file: " + I1i11i
     if 73 - 73: I1ii11iIi11i + OOo00O0 * I1IiiI * oOoO0o00OO0
   I11iiII1I1111 = [ I1i11i for I1i11i in os . listdir ( OO0o ) if os . path . isdir ( os . path . join ( OO0o , I1i11i ) ) ]
   try :
    for I1i11i in I11iiII1I1111 :
     try :
      if iiIIIII1i1iI == 'true' :
       if I1i11i not in OOoOO0oo0ooO and not 'repo' in I1i11i :
        O0OoO000O0OO . update ( 0 , "Removing Add-on: [COLOR=yellow]" + I1i11i + ' [/COLOR]' , '' , 'Please wait...' )
        shutil . rmtree ( os . path . join ( OO0o , I1i11i ) )
      else :
       if I1i11i not in OOoOO0oo0ooO :
        O0OoO000O0OO . update ( 0 , "Removing Add-on: [COLOR=yellow]" + I1i11i + ' [/COLOR]' , '' , 'Please wait...' )
        shutil . rmtree ( os . path . join ( OO0o , I1i11i ) )
     except : print "Failed to remove: " + I1i11i
   except : pass
   if 30 - 30: iIi1i1ii1 - O0 + I1IiiI . I1ii11iIi11i
   I111iI1IIIi1I = [ I1i11i for I1i11i in os . listdir ( ooOoOoo0O ) if os . path . isdir ( os . path . join ( ooOoOoo0O , I1i11i ) ) ]
   try :
    for I1i11i in I111iI1IIIi1I :
     try :
      if I1i11i not in OOoOO0oo0ooO :
       O0OoO000O0OO . update ( 0 , "Removing Add-on Data: [COLOR=yellow]" + I1i11i + ' [/COLOR]' , '' , 'Please wait...' )
       shutil . rmtree ( os . path . join ( ooOoOoo0O , I1i11i ) )
     except : print "Failed to remove: " + I1i11i
   except : pass
   if 21 - 21: OOo00O0 % O0 . oOO / OoOoOO00
   oO0o0O00O00O = [ I1i11i for I1i11i in os . listdir ( iiI1IiI ) if os . path . isdir ( os . path . join ( iiI1IiI , I1i11i ) ) ]
   try :
    for I1i11i in oO0o0O00O00O :
     try :
      if I1i11i not in OOoOO0oo0ooO :
       O0OoO000O0OO . update ( 0 , "Cleaning Directory: [COLOR=yellow]" + I1i11i + ' [/COLOR]' , '' , 'Please wait...' )
       shutil . rmtree ( os . path . join ( iiI1IiI , I1i11i ) )
     except : print "Failed to remove: " + I1i11i
   except : pass
  if mode != 'CB' :
   oOOoO0 . ok ( 'Wipe Complete' , 'Kodi will now close.' , 'When you next load up Kodi it should boot into the default Confluence skin and you should have a fresh install.' )
   xbmc . executebuiltin ( 'quit' )
  try :
   os . remove ( OOOO )
  except : print "### Failed to remove startup.xml"
  try :
   os . remove ( iiiiiIIii )
  except : print "### Failed to remove id.xml"
 else : return
 if 58 - 58: iIII . I1ii11iIi11i * i1IIi
 if 79 - 79: OOo00O0
def I1I111i1i1i ( ) :
 IIii ( '' , 'Clear Cache' , 'url' , 'clear_cache' , 'Clear_Cache.png' , '' , '' , '' )
 IIii ( '' , 'Clear My Cached Artwork' , 'none' , 'remove_textures' , 'Delete_Cached_Artwork.png' , '' , '' , '' )
 IIii ( '' , 'Delete Addon_Data' , 'url' , 'remove_addon_data' , 'Delete_Addon_Data.png' , '' , '' , '' )
 IIii ( '' , 'Delete Old Builds/Zips From Device' , 'url' , 'remove_build' , 'Delete_Builds.png' , '' , '' , '' )
 IIii ( '' , 'Delete Old Crash Logs' , 'url' , 'remove_crash_logs' , 'Delete_Crash_Logs.png' , '' , '' , '' )
 IIii ( '' , 'Delete Packages Folder' , 'url' , 'remove_packages' , 'Delete_Packages.png' , '' , '' , '' )
 IIii ( '' , 'Wipe My Install (Fresh Start)' , 'none' , 'wipe_xbmc' , 'Fresh_Start.png' , '' , '' , '' )
 if 25 - 25: oOO . iIII - I1IiiI * ooOo
 if 32 - 32: oOoO0o00OO0
def i1111ii1 ( url ) :
 IIii ( 'folder' , '[COLOR=yellow]1. Install[/COLOR]' , str ( url ) + '&tags=Install&XBMC=1' , 'grab_tutorials' , 'Install.png' , '' , '' , '' )
 IIii ( 'folder' , '[COLOR=lime]2. Settings[/COLOR]' , str ( url ) + '&tags=Settings' , 'grab_tutorials' , 'Settings.png' , '' , '' , '' )
 IIii ( 'folder' , '[COLOR=orange]3. Add-ons[/COLOR]' , str ( url ) , 'tutorial_addon_menu' , 'Addons.png' , '' , '' , '' )
 IIii ( 'folder' , '[COLOR=dodgerblue][XBMC/Kodi][/COLOR]  Audio' , str ( url ) + '&tags=Audio' , 'grab_tutorials' , 'Audio.png' , '' , '' , '' )
 IIii ( 'folder' , '[COLOR=dodgerblue][XBMC/Kodi][/COLOR]  Errors' , str ( url ) + '&tags=Errors' , 'grab_tutorials' , 'Errors.png' , '' , '' , '' )
 IIii ( 'folder' , '[COLOR=dodgerblue][XBMC/Kodi][/COLOR]  Gaming' , str ( url ) + '&tags=Gaming' , 'grab_tutorials' , 'gaming_portal.png' , '' , '' , '' )
 IIii ( 'folder' , '[COLOR=dodgerblue][XBMC/Kodi][/COLOR]  LiveTV' , str ( url ) + '&tags=LiveTV' , 'grab_tutorials' , 'LiveTV.png' , '' , '' , '' )
 IIii ( 'folder' , '[COLOR=dodgerblue][XBMC/Kodi][/COLOR]  Maintenance' , str ( url ) + '&tags=Maintenance' , 'grab_tutorials' , 'Maintenance.png' , '' , '' , '' )
 IIii ( 'folder' , '[COLOR=dodgerblue][XBMC/Kodi][/COLOR]  Pictures' , str ( url ) + '&tags=Pictures' , 'grab_tutorials' , 'Pictures.png' , '' , '' , '' )
 IIii ( 'folder' , '[COLOR=dodgerblue][XBMC/Kodi][/COLOR]  Profiles' , str ( url ) + '&tags=Profiles' , 'grab_tutorials' , 'Profiles.png' , '' , '' , '' )
 IIii ( 'folder' , '[COLOR=dodgerblue][XBMC/Kodi][/COLOR]  Skins' , str ( url ) + '&tags=Skins' , 'grab_tutorials' , 'Skin.png' , '' , '' , '' )
 IIii ( 'folder' , '[COLOR=dodgerblue][XBMC/Kodi][/COLOR]  Video' , str ( url ) + '&tags=Video' , 'grab_tutorials' , 'Video.png' , '' , '' , '' )
 IIii ( 'folder' , '[COLOR=dodgerblue][XBMC/Kodi][/COLOR]  Weather' , str ( url ) + '&tags=Weather' , 'grab_tutorials' , 'Weather.png' , '' , '' , '' )
 if 30 - 30: O0 / Oo + OoOoOO00 % OoO0O00 + iIi1i1ii1
 if 8 - 8: I1ii11iIi11i - i1IIi - ooOo / ooOo % o0oOOo0O0Ooo
def OOO0OoO00oOo ( url ) :
 oOoO00 = xbmc . getInfoLabel ( "System.BuildVersion" )
 iIIiIiI1I1 = float ( oOoO00 [ : 4 ] )
 if iIIiIiI1I1 < 14 :
  IiIoOo = 'You are running XBMC'
 else :
  IiIoOo = 'You are running Kodi'
 oOOoO0 = xbmcgui . Dialog ( )
 oOOoO0 . ok ( IiIoOo , "Your version is: %s" % iIIiIiI1I1 )
 if 49 - 49: o0oOOo0O0Ooo * iI1iiIiiII + Oo0Ooo
 if 1 - 1: o0oOOo0O0Ooo / II111iiii + oOoO0o00OO0 . i11iIiiIii + oOO . OoOoOO00
 if 95 - 95: o0oOOo0O0Ooo / iIi1i1ii1 % II111iiii + oOO
 if 97 - 97: Oo
 if 55 - 55: oOO
 if 1 - 1: OoO0O00
 if 43 - 43: iIii1I11I1II1 - Oo - o0oOOo0O0Ooo + I1ii11iIi11i - iIi1i1ii1 % I1ii11iIi11i
 if 58 - 58: OoOoOO00
 if 27 - 27: iIII * Oo - OoooooooOO . iI1iiIiiII - II111iiii
 if 62 - 62: I1IiiI / iIii1I11I1II1 * oOoO0o00OO0
 if 84 - 84: iIII - OoOoOO00 . iIII + oOO . OOo00O0
 if 96 - 96: iI1iiIiiII % OOo00O0 * iI1iiIiiII % I1IiiI . o0oOOo0O0Ooo / o0oOOo0O0Ooo
 if 7 - 7: OoO0O00 - oOO % i1IIi
 if 24 - 24: OoO0O00 % O0 % oOoO0o00OO0
 if 61 - 61: oOO . OOo00O0 / oOO * OoooooooOO
 if 13 - 13: II111iiii
 if 17 - 17: II111iiii
 if 66 - 66: iIII * ooOo
 if 73 - 73: i11iIiiIii + O0 % O0
 if 70 - 70: II111iiii * OoooooooOO - iI1iiIiiII + ooOo * O0
 if 49 - 49: ooOo . iI1iiIiiII . OoOoOO00 - I1ii11iIi11i
 if 74 - 74: oOO % I1ii11iIi11i * i1IIi
I1IIIi = iI1Ii11 ( )
OOOOO0O00 = None
o0O0ooooooo00 = None
O0oO00oOOooO = None
I1111ii11IIII = None
iiiii1I = None
iI1Iii1i1 = None
IIIii = None
OOO0OO00 = None
OoO00oo00 = None
i1iI1 = None
iii1IIIiiiI = None
iiiiI = None
O0ooO = None
OoOoo = None
i1ii1iIiI1 = None
I1i11i = None
oOO00 = None
IiI = None
Iii = None
O0o = None
IiIoOoOo0OoOOoo = None
o00oIIi1i1 = None
ii1IiiII = None
iIIi11i1i1i1I = None
oOoO0 = None
O0oOoOooo00oo = None
o0oOOoo0O = None
iIIiIiI1I1 = None
i1ii1I1I1 = None
o0O0Ooo = None
iI1iIiI1Ii1iI = None
i1iIIi1iIii = None
oOOoo0o00 = 'maintenance'
if 75 - 75: iIii1I11I1II1 * OOo00O0 / OoOoOO00 * II111iiii . i1IIi
try : OOOOO0O00 = urllib . unquote_plus ( I1IIIi [ "addon_id" ] )
except : pass
try : IiiI1II1II1i = urllib . unquote_plus ( I1IIIi [ "adult" ] )
except : pass
try : o0O0ooooooo00 = urllib . unquote_plus ( I1IIIi [ "artpack" ] )
except : pass
try : O0oO00oOOooO = urllib . unquote_plus ( I1IIIi [ "audioaddons" ] )
except : pass
try : I1111ii11IIII = urllib . unquote_plus ( I1IIIi [ "author" ] )
except : pass
try : iiiii1I = urllib . unquote_plus ( I1IIIi [ "buildname" ] )
except : pass
try : iI1Iii1i1 = urllib . unquote_plus ( I1IIIi [ "data_path" ] )
except : pass
try : IIIii = urllib . unquote_plus ( I1IIIi [ "description" ] )
except : pass
try : OOO0OO00 = urllib . unquote_plus ( I1IIIi [ "email" ] )
except : pass
try : OoO00oo00 = urllib . unquote_plus ( I1IIIi [ "fanart" ] )
except : pass
try : i1iI1 = urllib . unquote_plus ( I1IIIi [ "forum" ] )
except : pass
try : iIO0OO0o0O00oO = urllib . unquote_plus ( I1IIIi [ "guisettingslink" ] )
except : pass
try : iii1IIIiiiI = urllib . unquote_plus ( I1IIIi [ "iconimage" ] )
except : pass
try : iiiiI = urllib . unquote_plus ( I1IIIi [ "link" ] )
except : pass
try : O0ooO = urllib . unquote_plus ( I1IIIi [ "local" ] )
except : pass
try : OoOoo = urllib . unquote_plus ( I1IIIi [ "messages" ] )
except : pass
try : i1ii1iIiI1 = str ( I1IIIi [ "mode" ] )
except : pass
try : I1i11i = urllib . unquote_plus ( I1IIIi [ "name" ] )
except : pass
try : Iii1iiI = urllib . unquote_plus ( I1IIIi [ "pictureaddons" ] )
except : pass
try : oOO00 = urllib . unquote_plus ( I1IIIi [ "posts" ] )
except : pass
try : IiI = urllib . unquote_plus ( I1IIIi [ "programaddons" ] )
except : pass
try : Iii = urllib . unquote_plus ( I1IIIi [ "provider_name" ] )
except : pass
try : IiIoOoOo0OoOOoo = urllib . unquote_plus ( I1IIIi [ "repo_link" ] )
except : pass
try : O0o = urllib . unquote_plus ( I1IIIi [ "repo_id" ] )
except : pass
try : o00oIIi1i1 = urllib . unquote_plus ( I1IIIi [ "skins" ] )
except : pass
try : ii1IiiII = urllib . unquote_plus ( I1IIIi [ "sources" ] )
except : pass
try : iIIi11i1i1i1I = urllib . unquote_plus ( I1IIIi [ "title" ] )
except : pass
try : oOoO0 = urllib . unquote_plus ( I1IIIi [ "updated" ] )
except : pass
try : O0oOoOooo00oo = urllib . unquote_plus ( I1IIIi [ "unread" ] )
except : pass
try : o0oOOoo0O = urllib . unquote_plus ( I1IIIi [ "url" ] )
except : pass
try : iIIiIiI1I1 = urllib . unquote_plus ( I1IIIi [ "version" ] )
except : pass
try : i1ii1I1I1 = urllib . unquote_plus ( I1IIIi [ "video" ] )
except : pass
try : o0O0Ooo = urllib . unquote_plus ( I1IIIi [ "videoaddons" ] )
except : pass
try : iI1iIiI1Ii1iI = urllib . unquote_plus ( I1IIIi [ "welcometext" ] )
except : pass
try : i1iIIi1iIii = urllib . unquote_plus ( I1IIIi [ "zip_link" ] )
except : pass
if 6 - 6: iI1iiIiiII % iI1iiIiiII / OoooooooOO * ooOo . I1IiiI . i1IIi
if not os . path . exists ( OOOO0OOoO0O0 ) :
 os . makedirs ( OOOO0OOoO0O0 )
 if 59 - 59: oOoO0o00OO0 . oOoO0o00OO0 * I1IiiI - iI1iiIiiII % OoOoOO00
if not os . path . exists ( OOOO ) :
 II1II1IIII = open ( OOOO , mode = 'w+' )
 II1II1IIII . write ( 'date="01011001"\nversion="0.0"' )
 II1II1IIII . close ( )
 if 19 - 19: OoooooooOO / Oo0Ooo - iIi1i1ii1 . OoOoOO00
if not os . path . exists ( iiiiiIIii ) :
 II1II1IIII = open ( iiiiiIIii , mode = 'w+' )
 II1II1IIII . write ( 'id="None"\nname="None"' )
 II1II1IIII . close ( )
 if 8 - 8: oOoO0o00OO0 % oOO . iIii1I11I1II1
if os . path . exists ( O000OO0 ) :
 try :
  shutil . rmtree ( O000OO0 )
 except : pass
 if 95 - 95: o0oOOo0O0Ooo + i11iIiiIii . I1ii11iIi11i . oOO . o0oOOo0O0Ooo
if os . path . exists ( I11iii1Ii ) :
 try :
  shutil . rmtree ( I11iii1Ii )
 except : pass
 if 93 - 93: OOo00O0
if os . path . exists ( I1IIiiIiii ) :
 try :
  shutil . rmtree ( I1IIiiIiii )
 except : pass
 if 55 - 55: II111iiii % o0oOOo0O0Ooo - OoO0O00
if os . path . exists ( O000oo0O ) :
 try :
  shutil . rmtree ( O000oo0O )
 except : pass
 if 48 - 48: oOO * iIii1I11I1II1 % OoOoOO00
# OoOo0OO0 = binascii . unhexlify ( '6164646f6e2e786d6c' )
# i11Ii = xbmc . translatePath ( os . path . join ( OO0o , I1IiI , OoOo0OO0 ) )
# ooooO0000 = open ( i11Ii , mode = 'r' )
# OooOo0o0Oo = file . read ( ooooO0000 )
# file . close ( ooooO0000 )
# o0ooooOOo = re . compile ( '<ref>(.+?)</ref>' ) . findall ( OooOo0o0Oo )
# oo0i1ii = o0ooooOOo [ 0 ] if ( len ( o0ooooOOo ) > 0 ) else ''
# I1ii1ii = hashlib . md5 ( open ( oo0OooOOo0 , 'rb' ) . read ( ) ) . hexdigest ( )
# if oo0i1ii != I1ii1ii :
#  os . remove ( oo0OooOOo0 )
 if 22 - 22: i11iIiiIii
if i1ii1iIiI1 == None : Oo0oo ( )
elif i1ii1iIiI1 == 'addon_final_menu' : iI ( o0oOOoo0O )
elif i1ii1iIiI1 == 'addon_categories' : oOo00oOoO000 ( o0oOOoo0O )
elif i1ii1iIiI1 == 'addon_countries' : O0oO ( o0oOOoo0O )
elif i1ii1iIiI1 == 'addon_genres' : IiiiIi1i ( o0oOOoo0O )
elif i1ii1iIiI1 == 'addon_install' : I1i ( I1i11i , i1iIIi1iIii , IiIoOoOo0OoOOoo , O0o , OOOOO0O00 , Iii , i1iI1 , iI1Iii1i1 )
elif i1ii1iIiI1 == 'addon_install_badzip' : IIiIiiiIIIIi1 ( I1i11i , i1iIIi1iIii , IiIoOoOo0OoOOoo , O0o , OOOOO0O00 , Iii , i1iI1 , iI1Iii1i1 )
elif i1ii1iIiI1 == 'addon_install_na' : oo0O0oo ( I1i11i , i1iIIi1iIii , IiIoOoOo0OoOOoo , O0o , OOOOO0O00 , Iii , i1iI1 , iI1Iii1i1 )
elif i1ii1iIiI1 == 'addon_install_zero' : I1iIi1iiiIiI ( I1i11i , i1iIIi1iIii , IiIoOoOo0OoOOoo , O0o , OOOOO0O00 , Iii , i1iI1 , iI1Iii1i1 )
elif i1ii1iIiI1 == 'addon_loop' : oO00oo000O ( )
elif i1ii1iIiI1 == 'addon_removal_menu' : oo00ooOoo ( )
elif i1ii1iIiI1 == 'addonfix' : I11IiI1i ( )
elif i1ii1iIiI1 == 'addonfixes' : IiiI ( )
elif i1ii1iIiI1 == 'addonmenu' : Ii1iIi111i1i1 ( o0oOOoo0O )
elif i1ii1iIiI1 == 'addon_settings' : IIiiiiIiIIii ( )
elif i1ii1iIiI1 == 'backup' : BACKUP ( )
elif i1ii1iIiI1 == 'backup_option' : iI1I1II1 ( )
elif i1ii1iIiI1 == 'backup_restore' : III1I ( )
elif i1ii1iIiI1 == 'browse_repos' : I11oOOooo ( )
elif i1ii1iIiI1 == 'check_storage' : checkPath . check ( oOOoo0o00 )
elif i1ii1iIiI1 == 'check_updates' : O00o0OO0 ( )
elif i1ii1iIiI1 == 'clear_cache' : I111i ( )
elif i1ii1iIiI1 == 'cb_test_loop' : oO00oo000O ( )
elif i1ii1iIiI1 == 'CB_Menu' : Ii1i1 ( o0oOOoo0O )
elif i1ii1iIiI1 == 'community' : CB_Root_Menu ( o0oOOoo0O )
elif i1ii1iIiI1 == 'community_backup' : iII1i1IIiI1I ( )
elif i1ii1iIiI1 == 'community_backup_2' : OooOoOO0OO ( )
elif i1ii1iIiI1 == 'community_menu' : Ii1Ii1 ( o0oOOoo0O , i1ii1I1I1 )
elif i1ii1iIiI1 == 'countries' : oOooo00000 ( o0oOOoo0O )
elif i1ii1iIiI1 == 'description' : i1iii1IiiiI1i1 ( I1i11i , o0oOOoo0O , iiiii1I , I1111ii11IIII , iIIiIiI1I1 , IIIii , oOoO0 , o00oIIi1i1 , o0O0Ooo , O0oO00oOOooO , IiI , Iii1iiI , ii1IiiII , IiiI1II1II1i )
elif i1ii1iIiI1 == 'fix_special' : i1iIIII1iiIIi ( o0oOOoo0O )
elif i1ii1iIiI1 == 'full_backup' : i1i111I ( )
elif i1ii1iIiI1 == 'genres' : I1IOoo ( o0oOOoo0O )
elif i1ii1iIiI1 == 'gotham' : ii11Ii1IiiI1 ( )
elif i1ii1iIiI1 == 'grab_addons' : iiIIIi1iIi ( o0oOOoo0O )
elif i1ii1iIiI1 == 'grab_builds' : oO00oOoo00o0 ( o0oOOoo0O )
elif i1ii1iIiI1 == 'grab_builds_premium' : Grab_Builds_Premium ( o0oOOoo0O )
elif i1ii1iIiI1 == 'grab_hardware' : III1I1ii ( o0oOOoo0O )
elif i1ii1iIiI1 == 'grab_news' : o0oOOoO000 ( o0oOOoo0O )
elif i1ii1iIiI1 == 'grab_tutorials' : oOooOoOOo0O ( o0oOOoo0O )
elif i1ii1iIiI1 == 'guisettingsfix' : I1I111IIIi1 ( o0oOOoo0O , O0ooO )
elif i1ii1iIiI1 == 'hardware_filter_menu' : IIiIIiI1iIII ( o0oOOoo0O )
elif i1ii1iIiI1 == 'hardware_final_menu' : o0000oOooo0oo ( o0oOOoo0O )
elif i1ii1iIiI1 == 'hardware_root_menu' : Ii1o0OOOoo0000 ( )
elif i1ii1iIiI1 == 'helix' : ii1iI1i1 ( )
elif i1ii1iIiI1 == 'hide_passwords' : oO0o00o000Oo0 ( )
elif i1ii1iIiI1 == 'ipcheck' : I1iiIIiI11I ( )
elif i1ii1iIiI1 == 'install_content' : iiI1 ( o0oOOoo0O )
elif i1ii1iIiI1 == 'install_from_zip' : OO0OOoOOO ( )
elif i1ii1iIiI1 == 'instructions' : o0Oo00o0 ( )
elif i1ii1iIiI1 == 'instructions_1' : Iii1i11 ( )
elif i1ii1iIiI1 == 'instructions_2' : o0oOOoOo00o ( )
elif i1ii1iIiI1 == 'instructions_3' : oOOo ( )
elif i1ii1iIiI1 == 'instructions_4' : Instructions_4 ( )
elif i1ii1iIiI1 == 'instructions_5' : Instructions_5 ( )
elif i1ii1iIiI1 == 'instructions_6' : Instructions_6 ( )
elif i1ii1iIiI1 == 'keywords' : oOoO ( o0oOOoo0O )
elif i1ii1iIiI1 == 'kill_xbmc' : iI1i1iI1iI ( )
elif i1ii1iIiI1 == 'kodi_settings' : OoIII ( )
elif i1ii1iIiI1 == 'local_backup' : I1I111iiiIi11 ( )
elif i1ii1iIiI1 == 'LocalGUIDialog' : i1II1 ( )
elif i1ii1iIiI1 == 'log' : ii1O0oOOo ( )
elif i1ii1iIiI1 == 'manual_search' : o0oOOO0 ( o0oOOoo0O )
elif i1ii1iIiI1 == 'manual_search_builds' : Manual_Search_Builds ( )
elif i1ii1iIiI1 == 'news_root_menu' : Ooii ( o0oOOoo0O )
elif i1ii1iIiI1 == 'news_menu' : OOI1 ( o0oOOoo0O )
elif i1ii1iIiI1 == 'notify_msg' : o0o000O0ooo0O ( o0oOOoo0O )
elif i1ii1iIiI1 == 'open_system_info' : iIIiio000oo ( )
elif i1ii1iIiI1 == 'open_filemanager' : ooooooo0oOo0 ( )
elif i1ii1iIiI1 == 'openelec_backup' : o00oO00O0 ( )
elif i1ii1iIiI1 == 'openelec_settings' : o00oO00 ( )
elif i1ii1iIiI1 == 'OSS' : Oooo0O ( I1i11i , o0oOOoo0O , iii1IIIiiiI , IIIii )
elif i1ii1iIiI1 == 'play_video' : yt . PlayVideo ( o0oOOoo0O )
elif i1ii1iIiI1 == 'platform_menu' : ii1iiIiiiI11 ( o0oOOoo0O )
elif i1ii1iIiI1 == 'popular' : I1ii ( )
elif i1ii1iIiI1 == 'popularwizard' : OOOOO0oOOoO ( I1i11i , o0oOOoo0O , iii1IIIiiiI , IIIii )
elif i1ii1iIiI1 == 'register' : Ii1i1iiiIiIIiIiiii ( )
elif i1ii1iIiI1 == 'remove_addon_data' : O0OO0oOo00o0 ( )
elif i1ii1iIiI1 == 'remove_addons' : IiiiIiiI ( o0oOOoo0O )
elif i1ii1iIiI1 == 'remove_build' : oo0o0o ( )
elif i1ii1iIiI1 == 'remove_crash_logs' : IiiI11iIi ( )
elif i1ii1iIiI1 == 'remove_packages' : iiiiIIi11I1 ( )
elif i1ii1iIiI1 == 'remove_textures' : oO0O0o0o00 ( )
elif i1ii1iIiI1 == 'restore' : RESTORE ( )
elif i1ii1iIiI1 == 'restore_backup' : I1IiiI1I1I ( I1i11i , o0oOOoo0O , IIIii )
elif i1ii1iIiI1 == 'restore_community' : ooOO0O0O ( I1i11i , o0oOOoo0O , i1ii1I1I1 , IIIii , o00oIIi1i1 , iIO0OO0o0O00oO , o0O0ooooooo00 )
elif i1ii1iIiI1 == 'restore_local_CB' : I1II11Ii11iI1 ( o0oOOoo0O )
elif i1ii1iIiI1 == 'restore_local_gui' : Oo00o0o0O ( )
elif i1ii1iIiI1 == 'restore_local_OE' : iI11iI ( )
elif i1ii1iIiI1 == 'restore_openelec' : I111i1i ( o0oOOoo0O , IIIii )
elif i1ii1iIiI1 == 'restore_option' : oO0Ooo00O ( )
elif i1ii1iIiI1 == 'restore_zip' : ooo0Oo000o ( o0oOOoo0O )
elif i1ii1iIiI1 == 'run_addon' : o0OooOO0 ( o0oOOoo0O )
elif i1ii1iIiI1 == 'runtest' : speedtest . runtest ( o0oOOoo0O )
elif i1ii1iIiI1 == 'search_addons' : o00O00O0O0 ( o0oOOoo0O )
elif i1ii1iIiI1 == 'search_builds' : II111II1IiI ( o0oOOoo0O )
elif i1ii1iIiI1 == 'Search_Private' : Private_Search ( o0oOOoo0O )
elif i1ii1iIiI1 == 'showinfo' : iIIiiiIiiii11 ( o0oOOoo0O )
elif i1ii1iIiI1 == 'showinfo2' : II1i1II1iIi ( o0oOOoo0O )
elif i1ii1iIiI1 == 'SortBy' : i1iI1IIi1I ( BuildURL , type )
elif i1ii1iIiI1 == 'speed_instructions' : OO0o0 ( )
elif i1ii1iIiI1 == 'speedtest_menu' : III11i ( )
elif i1ii1iIiI1 == 'text_guide' : oooOoo ( I1i11i , o0oOOoo0O )
elif i1ii1iIiI1 == 'tools' : OOo ( )
elif i1ii1iIiI1 == 'tutorial_final_menu' : iiIIi1Ii1 ( o0oOOoo0O )
elif i1ii1iIiI1 == 'tutorial_addon_menu' : o0o00O0oO ( o0oOOoo0O )
elif i1ii1iIiI1 == 'tutorial_root_menu' : i1I1I1iiI ( )
elif i1ii1iIiI1 == 'unhide_passwords' : o00OOOOoOO ( )
elif i1ii1iIiI1 == 'update' : IIi1I1iiiii ( )
elif i1ii1iIiI1 == 'uploadlog' : O0O00 ( )
elif i1ii1iIiI1 == 'user_info' : I1I11I11iIII ( )
elif i1ii1iIiI1 == 'wipetools' : I1I111i1i1i ( )
elif i1ii1iIiI1 == 'xbmc_menu' : i1111ii1 ( o0oOOoo0O )
elif i1ii1iIiI1 == 'xbmcversion' : OOO0OoO00oOo ( o0oOOoo0O )
elif i1ii1iIiI1 == 'wipe_xbmc' : oOoOO00Ooo ( i1ii1iIiI1 )
xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) ) # dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
