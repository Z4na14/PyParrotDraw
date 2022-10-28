# encoding=utf-8
import os, platform, sys, argparse
from time import sleep

class animate:

    frames = (
        """
                             .cccc;;cc;';c.           
                          .,:dkdc:;;:c:,:d:.          
                         .loc'.,cc::c:::,..;:.        
                       .cl;....;dkdccc::,...c;        
                      .c:,';:'..ckc',;::;....;c.      
                    .c:'.,dkkoc:ok:;llllc,,c,';:.     
                   .;c,';okkkkkkkk:;lllll,:kd;.;:,.   
                   co..:kkkkkkkkkk:;llllc':kkc..oNc   
                 .cl;.,oxkkkkkkkkkc,:cll;,okkc'.cO;   
                 ;k:..ckkkkkkkkkkkl..,;,.;xkko:',l'   
                .,...';dkkkkkkkkkkd;.....ckkkl'.cO;   
             .,,:,.;oo:ckkkkkkkkkkkdoc;;cdkkkc..cd,   
          .cclo;,ccdkkl;llccdkkkkkkkkkkkkkkkd,.c;     
         .lol:;;okkkkkxooc::coodkkkkkkkkkkkko'.oc     
       .c:'..lkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkd,.oc     
      .lo;,:cdkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkd,.c;     
    ,dx:..;lllllllllllllllllllllllllllllllllc'...     
    cNO;........................................      
        """,
        """
                    .ckx;'........':c.                
                 .,:c:::::oxxocoo::::,',.             
                .odc'..:lkkoolllllo;..;d,             
                ;c..:o:..;:..',;'.......;.            
               ,c..:0Xx::o:.,cllc:,'::,.,c.           
               ;c;lkXKXXXXl.;lllll;lKXOo;':c.         
             ,dc.oXXXXXXXXl.,lllll;lXXXXx,c0:         
             ;Oc.oXXXXXXXXo.':ll:;'oXXXXO;,l'         
             'l;;kXXXXXXXXd'.'::'..dXXXXO;,l'         
             'l;:0XXXXXXXX0x:...,:o0XXXXx,:x,         
             'l;;kXXXXXXXXXKkol;oXXXXXXXO;oNc         
            ,c'..ckk0XXXXXXXXXX00XXXXXXX0:;o:.        
          .':;..:do::ooookXXXXXXXXXXXXXXXo..c;        
        .',',:co0XX0kkkxxOXXXXXXXXXXXXXXXOc..;l.      
      .:;'..oXXXXXXXXXXXXXXXXXXXXXXXXXXXXXko;';:.     
    .ldc..:oOXKXXXXXXKXXKXXXXXXXXXXXXXXXXXXXo..oc     
    :0o...:dxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxo,.:,     
    cNo........................................;'
        """,
        """
                .cc;.  ...  .;c.                      
             .,,cc:cc:lxxxl:ccc:;,.                   
            .lo;...lKKklllookl..cO;                   
          .cl;.,:'.okl;..''.;,..';:.                  
         .:o;;dkd,.ll..,cc::,..,'.;:,.                
         co..lKKKkokl.':lloo;''ol..;dl.               
       .,c;.,xKKKKKKo.':llll;.'oOxl,.cl,.             
       cNo..lKKKKKKKo'';llll;;okKKKl..oNc             
       cNo..lKKKKKKKko;':c:,'lKKKKKo'.oNc             
       cNo..lKKKKKKKKKl.....'dKKKKKxc,l0:             
       .c:'.lKKKKKKKKKk;....lKKKKKKo'.oNc             
         ,:.'oxOKKKKKKKOxxxxOKKKKKKxc,;ol:.           
         ;c..'':oookKKKKKKKKKKKKKKKKKk:.'clc.         
       ,xl'.,oxo;'';oxOKKKKKKKKKKKKKKKOxxl:::;,.      
      .dOc..lKKKkoooookKKKKKKKKKKKKKKKKKKKxl,;ol.     
      cx,';okKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKl..;lc.   
      co..:dddddddddddddddddddddddddddddddddl::',::.  
      co...........................................  
        """,
        """
               .ccccccc.                              
          .,,,;cooolccoo;;,,.                         
         .dOx;..;lllll;..;xOd.                        
       .cdo;',loOXXXXXkll;';odc.                      
      ,ol:;c,':oko:cccccc,...ckl.                     
      ;c.;kXo..::..;c::'.......oc                     
    ,dc..oXX0kk0o.':lll;..cxxc.,ld,                   
    kNo.'oXXXXXXo',:lll;..oXXOo;cOd.                  
    KOc;oOXXXXXXo.':lol;..dXXXXl';xc                  
    Ol,:k0XXXXXX0c.,clc'.:0XXXXx,.oc                  
    KOc;dOXXXXXXXl..';'..lXXXXXo..oc                  
    dNo..oXXXXXXXOx:..'lxOXXXXXk,.:; ..               
    cNo..lXXXXXXXXXOolkXXXXXXXXXkl,..;:';.            
    .,;'.,dkkkkk0XXXXXXXXXXXXXXXXXOxxl;,;,;l:.        
      ;c.;:''''':doOXXXXXXXXXXXXXXXXXXOdo;';clc.      
      ;c.lOdood:'''oXXXXXXXXXXXXXXXXXXXXXk,..;ol.     
      ';.:xxxxxocccoxxxxxxxxxxxxxxxxxxxxxxl::'.';;.   
      ';........................................;l'
        """,
        """
                                                          
            .;:;;,.,;;::,.                            
         .;':;........'co:.                           
       .clc;'':cllllc::,.':c.                         
      .lo;;o:coxdllllllc;''::,,.                      
    .c:'.,cl,.'l:',,;;'......cO;                      
    do;';oxoc;:l;;llllc'.';;'.,;.                     
    c..ckkkkkkkd,;llllc'.:kkd;.':c.                   
    '.,okkkkkkkkc;lllll,.:kkkdl,cO;                   
    ..;xkkkkkkkkc,ccll:,;okkkkk:,co,                  
    ..,dkkkkkkkkc..,;,'ckkkkkkkc;ll.                  
    ..'okkkkkkkko,....'okkkkkkkc,:c.                  
    c..ckkkkkkkkkdl;,:okkkkkkkkd,.',';.               
    d..':lxkkkkkkkkxxkkkkkkkkkkkdoc;,;'..'.,.         
    o...'';llllldkkkkkkkkkkkkkkkkkkdll;..'cdo.        
    o..,l;'''''';dkkkkkkkkkkkkkkkkkkkkdlc,..;lc.      
    o..;lc;;;;;;,,;clllllllllllllllllllllc'..,:c.     
    o..........................................;' 
        """,
        """
                                                          
               .,,,,,,,,,.                            
             .ckKxodooxOOdcc.                         
          .cclooc'....';;cool.                        
         .loc;;;;clllllc;;;;;:;,.                     
       .c:'.,okd;;cdo:::::cl,..oc                     
      .:o;';okkx;';;,';::;'....,:,.                   
      co..ckkkkkddkc,cclll;.,c:,:o:.                  
      co..ckkkkkkkk:,cllll;.:kkd,.':c.                
    .,:;.,okkkkkkkk:,cclll;.ckkkdl;;o:.               
    cNo..ckkkkkkkkko,.;loc,.ckkkkkc..oc               
    ,dd;.:kkkkkkkkkx;..;:,.'lkkkkko,.:,               
      ;:.ckkkkkkkkkkc.....;ldkkkkkk:.,'               
    ,dc..'okkkkkkkkkxoc;;cxkkkkkkkkc..,;,.            
    kNo..':lllllldkkkkkkkkkkkkkkkkkdcc,.;l.           
    KOc,c;''''''';lldkkkkkkkkkkkkkkkkkc..;lc.         
    xx:':;;;;,.,,...,;;cllllllllllllllc;'.;od,        
    cNo.....................................oc
        """,
        """
                                                          
                                                      
                       .ccccccc.                      
                   .ccckNKOOOOkdcc.                   
                .;;cc:ccccccc:,:c::,,.                
             .c;:;.,cccllxOOOxlllc,;ol.               
            .lkc,coxo:;oOOxooooooo;..:,               
          .cdc.,dOOOc..cOd,.',,;'....':l.             
          cNx'.lOOOOxlldOc..;lll;.....cO;             
         ,do;,:dOOOOOOOOOl'':lll;..:d:''c,            
         co..lOOOOOOOOOOOl'':lll;.'lOd,.cd.           
         co.'dOOOOOOOOOOOo,.;llc,.,dOOc..dc           
         co..lOOOOOOOOOOOOc.';:,..cOOOl..oc           
       .,:;.'::lxOOOOOOOOOo:'...,:oOOOc.'dc           
       ;Oc..cl'':lldOOOOOOOOdcclxOOOOx,.cd.           
      .:;';lxl''''':lldOOOOOOOOOOOOOOc..oc            
    ,dl,.'cooc:::,....,::coooooooooooc'.c:            
    cNo.................................oc   
        """,
        """
                                                      
                                                      
                                                      
                            .cccccccc.                
                      .,,,;;cc:cccccc:;;,.            
                    .cdxo;..,::cccc::,..;l.           
                   ,do:,,:c:coxxdllll:;,';:,.         
                 .cl;.,oxxc'.,cc,.';;;'...oNc         
                 ;Oc..cxxxc'.,c;..;lll;...cO;         
               .;;',:ldxxxdoldxc..;lll:'...'c,        
               ;c..cxxxxkxxkxxxc'.;lll:'','.cdc.      
             .c;.;odxxxxxxxxxxxd;.,cll;.,l:.'dNc      
            .:,''ccoxkxxkxxxxxxx:..,:;'.:xc..oNc      
          .lc,.'lc':dxxxkxxxxxxxol,...',lx:..dNc      
         .:,',coxoc;;ccccoxxxxxxxxo:::oxxo,.cdc.      
      .;':;.'oxxxxxc''''';cccoxxxxxxxxxxxc..oc        
    ,do:'..,:llllll:;;;;;;,..,;:lllllllll;..oc        
    cNo.....................................oc 
        """,
        """
                                                      
                                                      
                                  .ccccc.             
                             .cc;'coooxkl;.           
                         .:c:::c:,,,,,;c;;,.'.        
                       .clc,',:,..:xxocc;'..c;        
                      .c:,';:ox:..:c,,,,,,...cd,      
                    .c:'.,oxxxxl::l:.,loll;..;ol.     
                    ;Oc..:xxxxxxxxx:.,llll,....oc     
                 .,;,',:loxxxxxxxxx:.,llll;.,,.'ld,   
                .lo;..:xxxxxxxxxxxx:.'cllc,.:l:'cO;   
               .:;...'cxxxxxxxxxxxxoc;,::,..cdl;;l'   
             .cl;':,'';oxxxxxxdxxxxxx:....,cooc,cO;   
         .,,,::;,lxoc:,,:lxxxxxxxxxxxo:,,;lxxl;'oNc   
       .cdxo;':lxxxxxxc'';cccccoxxxxxxxxxxxxo,.;lc.   
      .loc'.'lxxxxxxxxocc;''''';ccoxxxxxxxxx:..oc     
    olc,..',:cccccccccccc:;;;;;;;;:ccccccccc,.'c,     
    Ol;......................................;l'   
        """,
        """
                                                      
                                  ,ddoodd,            
                             .cc' ,ooccoo,'cc.        
                          .ccldo;...',,...;oxdc.      
                       .,,:cc;.,'..;lol;;,'..lkl.     
                      .dOc';:ccl;..;dl,.''.....oc     
                    .,lc',cdddddlccld;.,;c::'..,cc:.  
                    cNo..:ddddddddddd;':clll;,c,';xc  
                   .lo;,clddddddddddd;':clll;:kc..;'  
                 .,c;..:ddddddddddddd:';clll,;ll,..   
                 ;Oc..';:ldddddddddddl,.,c:;';dd;..   
               .''',:c:,'cdddddddddddo:,''..'cdd;..   
             .cdc';lddd:';lddddddddddddd;.';lddl,..   
          .,;::;,cdddddol;;lllllodddddddlcldddd:.'l;  
         .dOc..,lddddddddlcc:;'';cclddddddddddd;;ll.  
       .coc,;::ldddddddddddddlcccc:ldddddddddl:,cO;   
    ,xl::,..,cccccccccccccccccccccccccccccccc:;':xx,  
    cNd.........................................;lOc 
        """)
    colores = ['0;31;40', '0;32;40', '0;33;40', '0;34;40', '0;35;40', '0;36;40', '0;37;40', ]
    archivos = []

    uso_col = False
    folder = None

    def __init__(self, folder, color):
        if folder != None:
            self.carpeta(folder)
        if color == True:
            self.color()

    def clear(self):
        if platform.system() == 'Windows':
            os.system('cls')
        else:
            os.system('clear')

    def color(self):
        color = 0
        self.uso_col = True
    def carpeta(self, opcion):
        self.folder = opcion
        self.frames = []

        for b in os.listdir("./{folder}/".format(folder = self.folder)):
            self.archivos.append(b)

        for c in range(len(self.archivos)):
            hola = open('./{folder}/{archivo}'.format(folder = self.folder, archivo = self.archivos[c]), 'r')
            self.frames.append(str(hola))
            hola.close()



parser = argparse.ArgumentParser(description='Literraly just a CLI ASCII animator')
parser.add_argument('-f', '--folder',
                    required=False)
parser.add_argument('-c', '--color',
                    required=False,
                    action='store_true')
args = parser.parse_args()


animate = animate(args.folder, args.color)

color = 0
while True:
    for a in range(len(animate.frames)):
        animate.clear()

        if animate.uso_col != True:
            print(animate.frames[a])

        if animate.uso_col == True:
            if color >= 7:
                color = 0

            print('\x1b[{color}m'.format(color = animate.colores[color]) + animate.frames[a] + '\x1b[0m')
            color += 1

        sleep(0.07)