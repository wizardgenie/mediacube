import urllib, urllib2, re, xbmcplugin, xbmcgui, xbmc, xbmcaddon, os, sys, time, xbmcvfs
import shutil
import time

#################################################
AddonID        = 'plugin.program.mediacube'
#################################################
dialog         =  xbmcgui.Dialog()
dp             =  xbmcgui.DialogProgress()
ADDON          =  xbmcaddon.Addon(id=AddonID)
ADDONDATA      =  xbmc.translatePath(os.path.join('special://home/userdata/addon_data',''))
TBSXML         =  xbmc.translatePath(os.path.join('special://home/addons/plugin.program.mediacube/addon.xml'))
firstrun       =  xbmc.translatePath('special://home/userdata/firstrun/')
sellername     =  ADDON.getSetting('resellername')
internetcheck  =  ADDON.getSetting('internetcheck')
cbnotifycheck  =  ADDON.getSetting('cbnotifycheck')
mynotifycheck  =  ADDON.getSetting('mynotifycheck')
idfile         =  xbmc.translatePath(os.path.join(ADDONDATA,AddonID,'id.xml'))
TBSDATA        =  xbmc.translatePath(os.path.join(ADDONDATA,AddonID,''))

if AddonID=='plugin.program.mediacube' and not os.path.exists('special://home/addons/plugin.program.mediacube/resources/troec.hgf'):
    localfile2      = open(TBSXML, mode='r')
    content2        = file.read(localfile2)
    file.close(localfile2)
    
    localnamematch  = re.compile('mediacube" name="(.+?)"').findall(content2)
    localnamecheck  = localnamematch[0] if (len(localnamematch) > 0) else 'TBS'
    print'###### '+localnamecheck+' Update Service ######'

if not os.path.exists(TBSDATA):
    os.makedirs(TBSDATA)

if not os.path.exists(idfile):
    localfile = open(idfile, mode='w+')
    localfile.write('id="None"\nname="None"')
    localfile.close()
	
if not os.path.exists(firstrun):
    xbmc.executebuiltin('XBMC.RunScript(special://home/addons/'+AddonID+'/notify.py)')
    xbmc.sleep(20000)
        
    if not os.path.exists(firstrun):
        choice = dialog.yesno("Install Packs Available",'[COLOR=gold]Would you like to view the packs available on this device?[/COLOR]','[COLOR=lime]IMPORTANT:[/COLOR] Packs may contain add-ons offering access to','content deemed unlawful in your country. Please check your local laws before installing.')
            
        if choice ==1:
            os.makedirs(firstrun)
            xbmc.executebuiltin('RunAddon(plugin.program.mediacube)')
            
        if choice ==0:
            dialog.ok('Vanilla Setup','You now have a vanilla Kodi setup, a complete blank','canvas to create to your own taste. If you wish to install','any content you can still find it in the [COLOR=lime]'+localnamecheck+'[/COLOR] add-on.')
            os.makedirs(firstrun)

			
while xbmc.Player().isPlaying():
    xbmc.sleep(500)
xbmc.executebuiltin('RunScript(special://home/addons/'+AddonID+'/notify.py)')

xbmc.executebuiltin('XBMC.AlarmClock(Notifyloop,XBMC.RunScript(special://home/addons/'+AddonID+'/notify.py,silent=true),00:30:00,silent,loop)')

if internetcheck == 'true':
    xbmc.executebuiltin('XBMC.AlarmClock(internetloop,XBMC.RunScript(special://home/addons/'+AddonID+'/connectivity.py,silent=true),00:00:30,silent,loop)')