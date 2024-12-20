import FreeSimpleGUI as sG
import PasswordGenerator as pG

password = ''
length = int(8)

# initialize some widgets
label = sG.Text("Generate password here")
input_box = sG.Input(length, key='inputer', size=8)
len_label = sG.Text("Password Length: ")
submit_button = sG.Button("Generate", key='submit', size=8)
choice_label = sG.Text("Select strength of password:")
weak_pass = sG.Radio("weak password", group_id="rad1", background_color='yellow', text_color='black', key="rad1")
strong_pass = sG.Radio("Strong password", group_id="rad1", background_color='green', text_color='black', key="rad2")
generated_password = sG.LBox([password], size=(30, 1), key="gener")


# set window layouts and app title
window = sG.Window("Password Generator App", layout=[[label], [len_label, input_box],
                                                     [choice_label], [weak_pass, strong_pass], [submit_button],
                                                     [generated_password]])

# loop the operation
while True:
    event, values = window.read()
    match event:
        case 'submit':
            if values['rad2']:
                try:
                    length = int(values['inputer'])
                    if length < 8:
                        sG.popup("password length for strong version\n can't be less than 8,"
                                 " \n so use auto produced",
                                 font=('Helvetica', 10))
                    password = pG.strong_pass(length)
                    window['gener'].update(values=[password])
                except ValueError:
                    sG.popup("caution your input isn't a digit!", font=("Helvetica", 15))
            else:
                try:
                    length = int(values['inputer'])
                    if length < 8:
                        sG.popup("password length for weak version\n can't be less than 4,"
                                 " \n so use auto produced",
                                 font=('Helvetica', 10))
                    password = pG.weak_pass(length)
                    window['gener'].update(values=[password])
                except ValueError:
                    sG.popup("caution your input isn't a digit!", font=("Helvetica", 15))
        case sG.WIN_CLOSED:
            break

window.close()
