from textblob import TextBlob

#Train 181
train = [
(' Lenin No a la consulta maosa mil veces NOOOOOOO ', 'no'),
('Por favor compaeros compartir la entrevista sobre la consulta realizada en Radio lite   7VecesNo  ', 'no'),
('A la de regresin de Derechos, a la 2   DilesNO  7VecesNO a la  ConsultaPopularEC  EcuadorRC  MashiRafael  ', 'no'),
(' DilesNO!!DISTRITO 3 PARROQUIA LETAMENDIEL 4 DE FEBRERO LOS PUEBLOS DIRAN EL  NO ROTUNDO EN LAS URNAS  A LA CONS  ', 'no'),
(' ecuadordiceno es ahora una tendencia en Ecuador   ', 'no'),
('El traidor 7vecesNo   EcuadorRC   MashiRafael  GabrielaEsPais  ', 'no'),
('Los compatriotas migrantes ecuatorianos en Madrid, apoyan con alegra el NO  Dirn  7VecesNO a  LaConsultaMaosa  L  ', 'no'),
('El Guasmo a full con el  NO   DurnPresente  EcuadorDiceNO  DilesNo  NOaLaViolenciaMoreNO  ', 'no'),
('Iva a botar si, pero con tanta leguleyada, odio y figuretes que nos damos cuenta, mi voto sera no a la consulta   ', 'no'),
(' JorgeGestoso NO Y MIL VECES NO A LA CONSULTA NEOLIBERAL Y PUNTO!!! El CANALLA TRAIDOR CAER', 'no'),
('De Babyshower en el Sur  FelizFinDeSemana  FelizSbado Y tambin  DilesNO   ', 'no'),
(' MashiRoberto Un cerdo como Voldemort que hasta en la pregunta 4, por sentido comn vota NO  Eres un asco Roberstupido', 'no'),
('NO a la Consulta   ', 'no'),
(' sincerebror 1000 RAZONES PARA DECIR NO!NO a la consulta maosa!NO a los mismos de siempre! NO a las mafias!  ', 'no'),
(' AugustoBarreraG  CPCCS 1000 RAZONES PARA DECIR NO!NO a la consulta maosa!NO a los mismos de siempre! NO a l  ', 'no'),
('Para quienes aun NO deciden su voto, por favor, meditenlo de cara al futuro de nuestro pais   DilesNO en la  ', 'no'),
(' DilesNO!!EL 4 DE FEBRERO LOS PUEBLOS DIRAN EL  NO ROTUNDO A LA CONSULTA CORRUPTA DE LAS OLIGARQUIAS !!!  ', 'no'),
('Opinin de algunos comunes frente a los notables que pululan hoy en da   DilesNO  ', 'no'),
('Mira t!con quin ahora se entrevistan  DilesNO  ', 'no'),
(' juancarlosz86 Miiii vemonos el finde en Rio, tengo buenas noticias  Chch   7VecesNO miiii ', 'no'),
('Sabes por qu renunci el procurador Diego Garca? Entrate   DilesNO  ', 'no'),
('Esto no es pagado, es pueblo organizado   DurnDiceNO  EcuadorDiceNO  DurnDiceNo GuayasDiceNo  ', 'no'),
(' LGBT hace un llamado para votar No en preguntas 2, 3, 6 de la  ConsultaPopular o  7VecesNo  PorLaPatriaDilesNO  ', 'no'),
('Para que los ricos no vuelvan a destruir el pas   DilesNo  PorLaPatriaDilesNO  NOaLaViolenciaMoreNO  ', 'no'),
(' CunticoTraidor ayudando a  BanqueroLasso En la  ConsultaMentirosa vota  7VecesNO  ', 'no'),
('Ahora a cualquier pendejada la llaman consulta  Por eso  7vecesNo', 'no'),
(' ConsultaEc2018 como hay gente que vota No en la pregunta 4 respecto a los abusadores sexuales? Que hijos de p, tan  ', 'no'),
('Si  NO a la CONSULTA MAOSA impuesta por el IMPOSTOR MENTIROSO CONVULSIVO y TRAIDOR de Lenin Moreno  ', 'no'),
(' DrMedinaUrresta  Lenin 1000 RAZONES PARA DECIR NO!NO a la consulta maosa!NO a los mismos de siempre! NO a l  ', 'no'),
(' RafaelVuelve 1000 RAZONES PARA DECIR NO!NO a la consulta maosa!NO a los mismos de siempre! NO a las mafias!  ', 'no'),
(' ODigitalEc 1000 RAZONES PARA DECIR NO!NO a la consulta maosa!NO a los mismos de siempre! NO a las mafias!  ', 'no'),
(' DilesNO!!Distrito 3  ParroquiaLetamendiEL 4 DE FEBRERO LOS PUEBLOS DIRAN EL  NO ROTUNDO A LA CONSULTA CORRUPTA D  ', 'no'),
('Para conversar sobre la 3era en la maana de martes, Con conviccin! En la 3  DilesNO  ', 'no'),
(' TVNCanal  diegoesimbabura Asi se habla Dr Garca   7VecesNO  a la  consultamaosa  Los traidores no pasaran ', 'no'),
('URGENTE Ests son las razones por las que renunci el Procurador del Estado, Diego Garca  DilesNO  ', 'no'),
('Gran alegra esta noche en el cierre de campaa en Guayaquil  GuayasDiceNO  EcuadorDiceNO al  ', 'no'),
('Que Berguenza con B de Burros   7VecesNO a los Neoliberales      teleSURtv  ', 'no'),
(' 7VecesNO en la  ConsultaMentirosa  FueraLeninFuera  TraidorXXX  ', 'no'),
('En la  ConsultaMentirosa votaremos  7VecesNO  ', 'no'),
('As reacciona la ciudadana contra el  CunticoTraidor y en la  ConsultaMaosa votaremos  7VecesNO  ', 'no'),
('Todos no  sucia consulta vota  no  ', 'no'),
('Si todava estas indeciso sobre como votar  Ac una ayuda   ConsultaPopular2018 DilesNo EcuadorEnDemocracia  ', 'no'),
('Aunque el fotgrafo no fue preciso, mi voto fue todo NO,  como la mayora d Ecuatorianos  7VecesNO en sta  ', 'no'),
('Con decisin y firmeza me dirijo a votar  YoVotoNO   PorLaPatriaDilesNO   7vecesNO', 'no'),
(' jpjaramillo25  Lenin  CPCCS 1000 RAZONES PARA DECIR NO!NO a la consulta maosa!NO a los mismos de siempre! N  ', 'no'),
(' florcisparedes  MashiRafael 1000 RAZONES PARA DECIR NO!NO a la consulta maosa!NO a los mismos de siempre!  ', 'no'),
(' LorenaTapiaN  eluniversocom Lorena manda un mensaje subliminal de como votar en la consulta  NO A LA CONSULTA DEL PENDEJO TRAIDOR', 'no'),
(' MashiRafael Si van a hacerle enojar a Correa, piensen en las consecuencias   7VecesNO', 'no'),
('Si usted vota si  El pueblo vota NO   ', 'no'),
('No volvamos al pasado 7 veces  DilesNO  en Guayaquil, Ecuador  ', 'no'),
(' DilesNO!!!A DERROCAR A LAS OLIGARQUIAS Y AL CUANTICO TRAIDOR  ASI SE UNAN NO VENCERAN A LOS PUEBLOS! LUCHARE  ', 'no'),
('No vamos a entregar el poder a cualquier aparecido  7VecesNO   MashiRafael  PatricioMery  ', 'no'),
('Sorry pero las gestiones comenzaron mucho antes, en el gobierno de Rafael Correa  DilesNO  ', 'no'),
('En la  ConsultaMaosa d este  CunticoTraidor vota  7VecesNO  FueraLeninFuera  TraidorXXX  ', 'no'),
('EXPLICACIONES??? SEGURO NO, POR ESTO Y MUCHO MS, NO Y MIL VECES NO A LA CONSULTA NEOLIBERAL Y PUNTO!!!  ', 'no'),
('Hay un JUEZ que este par no podr evadir, SU CONCIENCIA, que por suerte les quitar el sueo !  7VecesNO  DilesNO  ', 'no'),
(' ValeriaCoronelV Ese 40 depender de en cul pregunta el pas vota No  Con el cinismo de Correa y los suyos, es ca  ', 'no'),
('Aunque el fotgrafo no fue preciso, mi voto fue todo NO,  como la mayora d Ecuatorianos  7VecesNO en sta  ', 'no'),
('Depende de nosotros   7vecesSi                          7VecesNO  ', 'no'),
('Ahora si es bueno el dinero electrnico? falsos politiqueros cmo creerles??  NO A LA CONSULTA  ', 'no'),
(' jimmyjairala 1000 RAZONES PARA DECIR NO!NO a la consulta maosa!NO a los mismos de siempre! NO a las mafias!  ', 'no'),
(' RafaelVuelve 1000 RAZONES PARA DECIR NO!NO a la consulta maosa!NO a los mismos de siempre! NO a las mafias!  ', 'no'),
(' DilesNO  7VecesNO a la  ConsultaMentirosa  Paremos los proyectos privatizadores de la derecha a los que se ha subo  ', 'no'),
(' DilesNO!!!Se desvanece la CONSULTA CORRUPTA MAOSA E INCONSTITUCIONAL!!!VENCERAN LOS MANDANTES LOS DUEOS DE LA  ', 'no'),
(' EcuadorDiceNO a la regresin en derechos, NO a la designacin a dedo de 150 autoridades de control, NO los especul  ', 'no'),
('A la  ConsultaMaosa dile  7VecesNO  FueraLeninFuera  NOaLaViolenciaMoreNO  ', 'no'),
('Caravana de cierre de campaa  NO a las preguntas 2, 3 y 6 de la  ConsultaMaosa  EcuadorDiceNO  Esa ser la consig  ', 'no'),
('Estn desesperados, no saben como detener al gigante  MashiRafael  Este 4 de febrero todos a votar  7VecesNO a la  ', 'no'),
(' lduranaguilar  MashiRafael  ForoNacMujeres Por la patria por la dignidad NO a la consulta maosa  ', 'no'),
(' YaVisteFerdinand NO NO  DilesNO  ', 'no'),
('El domingo solo digamos NO por cada mes de mentiras, engaos y prebendas !  7VecesNO  ', 'no'),
('Gran cierre de campaa por el  7VecesNO  As dejamos confirmado que el NO les da palo y de largo a la consulta ma  ', 'no'),
('El amor a la revolucin y al ms grande  MashiRafael dicindole  7VecesNo a la corrupcin del Cuntico y los 40 con  ', 'no'),
('En la  ConsultaMaosa vota  7VecesNO  ', 'no'),
(' MashiRafael PRESIDENTE, SI SE METEN CON USTED, SE METEN CON EL PUEBLO  POR ESTO, NO Y MIL VECES NO A LA CONSULTA NEOLIBERAL Y PUNTO!!!', 'no'),
(' 35PAIS Ya dira por el viejo pais para que volvamos ha eso pais vota no y 7 veces no  ', 'no'),
('  EcuadorDiceNO con alegra !  ', 'no'),
('La consulta no consulta  Vota si o vota no  Pan con caca  para todos!', 'no'),
('Por mi patria, por la traicin, mi voto con infinito amor  7vecesNo  MashiRafael  ', 'no'),
('La mayora de Nuestros migrantes en Europa le dijo NO a la consulta popular  abrazo inmenso a todos! ', 'no'),
('Recorrimos Quito de norte a sur explicando a cada ciudadano el porqu votar  7VecesS  Lenin  jimmyjairala  ', 'si'),
(' raulclementelh  MarceloHCabrera Apoyo incondicional al lider del  Movimiento Igualdad 82 Ing  Marcelo Cabrera  Por eso  Cuenca7VecesS', 'si'),
('Desde la  UnidadPopularUP y desde nuestra  UnidadPopularAz a una sola voz siempre  7VecesSi por nuestro Ecuador  ', 'si'),
(' FernanCabezasG  LeninistasEC  VamosLenin Apoyo total  Los Ecuatorianos queremos un cambio   Cuenca7VecesS', 'si'),
('Si en Ecuador se lanzan huevos, es por que nos sobran huevos!!!  7VecesS  vamosporels', 'si'),
(' Polificcion La nica forma de eliminar a los dictadores es con nuestro puo y letra  por eso  7VecesSi', 'si'),
(' PaolaCabezasC Nravo Quinind no acepten corruptos  7VecesSi', 'si'),
(' Lenin La consulta popular es una expresin de democracia directa   PichinchaDiceS', 'si'),
(' Cayambe le dice  7VecesS a esta  ConsultaPopular que cambiar a este pas que busca un mejor futuro   ', 'si'),
('En cierre de campaa en la Michelena, sur de  Quito  7VecesSi  ', 'si'),
('Estamos presentes apoyando el  SI y toda la gestin de nuestro Presidente  Lenin  HumanistasConLenin  7vecesSI  ', 'si'),
('Con la  ConsultaPopular respaldamos el camino hacia un nuevo  Ecuador  Cuenca7VecesS  UNSIONTV  ', 'si'),
('Gracias por visitarnos qurrida  mfespinosaEC seguimos en pie de lucha  En un solo sentir  7VecesS respaldando  ', 'si'),
(' CierreDeCampaa 7VecesS  VamosEcuadorPorElCambio en Guayaquil,  ', 'si'),
('Las imgenes hablan por S solas  7VecesS  ', 'si'),
(' CierreDeCampaa 7VecesS  VamosEcuadorPorElCambio en Guayaquil,  ', 'si'),
('Si y  7VecesSi en la  Consulta Popular  ', 'si'),
(' CierreDeCampaa 7VecesS  VamosEcuadorPorElCambio en Guayaquil,  ', 'si'),
(' CierreDeCampaa 7VecesS  VamosEcuadorPorElCambio en Guayaquil,  ', 'si'),
(' CierreDeCampaa  7VecesS  EcuadorUnidoPorElCambio en Guayaquil,  ', 'si'),
('Maana acompaemos a nuestra vicepresidenta  marialevicuna! Porque todos votaremos  7VecesS  VotaTodoS  ', 'si'),
(' atufuturodiles es ahora una tendencia en Ecuador   ', 'si'),
('Maana tenemos la oportunidad de regalarnos un nuevo Ecuador   ATuFuturoDileS  7VecesSi  GAFT75  PaulGranda  ', 'si'),
(' GabrielaEsPais  cnegobec  OEAoficial Nueva rica como usted que ahora come mierda  7VecesSi', 'si'),
('Hemos cumplido con nuestro derecho  7VecesSi  ElPaisquiereunCambio  Lenin  PresidenciaEc  ', 'si'),
(' 7VecesSi  de acuerdo   ', 'si'),
('Cumpliendo con la democracia  Ecuador  7VecesSI  Nios  Naturaleza  Corrupcin  Construccin  ', 'si'),
('Nunca en mi vida he dicho 7 veces si, esta vez con voz firme y mano dura dir Si a la consulta,  7VecesSi  ', 'si'),
(' CarlosAMontaner La nica forma de eliminar a los dictadores es con nuestro puo y letra  por eso  7VecesSi', 'si'),
('Todas las preguntas de la  ConsultaPopular2018 tienen ms del 70 de votos a favor del S  Es literalmente una paliza  7VecesSi', 'si'),
('suburbio de Guayaquil tambien arroja huevos!  7VecesSi', 'si'),
('La alegra es de todos en este da!  7VecesS  SALUDesSAUDE  VotaTodoS  ', 'si'),
('Con la bandera del  Ecuador en la mano, nuestro lder  GustavoLarrea llama a votar este domingo  7VecesS y agrad  ', 'si'),
('Se vivi una fiesta,  GuayasDiceS y  7VecesS  Lenin  ', 'si'),
('Nuestro total apoyo  jimmyjairala  7VecesS en la consulta popular   ', 'si'),
(' CierreDeCampaa 7VecesS  VamosEcuadorPorElCambio en Guayaquil,  ', 'si'),
(' CierreDeCampaa  7VecesS  Unidos en Guayaquil, Ecuador  ', 'si'),
(' 7VecesSi por un nuevo  Ecuador mi voz y mi voto cuenta   ', 'si'),
('Porque Juntos haremos realidad el sueo del Ecuador  que todos queremos  VotaTodoSi  7VecesSi  GAFT75  PaulGranda  ', 'si'),
('A ver shunshos que repiten  SieteVecesSI  7VecesSi lean este prrafo del anexo de la pregunta 3 ojo tampoco es ap  ', 'si'),
('Maana rayo todo SI, vamos con alegra a sufragar por una PATRIA de respeto,libre y soberana   ATuFuturoDileS  ', 'si'),
('Yo ya le puse todo, todito S   ATuFuturoDileS', 'si'),
('Mi voto  7VecesS por el Cambio, por el Empleo, por nuestros Hijos, por el pas que aspira la gran mayora de los e  ', 'si'),
('Formemos parte de esta iniciativa y votemos   7VecesSi en la consulta popular de este prximo Febrero, los espero a  ', 'si'),
(' ricardozampais  ComunicacionEc  PichinchaPAIS  7vecessi  35PAIS  35appichincha  GoberCotopaxi Desconfo el supuesto apoyo de Ral Patio', 'si'),
('Por apoyar a que las reas protegidas no sean explotadas indiscriminadamente  Decimos  Cuenca7VecesS  ', 'si'),
(' Cuenca7VecesS  para proteger nuestros pramos, nuestro Cajas fuentes del agua vital   ', 'si'),
('El 4 de febrero yo voto  SI 7VecesSI  asiSi votaSI VotaTodoSi2a  parte videovia  ResistenciaEC1  ', 'si'),
(' GabrielaEsPais  7VecesSi  Si y solo Si   Adios corruptos!', 'si'),
('Con alegra, con esperanza y con mucha conviccin este 4 de febrero todos as a votar  Si  7VecesSi  Cuenca7VecesS  ', 'si'),
(' Lenin  PichinchaDiceS por que creemos en su palabra Presidente, por el futuro de nuestros hijos y este domingo le diremos  7VecesS ', 'si'),
(' INFORMACIN OFICIAL  Agenda para el da de hoy en Cuenca  ObvioQueS  7VecesS  Lenin  JorgeWated  ', 'si'),
('Vamos Ecuador!A votar  7VecesSi A votar contra esos corruptos que saquearon el pas en 10  aos y que nos dividie  ', 'si'),
('Votar  7vecesSi   con los dedos cruzados ', 'si'),
(' ConsultaPopular2018 con todo el nimo  7VecesSi  ', 'si'),
('7 Veces SI   PorMiPais  PorLasFamiliasEcuatorianas  PorMiFamilia  7VecesSi  YoCREOEnLaConsulta  ', 'si'),
('He votado  7VecesS  como lo dije desde el principio!Que se sepa ', 'si'),
(' MarioEcuador  jimmyjairala  Lenin  cendemocratico  CdPichincha  frentesomosec Votamos por un cambio, votamos por das mejores  7VecesS', 'si'),
('Cumpliendo con la democracia  Ecuador  7VecesSI  Nios  Naturaleza  Corrupcin  Construccin  ', 'si'),
(' ricardozampais  ComunicacionEc  PichinchaPAIS  7vecessi  35PAIS  35appichincha  GoberCotopaxi 7 Veces Si', 'si'),
(' PichinchaDiceS   QUIEN DICE ?', 'si'),
('El domingo no hay ms opciones  7VecesSi', 'si'),
('Para incentivar y reactivar el sector de la construccin que genera miles de empleos vamos a decir  7VecesS  ', 'si'),
('Al decirle S a la  ConsultaPopular2018 reafirma la Democracia en el pas   Cuenca7VecesS  UNSIONTV  ', 'si'),
('Seguimos recorriendo, activando  TOdosPorelSI  HumanistasEC  humanistasConLenin  7VecesS  ', 'si'),
('Miles de corazones  unidos en apoyo a  GustavoLarrea y  DemocraciaSiEcu hoy decimos en un solo   7vecesS  ', 'si'),
('Aqu  estamos Presidente   7VecesS  GuayaquilVotaSI  GuayasDiceS  GuayaquildiceSI  marialevicuna  HumanistasEC  ', 'si'),
('Hoy se sinti miles de  ardientes gritando  S y  7VecesS por la democracia y contra la corrupcin   ', 'si'),
(' CierreDeCampaa 7VecesS  VamosEcuadorPorElCambio en Guayaquil,  ', 'si'),
(' CierreDeCampaa 7VecesS  VamosEcuadorPorElCambio en Guayaquil,  ', 'si'),
(' 7VecesSi por un nuevo  Ecuador mi voz y mi voto cuenta   ', 'si'),
('Para permitirnos hacer realidad el sueo de todos los ecuatorianos de tener el pais que queremos  7VecesS  ', 'si'),
('Maana rayo todo SI, vamos con alegra a sufragar por la PATRIA libre y soberana   ATuFuturoDileS  ', 'si'),
('A cumplir con el deber antes que salga el sol!  SI  7VecesS', 'si'),
('La razn ms importante para votar  7VecesSi es el deseo de un mejor pas para las nuevas generaciones  Ejercimos  ', 'si'),
('Certificado emplasticado a solo 0,25  ConsultaPopular  7VecesS', 'si'),
('Depende de nosotros   7vecesSi                          7VecesNO  ', 'si'),
('Despus de votar  7VecesSi vamos por tacos californianos ', 'si'),
('Triunfo potente e inevitable, contundente 2 a 1 del  7VecesS  Lenin , sino  VayaYPregunte !!', 'si'),
(' cendemocratico  Lenin L s quite s y Ecuatorian s queremos un mejor pas por eso este 4 de febrero votaremos  7VecesSi', 'si'),
('Asi votar yo 1 SI 2 SI 3 SI 4 SI 5 SI 6 SI 7 SI  Si7VecesSi', 'si'),
('Recorrido por nuestra Provincia Orgullosamente Montuvios llegando con el Mensaje de la  Consulta Popular  7VecesSi  ', 'si'),
('Porque la ternura es la respuesta a todas las preguntas  7VecesS   ', 'si'),
('La nica forma de eliminar a los dictadores es con nuestro puo y letra  por eso  7VecesSi  ', 'si'),
('Asi desprecia Quinind a los prepotentes y corruptos  MashiRafael  todo Ecuador votar Si  7VecesSi  ', 'si'),
('Ah est tu aerosol  ricardopatinoec   7VecesSI  ', 'si'),
('  Lenin Sr  Presidente por cuidar el medio ambiente, por fomentar la inversin hacia el ecoturismo  PichinchaDiceS  ', 'si'),
(' CierreDeCampaa 7VecesS  VamosEcuadorPorElCambio en Guayaquil,  ', 'si'),
(' CierreDeCampaa 7VecesS  VamosEcuadorPorElCambio en Guayaquil,  ', 'si'),
('Con tu voto este domingo gana el Ecuador   VotaTodoS  7VecesSi  GuayasVotaS  GAFT75  PaulGranda  Lenin  ', 'si'),
(' jimmyjairala  cendemocratico  PrefecturGuayas Lo maravilloso de la diversidad!  7VecesS', 'si'),
(' 7VecesSi por un nuevo  Ecuador mi voz y mi voto cuenta   ', 'si'),
(' 7VecesSi por un nuevo  Ecuador mi voz y mi voto cuenta   ', 'si'),
(' atufuturodiles es ahora una tendencia en  Guayaquil   ', 'si'),
('Por un pas mejor Siete veces  si  consultaecuador  7vecess en Guayaquil, Ecuador  ', 'si'),
(' INFORMACIN OFICIAL  Agenda para el da de hoy en Cuenca  ObvioQueS  7VecesS  Lenin  JorgeWated  ', 'si'),
('Usted que les deca borregos a los correistas es el mismo que ahora dice  SieteVecesSI  7VecesSi ??El mismo nive  ', 'si'),
('A votar  7VecesS en Liceo Aeronautico FAE   2  ', 'si'),
('Recin hasta ahora logr votar   ConsultaPopular2018 Ya sabe  7VecesS  ', 'si'),
('Vamos Ecuador  YoVotoSi  7VecesSi  Ecuador', 'si'),
(' ConsultaPopular50 son los votantes de la OPOSICIN Porcentaje adicional, es lo que  Lenin gan al correato  7VecesSi ', 'si')
]
# TEST 5
test = [
('Solo como dato el vdeo dice que leas y te instruyas NO DICE VOTA NO  Una vez ms la manipulacin de la informac  ', 'no'),
('Cualquiera vota no en todo, excepto en las preguntas de los abusadores sexuales contra menores y para q los corrupt  ', 'no'),
('Desde  frentesomos apoyamos el S en las siete preguntas de la  ConsultaPopular  Entrevista  teleramaec 7VecesS  ', 'si'),
('Mujeres apoyando por un cambio positivo para los Ecuatorianos  Cuenca7VecesS  ', 'si'),
('El 4 de febrero yo voto  SI 7VecesSI  asiSi votaSI VotaTodoSi  1a  parte video via  ResistenciaEC1  ', 'si'),
]

from textblob.classifiers import NaiveBayesClassifier
cl = NaiveBayesClassifier(train)

print("La precision es de: " + str(cl.accuracy(test)))

#print(cl.show_informative_features(10))
