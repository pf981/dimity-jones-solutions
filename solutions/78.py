import collections
import re

import decrypter

walls = [
    """ypyeypaseliwioksnaxoxdwaoswsws
lrlhtleasiwtskokaxobanoesesosw
ylrlyeaseiiwkoldxobnidwsenonnn
aearlrsrsswtoldnaiaraisesoynan
enroreeeeotskolorbrbraisenoaea
aeoreveehtwtskoeheiraineneneul
raroreretxiwtwkhtilodbohoynaec
lrlrwheehexiwestslflbohwnehocl
veyegwhenitxthtsdfdolbwseswhoc
ererninnknhtheidolfdflseseswan
rehwgnieriehserbdolflhwheswhna
erwgnigekrirbnkesdsdbrewhwhden
hwgnhgebsenkreibthdolashohside
lvegnigebsbnknnrbessolereoehen
reregniginseeginrabeueuararehi
byehwenigebsbiniaieuecluesareh
bbenhnenigegeginiesececluareri
oraeneeininieininracereclrehxh
ilraibvnengnnnrehlcerhtebibmom
ppwsesebeinnedireslrhtibihmode
ltiwilveeremseheserhtstssxedst
rhteanahyvhisfibeueuhthtiwisie
eiabfkwuoswiahgtoeceohtswdwiwm
rlbbiksreyatoeosbslodrhwdnandu
esotfolemaliopmareulsiwdnandpm
wblttobmlweotliraseuiwdwdwonmu
bxbbeoerasbelpterwsesiwawaitug
odimiiiwodiwhhatstararisiitpmu
ooaepdibsrfkptshxibihehdnaitpo
toalfoeihntlitsbhathxeerdnoiti""",
    """eseswbfincliedefotdadheheaotbe
anyenfefaluifisetoaehrurheahur
eanyoeainclrndenotdngyoueaouou
ulyonaeftaefiesengninourheadyo
eaenaafeftheffisiniwolrloaiygy
cnafinihnheffedidawolalaliwino
lifefndtaeafifededndadndowinif
afehnataepforififnuououawingua
nihtdnaepeotsririnnrnrndalgyou
ifehtdnaerfotorstgrgegrgrnddur
nifihtlirlafotstiygehthegthreh
buinefalerlafotosiehtmomemthre
nbnuniaupeatapopotelmororogegb
bubuoctaehenooeopowmorfrfrogtb
disnnestetfitehposewaoraromoho
innudsehvobrsktisitalmffarfrog
dbdnltorepawalntewawelesfarege
enrdilydyisemkoonalrnslfsrsheg
nbuasilndaeaamneruturrerfleegr
buteifoureptsothnrurnetesearri
uteylyundaeaepoelnrteletesfaou
alisilrdrefthepoefninelelesfai
iglieletriososppataninelslffru
gelblbrrelfpetsdnandninersardn
elbabaitbiletstsdndniletslrfrs
lbakriarebipetotndsewslssrfrew
elbmagitrtbsfefoololbwstffrifo
gemeribitrofehwowofoloeigrgtle
nramstetssfehtsloholoertifikot
mkrarstsstofehtofwfolrtitaoisf""",
    """rartlorgdhedhebzbkttkoteobwsne
bwsneweeirartlorgdhedhebzottek
bttakotebbwsneweeirartlorgdhed
gdhedhebzedtikotesbwsneweeirar
eirartlorgdhedhebzrtttkotetbws
enbwsneweeirartlorgdhedhebzsnt
bznrttkotebbwsneweeirartlorgdh
orgdhedhebzwettkoterbwsneweeir
weeirartlorgdhedhebzoatskotesb
oterbwsneweeirartlorgdhedhebze
hebzhrttkoteebwsneweeirartlorg
tlorgdhedhebzdktskotehbwsnewee
neweeirartlorgdhedhebzsttbkote
tkoteebwsneweeirartlorgdhedheb
edhebzletrkotetbwsneweeirartlo
artlorgdhedhebzsetdkotetbwsnew
wsneweeirartlorgdhedhebzwrtdko
btwkoteabwsneweeirartlorgdhedh
dhedhebzsdtokoterbwsneweeirart
irartlorgdhedhebzgrtlkoteebwsn
tbwsneweeirartlorgdhedhebzwtta
zrsttkoteebwsneweeirartlorgdhe
rgdhedhebzhetdkoteebwsneweeira
eeirartlorgdhedhebzlrtekoterbw
teibwsneweeirartlorgdhedhebzeb
ebzrttbkoteibwsneweeirartlorgd
lorgdhedhebzlrthkotetbwsneweei
eweeirartlorgdhedhebzrwtnkotee
kotebbwsneweeirartlorgdhedhebz
dhebzrhttkoteebwsneweeirartlor
""",
    """rbggbrbeegerbifgbeigeebelfbbbr
ttbieebflerteiilibetgbbggbbtrb
beirbbibbitribibttebiilebiefib
iilbiftiibtbbblbetebietbieibeb
lgrtifebleitiieiigblibbibeeirt
bigtbbtigigibibbligfrbbielbgli
gegebtbbtgibrigiebbielibbebeli
trbbitbeligebbilfbbbittgtgtibb
befbiifbfeettbfeieifiiiitbiebb
libfribbbietrbfiiibbgieigbiftb
fitbtitfbertetbbgbbbbfettifigf
ifbttrfbeflitrfiibgttiliiifttl
rtebeibbgebgifbleteetegblgiebg
tirbreireigbiftitblilttbiliief
eiritbbfrtibtffbbibifeieerebfi
ebifigilebbbebiffblegiigbiebii
bbeblibbefiffbieebettfgibbbter
rligiftbtfltbbtifbrlrrlebebttb
bebbbtgreteiriiiibrebigbbeligg
begibeieibifebebgrtbritbitebie
ebeeiliibgtferbfbifrbtrigbitfb
beflfbiibbbtbiebtriibebtttttgl
ftbbirifbtifeiteeeibebgltegfrt
lrfgbieibifeftiblfbibbibribbie
ibiirilbieefiibirtgbfefpietftf
bblttbbbgribieblfletebtebfeelb
ibbtrbifiigifbbtbrlebletlbtllf
gtegfbbbbrfliigrrbltbgbtbigbgb
bibbeebbltirbiigetileilrtgtrgb
ibrtlibgbtbbebilbitibtigttebib""",
    """tmhereheyrammieeodanieeeececes
mhmlliltoeyhrtdsihesmieeyticir
odanmdhieryshioemdetriedheshyd
rcmidilnritetmontmcicsryoehhdt
meecetiehdiedhymemitrmeortimoe
mmlhitthrciistrhedeersrhhtcmoi
htmishshoieertiiemneihhyhmentd
ahttheyeeordtahlmammlemamcrnee
tddahdrnyohihnhhtmmomelleteecm
ymeeatssiimrldclehylhheoityaie
amcnsaiseeyddcccmmtemhietciieh
ynaeilieyemytlehmteaiahhmarimi
oycmrlrleriethheliisrieihdtttc
mhrlmlmilheteimhteonnmnssdemlh
mryinyedhtaeeeeedsycioadiyeene
teleteremsamhmmiieymientmhhmen
reistmrrhchrtemmeltdtmmtcymhte
shmlttenmhhlmmilamnetteehmlsrt
oytiecsmhtitthhictmthsmehtmein
imsldhostnmhmommhiddhhtardlhmh
taimtnaeetmsestriedhhenntatrry
rrernmeyeheoeemdshmtneeeedlist
eairrteecymhhneeeammersertthet
hlychniirmtneteetheosnaeeiimri
inileirarmhrimmecseeosrmecyeei
edlcemetmetimiirmoiintiyrsemem
eamctmcemmohmeiyeaeheeeishihhy
esiersieieimilyatcssimdsnthsts
lrdesimaalomerdsimimhmylciemed
ysaedhoyitolarmziimiltmnhschtm""",
    """inmmhhahdihtcyemrirrsrlmseimet
enmieshtahmhtihtemrhyrrohecrih
hehncetilmttnieirmdedncyhmsena
tciermihimeiitmtcslcoehreidasm
lrcimmaddtecdehaoieehhemsledel
hemmtitsrhmimmeiemymeeriseieml
lyenhhiicherathiieirmdetosmlel
hlcereoieiaythicmemieecmietiyl
ethmhemrsthtomyemiinemeymmdeee
tlcyemseoamrenrtctmcdolnyhoire
eeremmtlohtoihlehmmdsmmthtcsmr
neanarrtdennmthemstdnmtrmdhete
eeerettcioelisicdteynnrtsmmtil
srottetoealrteadtlmysylmreehci
lmmleteeiiseoeehitccoimimimoyi
ltteatedcsmdyeoehersnaihdieyat
mmmiymemimhirehoheaeimrmieitei
honrmnllsetseoemererttmyheisme
hmoyeimymrreamochtmesthemhtcea
iemoeioinhmhsiooreotldoemaeodh
dtehdhaeetsnhmrrdrdnhlmchimhce
sremidiasdyilernancerheecemhei
tllomiiilaohsetaecerneerdmlrii
hoeyhnmhmnmhaoserneteeiricmeet
trthmrimmhhildcsdtyemetidyhiei
ymditdcacittsmimyiacmmmirirenn
tseedeseeehhisletcmtdcisiencht
meeimedothrootsimelmhehycmiyhc
yoedeodnhotlatmdereceteimehsim
nnmytthmmheeoneeohdirltatcemeh""",
]

walls = [wall.splitlines() for wall in walls]

text = """They took the door to the left marked "Write this letter". They took the door to the right marked "Write this letter". They took the door to the right marked "Write this letter twice". They took the door straight ahead marked "Write this letter". They took the door to the left marked "Write this letter". They took the door to the left marked "Write this letter followed by a space". They took the door to the right marked "Write this letter". They took the door to the left marked "Write this letter". They backtracked. They took the door straight ahead marked "Write this letter". They took the door straight ahead marked "Write this letter followed by a space". They took the door to the right marked "Write this letter". They took the door straight ahead marked "Write this letter twice". They took the door to the left marked "Write this letter". They backtracked. They backtracked. They took the door to the right marked "Write this letter twice". They took the door straight ahead marked "Write this letter". They took the door to the left marked "Write this letter". They took the door to the left marked "Write this letter". They backtracked. They took the door straight ahead marked "Write this letter". They took the door to the left marked "Write this letter". They backtracked. They backtracked. "This is so stupid," Leland moaned. They took the door to the right marked "Write this letter". They took the door straight ahead marked "Write this letter". They took the door to the left marked "Write this letter". They backtracked. They took the door straight ahead marked "Write this letter". They took the door straight ahead marked "Write this letter followed by a space". They took the door to the right marked "Write this letter". They backtracked. They took the door straight ahead marked "Write this letter". They took the door to the right marked "Write this letter twice with a space in between". They backtracked. They took the door straight ahead marked "Write this letter twice with a space in between". They took the door straight ahead marked "Write this letter". They took the door straight ahead marked "Write this letter". They took the door straight ahead marked "Write this letter twice". They backtracked. They took the door to the left marked "Write this letter twice". They backtracked. They backtracked. They backtracked. They took the door to the left marked "Write this letter". They took the door to the left marked "Write this letter". They took the door to the right marked "Write this letter twice". They took the door to the right marked "Write this letter". They took the door straight ahead marked "Write this letter". They backtracked. They took the door to the right marked "Write this letter". They took the door to the left marked "Write this letter". They backtracked. They took the door straight ahead marked "Write this letter". They backtracked. They backtracked. They backtracked. They took the door straight ahead marked "Write this letter". They took the door straight ahead marked "Write this letter". They took the door straight ahead marked "Write this letter". They took the door to the right marked "Write this letter". They backtracked. They backtracked. They took the door to the right marked "Write this letter". They backtracked. They backtracked. They took the door to the left marked "Write this letter". They took the door to the left marked "Write this letter". They took the door to the right marked "Write this letter". They took the door straight ahead marked "Write this letter". They took the door to the right marked "Write this letter". They backtracked. They took the door straight ahead marked "Write this letter". They took the door to the left marked "Write this letter twice". They took the door to the right marked "Write this letter". They took the door straight ahead marked "Write this letter". They backtracked. They took the door to the left marked "Write this letter". They took the door to the left marked "Write this letter then start a new line". They backtracked. They took the door to the left marked "Write this letter then start a new line". They took the door to the right marked "Write this letter capitalized". They took the door to the left marked "Write this letter". They took the door straight ahead marked "Write this letter". They took the door to the left marked "Write this letter". They backtracked. They backtracked. They took the door to the right marked "Write this letter". They took the door straight ahead marked "Write this letter". They took the door to the left marked "Write this letter". They backtracked. They took the door straight ahead marked "Write this letter". They took the door straight ahead marked "Write this letter". They backtracked. They backtracked. They backtracked. They backtracked. "I hate this goddamn stupid labyrinth!" cried Leland. They took the door straight ahead marked "Write this letter". They took the door to the right marked "Write this letter". They took the door to the left marked "Write this letter". They took the door to the left marked "Write this letter". They took the door to the right marked "Write this letter". They took the door straight ahead marked "Write this letter". They backtracked. They took the door to the right marked "Write this letter". They took the door to the right marked "Write this letter". They took the door to the left marked "Write this letter followed by a space". They took the door to the right marked "Write this letter". They backtracked. They backtracked. They backtracked. They took the door to the right marked "Write this letter". They backtracked. They backtracked. They took the door straight ahead marked "Write this letter". They took the door to the left marked "Write this letter". They backtracked. They backtracked. They backtracked. They took the door to the right marked "Write this letter". They took the door to the left marked "Write this letter". They backtracked. They took the door to the left marked "Write this letter". They took the door straight ahead marked "Write this letter". They backtracked. They took the door to the right marked "Write this letter". They took the door to the right marked "Write this letter followed by a space". They took the door to the left marked "Write this letter". They backtracked. They took the door to the left marked "Write this letter". They took the door straight ahead marked "Write this letter". They backtracked. They took the door to the left marked "Write this letter". They took the door to the left marked "Write this letter". They backtracked. They took the door to the left marked "Write this letter". They backtracked. They backtracked. They took the door straight ahead marked "Write this letter". They took the door to the right marked "Write this letter". They took the door straight ahead marked "Write this letter". They took the door to the right marked "Write this letter". They backtracked. They took the door straight ahead marked "Write this letter". They took the door straight ahead marked "Write this letter". They backtracked. They backtracked. They took the door to the left marked "Write this letter". They took the door straight ahead marked "Write this letter". They backtracked. They took the door to the right marked "Write this letter". They took the door straight ahead marked "Write this letter". They took the door to the right marked "Write this letter followed by a space". They backtracked. They backtracked. They backtracked. They took the door straight ahead marked "Write this letter". They took the door straight ahead marked "Write this letter". They took the door straight ahead marked "Write this letter followed by a space". They took the door straight ahead marked "Write this letter". They took the door to the right marked "Write this letter". They took the door straight ahead marked "Write this letter followed by a space". They took the door to the left marked "Write this letter". They took the door straight ahead marked "Write this letter". They took the door straight ahead marked "Write this letter". They took the door straight ahead marked "Write this letter". They took the door straight ahead marked "Write this letter". They took the door to the right marked "Write this letter followed by a space". They took the door to the right marked "Write this letter". They backtracked. They backtracked. They backtracked. They backtracked. They backtracked. They backtracked. They backtracked. They backtracked. They took the door to the left marked "Write this letter followed by a space". They backtracked. They backtracked. They backtracked. They took the door to the right marked "Write this letter". They took the door straight ahead marked "Write this letter". They took the door to the left marked "Write this letter followed by a space". They took the door to the right marked "Write this letter". They backtracked. They took the door to the right marked "Write this letter". They took the door straight ahead marked "Write this letter". They took the door to the right marked "Write this letter". They took the door to the left marked "Write this letter". They backtracked. They backtracked. They backtracked. They backtracked. They took the door to the right marked "Write this letter". They backtracked. They backtracked. They took the door to the left marked "Write this letter followed by a space". They took the door straight ahead marked "Write this letter". They took the door straight ahead marked "Write this letter". They took the door straight ahead marked "Write this letter". They backtracked. They backtracked. They backtracked. They took the door to the left marked "Write this letter". They backtracked. They backtracked. They backtracked. They took the door to the left marked "Write this letter". They took the door to the left marked "Write this letter followed by a space". They took the door to the right marked "Write this letter". They took the door straight ahead marked "Write this letter". They took the door straight ahead marked "Write this letter". They backtracked. They backtracked. They backtracked. They backtracked. They took the door to the left marked "Write this letter followed by a space". They took the door to the right marked "Write this letter". They took the door to the left marked "Write this letter". They backtracked. They took the door to the left marked "Write this letter". They took the door to the left marked "Write this letter". They took the door straight ahead marked "Write this letter". They took the door straight ahead marked "Write this letter". They took the door to the left marked "Write this letter followed by a space". They took the door to the left marked "Write this letter". They took the door to the right marked "Write this letter". They took the door to the right marked "Write this letter". They took the door straight ahead marked "Write this letter". They took the door to the left marked "Write this letter". They backtracked. They backtracked. They took the door to the right marked "Write this letter". They took the door straight ahead marked "Write this letter". They took the door straight ahead marked "Write this letter". They took the door to the right marked "Write this letter". They backtracked. They took the door straight ahead marked "Write this letter". They took the door to the left marked "Write this letter followed by a period then skip a line". They backtracked. They took the door straight ahead marked "Write this letter followed by a period then skip a line". They took the door to the left marked "Write this letter capitalized". They backtracked. They took the door to the left marked "Write this letter capitalized". They took the door straight ahead marked "Write this letter". They backtracked. They backtracked. They took the door to the left marked "Write this letter capitalized". They took the door to the left marked "Write this letter". They took the door straight ahead marked "Write this letter". They took the door to the right marked "Write this letter twice followed by a space". They backtracked. They backtracked. They backtracked. They took the door to the left marked "Write this letter". They took the door straight ahead marked "Write this letter". They took the door straight ahead marked "Write this letter twice followed by a space". They took the door to the left marked "Write this letter". They backtracked. They took the door to the left marked "Write this letter". They backtracked. They backtracked. They took the door to the left marked "Write this letter twice followed by a space". They took the door to the left marked "Write this letter". They took the door straight ahead marked "Write this letter". They took the door straight ahead marked "Write this letter". They took the door straight ahead marked "Write this letter". They took the door straight ahead marked "Write this letter followed by a space". They took the door to the left marked "Write this letter". They took the door to the right marked "Write this letter". They took the door to the right marked "Write this letter followed by a space". They backtracked. They backtracked. They backtracked. They backtracked. They backtracked. They backtracked. They backtracked. They took the door to the left marked "Write this letter". They took the door straight ahead marked "Write this letter". They took the door to the left marked "Write this letter". They took the door to the right marked "Write this letter followed by a space". They took the door straight ahead marked "Write this letter". They backtracked. They took the door to the left marked "Write this letter". They took the door straight ahead marked "Write this letter". They took the door to the left marked "Write this letter followed by a space". They took the door straight ahead marked "Write this letter". They took the door to the left marked "Write this letter". They took the door to the left marked "Write this letter". They backtracked. Leland groaned, "We're just going in circles!" They took the door straight ahead marked "Write this letter". They backtracked. They took the door to the right marked "Write this letter". They took the door to the right marked "Write this letter followed by a space". They took the door to the left marked "Write this letter". They backtracked. They took the door to the left marked "Write this letter". They took the door to the left marked "Write this letter". They backtracked. They took the door to the left marked "Write this letter". They backtracked. They took the door to the left marked "Write this letter". They took the door to the left marked "Write this letter twice". They took the door to the right marked "Write this letter". They took the door straight ahead marked "Write this letter followed by a space". They took the door to the left marked "Write this letter". They took the door to the right marked "Write this letter". They took the door to the left marked "Write this letter followed by a space". They took the door straight ahead marked "Write this letter". They took the door to the left marked "Write this letter". They took the door to the right marked "Write this letter". They took the door to the left marked "Write this letter". They took the door straight ahead marked "Write this letter". They took the door to the right marked "Write this letter followed by a space". They took the door to the left marked "Write this letter". They took the door straight ahead marked "Write this letter". They backtracked. They took the door to the left marked "Write this letter". They backtracked. They took the door straight ahead marked "Write this letter". They took the door to the right marked "Write this letter". They backtracked. They took the door to the right marked "Write this letter". They took the door to the right marked "Write this letter". They backtracked. They took the door to the right marked "Write this letter". They backtracked. They took the door to the right marked "Write this letter". They took the door straight ahead marked "Write this letter followed by a colon then start a new line". They took the door to the right marked "Write this letter capitalized". They backtracked. They backtracked. They took the door to the left marked "Write this letter followed by a colon then start a new line". They backtracked. They backtracked. They backtracked. They backtracked. They backtracked. They backtracked. They backtracked. They backtracked. They took the door to the left marked "Write this letter". They took the door straight ahead marked "Write this letter". They took the door to the left marked "Write this letter followed by a space". They backtracked. They backtracked. They backtracked. They took the door to the left marked "Write this letter". They took the door straight ahead marked "Write this letter". They took the door to the right marked "Write this letter followed by a space". They backtracked. They took the door straight ahead marked "Write this letter followed by a space". They took the door to the left marked "Write this letter". They took the door to the right marked "Write this letter". They took the door to the right marked "Write this letter". They backtracked. They took the door to the right marked "Write this letter". They took the door to the left marked "Write this letter". They took the door to the right marked "Write this letter followed by a colon then start a new line". They backtracked. They backtracked. They took the door straight ahead marked "Write this letter". They took the door straight ahead marked "Write this letter followed by a colon then start a new line". They backtracked. They took the door to the right marked "Write this letter followed by a colon then start a new line". They took the door to the left marked "Write this letter capitalized". They took the door to the right marked "Write this letter". They took the door straight ahead marked "Write this letter". They took the door to the left marked "Write this letter". They took the door to the right marked "Write this letter". They backtracked. They took the door straight ahead marked "Write this letter". They took the door to the right marked "Write this letter twice with a space in between". They took the door to the left marked "Write this letter". They backtracked. They backtracked. They backtracked. They backtracked. They took the door straight ahead marked "Write this letter". They took the door to the right marked "Write this letter". They backtracked. They took the door straight ahead marked "Write this letter". They took the door to the left marked "Write this letter twice with a space in between". They backtracked. They took the door straight ahead marked "Write this letter twice with a space in between". They took the door to the left marked "Write this letter". They took the door straight ahead marked "Write this letter followed by a space". They backtracked. They took the door to the right marked "Write this letter followed by a space". They took the door straight ahead marked "Write this letter". They took the door straight ahead marked "Write this letter". They took the door to the right marked "Write this letter". They backtracked. They took the door to the right marked "Write this letter". They took the door to the left marked "Write this letter followed by a space". They took the door straight ahead marked "Write this letter". They backtracked. They took the door to the left marked "Write this letter". They took the door to the right marked "Write this letter". They took the door to the left marked "Write this letter". They took the door to the right marked "Write this letter followed by a space". They backtracked. They backtracked. They took the door to the left marked "Write this letter". They took the door to the right marked "Write this letter followed by a space". They took the door to the left marked "Write this letter". They took the door to the right marked "Write this letter followed by a space". They took the door straight ahead marked "Write this letter". They took the door to the left marked "Write this letter". They took the door to the left marked "Write this letter followed by a space". They took the door straight ahead marked "Write this letter". They backtracked. They backtracked. They took the door straight ahead marked "Write this letter followed by a space". They took the door straight ahead marked "Write this letter". They took the door to the right marked "Write this letter twice". They backtracked. They took the door to the right marked "Write this letter twice". They backtracked. They backtracked. They took the door to the left marked "Write this letter". They took the door straight ahead marked "Write this letter twice". They took the door to the right marked "Write this letter". They backtracked. They backtracked. They backtracked. They backtracked. They backtracked. They backtracked. They backtracked. They took the door straight ahead marked "Write this letter followed by a space". They took the door straight ahead marked "Write this letter". They took the door straight ahead marked "Write this letter". They took the door straight ahead marked "Write this letter followed by a space". They took the door to the right marked "Write this letter". They took the door to the left marked "Write this letter twice". They took the door to the right marked "Write this letter". They backtracked. They backtracked. They took the door straight ahead marked "Write this letter twice". They backtracked. They took the door to the right marked "Write this letter twice". They took the door to the right marked "Write this letter". They took the door to the left marked "Write this letter". They took the door to the right marked "Write this letter". They took the door to the left marked "Write this letter". They backtracked. They backtracked. They backtracked. They took the door to the left marked "Write this letter". They took the door to the right marked "Write this letter". They took the door to the left marked "Write this letter". They took the door to the left marked "Write this letter followed by a space". They took the door straight ahead marked "Write this letter". They took the door straight ahead marked "Write this letter". They backtracked. They took the door to the left marked "Write this letter". They took the door to the left marked "Write this letter twice followed by a semicolon then start a new line". They took the door to the right marked "Write this letter capitalized". They took the door to the right marked "Write this letter". They took the door straight ahead marked "Write this letter". They took the door to the right marked "Write this letter followed by a space". They backtracked. They backtracked. They backtracked. They took the door straight ahead marked "Write this letter". They took the door straight ahead marked "Write this letter". They took the door to the left marked "Write this letter followed by a space". They backtracked. "I want my mom," Leland grunted. They took the door straight ahead marked "Write this letter followed by a space". They backtracked. They backtracked. They took the door to the right marked "Write this letter". They backtracked. They took the door straight ahead marked "Write this letter". They backtracked. They backtracked. They took the door to the left marked "Write this letter". They took the door straight ahead marked "Write this letter". They backtracked. They took the door to the left marked "Write this letter". They took the door to the left marked "Write this letter followed by a space". They backtracked. They took the door to the left marked "Write this letter followed by a space". They took the door to the left marked "Write this letter". They took the door straight ahead marked "Write this letter". They took the door to the left marked "Write this letter". They took the door to the right marked "Write this letter followed by a space". They took the door to the left marked "Write this letter". They took the door to the left marked "Write this letter". They backtracked. They backtracked. They took the door straight ahead marked "Write this letter". They took the door to the left marked "Write this letter". They took the door to the right marked "Write this letter followed by a comma and a space". They backtracked. They took the door to the right marked "Write this letter followed by a comma and a space". They took the door straight ahead marked "Write this letter". They backtracked. They backtracked. They backtracked. They backtracked. They took the door to the right marked "Write this letter". They took the door straight ahead marked "Write this letter". They took the door straight ahead marked "Write this letter followed by a comma and a space". They backtracked. They took the door to the right marked "Write this letter followed by a comma and a space". They backtracked. They backtracked. They took the door to the right marked "Write this letter". They took the door straight ahead marked "Write this letter followed by a comma and a space". They took the door straight ahead marked "Write this letter". They took the door straight ahead marked "Write this letter". They took the door straight ahead marked "Write this letter". They backtracked. They backtracked. They took the door to the left marked "Write this letter". They took the door to the right marked "Write this letter". They took the door to the left marked "Write this letter followed by a space". They backtracked. They backtracked. They backtracked. They backtracked. They took the door to the right marked "Write this letter". They took the door straight ahead marked "Write this letter". They backtracked. They took the door to the left marked "Write this letter". They took the door straight ahead marked "Write this letter". They took the door straight ahead marked "Write this letter followed by a space". They backtracked. They backtracked. They took the door to the right marked "Write this letter". They took the door straight ahead marked "Write this letter followed by a space". They backtracked. They took the door to the left marked "Write this letter followed by a space". They took the door to the left marked "Write this letter". They backtracked. They took the door to the left marked "Write this letter". They took the door to the left marked "Write this letter". They took the door to the right marked "Write this letter twice". They backtracked. They took the door to the right marked "Write this letter twice". They took the door straight ahead marked "Write this letter". They took the door to the right marked "Write this letter". They backtracked. They backtracked. They took the door to the left marked "Write this letter". They backtracked. They took the door straight ahead marked "Write this letter". They took the door to the right marked "Write this letter". They took the door straight ahead marked "Write this letter followed by a space". They took the door to the right marked "Write this letter". They backtracked. They took the door to the right marked "Write this letter". They took the door to the left marked "Write this letter". They backtracked. They took the door straight ahead marked "Write this letter". They took the door straight ahead marked "Write this letter twice followed by a space". They took the door straight ahead marked "Write this letter". They took the door straight ahead marked "Write this letter". They backtracked. They took the door to the right marked "Write this letter". They took the door to the right marked "Write this letter followed by a space". They backtracked. They backtracked. They backtracked. They took the door to the left marked "Write this letter". They backtracked. They took the door straight ahead marked "Write this letter". They took the door straight ahead marked "Write this letter". They took the door straight ahead marked "Write this letter followed by a space". They took the door to the right marked "Write this letter". They took the door straight ahead marked "Write this letter". They took the door straight ahead marked "Write this letter". They backtracked. They backtracked. They took the door to the left marked "Write this letter". They took the door to the left marked "Write this letter". They took the door straight ahead marked "Write this letter followed by a space". They backtracked. They backtracked. They backtracked. They took the door straight ahead marked "Write this letter". They took the door to the right marked "Write this letter". They took the door to the left marked "Write this letter followed by a space". They took the door to the right marked "Write this letter". They took the door straight ahead marked "Write this letter". They took the door to the right marked "Write this letter followed by a space". They took the door to the right marked "Write this letter". They backtracked. They took the door straight ahead marked "Write this letter". They took the door straight ahead marked "Write this letter". They backtracked. They backtracked. They took the door to the left marked "Write this letter". They backtracked. They backtracked. They backtracked. They backtracked. They backtracked. "I'm tired," murmured Leland. They backtracked. They backtracked. They backtracked. They took the door straight ahead marked "Write this letter". They took the door to the left marked "Write this letter". They backtracked. They took the door straight ahead marked "Write this letter". They took the door straight ahead marked "Write this letter". They took the door to the right marked "Write this letter followed by a space". They backtracked. They backtracked. They backtracked. They took the door to the right marked "Write this letter". They took the door to the left marked "Write this letter". They took the door straight ahead marked "Write this letter followed by a space". They backtracked. They backtracked. They took the door to the left marked "Write this letter". They took the door straight ahead marked "Write this letter followed by a space". They backtracked. They backtracked. They took the door to the left marked "Write this letter". They took the door straight ahead marked "Write this letter followed by a space". They took the door straight ahead marked "Write this letter". They took the door to the right marked "Write this letter". They took the door straight ahead marked "Write this letter followed by a space". They took the door to the left marked "Write this letter". They backtracked. They backtracked. They backtracked. They took the door straight ahead marked "Write this letter". They took the door straight ahead marked "Write this letter followed by a space". They backtracked. They took the door to the left marked "Write this letter followed by a space". They took the door to the right marked "Write this letter". They took the door straight ahead marked "Write this letter". They backtracked. They took the door to the right marked "Write this letter". They took the door straight ahead marked "Write this letter". They took the door to the left marked "Write this letter". They backtracked. They took the door straight ahead marked "Write this letter". They took the door to the left marked "Write this letter". They took the door to the left marked "Write this letter followed by a comma then start a new line". They took the door straight ahead marked "Write this letter capitalized". They backtracked. They took the door to the left marked "Write this letter capitalized". They took the door to the left marked "Write this letter twice". They took the door to the right marked "Write this letter". They backtracked. They took the door to the right marked "Write this letter". They took the door straight ahead marked "Write this letter". They took the door to the right marked "Write this letter". They took the door straight ahead marked "Write this letter". They took the door to the left marked "Write this letter followed by a space". They backtracked. They backtracked. They took the door to the right marked "Write this letter". They backtracked. They backtracked. They backtracked. They took the door to the left marked "Write this letter". They took the door straight ahead marked "Write this letter". They took the door to the right marked "Write this letter". They took the door to the left marked "Write this letter followed by a space". They took the door to the right marked "Write this letter". They took the door to the right marked "Write this letter". They backtracked. They took the door to the right marked "Write this letter". They took the door to the right marked "Write this letter". They took the door to the left marked "Write this letter followed by a space". They backtracked. They backtracked. They took the door straight ahead marked "Write this letter". They took the door to the left marked "Write this letter followed by a space". They took the door straight ahead marked "Write this letter". They took the door straight ahead marked "Write this letter". They took the door to the right marked "Write this letter". They took the door to the right marked "Write this letter followed by a space". They backtracked. They took the door straight ahead marked "Write this letter followed by a space". They backtracked. They backtracked. They took the door to the right marked "Write this letter". They took the door to the left marked "Write this letter followed by a space". They took the door to the right marked "Write this letter". They took the door to the right marked "Write this letter twice with a space in between". They backtracked. They took the door to the right marked "Write this letter twice with a space in between". They took the door straight ahead marked "Write this letter". They took the door straight ahead marked "Write this letter followed by a space". They backtracked. They backtracked. They took the door to the right marked "Write this letter". They took the door to the right marked "Write this letter followed by a space". They took the door to the left marked "Write this letter". They took the door to the left marked "Write this letter". They backtracked. They took the door straight ahead marked "Write this letter". They took the door to the left marked "Write this letter". They backtracked. "Dimity, I can't go on," said Leland. They backtracked. "Sure you can," said Dimity. They took the door to the right marked "Write this letter". They took the door to the left marked "Write this letter". They backtracked. They took the door to the left marked "Write this letter". They took the door to the left marked "Write this letter followed by a space". They backtracked. They took the door straight ahead marked "Write this letter followed by a space". They took the door straight ahead marked "Write this letter". They backtracked. They took the door to the right marked "Write this letter". They took the door to the right marked "Write this letter". They took the door straight ahead marked "Write this letter". They backtracked. They backtracked. They took the door to the right marked "Write this letter". They took the door straight ahead marked "Write this letter". They backtracked. They took the door to the left marked "Write this letter". They took the door straight ahead marked "Write this letter". They took the door straight ahead marked "Write this letter twice with a space in between". They took the door straight ahead marked "Write this letter followed by a space". They took the door to the right marked "Write this letter". They backtracked. They took the door straight ahead marked "Write this letter". They backtracked. They backtracked. They backtracked. They took the door to the right marked "Write this letter twice with a space in between". They took the door to the left marked "Write this letter followed by a space". They backtracked. They took the door straight ahead marked "Write this letter followed by a space". They took the door to the left marked "Write this letter". They took the door to the right marked "Write this letter". They took the door to the left marked "Write this letter twice followed by a comma then skip a line". They backtracked. They took the door to the left marked "Write this letter twice followed by a comma then skip a line". They took the door straight ahead marked "Write this letter capitalized". They backtracked. They took the door to the right marked "Write this letter capitalized". They backtracked. They took the door straight ahead marked "Write this letter capitalized". They took the door straight ahead marked "Write this letter". They took the door to the left marked "Write this letter". They took the door straight ahead marked "Write this letter". They backtracked. They backtracked. They took the door to the left marked "Write this letter". They took the door to the left marked "Write this letter". They took the door straight ahead marked "Write this letter". They took the door straight ahead marked "Write this letter followed by a semicolon and a space". They took the door straight ahead marked "Write this letter". They took the door to the right marked "Write this letter". They took the door to the right marked "Write this letter followed by a space". They took the door straight ahead marked "Write this letter". They took the door to the left marked "Write this letter". They took the door straight ahead marked "Write this letter followed by a space". They took the door straight ahead marked "Write this letter". They backtracked. They took the door to the left marked "Write this letter". They backtracked. They took the door straight ahead marked "Write this letter". They took the door to the left marked "Write this letter". They backtracked. They backtracked. They backtracked. They backtracked. They backtracked. They backtracked. They backtracked. They took the door to the right marked "Write this letter". They backtracked. They backtracked. They took the door to the right marked "Write this letter". They took the door straight ahead marked "Write this letter". They backtracked. They took the door to the left marked "Write this letter". They took the door straight ahead marked "Write this letter followed by a space". They took the door to the left marked "Write this letter". They backtracked. They took the door to the left marked "Write this letter". They took the door straight ahead marked "Write this letter". They took the door to the right marked "Write this letter followed by a space". They took the door to the left marked "Write this letter". They took the door to the right marked "Write this letter". They took the door straight ahead marked "Write this letter". They took the door straight ahead marked "Write this letter". They backtracked. They backtracked. They backtracked. They backtracked. They backtracked. Leland clutched his head by the ears and screamed wordlessly. They took the door straight ahead marked "Write this letter followed by a space". They took the door straight ahead marked "Write this letter". They backtracked. They took the door to the left marked "Write this letter". They took the door to the right marked "Write this letter". They backtracked. They took the door straight ahead marked "Write this letter". They backtracked. They took the door to the left marked "Write this letter". They took the door to the right marked "Write this letter". They took the door straight ahead marked "Write this letter". They took the door to the left marked "Write this letter followed by a space". They took the door to the left marked "Write this letter". They backtracked. They took the door to the left marked "Write this letter". They backtracked. They took the door to the left marked "Write this letter". They backtracked. They backtracked. They took the door to the left marked "Write this letter followed by a space". They took the door straight ahead marked "Write this letter". They took the door to the left marked "Write this letter". They took the door straight ahead marked "Write this letter". They took the door to the right marked "Write this letter followed by a space". They took the door straight ahead marked "Write this letter". They took the door straight ahead marked "Write this letter". They backtracked. They backtracked. They took the door to the right marked "Write this letter". They took the door to the right marked "Write this letter". They took the door to the left marked "Write this letter". They took the door to the left marked "Write this letter". They took the door to the right marked "Write this letter". They backtracked. They took the door to the right marked "Write this letter". They backtracked. They backtracked. They backtracked. They backtracked. They backtracked. They backtracked. They took the door straight ahead marked "Write this letter followed by a space". They backtracked. They took the door to the left marked "Write this letter followed by a space". They took the door to the left marked "Write this letter". They took the door to the right marked "Write this letter". They took the door straight ahead marked "Write this letter". They took the door straight ahead marked "Write this letter". They took the door to the right marked "Write this letter". They took the door to the right marked "Write this letter followed by a space". They backtracked. They took the door straight ahead marked "Write this letter followed by a space". They backtracked. They backtracked. They took the door straight ahead marked "Write this letter". They took the door straight ahead marked "Write this letter followed by a space". They took the door to the left marked "Write this letter". They took the door to the left marked "Write this letter twice". They backtracked. They backtracked. They took the door to the left marked "Write this letter". They took the door to the left marked "Write this letter twice". They took the door straight ahead marked "Write this letter then start a new line". They took the door straight ahead marked "Write this letter capitalized". They backtracked. They took the door to the left marked "Write this letter capitalized". They backtracked. "Let's rest awhile," Leland pleaded. They took the door straight ahead marked "Write this letter capitalized". "No," said Dimity. They took the door straight ahead marked "Write this letter". They took the door to the right marked "Write this letter followed by a space". They backtracked. They backtracked. They took the door to the left marked "Write this letter". They took the door straight ahead marked "Write this letter followed by a space". They backtracked. They backtracked. They backtracked. They backtracked. They backtracked. They took the door to the left marked "Write this letter twice". They took the door to the left marked "Write this letter then start a new line". They backtracked. They backtracked. They took the door to the left marked "Write this letter twice". They took the door to the right marked "Write this letter then start a new line". They took the door straight ahead marked "Write this letter capitalized". They took the door straight ahead marked "Write this letter". They backtracked. They took the door to the right marked "Write this letter". They took the door to the right marked "Write this letter followed by a space". They backtracked. They took the door to the right marked "Write this letter followed by a space". They took the door to the left marked "Write this letter". They took the door straight ahead marked "Write this letter". They backtracked. They took the door to the left marked "Write this letter". They backtracked. They backtracked. They took the door to the left marked "Write this letter". They took the door straight ahead marked "Write this letter". They took the door to the left marked "Write this letter twice". They took the door to the right marked "Write this letter". They took the door to the right marked "Write this letter". They took the door straight ahead marked "Write this letter". They backtracked. They backtracked. They took the door to the right marked "Write this letter". They took the door to the right marked "Write this letter". They backtracked. They backtracked. They backtracked. They took the door to the right marked "Write this letter". They took the door straight ahead marked "Write this letter". They backtracked. They took the door to the right marked "Write this letter". They backtracked. They took the door straight ahead marked "Write this letter". They took the door straight ahead marked "Write this letter". They took the door straight ahead marked "Write this letter twice". They took the door to the left marked "Write this letter". They took the door straight ahead marked "Write this letter followed by a space". They backtracked. They backtracked. They took the door to the left marked "Write this letter". They took the door to the right marked "Write this letter followed by a space". They took the door to the left marked "Write this letter". They backtracked. They backtracked. They backtracked. They took the door to the left marked "Write this letter". They took the door straight ahead marked "Write this letter followed by a space". They took the door straight ahead marked "Write this letter". They took the door straight ahead marked "Write this letter". They took the door to the right marked "Write this letter". They took the door to the right marked "Write this letter". They backtracked. They took the door to the right marked "Write this letter". They took the door to the left marked "Write this letter followed by a space". They took the door to the right marked "Write this letter". They took the door straight ahead marked "Write this letter". They took the door to the right marked "Write this letter". They took the door to the left marked "Write this letter". They backtracked. They backtracked. They took the door to the right marked "Write this letter". They took the door straight ahead marked "Write this letter". They took the door to the right marked "Write this letter". They backtracked. "I want to die," mouthed Leland voicelessly. They backtracked. "I really want to die." They took the door to the right marked "Write this letter". They backtracked. They backtracked. They backtracked. They took the door to the right marked "Write this letter". They took the door to the left marked "Write this letter". They took the door straight ahead marked "Write this letter". They backtracked. They backtracked. They took the door straight ahead marked "Write this letter". They took the door to the left marked "Write this letter". They took the door to the left marked "Write this letter". They took the door to the right marked "Write this letter". They took the door straight ahead marked "Write this letter". They took the door to the right marked "Write this letter followed by a space". They took the door to the right marked "Write this letter". They took the door to the left marked "Write this letter". They took the door to the right marked "Write this letter followed by a space". They backtracked. They took the door straight ahead marked "Write this letter followed by a space". They backtracked. They backtracked. They backtracked. They backtracked. They backtracked. They backtracked. They took the door to the right marked "Write this letter". They took the door straight ahead marked "Write this letter". They took the door straight ahead marked "Write this letter followed by a space". They took the door to the left marked "Write this letter". They took the door to the right marked "Write this letter". They took the door to the right marked "Write this letter followed by a space". They took the door to the left marked "Write this letter". They backtracked. They backtracked. They took the door to the right marked "Write this letter followed by a space". They took the door to the left marked "Write this letter". They took the door to the right marked "Write this letter twice". They took the door to the left marked "Write this letter". They backtracked. They took the door to the left marked "Write this letter". They took the door straight ahead marked "Write this letter followed by a space". They backtracked. They took the door to the right marked "Write this letter followed by a space". They took the door to the right marked "Write this letter". They took the door to the left marked "Write this letter". They backtracked. They took the door to the left marked "Write this letter". They backtracked. They backtracked. They took the door to the right marked "Write this letter". They took the door to the left marked "Write this letter". They backtracked. They took the door to the left marked "Write this letter". They took the door to the right marked "Write this letter". They took the door to the left marked "Write this letter". They took the door to the right marked "Write this letter twice with a space in between". They backtracked. They took the door straight ahead marked "Write this letter twice with a space in between". They took the door to the right marked "Write this letter". They took the door to the left marked "Write this letter". They took the door straight ahead marked "Write this letter". They took the door to the right marked "Write this letter followed by a space". They took the door straight ahead marked "Write this letter". They took the door to the right marked "Write this letter". They took the door to the right marked "Write this letter twice". They took the door to the left marked "Write this letter followed by a comma then start a new line". They took the door to the left marked "Write this letter capitalized". They backtracked. They backtracked. They backtracked. They backtracked. They backtracked. They backtracked. They backtracked. They backtracked. They backtracked. They took the door to the right marked "Write this letter". They took the door to the left marked "Write this letter". They backtracked. They backtracked. They backtracked. They took the door to the left marked "Write this letter twice with a space in between". They took the door to the right marked "Write this letter". They backtracked. They took the door to the right marked "Write this letter". They took the door to the right marked "Write this letter". They took the door straight ahead marked "Write this letter". They took the door to the left marked "Write this letter followed by a space". They took the door to the right marked "Write this letter". They backtracked. They backtracked. They took the door to the left marked "Write this letter followed by a space". They took the door to the right marked "Write this letter". They took the door straight ahead marked "Write this letter". They backtracked. They took the door to the right marked "Write this letter". They took the door to the left marked "Write this letter twice". They backtracked. They backtracked. They took the door straight ahead marked "Write this letter". They backtracked. They backtracked. "Is this hell?" asked Leland. They backtracked. They backtracked. They took the door to the right marked "Write this letter". They took the door to the left marked "Write this letter followed by a space". They took the door to the right marked "Write this letter". They took the door to the right marked "Write this letter". They took the door straight ahead marked "Write this letter twice". They took the door to the left marked "Write this letter followed by a comma then start a new line". They took the door to the right marked "Write this letter capitalized". They took the door straight ahead marked "Write this letter". They backtracked. They backtracked. They backtracked. They took the door to the left marked "Write this letter followed by a comma then start a new line". They took the door straight ahead marked "Write this letter capitalized". They took the door straight ahead marked "Write this letter". They took the door to the left marked "Write this letter". They backtracked. They took the door to the left marked "Write this letter". They took the door to the left marked "Write this letter". They backtracked. They took the door straight ahead marked "Write this letter". They backtracked. They backtracked. They backtracked. They took the door to the left marked "Write this letter". They took the door to the left marked "Write this letter". They took the door to the right marked "Write this letter". They took the door to the left marked "Write this letter twice". They backtracked. They took the door to the left marked "Write this letter twice". They took the door to the left marked "Write this letter". They took the door straight ahead marked "Write this letter". They took the door to the right marked "Write this letter followed by a space". They took the door to the right marked "Write this letter". They took the door straight ahead marked "Write this letter". They took the door straight ahead marked "Write this letter". They backtracked. They backtracked. They backtracked. They took the door to the right marked "Write this letter". They took the door to the right marked "Write this letter". They took the door straight ahead marked "Write this letter". They took the door to the left marked "Write this letter". They took the door to the right marked "Write this letter". They backtracked. They took the door to the right marked "Write this letter". They took the door to the left marked "Write this letter". They took the door to the right marked "Write this letter". They backtracked. They took the door straight ahead marked "Write this letter". They took the door to the right marked "Write this letter followed by a comma and a space". They backtracked. They backtracked. They took the door to the left marked "Write this letter". They took the door straight ahead marked "Write this letter followed by a comma and a space". They took the door straight ahead marked "Write this letter". They backtracked. "This IS hell," said Leland. They took the door to the right marked "Write this letter". They took the door straight ahead marked "Write this letter followed by a space". They backtracked. They backtracked. They took the door straight ahead marked "Write this letter". They took the door to the left marked "Write this letter followed by a space". They took the door straight ahead marked "Write this letter". They took the door to the right marked "Write this letter". They took the door to the right marked "Write this letter". They took the door to the left marked "Write this letter". They took the door to the left marked "Write this letter". They took the door straight ahead marked "Write this letter followed by a comma and a space". They backtracked. They backtracked. They took the door to the left marked "Write this letter". They backtracked. They backtracked. They took the door to the left marked "Write this letter". They took the door to the left marked "Write this letter". They took the door to the right marked "Write this letter followed by a comma and a space". They took the door to the left marked "Write this letter". "We're already dead and this is hell." They took the door to the left marked "Write this letter". They took the door to the right marked "Write this letter". They took the door to the left marked "Write this letter followed by a space". They took the door straight ahead marked "Write this letter". They backtracked. They backtracked. They took the door straight ahead marked "Write this letter followed by a space". They took the door straight ahead marked "Write this letter". They took the door to the right marked "Write this letter". They took the door straight ahead marked "Write this letter". They backtracked. They took the door to the right marked "Write this letter". They took the door to the right marked "Write this letter". They took the door straight ahead marked "Write this letter". They took the door straight ahead marked "Write this letter followed by an exclamation mark". They backtracked. They backtracked. "Dimity, please!" They took the door to the right marked "Write this letter". They backtracked. They backtracked. They took the door straight ahead marked "Write this letter". They backtracked. They took the door to the left marked "Write this letter". They took the door to the left marked "Write this letter". They took the door to the right marked "Write this letter followed by an exclamation mark"."""


actions = []

# "How to Write a Poem"
# "Start somewhere; Write this letter capitalized"
actions.append(("F", "L"))

# They entered an identical room with closed doors in the wall before them and in the wall to their right; each sported a sign marked, "Write this letter."
# "What letter?" said Leland, opening the door to the right (which caused the door they had just passed through to swing softly shut).
actions.append(("R", "l"))

# The room it led to had one other door in the opposite wall, marked "Write this letter"; they opened and passed through it
actions.append(("F", "l"))

# -- then immediately returned, for the room it led to had no other exits.
actions.append(("B", ""))

#  They had no choice but to backtrack again, straight ahead, through the second door they'd passed through, which on this side was marked "Start somewhere; Write this letter capitalized". They passed through it, back to the first room, which Dimity now thought of as the "Start somewhere" room.
actions.append(("B", ""))

# Their choices were either to backtrack through the very first door, now on their left (which was marked, sure enough, on this side, "How to Write a Poem"), or to continue through the other door marked "Write this letter", now on their right. They went right.
actions.append(("R", "l"))

# In this next room, there were doors to the left and straight ahead marked "Write this letter followed by a space." They took the door straight ahead.
actions.append(("F", "l "))

#  The only option from the next room was a door to the right marked "Write this letter"; they took it.
actions.append(("R", "l "))

# Now there were doors to the left, straight ahead, and to the right, marked "Write this letter". They took the door to the left.
actions.append(("L", "l"))

# From the next room, they took the only door, to the left, marked "Write this letter twice".
actions.append(("L", "ll"))

# But the room they entered was a dead end. They backtracked,
actions.append(("B", ""))

# and (now to the right) backtracked again.
actions.append(("B", ""))

# Leland pointed to the door on the right marked "Write this letter followed by a space". "That's the one we came through, right?"
#
# "Right," said Dimity. "Correct."
#
# But she was not as sure as she could wish to be. So she began taking notes.
#
# They took the door straight ahead marked "Write this letter".
actions.append(("F", "l"))

# But the next room was a dead end. They turned around and backtracked.
actions.append(("B", ""))

# They took the door to the right marked "Write this letter".
actions.append(("R", "l"))

# Dead end! They backtracked.
actions.append(("B", ""))

# Again they backtracked -- taking the door, now straight ahead, that Leland had pointed at, for all the others, they knew, were dead ends.
actions.append(("B", ""))

# And they backtracked again.
actions.append(("B", ""))

# They took the door to the right marked "Write this letter followed by a space".
actions.append(("R", "l "))


def parse_sentence(sentence: str) -> tuple[str, str] | None:
    if sentence == "They backtracked":
        return ("B", "")

    elif match := re.match(
        'They took the door (.+) marked "Write this letter ?(.*)"', sentence
    ):
        direction = {"straight ahead": "F", "to the left": "L", "to the right": "R"}[
            match.group(1)
        ]
        writes = {
            "": "l",
            "capitalized": "L",
            "followed by a colon then start a new line": "l:\n",
            "followed by a comma and a space": "l, ",
            "followed by a comma then start a new line": "l,\n",
            "followed by a period then skip a line": "l.\n\n",
            "followed by a semicolon and a space": "l; ",
            "followed by a space": "l ",
            "followed by an exclamation mark": "l!",
            "then start a new line": "l\n",
            "twice": "ll",
            "twice followed by a comma then skip a line": "ll,\n\n",
            "twice followed by a semicolon then start a new line": "ll;\n",
            "twice followed by a space": "ll ",
            "twice with a space in between": "l l",
        }[match.group(2)]

        return (direction, writes)

    else:
        # print(f"Ignoring {sentence!r}")
        return None


for sentence in re.split(r'[.!]"? ', text):
    sentence = sentence.strip()
    if parsed := parse_sentence(sentence):
        actions.append(parsed)

m = {
    "NF": "N",
    "EF": "E",
    "SF": "S",
    "WF": "W",
    "NR": "E",
    "ER": "S",
    "SR": "W",
    "WR": "N",
    "NL": "W",
    "EL": "N",
    "SL": "E",
    "WL": "S",
}

rev = {"N": "S", "E": "W", "S": "N", "W": "E"}

r = c = 0
heading = "N"
stack = []  # [(direction, write), ...]
for direction, write in actions:
    if direction == "B":
        prev_heading, prev_write = stack.pop()
        heading = rev[prev_heading]
        direction = "F"
    else:
        heading = m[heading + direction]
        stack.append((heading, write))

    r += (heading == "S") - (heading == "N")
    c += (heading == "E") - (heading == "W")


grid = [row1 + row2 for row1, row2 in zip(walls[0], walls[1])]

r = 30
c = 47
result = []
for heading, write in stack:
    if heading:
        r += (heading == "S") - (heading == "N")
        c += (heading == "E") - (heading == "W")

    ch = grid[r][c]
    result.append(write.replace("l", ch).replace("L", ch.upper()))

poem = "".join(result)
# # print(poem)
# Who follows the footsteps of flibbertigibbets
# Remarkable gumption and wisdom exhibits.
#
# Three clues are here hidden but easily found:
# Repeat the same walk on the opposite wall;
# Turn left and, nine letters less far from the ground,
# Allowing your head to one side first to fall,
#
# Repeat; and the final clue anyone sees
# Who bloodfloods their brainbox and looks twixt their knees,
# Beginning wherever, or nearly, they please!


fb_grid = walls[3]
nrows = len(fb_grid)
ncols = len(fb_grid[0])
target = "flibbertigibbetflibbertigibbet"
q = collections.deque(
    [
        (r, c, "", frozenset({(r, c)}))
        for r, row in enumerate(fb_grid)
        for c, ch in enumerate(row)
        if ch == "f"
    ]
)
for target_ch in target[1:]:
    for _ in range(len(q)):
        r, c, path, seen = q.popleft()

        for heading in "NESW":
            r2 = r + (heading == "S") - (heading == "N")
            c2 = c + (heading == "E") - (heading == "W")

            if not (0 <= r2 < nrows and 0 <= c2 < ncols or (r2, c2) in seen):
                continue

            if fb_grid[r2][c2] == target_ch:
                q.append((r2, c2, path + heading, seen | {(r2, c2)}))


# # There are multiple paths
# for _, _, _, s in q:
#     print(hash(s))
#     for r, row in enumerate(fb_grid):
#         for c, ch in enumerate(row):
#             if (r, c) in s:
#                 ch = ch.upper()
#             else:
#                 ch = "."
#             print(ch, end="")
#         print()
#     print("\n\n")

path = q[4][2]  # This one produces the correct result
tilt = {"N": "W", "E": "N", "S": "E", "W": "S"}
r, c = 23, 7
grid2 = walls[0]
message = ""
for heading in path:
    message += grid2[r][c]

    heading = tilt[heading]

    r += (heading == "S") - (heading == "N")
    c += (heading == "E") - (heading == "W")
message += grid2[r][c]

# # print(message)
# rememberalwayswhereyouhavebeen


# Who bloodfloods their brainbox and looks twixt their knees,
# Beginning wherever, or nearly, they please!
r, c = 23, 6  # just tried a bunch of starting points until it made sense
grid3 = walls[2]
message2 = ""
for heading in path:
    message2 += grid3[r][c]

    heading = rev[heading]

    r += (heading == "S") - (heading == "N")
    c += (heading == "E") - (heading == "W")
message2 += grid3[r][c]

# print(message2)
# # thelowerzbetokensthedrawbridge


path = "NNWSWNNUESWWNDWWWNENESUW"

floor = walls[4]
ceiling = walls[5][::-1]

r = len(floor) - 1
c = floor[r].index("z")
side = "D"
wall = floor

result = []
for heading in path:
    r += (heading == "S") - (heading == "N")
    c += (heading == "E") - (heading == "W")

    if heading == "U":
        wall = ceiling
    elif heading == "D":
        wall = floor

    result.append(wall[r][c])

key = "".join(result)
# key = "saydrletmeinimhomethrice"


@decrypter.decrypter(chapter=78)
def decrypt(cipher: str) -> str:
    return decrypter.vigenere_cipher(cipher, key)


# import itertools
# import decrypter

# dec = decrypter.decrypter(chapter=78)(lambda x: x)
# ciphertext = dec.decrypt_one_chapter()[:5000]

# # key = "saydrletmein;m\\om_5hridesaydr_etmeini hom_thriceLaydr_et =iBimhom=thrice"
# # key = "saydrletmeinimhXthrice"
# # key = "saydrletmeinimhotoutsXXXXXXXXXXXXXXXXXXXidethriceLaydr_et =iBimhom=thrice"
# # key = "saydrletmeinimhotoutside"
# # ke= "saydrletmein;m|om_5hridesaydr_etmeini hom_thriceLaydr_et =iBimhom=thrice"
# #     thriceLaydr_et =iBimhom=thrice
# # y = "saydrletmein;m\\om_5hridesaydr_etmeini hom_thriceLaydr_et =iBimhom=thrice"


# key = "saydrletmeinimhomethrice"

# plain = decrypter.vigenere_cipher(ciphertext, key)

# # print(plain)
# print(plain[:500])

# for a, b in zip(plain[:50], itertools.cycle(key)):
#     print(a, b)

# alphabet = """0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz.,?!:;'"-()[]{}|+=%/\\*#$_ \n"""
# have, want, key = "$Dt"
# alphabet[
#     (alphabet.index(have) - (alphabet.index(want) - alphabet.index(key)))
#     % len(alphabet)
# ]


# import decrypter
# from decrypter import vigenere_breaker

# reference_text = []
# for chapter in range(78):
#     with open(f"data/{chapter:02}.chp") as f:
#         reference_text.append(f.read())
# reference_text = "".join(reference_text)

# ciphertext = decrypter.decrypter(78)(lambda x: x).decrypt_one_chapter()

# result = vigenere_breaker.break_vigenere_cipher(
#     ciphertext[:10000],
#     reference_text,
#     decrypter_func=decrypter.vigenere_cipher,
#     key_chars=vigenere_breaker.ALPHABET,
#     max_key_length=300,
#     verbose=True,
# )
