from kivymd.app import MDApp
from kivymd.uix.relativelayout import MDRelativeLayout
from kivymd.uix.behaviors import RectangularRippleBehavior
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.properties import StringProperty,NumericProperty,BooleanProperty,ListProperty
from kivy.uix.behaviors import ButtonBehavior
from kivy.animation import Animation
from random import choice

kv='''
#:import choice random.choice
#:import App kivymd.app
#:import ShowCard main
<CardSelect>:
    size_hint:None,None
    size:dp(120),dp(120)
    radius:dp(7)
    md_bg_color:root.cor
    MDIconButton:
        icon:'information-outline'
        pos_hint:{'right':1,'top':1}
        on_press:App.MDApp.get_running_app().sm.ids.home.info(f'info-{root.titulo}')
    MDIcon:
        icon:root.icone
        pos_hint:{'center_y':root.icone_pos}
        halign:'center'
        font_size:root.icone_size

    MDLabel:
        text:root.titulo
        pos_hint:{'center_y':0.3}
        halign:'center'
        font_style:'Overline'
        font_size:dp(15)
        bold:True
        
    MDLabel:
        text:root.desc
        pos_hint:{'center_y':0.15}
        halign:'center'
        font_style:'Overline'
        font_size:dp(12)
        bold:True    

<Home>:
    MDBoxLayout:
        orientation:'vertical'
        md_bg_color:25/255,25/255,25/255,1
        MDRelativeLayout:
            size_hint_y:0.25
            MDIcon:
                icon:'beer'
                halign:'center'
                font_size:dp(70)
                pos_hint:{'center_y':0.6}
                color:1,1,1,1

            MDLabel:
                text:'Selecione As Cartas'
                pos_hint:{'center_y':0.2}
                halign:'center'
                font_style:'Overline'
                font_size:dp(15)
                bold:True
                color:1,1,1,1
                
        MDGridLayout:
            cols:2
            size_hint_x:None
            width:dp(250)
            pos_hint:{'center_x':0.5}
            spacing:dp(10)
            CardSelect:
                id:classic
                color_on:1,1,1,1
                color_off:0.6,0.6,0.6,1
                icone:'beer'
                titulo:'classico'
                desc:f'{len(App.MDApp.get_running_app().showcard.perguntas_classico)} Cartas'
                on_release:root.in_play(classic.selected,eununca.selected,hot.selected)

            CardSelect:
                id:eununca
                color_on:0,0.8,0,1
                color_off:0,0.4,0,1
                icone:'comment-processing-outline'
                titulo:'eu nunca'
                desc:f'{len(App.MDApp.get_running_app().showcard.perguntas_eu_nunca)} Cartas'
                on_release:root.in_play(classic.selected,eununca.selected,hot.selected)

            CardSelect:
                id:hot
                color_on:1,0.2,0.2,1
                color_off:0.6,0.2,0.2,1
                icone:'fire'
                icone_size:'60dp'
                icone_pos:0.6
                titulo:'hot'
                desc:f'{len(App.MDApp.get_running_app().showcard.perguntas_hot)} Cartas'
                on_release:root.in_play(classic.selected,eununca.selected,hot.selected)

        MDFloatLayout:
            id:player
            size_hint_y:None
            height:dp(70)
            MDFloatingActionButton:
                icon:'play'
                pos_hint:{'right':0.95,'y':-0.8}
                
                md_bg_color:1,1,1,1
                theme_text_color:'Custom'
                text_color:0,0,0.01,1
                on_press:root.play()
                
<ShowCard>:
    MDBoxLayout:
        orientation:'vertical'
        md_bg_color:root.fundo
        size_hint:0.9,0.8
        padding:dp(3)
        radius:dp(7)
        MDIconButton:
            icon:'close'
            pos_hint:{'right':1}
            on_press:root.dismiss()

        MDIcon:
            icon:root.icone
            halign:'center'
            font_size:dp(80)
            adaptive_height:True
            
        MDBoxLayout:
            MDLabel:
                text:root.texto
                halign:'center'
                bold:True
                font_style:'Overline'
                font_size:dp(18)

        MDIconButton:
            id:replay
            icon:'replay'
            pos_hint:{'center_x':0.5}
            user_font_size:dp(35)
            on_press:root.set_tipo(choice(root.tipos))
            theme_text_color:'Custom'
            
<Manager>:
    Home:
        id:home
        name:'home'
'''
class CardSelect(RectangularRippleBehavior,ButtonBehavior,MDRelativeLayout):
    icone = StringProperty('')
    titulo = StringProperty('')
    desc = StringProperty('')
    icone_size = StringProperty('40dp')
    icone_pos = NumericProperty(0.5)
    cor = ListProperty([1,1,1,1])
    selected = BooleanProperty(False)
    color_on = ListProperty([1,1,1,1])
    color_off = ListProperty([1,1,1,1])
    def on_color_off(self,element,valor):
        self.cor = valor
        
    def on_press(self,*args):
        self.selected = not self.selected
    
    def on_selected(self,objeto,valor):
        self.cor = self.color_on if valor else self.color_off

from kivymd.uix.dialog import BaseDialog
class ShowCard(BaseDialog):
    fundo = ListProperty([1,1,1,1])
    icone = StringProperty('')
    texto = StringProperty('')
    perguntas_classico = [
        'quem é mais provavel de iludir?',
        'quem é mais provavel de engravidar primeiro?',
        'quem é mais provavel de voltar com o ex?',
        'quem é mais provavel de se apaixonar facil?',
        'quem é mais provavel de arrumar briga?',
        'quem é mais provavel de ir preso?',
        'quem é mais provavel de se irritar mais facil?',
        'quem é mais provavel de nao ir num encontro confirmado?',
        'quem é mais provavel de desistir de sair na ultima hora?',
        'quem é mais provavel de morar fora do pais?',
        'quem é mais provavel de casar primeiro?',
        'quem é mais provavel de chegar atrasado?',
        'quem é mais provavel de esquecer o aniversario da outra?',
        'quem é mais provavel de ficar irritado mais facil?',
        'quem é mais provavel de fazer mais drama?',
        'quem é mais provavel de ir ao shopping passear e acabar comprando coisas que nao precisa?'
    ]
    perguntas_eu_nunca = [
        'eu nunca fiquei abcecado em stalkear alguem nas redes sociais',
        'eu nunca fui expulso da sala de aula',
        'eu nunca desmaiei na rua',
        'eu nunca peguei corona com estranhos',
        'eu nunca andei a cavalo',
        'eu nunca quebrei um osso',
        'eu nunca quebrei um dente',
        'eu nunca tive uma experiencia paranormal',
        'eu nunca tive algum perfil na rede social hacheado',
        'eu nunca roubei algo em uma loja',
        'eu nunca tive paralisia do sono',
        'eu nunca fiquei preso no elevador',
        'eu nunca tentei cortar meu proprio cabelo',
        'eu nunca pintei o cabelo de alguma cor estranha',
        'eu nunca cantei em um karaoke na frente de varias pessoas',
        'eu nunca apareci na tv',
        'eu nunca passei mal em um parque de diversões',
        'eu nunca corri da policia',
        'eu nunca pedi dinheiro no sinal',
        'eu nunca me arrependi imediatamente apos enviar uma mensagem',
        'eu nunca levei um tapa no rosto',
        'eu nunca dei um tapa no rosto de alguem',
        'eu nunca chorei no tranporte publico',
        'eu nunca passei mais de dois dias sem tomar banho',
        'eu nunca olhei o celular de alguem sem que a pessoa soubesse',
        'eu nunca fui demitido',
        'eu nunca dormi na rua',
        'eu nunca peguei comida do lixo e comi'

        ]
    perguntas_hot = [
        'se voce pucesse ficar com qualquer pessoa no mundo, quem seria?',
        'qual foi sua experiencia mais vergonhosa?',
        'aqui ta calor ne? tira uma peça de roupa!',
        'qual é o seu maior desejo?',
        'quel é o seu pior defeito?',
        'colocaria silicone?',
        'geme alto ou baixinho?',
        'qual foi o sonho mais louco que voce ja teve?',
        'prefere por cima ou por baixo?',
        'gosta de dominar ou ser dominada?',
        'foder deitada ou de quatro é mais gostoso?',
        'pegaria alguem que esta jogando ?',
        'ja pegou alguem que esta jogando ?',
        'essa é sua chance escolha alguem do jogo para beijar!',
        'voce ja disse "eu te amo" para alguem ?',
        'voce ja disse "eu te amo" para alguem, mas era mentira ?',
        'ja fez alguma coisa estupida por amor ?',
        'nao é tão facil mas tire suas peças intimas',
        ]
    def __init__(self,tipos):
        super().__init__()
        self.tipos = tipos
        self.set_tipo(choice(self.tipos))
        
    def set_tipo(self,tipo):
        if tipo == 'classic':
            self.fundo = [1,1,1,1]
            self.icone = 'beer'
            self.texto = choice(self.perguntas_classico)
            self.ids.replay.text_color = [0,0,0,1]
        elif tipo == 'eununca':
            self.fundo = [0,0.8,0,1]
            self.icone = 'comment-processing-outline'
            self.texto = choice(self.perguntas_eu_nunca)
            self.ids.replay.text_color = [0,0,0,1]
        elif tipo == 'hot':
            self.fundo = [0.8,0,0,1]
            self.icone = 'fire'
            self.texto = choice(self.perguntas_hot)
            self.ids.replay.text_color = [0,0,0,1]
        elif tipo == 'info-classico':
            self.fundo = [1,1,1,1]
            self.icone = 'information-outline'
            self.texto = 'aqui o game é mais family friend'
            self.ids.replay.text_color = self.fundo
        elif tipo == 'info-eu nunca':
            self.fundo = [0,0.8,0,1]
            self.icone = 'information-outline'
            self.texto = 'eu nunca, você ja ?\njogo que sera falado um eu nunca e quem ja fez perde'
            self.ids.replay.text_color = self.fundo
        elif tipo == 'info-hot':
            self.fundo = [0.8,0,0,1]
            self.icone = 'information-outline'
            self.texto = 'é aqui onde o jogo fica mais quente\nrecomendo fortemente, que tenha certeza que quer esse modo de jogo\n+18'
            self.ids.replay.text_color = self.fundo
from kivy.metrics import dp
class Home(Screen):
    def on_enter(self, *args):
        return super().on_enter(*args)
    def in_play(self,*values):
        if any(values):
            Anime = Animation(top=dp(150),duration=0.2)
            
            Anime.start(self.ids.player)
        else:
            Anime = Animation(top =dp(60),duration=0.2)
            Anime.start(self.ids.player)
    def play(self):
        tipos = []
        if self.ids.classic.selected:
            tipos.append('classic')
        if self.ids.eununca.selected:
            tipos.append('eununca')
        if self.ids.hot.selected:
            tipos.append('hot')
        self.card = ShowCard(tipos)
        self.card.open()

    def info(self,tipo):
        self.card = ShowCard([tipo])
        self.card.open()
        
class Manager(ScreenManager):
    ...

class MainApp(MDApp):
    showcard = ShowCard
    def build(self):
        Builder.load_string(kv)
        self.sm = Manager()
        return self.sm
    
MainApp().run()
