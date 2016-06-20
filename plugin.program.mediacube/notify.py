import urllib, urllib2, re, xbmcplugin, xbmcgui, xbmc, xbmcaddon, os, sys, time
#################################################
AddonID        = 'plugin.program.mediacube'
#################################################
dialog         =  xbmcgui.Dialog()
ADDON          =  xbmcaddon.Addon(id=AddonID)
ADDONDATA      =  xbmc.translatePath(os.path.join('special://home','userdata','addon_data'))
TBSXML         =  xbmc.translatePath(os.path.join('special://home/addons/plugin.program.mediacube/addon.xml'))
sellername     =  ADDON.getSetting('resellername')
cbnotifycheck  =  ADDON.getSetting('cbnotifycheck')
idfile         =  xbmc.translatePath(os.path.join(ADDONDATA,AddonID,'id.xml'))
TBSDATA        =  xbmc.translatePath(os.path.join(ADDONDATA,AddonID,''))

print"#### MediaCube UPDATE SERVICE LOADED OK###"
def Notify_Check():
    print"#### MediaCube UPDATE SERVICE - CHECK FOR NOTIFICATION ###"
    isplaying = xbmc.Player().isPlaying()
    
    if isplaying == 0:
        tbsnotifypath = os.path.join(ADDONDATA,AddonID,'tbsnotification.txt')
        
        if not os.path.exists(tbsnotifypath):
            localfile = open(tbsnotifypath, mode='w+')
            localfile.write('20150101000000')
            localfile.close()
        
        datefile=open(tbsnotifypath, 'r')
        olddate = datefile.read()
        datefile.close()
        BaseURL1='http://camglomerate.com/wizard/notify.txt'
        BaseURL2='http://mediacube.co/notify.txt'
        try:
            link = Open_URL(BaseURL1).replace('\n','').replace('\r','')
            if 'notify="' in link:
                print"### MAIN URL OK"
            else:
                link = Open_URL(BaseURL2).replace('\n','').replace('\r','')
                print"### BACKUP URL USED"
        except:
            print"### No update URLs are resolving"
        notifymatch = re.compile('notify="(.+?)"').findall(link)
        notifymsg = notifymatch[0] if (len(notifymatch) > 0) else 'No news items available'
        datematch = re.compile('date="(.+?)"').findall(link)
        datecheck = datematch[0] if (len(datematch) > 0) else '10000000000000'
        cleantime = datecheck.replace('-','').replace(' ','').replace(':','')
        
        if int(olddate)<int(cleantime):
            print"New Notification Message from "+sellername
            dialog.ok('Update From '+sellername,notifymsg)
            localfile = open(tbsnotifypath, mode='w')
            localfile.write(cleantime)
            localfile.close()
        
        else:
            pass
            
def Open_URL(url):
    req      = urllib2.Request(url)
    req.add_header('User-Agent','Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
    response = urllib2.urlopen(req)
    link     = response.read()
    response.close()
    return link.replace('\r','').replace('\n','').replace('\t','')

Notify_Check()