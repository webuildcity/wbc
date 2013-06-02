import sys,os
sys.path.append('/home/jochen/code/bbs')
os.environ['DJANGO_SETTINGS_MODULE'] = 'bbs.settings'

from projekte.models import Bezirk,Projekt,Veroeffentlichung
from news.models import Abonent

for abonent in Abonent.objects.all():
    print abonent
    for bezirk in abonent.bezirke.all():
        print '->',bezirk
        for projekt in bezirk.projekte.all():
            print '--->',projekt
            for veroeffentlichung in projekt.veroeffentlichungen.all():
                print '----->',projekt
