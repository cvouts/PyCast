import time
import tkinter as tk
import pychromecast


def cast_on_button():
    media_controller.play_media("https://ert-live-bcbs15228.siliconweb.com/media/ert_1/ert_1medium.m3u8", "video/MP2T")
    media_controller.block_until_active()
    media_controller.pause()
    time.sleep(5)
    media_controller.play()


services, browser = pychromecast.discovery.discover_chromecasts()
print(services)
pychromecast.discovery.stop_discovery(browser)

all_chromecasts, browser = pychromecast.get_listed_chromecasts(friendly_names=["Living Room TV"])
chromecast = all_chromecasts[0]

chromecast.wait()
print(chromecast.status)

media_controller = chromecast.media_controller
# media_controller.play_media("https://youtu.be/bbD-CH9SWf8", "video/MP2T")
# media_controller.play_media("http://commondatastorage.googleapis.com/gtv-videos-bucket/sample/BigBuckBunny.mp4", "video/mp4")

# media_controller.play_media("https://antennalivesp-lh.akamaihd.net/i/live_1@715138/index_800_av-p.m3u8", "video/MP2T")

# create a window
window = tk.Tk()
btn_decrease = tk.Button(master=window, text="ert1", command=cast_on_button)
btn_decrease.grid(row=0, column=0, sticky="nsew")

#media_controller.play_media("https://ert-live-bcbs15228.siliconweb.com/media/ert_1/ert_1medium.m3u8", "video/MP2T")



# media_controller.play_media("https://alphalive-i.akamaihd.net/hls/live/682300/live/high/prog_index.m3u8", "video/MP2T")

media_controller.block_until_active()
print("~~~~~")
print(media_controller.status.player_state)

# media_controller.pause()
# time.sleep(5)
# media_controller.play()
print(media_controller.status.player_state)
window.mainloop()
pychromecast.discovery.stop_discovery(browser)
