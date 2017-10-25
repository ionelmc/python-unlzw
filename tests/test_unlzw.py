from os.path import dirname
from os.path import join

from unlzw import unlzw


def test_decode_small():
    assert unlzw(b'\x1f\x9d\x90f\xde\xbc\x11\x13FN\xc0\x81\x05\x0f\x124(p\xa1\xc2\x82') == b'foobarfoobarfoobarfoobarfoobar'


def test_decode():
    assert unlzw(open(join(dirname(__file__), 'lipsum.txt.Z'), 'rb').read()) == b'''
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam at
convallis neque. Mauris pharetra dui non tortor feugiat eleifend. Donec
commodo congue nisl, ac accumsan elit eleifend in. Aliquam quis erat
dictum, aliquet augue non, facilisis tellus. Vestibulum eu ex lacinia,
blandit augue ac, aliquam nunc. Etiam nec congue ipsum. Nunc tempor
urna vel ante bibendum, vitae dignissim lorem feugiat. Sed dapibus neque
in nunc porta, quis tincidunt augue facilisis. Phasellus justo libero,
vestibulum ut aliquet nec, vehicula ac urna. Vestibulum fringilla tempor
purus ac vulputate. Quisque tempor magna tristique nibh tincidunt
lacinia. Proin lacinia, nibh non pretium mattis, sem odio tristique
mauris, in interdum sapien est ac sem. Proin convallis quam magna,
et accumsan urna euismod id. Pellentesque ultrices nec diam vel
sollicitudin. Integer vitae orci aliquet, cursus arcu ac, rutrum neque.

Aliquam vulputate, ligula quis tempor aliquam, tortor est pellentesque
ligula, eget viverra tellus orci condimentum massa. Duis in dolor
sit amet augue suscipit accumsan. Nam eu velit finibus, ornare nulla
vestibulum, auctor ex. Sed aliquet arcu vel interdum semper. Ut
pharetra porta auctor. Orci varius natoque penatibus et magnis dis
parturient montes, nascetur ridiculus mus. Nunc vel magna laoreet,
volutpat magna ut, sagittis neque. Interdum et malesuada fames ac ante
ipsum primis in faucibus. Aenean ac lacus quam. Nam a augue sed enim
luctus rhoncus. Maecenas ultrices lacus auctor lorem aliquam, sit amet
pellentesque nisi pretium. Nulla odio ipsum, molestie eu condimentum
eget, tristique pretium dui. Integer eu libero nulla. Morbi arcu erat,
vestibulum eu cursus eget, luctus id ante. Morbi pulvinar ullamcorper
maximus. Proin urna nibh, accumsan non mauris non, egestas auctor mi.

Integer eget ornare tellus, in laoreet felis. Aliquam pellentesque nulla
ut nulla consequat, nec interdum massa accumsan. Integer fermentum
malesuada erat, non convallis ipsum bibendum id. Proin sapien ipsum,
egestas ut tincidunt nec, condimentum facilisis metus. Pellentesque porta
metus ut dictum rutrum. Cras ipsum risus, lacinia sit amet dignissim sit
amet, aliquam id mi. Fusce eget elit eu tellus efficitur tempor. Quisque
pulvinar dolor ut quam tristique, nec auctor enim commodo. Maecenas
faucibus sit amet urna eget viverra. In lacinia in lacus nec aliquam.

Nullam ultrices elit at libero finibus, eu ultricies orci
mattis. Curabitur finibus placerat libero in accumsan. Sed leo est,
ullamcorper et aliquet sit amet, fringilla at nibh. In porta porta purus
nec bibendum. Morbi tristique dui quis purus venenatis accumsan. Etiam
imperdiet, lorem ut placerat molestie, elit ipsum mattis ligula, ut
viverra enim ligula quis purus. Nulla cursus aliquet nisi, a auctor nibh
posuere ut. Phasellus pulvinar, sem semper imperdiet euismod, ex tellus
mattis nunc, sit amet elementum elit mauris vitae ante. Vestibulum dictum
in ligula mollis scelerisque.

Etiam non augue tincidunt, rutrum odio vel, ultricies dolor. Curabitur
libero odio, congue ut pretium nec, accumsan sed purus. Aliquam ex nibh,
luctus id ullamcorper et, suscipit ut libero. Cras blandit justo elit,
ut mattis leo facilisis quis. Ut tellus velit, ultricies a sagittis
a, semper vitae quam. Nunc sollicitudin vel mi nec volutpat. Maecenas
libero nulla, iaculis nec faucibus sit amet, faucibus vel felis. Nulla
a tincidunt libero. Duis eleifend rutrum sem, quis faucibus sapien
sollicitudin sit amet.

Nam eget interdum metus. Proin tincidunt felis non viverra
scelerisque. Mauris ultrices sed nulla vel fringilla. Suspendisse mauris
eros, rutrum sit amet ligula nec, egestas sollicitudin neque. Duis gravida
lorem at nisl feugiat eleifend. Proin ipsum lorem, suscipit vitae velit
vel, fringilla ultricies mi. Mauris a ligula dui. Duis dictum, turpis
id egestas finibus, dui ipsum condimentum augue, id venenatis felis enim
non ipsum. Nulla bibendum euismod erat vel ornare. Sed luctus, purus nec
efficitur dapibus, orci nisi aliquam diam, id finibus dolor erat eget
leo. Phasellus tincidunt eros vitae sapien molestie, sit amet blandit
dolor scelerisque. Aenean eleifend orci non leo vulputate luctus. Sed
dui libero, congue non enim porta, mattis pretium tellus. Praesent eget
hendrerit nulla. Vestibulum accumsan tincidunt elit non dictum. Aenean
vitae gravida turpis, at luctus diam.

Pellentesque ullamcorper urna non dapibus rhoncus. Praesent dictum
placerat convallis. Sed pulvinar velit vel massa sodales, at maximus
mi laoreet. Pellentesque volutpat euismod diam, a varius nulla egestas
ac. In ornare placerat enim, sed pellentesque quam auctor sed. Aliquam
lacinia nulla vel nisi ultricies, a euismod tortor dictum. Morbi mattis
finibus enim, ac tristique est. Phasellus libero nunc, imperdiet sit
amet mi vel, hendrerit sollicitudin risus. Mauris auctor diam neque,
quis sagittis elit fermentum sed. Donec vitae faucibus augue. Aliquam
erat volutpat. Sed iaculis molestie velit, eu fringilla eros malesuada
vel. Sed pharetra ac sem eu faucibus. Aenean eu est bibendum, lacinia
nunc in, blandit lorem.

Nullam varius, sapien molestie placerat feugiat, erat ante luctus nulla,
fermentum vehicula eros ex fringilla felis. Ut gravida pulvinar libero,
pretium aliquam massa varius non. Vestibulum ullamcorper bibendum quam, eu
aliquet quam consequat ac. Vestibulum ornare ac eros a tristique. Duis nec
dolor quis velit accumsan rhoncus consequat vitae justo. In vulputate at
velit vitae consequat. Sed consequat ligula ante, eget cursus ex hendrerit
ut. Etiam lacinia justo odio, vitae sagittis dui ultrices at. Aliquam
erat volutpat. Quisque maximus semper tortor non maximus. Vivamus sit
amet vehicula enim.

Nunc vel nulla porttitor neque venenatis malesuada. In neque nunc, finibus
vel turpis vitae, commodo porta tellus. Nullam laoreet risus suscipit
dictum suscipit. In id bibendum neque, vel vehicula lectus. Fusce ac
ex hendrerit, posuere libero in, luctus ligula. Donec placerat laoreet
tempor. Praesent blandit ipsum vitae faucibus pellentesque. Aliquam
mollis a velit accumsan tincidunt. Praesent blandit justo et accumsan
lacinia. Suspendisse potenti. Morbi ut lacus et lorem placerat gravida.

Aenean eget gravida augue, sed pulvinar tortor. Aliquam varius accumsan
eros, at placerat sapien tempus eu. Aliquam rutrum quis mi blandit
placerat. Nunc facilisis dolor ac rutrum congue. Suspendisse maximus
faucibus facilisis. Sed accumsan eros a ipsum vestibulum blandit. Aenean
porta ex sit amet turpis fringilla fermentum. In venenatis tempus quam
eget dapibus. Sed dolor mauris, laoreet vel sem et, vehicula iaculis
odio. Integer ut pulvinar nisl. Sed eget porttitor velit. Nunc cursus
orci risus, eu pulvinar tortor molestie molestie. Nulla justo eros,
vulputate id lacinia quis, interdum eget mi. Donec nec tristique nunc,
quis facilisis ligula.

Nullam auctor est nec felis accumsan, ultrices mollis dolor
sodales. Phasellus sed est ac risus aliquam scelerisque. Pellentesque
consectetur, orci sit amet suscipit maximus, arcu nisl porta nulla, id
malesuada enim enim sed lorem. Maecenas lectus urna, lacinia ultricies
dapibus et, pulvinar ac massa. Morbi vitae dui quis dolor eleifend
consectetur a vel ligula. Pellentesque nec tristique mi, id commodo
purus. Nulla fermentum urna semper, convallis sapien luctus, tincidunt
purus. Proin sit amet lorem sapien. Pellentesque interdum et neque a
tristique. Vivamus vitae egestas metus, id molestie eros. Cras convallis
lacus sit amet ipsum ornare tincidunt.

In aliquam pellentesque pharetra. Morbi euismod convallis accumsan. Sed
ante nunc, blandit ut felis id, malesuada elementum mi. Aliquam erat
volutpat. In sed nulla sed est porta elementum. Sed vel quam eu libero
cursus commodo eu non tortor. Vivamus dui ligula, pellentesque at enim
in, pellentesque auctor dui. Phasellus dictum vestibulum maximus.

Vivamus quis velit sed leo mollis porta sed in mi. Phasellus arcu ante,
laoreet eu libero et, tincidunt ullamcorper elit. Vestibulum auctor
euismod libero, quis tristique dolor tristique eget. Fusce iaculis justo
massa, sed varius nulla pellentesque vel. Vivamus enim sapien, accumsan
sed ex vitae, finibus vulputate metus. Vivamus varius risus leo, vitae
tincidunt tellus feugiat vel. Nunc lacinia, elit ac interdum fringilla,
dui lacus vulputate mi, vel finibus massa dui quis ex.

Nullam porttitor sed quam non finibus. Donec eget bibendum libero. Aliquam
ullamcorper, turpis at pretium ultrices, leo lacus pretium ante,
a lobortis enim risus id urna. Ut eget augue dignissim, mattis leo a,
condimentum leo. Pellentesque habitant morbi tristique senectus et netus
et malesuada fames ac turpis egestas. Fusce nec nunc blandit, dignissim
sem ut, varius nulla. Quisque tempus vitae risus vel sodales. Donec
ullamcorper sodales ipsum. Aliquam faucibus est in purus placerat mattis.

Integer eleifend rutrum dui ut semper. Duis hendrerit id ipsum et
aliquam. Donec at enim ut sem consequat pulvinar non ut purus. Vivamus
in tristique eros, nec interdum turpis. Aliquam maximus, nibh quis
pretium vulputate, sem nisi condimentum mi, dictum semper felis lectus
ac turpis. Nullam suscipit elit eu augue malesuada, et auctor dui
vestibulum. Sed nec mauris vitae nunc malesuada aliquam. Sed ac ultrices
neque. Duis enim neque, eleifend sodales dapibus non, ullamcorper ac
eros. Cras sed metus blandit, interdum mi rutrum, tempus nisl. Quisque
est libero, semper eu orci eget, rhoncus consectetur eros. Ut tristique
ex a mi luctus consequat.

Curabitur eget nunc in felis consequat faucibus. Maecenas efficitur
diam id lacus aliquam, at laoreet lectus euismod. Maecenas vel lobortis
libero. Nulla porttitor, tortor eu viverra feugiat, justo lectus interdum
odio, sed gravida justo mi sit amet erat. Sed at quam sagittis, pharetra
erat quis, dictum leo. Ut nec tempor dui, gravida faucibus lorem. Donec
non arcu et sem convallis laoreet in in nulla. Fusce quis nulla tincidunt,
accumsan tellus eget, rhoncus mauris. Praesent auctor leo vitae orci
consequat commodo. Nam a scelerisque leo. Aenean vel risus elementum,
molestie nisl rhoncus, ultricies ante. Duis et dictum arcu. Proin nec
fringilla dui. Duis dapibus condimentum risus a cursus.

Morbi varius dui ac ante dictum eleifend. Pellentesque massa metus,
eleifend euismod dui id, eleifend tempor tortor. In sit amet eros
consequat, volutpat nibh eget, luctus ligula. Vestibulum placerat turpis
vel metus dapibus, id lobortis est sagittis. Donec et elit rhoncus,
commodo quam dictum, dapibus ex. Sed eu nulla vel ex sodales ultrices nec
vitae erat. Cras mollis tellus ut semper tincidunt. Morbi ut volutpat
ipsum. Phasellus a congue dolor, vitae imperdiet lorem. Integer sed
purus gravida, malesuada sem sed, condimentum lacus. Vivamus quis
pellentesque libero.

Vivamus tempus massa ante, ac sollicitudin orci luctus sit amet. Proin
massa diam, placerat nec enim ac, molestie eleifend velit. Fusce aliquet
turpis ante, id faucibus metus molestie quis. Praesent iaculis massa
leo, venenatis posuere lectus interdum lobortis. Nulla ligula lorem,
viverra sed condimentum ac, semper nec dolor. Suspendisse facilisis
luctus dictum. Fusce tincidunt leo ac purus iaculis porta. Quisque
lacinia felis non efficitur sagittis. Integer ac porta purus.

Morbi a libero sit amet dui egestas porta. Maecenas condimentum urna
sed felis varius rutrum. Duis tincidunt neque a lacus sagittis lobortis
id pharetra mi. Nulla a fermentum ante, vel porttitor purus. Proin vel
tellus dui. Ut et sagittis nisl. Ut commodo ornare urna, eu semper dui
tempus vel. Nulla a nunc vitae diam cursus auctor. Curabitur a pulvinar
quam. Cras vitae nisi ac magna faucibus lacinia. In non hendrerit
metus. Vivamus lobortis porttitor justo vel aliquet. Suspendisse ut
ullamcorper velit. Aliquam scelerisque leo eu risus vehicula, dapibus
euismod lectus sodales. Class aptent taciti sociosqu ad litora torquent
per conubia nostra, per inceptos himenaeos.

In hac habitasse platea dictumst. Vestibulum commodo, sapien a
vehicula porta, lorem arcu aliquam lorem, vel convallis velit neque eu
risus. Nam sit amet leo suscipit, sagittis orci in, posuere nisi. In
non ornare odio. Interdum et malesuada fames ac ante ipsum primis in
faucibus. Pellentesque vitae fringilla metus. Aenean vitae massa quis mi
blandit semper lobortis ac urna. Morbi tellus ex, dictum vitae tincidunt
nec, maximus vitae quam. Etiam efficitur sem in vestibulum congue. Aliquam
non nulla iaculis, ornare ante non, ultrices felis.

Mauris a venenatis turpis, quis tincidunt velit. Vivamus at ligula sodales
lorem pulvinar suscipit at quis libero. Cras commodo dui sit amet dolor
gravida, nec varius ipsum semper. Praesent rhoncus, ex id vehicula
dignissim, nunc mi maximus elit, eu finibus ex ipsum vel nisl. Aenean
imperdiet, ex non mattis hendrerit, tellus enim laoreet magna, eget
posuere neque purus volutpat ipsum. Nullam ut efficitur ex. Duis feugiat
vulputate augue, at pretium sapien feugiat dapibus. Pellentesque mollis
dictum orci, vel interdum turpis porttitor at. Suspendisse arcu purus,
tincidunt id tortor quis, sodales condimentum metus. Proin laoreet, orci
ac elementum condimentum, ex nibh imperdiet felis, posuere scelerisque
est dolor nec turpis. Cras nec risus imperdiet, rhoncus metus efficitur,
porttitor arcu.

Nam egestas, sapien quis tristique porttitor, mauris dolor pulvinar eros,
at congue libero orci at justo. Phasellus sit amet rhoncus ex. Donec
facilisis velit ac purus facilisis, ut tincidunt arcu accumsan. Sed
et vulputate odio. Praesent et elit sed purus vulputate dictum. Sed ac
euismod dolor. Fusce vulputate metus magna, ac ornare ipsum hendrerit sed.

Etiam arcu diam, auctor a condimentum eu, dignissim vel eros. Vestibulum
ut lacinia magna. Nam eu quam vitae odio condimentum fermentum. Mauris
velit dui, semper non est sit amet, vulputate pellentesque quam. Donec
sit amet feugiat augue. Fusce tristique lectus odio. Donec at magna
rutrum, elementum purus ut, porttitor tellus. Aenean mollis lacus quam,
ut aliquam mauris lacinia sed. Cras semper justo sit amet tincidunt
maximus. Quisque tortor metus, pharetra eu auctor sed, pulvinar vel
orci. Suspendisse non mi non purus sollicitudin gravida. Donec eu lacus
quis elit rutrum rutrum. Pellentesque habitant morbi tristique senectus
et netus et malesuada fames ac turpis egestas. Nunc ut urna justo.

Suspendisse eget lectus egestas, euismod risus vitae, vulputate
magna. Nunc cursus odio et posuere tempor. Vestibulum ante ipsum primis
in faucibus orci luctus et ultrices posuere cubilia Curae; Vestibulum
ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia
Curae; Pellentesque euismod ex sed augue dignissim, quis dignissim velit
facilisis. Maecenas commodo mi vel tortor ullamcorper, quis rhoncus ante
euismod. Aliquam placerat lacinia nisl in faucibus. Proin rhoncus libero
in arcu facilisis, et scelerisque erat tincidunt.

Etiam elit augue, bibendum sed rhoncus eu, pretium sit amet massa. Aenean
placerat, urna congue tempus faucibus, felis eros dapibus risus, placerat
ultrices sapien eros vitae orci. Cras varius dui et felis semper,
a mattis leo pharetra. Pellentesque vitae tincidunt ipsum. Vivamus in
orci at ipsum aliquam tincidunt et et nulla. Fusce vel efficitur mauris,
eu viverra leo. Maecenas pulvinar diam vel felis placerat, et scelerisque
nibh vulputate. Pellentesque habitant morbi tristique senectus et netus
et malesuada fames ac turpis egestas. Donec neque elit, faucibus eget
lorem quis, convallis fringilla ex. Nullam porta efficitur eros, ac
mattis dolor dictum a. Mauris est massa, aliquet et placerat sit amet,
rutrum et lacus. Fusce a aliquet leo, eget fermentum tellus. Nunc eget
vulputate felis.

Donec dui diam, vulputate eu placerat quis, iaculis dignissim
mauris. Fusce convallis velit odio, sit amet elementum dui malesuada
quis. Curabitur faucibus vel felis ut tempus. Curabitur in neque eget
ipsum faucibus pretium. Suspendisse quis dictum velit, non congue
enim. Morbi nec sollicitudin quam. Vestibulum sapien elit, pretium id
dignissim at, gravida eget elit. Phasellus eu posuere metus, sed congue
augue. Orci varius natoque penatibus et magnis dis parturient montes,
nascetur ridiculus mus. In eu maximus ligula, a maximus elit. Nam eget
turpis scelerisque nulla imperdiet congue in sit amet ipsum. Vivamus
sodales tempus pellentesque. Pellentesque in ligula vel quam varius
aliquet. Morbi feugiat tincidunt gravida.

Nunc sagittis sit amet est a varius. Etiam vitae ex eleifend lorem
mattis tincidunt nec non libero. Aenean mollis, nibh sed accumsan
feugiat, augue diam gravida dolor, in euismod nisl purus et lacus. Ut
nec ante vel magna tincidunt auctor id vitae sapien. In ac facilisis
mauris. Praesent non gravida ipsum, sed faucibus tortor. Nam non placerat
quam, id ultrices massa. Mauris feugiat pharetra tortor, ac suscipit dui
imperdiet at. Class aptent taciti sociosqu ad litora torquent per conubia
nostra, per inceptos himenaeos. Cras eget mauris in tortor accumsan
convallis. Morbi ullamcorper sapien tincidunt sagittis tincidunt. Ut non
tristique nulla. Curabitur et bibendum magna, vitae semper dolor. Quisque
non est vestibulum, euismod tellus ut, consectetur est.

Praesent eleifend finibus mi sodales placerat. Aenean lobortis sapien
lorem, ac rhoncus ex efficitur ac. Suspendisse potenti. Nunc maximus
est nunc, vel fermentum orci fermentum nec. Nam eget placerat erat, non
sodales sapien. Nullam lobortis vitae nisi et consequat. Aenean mi neque,
congue id aliquam eget, suscipit a mauris.

Nunc convallis dapibus lacinia. Sed euismod vehicula velit. Aenean
venenatis sem in lectus tristique, ut varius purus tristique. Sed ac
fringilla odio. Aliquam porttitor, nibh in fermentum maximus, nisi nisi
malesuada odio, eget pulvinar eros nibh nec mauris. Proin in consectetur
metus. Aenean sed bibendum nibh. Nulla a neque euismod erat bibendum
sagittis. Curabitur fermentum condimentum nulla id pellentesque. In
euismod orci eget justo eleifend lobortis.

Sed tincidunt dictum sapien, id maximus metus pellentesque vitae. Maecenas
rhoncus, lorem eu vestibulum rhoncus, felis nulla dapibus nisl,
sed fermentum massa justo ac eros. Cras pellentesque leo aliquam nibh
laoreet, vel ultricies nisl bibendum. Maecenas ac lorem sapien. Cras at
scelerisque elit, in bibendum ante. Praesent ut commodo arcu. Nullam
lacinia ornare nibh, eget pretium nisi sollicitudin id. Praesent ut
mauris vestibulum lectus laoreet vehicula. Donec enim turpis, rutrum
nec tempus a, imperdiet ut velit. Pellentesque posuere turpis vitae
nisl maximus dignissim. Sed dictum est ut lectus rutrum, ac ultrices
velit euismod. Sed commodo mi id purus tristique cursus. Duis dictum,
ipsum eget maximus posuere, turpis libero tristique est, id imperdiet
neque libero vitae purus. Proin ultrices, orci non vestibulum tristique,
turpis leo aliquet est, nec hendrerit nulla enim volutpat enim. Cras
pulvinar volutpat tortor, ut pulvinar quam.

Duis pulvinar eros metus, at tincidunt eros luctus nec. Integer malesuada
elit eget purus ultricies, et tincidunt justo eleifend. Donec eleifend
vulputate arcu. In sed fermentum enim. Phasellus mi lectus, pretium quis
euismod vitae, vestibulum in ipsum. Integer in sapien tempus, blandit
lorem eu, sagittis mi. In sit amet magna commodo, lacinia magna in,
viverra augue. Mauris vehicula, dui id vestibulum scelerisque, augue
elit vulputate ex, sit amet consequat dolor metus et sapien. Curabitur
lobortis mi ligula, ac ultricies libero ornare aliquam. In non nunc
turpis. Quisque vitae odio et leo aliquam rhoncus. Phasellus sit amet
risus odio. Cras accumsan purus vitae nisi mollis posuere.

Curabitur ullamcorper pharetra erat, quis eleifend mauris elementum
ornare. Donec sodales varius nunc in tincidunt. Aenean tellus turpis,
finibus eget blandit vel, vestibulum id velit. Duis quis feugiat
ante. Nulla scelerisque, arcu nec blandit imperdiet, turpis mauris
suscipit magna, at ultricies risus lacus sed velit. Sed aliquet tortor et
metus semper, vitae commodo ipsum eleifend. Nam non scelerisque ex, vitae
ullamcorper est. Pellentesque et est nisi. Nulla nec lacus consectetur,
fringilla nisl at, commodo lectus. Integer ipsum elit, blandit vel libero
eu, facilisis finibus diam.

Donec gravida luctus congue. Donec et fermentum mauris, id commodo
turpis. Donec feugiat justo mauris, in auctor dolor sollicitudin ac. Nulla
sollicitudin, turpis in posuere euismod, leo lectus dignissim justo,
id venenatis est felis vel justo. Duis vel venenatis erat. Suspendisse
a justo vel mauris tincidunt ultrices ut ut odio. Vestibulum at neque
pulvinar, lobortis ligula nec, commodo tellus. Fusce risus ante,
eleifend eu venenatis a, elementum eget ex. Quisque vitae sodales
lacus. Quisque quis urna in justo dictum luctus. Nam convallis venenatis
hendrerit. Mauris imperdiet at ligula eu accumsan. Phasellus consequat
ligula rutrum nisl varius placerat. In non quam nisi. Curabitur rutrum
lectus ut massa pulvinar, eget ullamcorper augue elementum. Suspendisse
dictum quis purus volutpat vehicula.

Duis ac sem vel metus fermentum commodo vel a erat. Aliquam id efficitur
tortor, eget pretium mi. Etiam ornare aliquet nisi, in interdum est
blandit et. Integer ac malesuada justo, at elementum ipsum. Suspendisse
semper malesuada tincidunt. Quisque ornare tempus nisl eu auctor. In
finibus tincidunt eros at fermentum. Mauris nec magna risus. Proin
tincidunt vulputate mi, non sodales ipsum condimentum a. Nunc at
pellentesque magna. Nam suscipit, lacus condimentum varius consectetur,
magna augue viverra erat, vel molestie erat erat eget arcu. Quisque id
lacus nec dui egestas eleifend. Phasellus aliquam volutpat fermentum.

Aenean fermentum felis sed libero feugiat, eu tincidunt urna
convallis. Praesent lacinia ac augue eu ullamcorper. Ut eget augue
sit amet metus aliquam pulvinar vitae imperdiet augue. Sed nec metus
sollicitudin, accumsan arcu et, porttitor ligula. Curabitur sed purus
semper, rhoncus est accumsan, malesuada mi. Nullam nec suscipit urna,
non pulvinar diam. Curabitur pellentesque scelerisque ante. In non
imperdiet metus. Aliquam tristique ornare mollis. Aliquam suscipit
placerat suscipit.

Mauris non sapien molestie, suscipit leo vitae, faucibus purus. Etiam
id nibh gravida, laoreet velit et, hendrerit arcu. Ut vehicula faucibus
elit vel dapibus. Mauris sollicitudin bibendum ex, feugiat accumsan arcu
efficitur non. Morbi molestie finibus tellus ac porttitor. Aenean et
massa vel dolor sollicitudin laoreet ac et libero. Cras luctus sed metus
et ultrices. Mauris quis ipsum ut urna euismod vehicula eget non ligula.

Nullam vitae accumsan eros. Duis quis est condimentum, consectetur justo
sit amet, lobortis massa. Orci varius natoque penatibus et magnis dis
parturient montes, nascetur ridiculus mus. In ac efficitur felis. Ut
laoreet rutrum aliquam. Morbi leo felis, mollis eu porta in, tempor at
dui. Curabitur lorem quam, pellentesque in felis eget, dictum blandit
nibh. Curabitur ullamcorper magna malesuada, lobortis orci commodo,
blandit massa. Sed mattis lorem in arcu accumsan sagittis. Etiam bibendum
quis eros nec commodo. Vestibulum a eros est. Nullam volutpat ex in nisl
blandit scelerisque. Nullam malesuada mauris eget lobortis congue. Cras
et malesuada massa.

Integer sollicitudin, elit eget pharetra pellentesque, sapien libero
blandit magna, sit amet consequat sapien odio eget nisl. Vivamus ut
mollis ante. Nulla imperdiet ex blandit, faucibus justo at, rhoncus
dui. Maecenas commodo vehicula odio, eget maximus nisl porta a. Nullam ut
odio consectetur, dapibus nisl eget, suscipit metus. Etiam a malesuada
purus, eu auctor lorem. Nunc magna velit, sagittis euismod orci in,
efficitur rhoncus est.
'''
