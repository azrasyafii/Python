import PySimpleGUI as sg
window = sg.Window(title="Profile Mahasiswa",layout=[
    [sg.Text("NPM       : 2210010285")],
    [sg.Text("Nama      : Muhammad Azra Syafi'i")],
    [sg.Text("Kelas     : 5A Non Reguler Banjarmasin")],
    [sg.Text("Matkul    : Pemrograman Visual 3")],
],size=(400,200))
window()
window.close()