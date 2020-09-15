import time
import tkinter as tk
import pychromecast


def create_gui(window, media_controller):
    ert1_logo = tk.PhotoImage(file="ert1.png")  # 382 x 134 is the size of the images for the buttons
    button = tk.Button(master=window, image=ert1_logo, command=lambda: cast_on_button(media_controller))
    button.grid(row=0, column=0, sticky="nsew")
    # button.pack()
    window.mainloop()


def cast_on_button(media_controller):
    media_controller.play_media("https://ert-live-bcbs15228.siliconweb.com/media/ert_1/ert_1medium.m3u8", "video/MP2T")
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
    create_gui(window, media_controller)

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