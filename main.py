import time
import tkinter as tk
import pychromecast


# pyinstaller --add-data "logos/*.png;logos/" main.py


def get_addresses():
    list_of_addresses = []

    list_of_addresses.append(["https://ert-live-bcbs15228.siliconweb.com/media/ert_1/ert_1medium.m3u8",
                              "video/MP2T", "ert1.png"])
    list_of_addresses.append(["https://antennalivesp-lh.akamaihd.net/i/live_1@715138/index_800_av-p.m3u8",
                              "video/MP2T", "antenna.png"])

    return list_of_addresses


def create_gui(window, media_controller, input_list):
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
                                     command=lambda: cast_on_button(media_controller, input_list[i])))
        
        button_list[i].image = this_logo  # without this line only the last image will be loaded
        button_list[i].grid(row=row_number, column=column_number, sticky="nsew")
        column_number += 1
    window.mainloop()


def cast_on_button(media_controller, input_data):
    media_controller.play_media(input_data[0], input_data[1])
    media_controller.block_until_active()
    media_controller.pause()
    time.sleep(5)
    media_controller.play()
    # print("pressed!")


def main():
    services, browser = pychromecast.discovery.discover_chromecasts()
    # print(services)
    pychromecast.discovery.stop_discovery(browser)

    all_chromecasts, browser = pychromecast.get_listed_chromecasts(friendly_names=["Living Room TV"])
    chromecast = all_chromecasts[0]
    chromecast.wait()
    # print(chromecast.status)

    media_controller = chromecast.media_controller

    window = tk.Tk()
    address_list = get_addresses()
    create_gui(window, media_controller, address_list)

    media_controller.block_until_active()
    print(media_controller.status.player_state)

    print(media_controller.status.player_state)
    # window.mainloop()

    pychromecast.discovery.stop_discovery(browser)


if __name__ == "__main__":
    main()

# media_controller.play_media("http://commondatastorage.googleapis.com/gtv-videos-bucket/sample/BigBuckBunny.mp4", "video/mp4")
# media_controller.play_media("https://antennalivesp-lh.akamaihd.net/i/live_1@715138/index_800_av-p.m3u8", "video/MP2T")
# media_controller.play_media("https://alphalive-i.akamaihd.net/hls/live/682300/live/high/prog_index.m3u8", "video/MP2T")
# media_controller.play_media("https://ert-live-bcbs15228.siliconweb.com/media/ert_1/ert_1medium.m3u8", "video/MP2T")
