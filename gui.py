import customtkinter as ctk
import tkinter as tk
from PIL import Image, ImageTk

def main():
    interface(callback)

def callback(list, string):
    return list,string
def interface(callback):
    # Configurar modo de apariencia y tema
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("theme/kaiju_theme.json")

    # Inicializar la ventana
    window = ctk.CTk()
    window.title("KaijuKana")
    window.geometry("1600x900")
    window.configure(bg="#44344F")

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

    # Función para cambiar el modo de apariencia
    global mode
    mode = "dark"


    def change_mode():
        global mode
        if mode == "dark":
            ctk.set_appearance_mode("light")
            mode = "light"
        else:
            ctk.set_appearance_mode("dark")
            mode = "dark"


    # Crear el label de cabecera
    header_frame = ctk.CTkFrame(window,
                                width=1600,
                                height=80,
                                fg_color=("#C2F970", "#44344F"))
    header_frame.pack()
    header_frame.columnconfigure(0, weight=1)

    label = ctk.CTkLabel(header_frame,
                        text="     KaijuKana",
                        font=("NotoSansJp", 50, "bold"),
                        fg_color=("#C2F970", "#44344F"),
                        text_color=("#44344F", "#C2F970"),
                        width=1600,
                        height=80,
                        anchor="w",
                        corner_radius=0)
    label.grid(column=0, row=0, padx=(0, 500))

    # Crear frame logo Godzilla
    godzilla_label = ctk.CTkLabel(window,
                                image=godzilla_logo,
                                text="",
                                fg_color=("#C2F970", "#44344F"),
                                )
    godzilla_label.place(x=320, y=10)

    # Crear el botón de cambio de modo claro/oscuro
    dark_light_button = ctk.CTkButton(header_frame,
                                    text="",
                                    image=dark_light_icon,
                                    fg_color=("#C2F970", "#44344F"),
                                    hover_color=("#C2F970", "#44344F"),
                                    corner_radius=0,
                                    command=change_mode)
    dark_light_button.grid(column=0, row=0, sticky="e")

    # Crear Tabview
    tab_frame = ctk.CTkFrame(window,
                            width=1600,
                            height=800,
                            fg_color=("#d7f9d9", "#2B2031"))
    tab_frame.pack()
    kana_tab = ctk.CTkTabview(tab_frame,
                            width=1600,
                            height=600,
                            fg_color=("#d7f9d9", "#2B2031"),
                            segmented_button_fg_color=("#C2F970", "#44344F"),
                            segmented_button_selected_color=("#acf63c", "#35283E"),
                            segmented_button_selected_hover_color=("#9BF514", "#44344F"),
                            segmented_button_unselected_color=("#c2f970", "#44344F"),
                            text_color=("#44344F", "#C2F970")
                            )
    kana_tab._segmented_button.configure(font=("NotoSansJp", 20, "bold"))
    kana_tab.pack()

    # Crear tabs
    tab_hiragana = kana_tab.add("Hiragana")
    tab_katakana = kana_tab.add("Katakana")

    create_selection_layout(kana_tab.tab("Hiragana"), "Hiragana", window)
    create_selection_layout(kana_tab.tab("Katakana"), "Katakana", window)

    # Background
    background = ctk.CTkLabel(window,
                            text=" ",
                            fg_color=("#d7f9d9", "#2B2031"),
                            width=1600,
                            height=900)
    background.pack()
    # Ejecutar el bucle principal de la aplicación
    window.mainloop()

def toggle_all(all_checkbox, main_checkbox, dakuten_checkbox, combination_checkbox, main_frame, dakuten_frame, combination_frame):
    if all_checkbox.get() == 1:
        for checkbox, frame in [(main_checkbox, main_frame), (dakuten_checkbox, dakuten_frame), (combination_checkbox, combination_frame)]:
            checkbox.select()
            toggle_group(checkbox, frame)
    else:
        for checkbox, frame in [(main_checkbox, main_frame), (dakuten_checkbox, dakuten_frame), (combination_checkbox, combination_frame)]:
            checkbox.deselect()
            toggle_group(checkbox, frame)


def toggle_group(group_checkbox, frame):
    if group_checkbox.get() == 1:
        for checkbox in frame.winfo_children():
            checkbox.select()
    else:
        for checkbox in frame.winfo_children():
            checkbox.deselect()


def start_quiz(main_frame, dakuten_frame, combination_frame, tab_name, window):
    selected_kana = []
    for frame in (main_frame, dakuten_frame, combination_frame):
        for checkbox in frame.winfo_children():
            if checkbox.get() == 1:
                text = checkbox.cget("text")
                selected_kana.append(text)
    print(selected_kana)
    callback(selected_kana, tab_name)
    window.destroy()




    # Usar place para posicionar el botón en la esquina superior derecha del label



def create_checkboxes(tab_name, frame_main, frame_dakuten, frame_combination):
    main_kana_hiragana = ["あ/a", "か/ka", "さ/sa", "た/ta",
                        "な/na", "は/ha", "ま/ma", "や/ya", "ら/ra", "わ/wa"]
    main_kana_katakana = ["ア/a", "カ/ka", "サ/sa", "タ/ta",
                        "ナ/na", "ハ/ha", "マ/ma", "ヤ/ya", "ラ/ra", "ワ/wa"]
    dakuten_kana_hiragana = ["が/ga", "ざ/za", "だ/da", "ば/ba", "ぱ/pa"]
    dakuten_kana_katakana = ["ガ/ga", "ザ/za", "ダ/da", "バ/ba", "パ/pa"]
    combination_kana_hiragana = ["きゃ/kya", "しゃ/sha", "ちゃ/cha", "にゃ/nya", "ひゃ/hya",
                                "みゃ/mya", "りゃ/rya", "ぎゃ/gya", "じゃ/ja", "ぢゃ/dya", "びゃ/bya", "ぴゃ/pya"]
    combination_kana_katakana = ["キャ/kya", "シャ/sha", "チャ/cha", "ニャ/nya", "ヒャ/hya",
                                "ミャ/mya", "リャ/rya", "ギャ/gya", "ジャ/ja", "ヂャ/dya", "ビャ/bya", "ピャ/pya",
                                "ヴァ/va", "ウィ/wi", "ファ/fa", "ツァ/tsa", "シェ/she", "ジェ/je", "チェ/che", "Irregular"]
    if tab_name == "Hiragana":
        main_kana = main_kana_hiragana
        dakuten_kana = dakuten_kana_hiragana
        combination_kana = combination_kana_hiragana
    else:
        main_kana = main_kana_katakana
        dakuten_kana = dakuten_kana_katakana
        combination_kana = combination_kana_katakana

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
    tab.grid_rowconfigure(0, weight=1)
    tab.grid_columnconfigure(0, weight=1)

    scroll_frame = ctk.CTkScrollableFrame(tab,
                                        width=1500,
                                        height=500,
                                        fg_color=("#d7f9d9", "#2B2031"))
    scroll_frame.grid(column=0)
    scroll_frame.grid_columnconfigure(0, weight=1, minsize=420)
    scroll_frame.grid_columnconfigure(1, weight=1, minsize=420)
    scroll_frame.grid_columnconfigure(2, weight=1, minsize=420)

    all_kana = ctk.CTkCheckBox(scroll_frame, text="All Kana", command=lambda: toggle_all(
        all_kana, all_main_kana, all_dakuten_kana, all_combination_kana, left_frame, center_frame, right_frame))
    all_kana.grid(row=0, column=1, pady=(20, 30))

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

    value_var = tk.IntVar(value=0)

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

    left_frame = ctk.CTkFrame(scroll_frame, fg_color="transparent")
    center_frame = ctk.CTkFrame(scroll_frame, fg_color="transparent")
    right_frame = ctk.CTkFrame(scroll_frame, fg_color="transparent")

    left_frame.grid(row=3, column=0, padx=(35, 0), sticky="nsew")
    center_frame.grid(row=3, column=1, sticky="nsew")
    right_frame.grid(row=3, column=2, sticky="nsew")

    # left_frame.grid_columnconfigure(0, weight=0)
    center_frame.grid_columnconfigure(0, weight=1)
    right_frame.grid_columnconfigure(0, weight=1)

    create_checkboxes(tab_name, left_frame, center_frame, right_frame)

    lower_frame = ctk.CTkFrame(tab,
                            width=1600,
                            height=100,
                            fg_color=("#C2F970", "#44344F"))
    lower_frame.grid()
    start_button = ctk.CTkButton(lower_frame,
                                height=50,
                                text="Start",
                                text_color=("#44344F", "#C2F970"),
                                fg_color=("#C2F970", "#44344F"),
                                hover_color=("#b4b7ae", "#6a6b6f"),
                                command=lambda: start_quiz(left_frame, center_frame, right_frame, tab_name, window))
    start_button.pack()


if __name__ == "__main__":
    main()
