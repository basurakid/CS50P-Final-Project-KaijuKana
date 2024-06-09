import customtkinter as ctk
from PIL import Image


class Window(ctk.CTk):
    def __init__(self):
        ctk.CTk.__init__(self)

        # Configurar modo de apariencia y tema
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("theme/kaiju_theme.json")

        # Inicializar la ventana
        self.title("KaijuKana")
        self.geometry("1600x900")
        self.configure(bg="#44344F")

        # Cargar imágenes para el botón de modo claro/oscuro
        dark_light_icon = ctk.CTkImage(light_image=Image.open("images/light_mode.png"),
                                       dark_image=Image.open("images/dark_mode.png"),
                                       size=(50, 50))
        # Cargar imágenes para el logo de Godzilla
        godzilla_logo = ctk.CTkImage(light_image=Image.open("images/godzilla_light.png"),
                                     dark_image=Image.open("images/godzilla_dark.png"),
                                     size=(64, 64))

        # Cargar Font
        ctk.FontManager.load_font("fonts/NotoSansJP.ttf")

        # Frame de cabecera
        self.header_frame = ctk.CTkFrame(self,
                                         width=1600,
                                         height=80,
                                         fg_color=("#C2F970", "#44344F"))
        self.header_frame.pack()
        self.header_frame.columnconfigure(0, weight=1)

        # Label cabecera
        self.label = ctk.CTkLabel(self.header_frame,
                                  text="     KaijuKana",
                                  font=("NotoSansJp", 50, "bold"),
                                  fg_color=("#C2F970", "#44344F"),
                                  text_color=("#44344F", "#C2F970"),
                                  width=1600,
                                  height=80,
                                  anchor="w",
                                  corner_radius=0)
        self.label.grid(column=0, row=0, padx=(0, 500))

        # Imagen godzilla cabecera
        self.godzilla_label = ctk.CTkLabel(self,
                                           image=godzilla_logo,
                                           text="",
                                           fg_color=("#C2F970", "#44344F"),
                                           )
        self.godzilla_label.place(x=320, y=10)
        self.mode = "dark"

        # Crear el botón de cambio de modo claro/oscuro
        self.dark_light_button = ctk.CTkButton(self.header_frame,
                                               text="",
                                               image=dark_light_icon,
                                               fg_color=("#C2F970", "#44344F"),
                                               hover_color=("#C2F970", "#44344F"),
                                               corner_radius=1,
                                               command=self.change_mode)
        self.dark_light_button.grid(column=3, row=0, sticky="e")

        # Almacenaje de seleccion y respuestas
        self.selected_kana = []
        self.selected_tab = ""
        self.quiz_kana = []
        self.quiz_answers = []

        # Interfaz de seleccion
        self.frame = SelectionFrame(self)
        self.frame.pack()

        # Contador de frames
        self.frame_counter = 0

    def switch_frame(self, frame: ctk.CTkFrame, *args):
        """
        Cambia el frame al siguiente con uso del contador frame_counter
        """
        self.frame.destroy()
        if self.frame_counter == 0:
            self.frame = QuizFrame(self, *args)
            self.frame_counter = 1
        else:
            self.frame = ScoreFrame(self, *args)
        self.frame.pack()

    # Función para cambiar el modo de apariencia
    def change_mode(self):
        """
        Toggle de modos para el boton
        """
        if self.mode == "dark":
            ctk.set_appearance_mode("light")
            self.mode = "light"
        else:
            ctk.set_appearance_mode("dark")
            self.mode = "dark"

# Frame de seleccion kana


class SelectionFrame(ctk.CTkFrame):
    def __init__(self, parent: Window):
        ctk.CTkFrame.__init__(self, parent)
        # Frame general
        self.tab_frame = ctk.CTkFrame(self,
                                      width=1600,
                                      height=800,
                                      fg_color=("#d7f9d9", "#2B2031"))
        self.tab_frame.pack()

        # Tabview de hiragana/katakana
        self.kana_tab = ctk.CTkTabview(self.tab_frame,
                                       width=1600,
                                       height=600,
                                       fg_color=("#d7f9d9", "#2B2031"),
                                       segmented_button_fg_color=("#C2F970", "#44344F"),
                                       segmented_button_selected_color=("#acf63c", "#35283E"),
                                       segmented_button_selected_hover_color=("#9BF514", "#44344F"),
                                       segmented_button_unselected_color=("#c2f970", "#44344F"),
                                       text_color=("#44344F", "#C2F970")
                                       )
        self.kana_tab._segmented_button.configure(font=("NotoSansJp", 20, "bold"))
        self.kana_tab.pack()

        # Crear tabs
        self.tab_hiragana = self.kana_tab.add("Hiragana")
        self.tab_katakana = self.kana_tab.add("Katakana")

        # Crear el layout de checkboxes y labels
        create_selection_layout(self.kana_tab.tab("Hiragana"), "Hiragana", parent)
        create_selection_layout(self.kana_tab.tab("Katakana"), "Katakana", parent)


# Frame de quiz para respuestas
class QuizFrame(ctk.CTkFrame):
    def __init__(self, parent: Window):
        ctk.CTkFrame.__init__(self, parent)

        # Frame scrolleable por si quiz es demasiado largo
        self.scroll_frame = ctk.CTkScrollableFrame(self,
                                                   width=1250,
                                                   height=550,
                                                   fg_color=("#d7f9d9", "#2B2031"))
        self.scroll_frame.grid(sticky="nsew")

        self.instructions = ctk.CTkLabel(self.scroll_frame,
                                             text="Type answer in Romaji",
                                             font=("NotoSansJp", 30, "bold"))
        # Si hay mas de 10 kanas, se asigna con divmod
        if len(parent.quiz_kana) > 10:

            self.instructions.grid(column=0, columnspan=10, row=0, pady=(15, 25))

            for i in range(10):
                self.scroll_frame.grid_columnconfigure(i, weight=1)

            for i, kana in enumerate(parent.quiz_kana):
                row, col = divmod(i, 10)
                self.label = ctk.CTkLabel(self.scroll_frame, text=kana[1], width=65)
                self.entry = ctk.CTkEntry(self.scroll_frame, width=65)
                self.label.grid(row=row*2+1, column=col, padx=10, pady=(10, 5))
                self.entry.grid(row=row*2+2, column=col, padx=10, pady=5)

        # Si hay menos de 10, se usa el numero de kanas para asignar columnas
        else:
            quiz_length = len(parent.quiz_kana)

            self.instructions.grid(column=0, columnspan=quiz_length, row=0, pady=(15, 25))

            for i in range(quiz_length):
                self.scroll_frame.grid_columnconfigure(i, weight=1)

            for i, kana in enumerate(parent.quiz_kana):
                self.label = ctk.CTkLabel(self.scroll_frame, text=kana[1], width=65)
                self.entry = ctk.CTkEntry(self.scroll_frame, width=65)
                self.label.grid(row=1, column=i, padx=10, pady=(10, 5))
                self.entry.grid(row=2, column=i, padx=10, pady=5)

        # Frame inferior y boton de entregar
        self.lower_frame = ctk.CTkFrame(self,
                                        width=1600,
                                        height=100,
                                        fg_color=("#d7f9d9", "#2B2031"))
        self.lower_frame.grid(sticky="ew")

        self.submit_button = ctk.CTkButton(self.lower_frame,
                                           height=50,
                                           text="Submit",
                                           text_color=("#44344F", "#C2F970"),
                                           fg_color=("#C2F970", "#44344F"),
                                           hover_color=("#b4b7ae", "#6a6b6f"),
                                           command=lambda: submit_quiz(self.scroll_frame, parent))
        self.submit_button.pack()

# Frame de resultados


class ScoreFrame(ctk.CTkFrame):
    def __init__(self, parent: Window):
        ctk.CTkFrame.__init__(self, parent)
        # Configurar el color de fondo de frame y columnas, rows
        self.configure(fg_color=("#d7f9d9", "#2B2031"))

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # Resultado en porcentajes para decidir el mensaje
        score_percentage = percentage = round(
            (parent.quiz_score / len(parent.quiz_answers)) * 100, 2)

        # Frame general
        self.inner_frame = ctk.CTkScrollableFrame(self,
                                        width=1600,
                                        height=800,
                                        fg_color=("#d7f9d9", "#2B2031"))
        self.inner_frame.grid(column=0, row=0, sticky="nsew")
        # self.inner_frame.grid_propagate(False)

        self.inner_frame.grid_columnconfigure(0, weight=1)

        for i in range(3):
            self.inner_frame.grid_rowconfigure(i, weight=1)


        # Mensaje custom con los resultados
        if score_percentage < 50:
            self.text_label = ctk.CTkLabel(self.inner_frame,
                                           text="Keep trying!",
                                           font=("NotoSansJp", 50, "bold"))

        elif 50 < score_percentage < 90:
            self.text_label = ctk.CTkLabel(self.inner_frame,
                                           text="Not bad!",
                                           font=("NotoSansJp", 50, "bold"))
        elif 90 < score_percentage < 99:
            self.text_label = ctk.CTkLabel(self.inner_frame,
                                           text="Very well done!",
                                           font=("NotoSansJp", 50, "bold"))
        else:
            self.text_label = ctk.CTkLabel(self.inner_frame,
                                           text="PERFECT!",
                                           font=("NotoSansJp", 50, "bold"))
        self.text_label.grid(column=0, row=0, pady=(80, 50))

        # Frame caja de texto para Score
        self.box = ctk.CTkFrame(self.inner_frame,
                                width=300,
                                height=200,
                                fg_color=("#C2F970", "#44344F"),
                                border_color=("#44344F", "#C2F970"),
                                border_width=3)
        self.box.grid(column=0, row=1, pady=(0,60))
        self.box.grid_propagate(False)

        self.box.columnconfigure(0, weight=1)
        self.box.rowconfigure(0, weight=0)
        self.box.rowconfigure(1, weight=0)

        # Label "score"
        self.score_label = ctk.CTkLabel(self.box,
                                        text=f"Score: {parent.quiz_score}/{len(parent.quiz_answers)}")
        self.score_label.grid(column=0, row=0, pady=(60, 10))

        # Label score en percentajes
        self.score_percentage = ctk.CTkLabel(self.box,
                                             text=f"{score_percentage}% correct")
        self.score_percentage.grid(column=0, row=1)

        # Cargar imagen godzilla para que aguante la caja
        big_godzilla_logo = ctk.CTkImage(light_image=Image.open("images/godzilla_light_128px.png"),
                                         dark_image=Image.open("images/godzilla_dark_128px.png"),
                                         size=(128, 128))

        self.big_godzilla_label = ctk.CTkLabel(self.inner_frame,
                                               image=big_godzilla_logo,
                                               text="",
                                               fg_color="transparent")
        self.big_godzilla_label.place(x=780, y=280)

        self.results_frame = ctk.CTkFrame(self.inner_frame,
                                          width=1250,
                                          fg_color=("#d7f9d9", "#2B2031"))
        self.results_frame.grid(column=0, row=2)


        if len(parent.quiz_kana) > 10:
            for i in range(10):
                self.results_frame.grid_columnconfigure(i, weight=1)

            for i, kana in enumerate(parent.quiz_kana):
                row, col = divmod(i, 10)
                self.kana_quiz = ctk.CTkLabel(self.results_frame, text=kana, width=65)
                self.answer = ctk.CTkLabel(self.results_frame,text=f"{parent.wrong_answers[i]} {parent.quiz_answers[i]}", width=65)
                self.kana_quiz.grid(row=row*2, column=col, padx=10, pady=(10, 5))
                self.answer.grid(row=row*2+1, column=col, padx=10, pady=5)

        # Si hay menos de 10, se usa el numero de kanas para asignar columnas
        else:
            quiz_length = len(parent.quiz_kana)

            for i in range(quiz_length):
                self.results_frame.grid_columnconfigure(i, weight=1)

            for i, kana in enumerate(parent.quiz_kana):
                self.kana_quiz = ctk.CTkLabel(self.results_frame, text=f"{kana[0]}/{kana[1]}", width=65)
                self.answer = ctk.CTkLabel(self.results_frame, text=f"{parent.wrong_answers[i]} {parent.quiz_answers[i]}", width=65)
                self.kana_quiz.grid(row=0, column=i, padx=10, pady=(10, 5))
                self.answer.grid(row=1, column=i, padx=10, pady=5)


def submit_quiz(scroll_frame, window):
    """
    Checkea si los widget son CTkEntry, lo asigna a atributo de window. Cambia de frame
    """
    quiz_answers = []
    for widget in scroll_frame.winfo_children():
        if isinstance(widget, ctk.CTkEntry):
            answer = widget.get()
            quiz_answers.append(answer)
    window.quiz_answers = quiz_answers


def toggle_all(all_checkbox, main_checkbox, dakuten_checkbox, combination_checkbox, main_frame, dakuten_frame, combination_frame):
    """
    Checkea el estado de all_checkbox, togglea todo a través de grupos con toggle_group
    """
    if all_checkbox.get() == 1:
        for checkbox, frame in [(main_checkbox, main_frame), (dakuten_checkbox, dakuten_frame), (combination_checkbox, combination_frame)]:
            checkbox.select()
            toggle_group(checkbox, frame)
    else:
        for checkbox, frame in [(main_checkbox, main_frame), (dakuten_checkbox, dakuten_frame), (combination_checkbox, combination_frame)]:
            checkbox.deselect()
            toggle_group(checkbox, frame)


def toggle_group(group_checkbox, frame):
    """
    Checkea el estado de group checkbox, togglea los checkbox dentro del respectivo frame
    """
    # Dependiendo del estado de group checkbox se itera para activar o desactivar
    if group_checkbox.get() == 1:
        for checkbox in frame.winfo_children():
            checkbox.select()
    else:
        for checkbox in frame.winfo_children():
            checkbox.deselect()


def start_quiz(main_frame, dakuten_frame, combination_frame, tab_name, window):
    """
    Crea lista selected_kana y por cada frame checkea el estado delos checkboxes, los añade si es necesario y lo devuelve a atributo window. Cambia de frame
    """
    # Itera en cada widget de cada frame, si esta activado pasa a la lista de seleccion
    selected_kana = []
    for frame in (main_frame, dakuten_frame, combination_frame):
        for checkbox in frame.winfo_children():
            if checkbox.get() == 1:
                text = checkbox.cget("text")
                selected_kana.append(text)
    # Si no hay nada salimos de funcion para que no
    if not selected_kana:
        return
    window.selected_kana = selected_kana
    window.selected_tab = tab_name


def create_checkboxes(tab_name, frame_main, frame_dakuten, frame_combination):
    """
    Helper para crear checkboxes de tabs a partir de listas de kana inicial
    """
    # Listas de kana
    main_kana_hiragana = ["あ/a", "か/ka", "さ/sa", "た/ta",
                          "な/na", "は/ha", "ま/ma", "や/ya", "ら/ra", "わ/wa"]
    main_kana_katakana = ["ア/a", "カ/ka", "サ/sa", "タ/ta",
                          "ナ/na", "ハ/ha", "マ/ma", "ヤ/ya", "ラ/ra", "ワ/wa"]
    dakuten_kana_hiragana = ["が/ga", "ざ/za", "だ/da", "ば/ba", "ぱ/pa"]
    dakuten_kana_katakana = ["ガ/ga", "ザ/za", "ダ/da", "バ/ba", "パ/pa", "ヴ/vu"]
    combination_kana_hiragana = ["きゃ/kya", "しゃ/sha", "ちゃ/cha", "にゃ/nya", "ひゃ/hya",
                                 "みゃ/mya", "りゃ/rya", "ぎゃ/gya", "じゃ/ja", "ぢゃ/dya", "びゃ/bya", "ぴゃ/pya"]
    combination_kana_katakana = ["キャ/kya", "シャ/sha", "チャ/cha", "ニャ/nya", "ヒャ/hya",
                                 "ミャ/mya", "リャ/rya", "ギャ/gya", "ジャ/ja", "ヂャ/dya", "ビャ/bya", "ピャ/pya",
                                 "ヴァ/va", "ウィ/wi", "ファ/fa", "ツァ/tsa", "シェ/she", "ジェ/je", "チェ/che", "Irregular"]
    # Seleccion de listas por tab name
    if tab_name == "Hiragana":
        main_kana = main_kana_hiragana
        dakuten_kana = dakuten_kana_hiragana
        combination_kana = combination_kana_hiragana
    else:
        main_kana = main_kana_katakana
        dakuten_kana = dakuten_kana_katakana
        combination_kana = combination_kana_katakana

    # Crear y ordena los checkbox de cada grupo
    for i, text in enumerate(main_kana):
        row, col = divmod(i, 2)
        checkbox = ctk.CTkCheckBox(frame_main, text=text)
        checkbox.grid(row=row, column=col, padx=(35), pady=(5, 5))

    for i, text in enumerate(dakuten_kana):
        checkbox = ctk.CTkCheckBox(frame_dakuten, text=text)
        checkbox.grid(row=i, column=0, padx=(25), pady=(5, 5))

    for i, text in enumerate(combination_kana):
        row, col = divmod(i, 2)
        checkbox = ctk.CTkCheckBox(frame_combination, text=text)
        checkbox.grid(row=row, column=col, padx=(25), pady=(5, 5), sticky="ew")


def create_selection_layout(tab, tab_name, window):
    """
    Crea interfaz básica de selección en tabs, con los frames para checkbox y boton de inicio
    """
    tab.grid_rowconfigure(0, weight=1)
    tab.grid_columnconfigure(0, weight=1)

    # Frame scrolleable para katakana
    scroll_frame = ctk.CTkScrollableFrame(tab,
                                          width=1500,
                                          height=500,
                                          fg_color=("#d7f9d9", "#2B2031"))
    scroll_frame.grid(column=0)
    scroll_frame.grid_columnconfigure(0, weight=1, minsize=420)
    scroll_frame.grid_columnconfigure(1, weight=1, minsize=420)
    scroll_frame.grid_columnconfigure(2, weight=1, minsize=420)

    # Boton all kana
    all_kana = ctk.CTkCheckBox(scroll_frame, text="All Kana", command=lambda: toggle_all(
        all_kana, all_main_kana, all_dakuten_kana, all_combination_kana, left_frame, center_frame, right_frame))
    all_kana.grid(row=0, column=1, pady=(20, 30))

    # Labels de grupo
    main_kana_label = ctk.CTkLabel(scroll_frame,
                                   width=5,
                                   anchor="center",
                                   text="Main Kana",
                                   font=("NotoSansJp", 30, "bold"))
    main_kana_label.grid(column=0, row=1, pady=(0, 20))

    dakuten_kana_label = ctk.CTkLabel(scroll_frame,
                                      width=5,
                                      anchor="center",
                                      text="Dakuten Kana",
                                      font=("NotoSansJp", 30, "bold"))
    dakuten_kana_label.grid(column=1, row=1, pady=(0, 20))

    combination_kana_label = ctk.CTkLabel(scroll_frame,
                                          width=5,
                                          anchor="center",
                                          text="Combination Kana",
                                          font=("NotoSansJp", 30, "bold"))
    combination_kana_label.grid(column=2, row=1, pady=(0, 20))


    # Botones de grupo
    all_main_kana = ctk.CTkCheckBox(scroll_frame, text="All Main Kana",
                                    command=lambda: toggle_group(all_main_kana, left_frame))
    all_main_kana.configure()
    all_main_kana.grid(row=2, column=0, padx=(0))

    all_dakuten_kana = ctk.CTkCheckBox(
        scroll_frame, text="All Dakuten Kana", command=lambda: toggle_group(all_dakuten_kana, center_frame))
    all_dakuten_kana.grid(row=2, column=1, padx=(0))

    all_combination_kana = ctk.CTkCheckBox(
        scroll_frame, text="All Combination Kana", command=lambda: toggle_group(all_combination_kana, right_frame))
    all_combination_kana.grid(row=2, column=2, padx=(0))

    # Crea frame por grupo para poder checkear por separado
    left_frame = ctk.CTkFrame(scroll_frame, fg_color="transparent")
    center_frame = ctk.CTkFrame(scroll_frame, fg_color="transparent")
    right_frame = ctk.CTkFrame(scroll_frame, fg_color="transparent")

    left_frame.grid(row=3, column=0, padx=(35, 0), sticky="nsew")
    center_frame.grid(row=3, column=1, sticky="nsew")
    right_frame.grid(row=3, column=2, sticky="nsew")

    # left_frame.grid_columnconfigure(0, weight=0) causa problemas
    center_frame.grid_columnconfigure(0, weight=1)
    right_frame.grid_columnconfigure(0, weight=1)

    # Funcion helper para checkboxes
    create_checkboxes(tab_name, left_frame, center_frame, right_frame)

    # Frame para albergar start boton
    lower_frame = ctk.CTkFrame(tab,
                               width=1600,
                               height=100,
                               fg_color=("#d7f9d9", "#2B2031"))
    lower_frame.grid()
    start_button = ctk.CTkButton(lower_frame,
                                 height=50,
                                 text="Start",
                                 text_color=("#44344F", "#C2F970"),
                                 fg_color=("#C2F970", "#44344F"),
                                 hover_color=("#b4b7ae", "#6a6b6f"),
                                 command=lambda: start_quiz(left_frame, center_frame, right_frame, tab_name, window))
    start_button.pack()
