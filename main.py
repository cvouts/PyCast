import time
import tkinter as tk
import pychromecast


# pyinstaller --add-data "logos/*.png;logos/" main.py


def get_channels():
    list_of_channels = []

    list_of_channels.append(["https://ert-live-bcbs15228.siliconweb.com/media/ert_1/ert_1medium.m3u8",
                            "video/MP2T", "ert1.png"])
    list_of_channels.append(["https://ert-live-bcbs15228.siliconweb.com/media/ert_2/ert_2medium.m3u8",
                            "video/MP2T", "ert2.png"])
    list_of_channels.append(["https://r1---sn-vuxbavcx-n3bl.googlevideo.com/", "video/mp4a", "ert3.png"])
    list_of_channels.append(["https://antennalivesp-lh.akamaihd.net/i/live_1@715138/index_800_av-p.m3u8",
                            "video/MP2T", "antenna.png"])
    list_of_channels.append(["https://alphalive-i.akamaihd.net/hls/live/682300/live/high/prog_index.m3u8",
                            "video/MP2T", "alpha.png"])
    list_of_channels.append(["https://liveopencloud.siliconweb.com/1/ZlRza2R6L2tFRnFJ/eWVLSlQx/hls/kcmblc8k/2728/chunklist.m3u8",
                             "video/MP2T", "open.png"])
    list_of_channels.append(["https://skai-live-gr-cy.siliconweb.com/media/cambria2/index_bitrate2750K.m3u8",
                             "video/MP2T", "skai.png"])
    list_of_channels.append(["https://livestar.siliconweb.com/media/star1/star1mediumhd.m3u8",
                             "video/MP2T", "star.png"])

    return list_of_channels

def create_gui(window, media_controller, input_list, cast):
    button_list = []

    row_number = 0
    column_number = 0

    for i in range(0, len(input_list)):
        if column_number == 3:  # three columns per row, starting with 0
            column_number = 0
            row_number += 1

        this_logo = tk.PhotoImage(file="logos/"+input_list[i][2])  # 382 x 134 is the size of the images for the buttons

        button_list.append(tk.Button(master=window,
                                     image=this_logo,
                                     command=lambda i=i: cast_on_button(media_controller, input_list[i])))
                                        # i=i here ensures that the current i is passed into input_list each time,
                                        # instead of the last one

        if i == 2:
            button_list[i]["state"] = "disabled"


        button_list[i].image = this_logo  # without this line only the last image will be loaded
        button_list[i].grid(row=row_number, column=column_number, sticky="nsew")
        column_number += 1

    stop_sign = tk.PhotoImage(file="logos/stop.png")
    exit_button = tk.Button(master=window, image=stop_sign, command=lambda: cast.quit_app())
    exit_button.grid(row=row_number, column=column_number)

    window.mainloop()


def cast_on_button(media_controller, input_data):
    print("got a request, current state is:", media_controller.status.player_state)
    media_controller.play_media(input_data[0], input_data[1])
    media_controller.block_until_active()
    media_controller.pause()
    time.sleep(3)
    media_controller.play()
    print("response sent, current state is:", media_controller.status.player_state)
    time.sleep(5)
    print("... current state is:", media_controller.status.player_state, "\n~")


def main():
    services, browser = pychromecast.discovery.discover_chromecasts()
    pychromecast.discovery.stop_discovery(browser)

    all_chromecasts, browser = pychromecast.get_listed_chromecasts(friendly_names=["Living Room TV"])
    chromecast = all_chromecasts[0]
    chromecast.wait()

    media_controller = chromecast.media_controller

    window = tk.Tk()
    address_list = get_channels()
    create_gui(window, media_controller, address_list, chromecast)

    media_controller.block_until_active()
    print(media_controller.status.player_state)

    print(media_controller.status.player_state)
    # window.mainloop()

    pychromecast.discovery.stop_discovery(browser)


if __name__ == "__main__":
    main()

# media_controller.play_media("http://commondatastorage.googleapis.com/gtv-videos-bucket/sample/BigBuckBunny.mp4", "video/mp4")