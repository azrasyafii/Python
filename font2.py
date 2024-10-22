import PySimpleGUI as sg
sg.theme("DarkTeal7")
sg.theme_text_color("#FF0000")
window = sg.Window(title="Profile Mahasiswa",
    layout=[[sg.Text("SELAMAT DATANG DI KELAS", font=("Arial",25))],
    [sg.Text("NPM       : 2210010285")],
    [sg.Text("Nama      : Muhammad Azra Syafi'i")],
    [sg.Text("Kelas     : 5A Non Reguler Banjarmasin")],
    [sg.Text("Matkul    : Pemrograman Visual 3")],
    ],
    size=(500,250),
    font=("Times", 18))
window()
window.close()
